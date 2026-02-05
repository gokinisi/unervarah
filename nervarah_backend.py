from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import json
from pywebpush import webpush, WebPushException
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import random
from transformers import pipeline

app = Flask(__name__, static_folder='.', static_url_path='')  # Serve files from current folder

# Database setup
conn = sqlite3.connect('subscriptions.db', check_same_thread=False)
c = conn.cursor()

# Create table with all columns
c.execute('''CREATE TABLE IF NOT EXISTS subscriptions
             (endpoint TEXT PRIMARY KEY,
              auth TEXT,
              p256dh TEXT,
              category TEXT,
              email TEXT,
              signup_date TEXT)''')

# Add missing columns safely
c.execute("PRAGMA table_info(subscriptions)")
columns = {row[1] for row in c.fetchall()}
for col in ['category', 'email', 'signup_date']:
    if col not in columns:
        c.execute(f"ALTER TABLE subscriptions ADD COLUMN {col} TEXT")
conn.commit()

# VAPID keys
VAPID_PUBLIC_KEY = "BA7mpoEQJEKRvhw2-9XUXWgI4fiYeqyKAh5x1wTv_6HeFW7oeLNyP3IOAgzD1Ka8bTOZodZlXafMStclk0mHMM0"
VAPID_PRIVATE_KEY = "fYq8-glCtPhKFc9NNfwYQiCF9F0CMlHz9yYpISSkI04"  # ← Your real private key
VAPID_CLAIMS = {"sub": "mailto:kris@nervarah.com"}

# ML model (distilgpt2 for speed)
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125m", device=-1)

# Prompts (very directive for uplifting tone)
PROMPTS = {
    "positive mindset": "Write a short, warm, uplifting, and empowering motivational message to inspire positive mindset and self-belief. Use kind, supportive, encouraging language. Make the reader feel seen, capable, and full of hope. End with a powerful 'I am' affirmation. Keep it 1–2 sentences only. Example tone: 'You are already enough. I am worthy of joy.' ",
    "exercise boost": "Write a short, energizing, positive, and motivating message to inspire someone to move their body today. Use enthusiastic, supportive, joyful language. Make them feel strong and excited to start. End with an empowering 'I am' statement. Keep it 1–2 sentences. Example tone: 'Your body is ready for this — let's go! I am strong and capable.' ",
    "healthy relationship": "Write a short, warm, loving, and hopeful message to nurture healthy relationships and emotional connection. Use gentle, kind, supportive language. Focus on self-love, respect, and open-heartedness. End with a positive 'I am' affirmation. Keep it 1–2 sentences. Example tone: 'You deserve real love. I am worthy of kind connections.' ",
    "healthy eating motivation": "Write a short, joyful, nourishing, and self-loving message to encourage healthy eating habits. Use positive, caring, celebratory language. Make the reader feel excited to fuel their body with love. End with an empowering 'I am' statement. Keep it 1–2 sentences. Example tone: 'Choose food that lights you up. I am worthy of vibrant health.' "
}

def generate_ml_motivation(category):
    prompt = PROMPTS.get(category, PROMPTS["positive mindset"])
    result = generator(
        prompt,
        max_new_tokens=50,
        num_return_sequences=1,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        repetition_penalty=1.3,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    message = result[0]['generated_text'].replace(prompt, '').strip()
    message = ''.join(c for c in message if c.isprintable())
    return message[:160] or "You are enough, right now. I am worthy of love."

def clean_uplifting_message(message):
    message = message.strip()
    # Remove junk at start/end
    junk_patterns = ['---', '–––', '…', '�', '\n', '\r', '  ']
    for junk in junk_patterns:
        message = message.replace(junk, ' ')
    # Remove negative starters
    negative_starters = ["don't", "stop", "never", "can't", "but", "however", "no", "not"]
    words = message.split()
    if words and words[0].lower() in negative_starters:
        message = ' '.join(words[1:]).strip()
    # Force positive ending
    if not message.endswith(('.', '!', '?', ')')):
        message += "!"
    # Add affirmation if missing
    if "I am" not in message and random.random() < 0.5:
        message += " I am worthy of joy and growth."
    # Final cleanup
    message = ' '.join(message.split())
    return message[:160] or "You are enough, right now. I am worthy of love."

# Serve HTML
@app.route('/')
def serve_html():
    return send_from_directory('.', 'nervarah.html')

# Serve service worker
@app.route('/sw.js')
def serve_sw():
    return send_from_directory('.', 'sw.js')

# Subscribe endpoint
@app.route('/subscribe', methods=['POST'])
def subscribe():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data received"}), 400

    print("Received payload:", json.dumps(data, indent=2))

    subscription = data.get('subscription', {})
    category = data.get('category')
    email = data.get('email')

    endpoint = subscription.get('endpoint')
    keys = subscription.get('keys', {})
    auth = keys.get('auth')
    p256dh = keys.get('p256dh')

    if not all([endpoint, auth, p256dh, category]):
        return jsonify({"error": "Missing required fields"}), 400

    if email and ("@" not in email or "." not in email.split("@")[-1]):
        return jsonify({"error": "Invalid email"}), 400

    try:
        signup_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        c.execute("INSERT OR REPLACE INTO subscriptions (endpoint, auth, p256dh, category, email, signup_date) VALUES (?, ?, ?, ?, ?, ?)",
                  (endpoint, auth, p256dh, category, email or None, signup_date))
        conn.commit()
        print(f"Subscription saved: {endpoint} | category: {category} | email: {email}")
        return jsonify({"status": "subscribed"})
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({"error": str(e)}), 500

# Test push
@app.route('/send-test')
def send_test():
    c.execute("SELECT endpoint, auth, p256dh, category FROM subscriptions")
    subs = c.fetchall()
    if not subs:
        return "No subscribers yet"
    sent_count = 0
    for endpoint, auth, p256dh, category in subs:
        message = generate_ml_motivation(category)
        message = clean_uplifting_message(message)
        data = json.dumps({
            "title": "Nervarah Daily Motivation",
            "body": message
        })
        try:
            webpush(
                subscription_info={"endpoint": endpoint, "keys": {"auth": auth, "p256dh": p256dh}},
                data=data,
                vapid_private_key=VAPID_PRIVATE_KEY,
                vapid_claims=VAPID_CLAIMS
            )
            print(f"Test push sent to {endpoint} for {category}: {message}")
            sent_count += 1
        except WebPushException as e:
            print(f"Push failed for {endpoint}: {e}")
            if e.response.status_code in [404, 410]:
                c.execute("DELETE FROM subscriptions WHERE endpoint = ?", (endpoint,))
                conn.commit()
                print(f"Removed expired subscription: {endpoint}")
    return f"Test pushes sent to {sent_count} subscribers"

# Daily scheduler
def send_daily_motivations():
    c.execute("SELECT endpoint, auth, p256dh, category FROM subscriptions")
    subs = c.fetchall()
    if not subs:
        print("No subscribers for daily send")
        return
    print(f"Starting daily send to {len(subs)} subscribers at {datetime.now()}")
    for endpoint, auth, p256dh, category in subs:
        message = generate_ml_motivation(category)
        message = clean_uplifting_message(message)
        data = json.dumps({
            "title": "Nervarah Daily Motivation",
            "body": message
        })
        try:
            webpush(
                subscription_info={"endpoint": endpoint, "keys": {"auth": auth, "p256dh": p256dh}},
                data=data,
                vapid_private_key=VAPID_PRIVATE_KEY,
                vapid_claims=VAPID_CLAIMS
            )
            print(f"Daily push sent to {endpoint} for {category}")
        except WebPushException as e:
            print(f"Daily push failed for {endpoint}: {e}")
            if e.response.status_code in [404, 410]:
                c.execute("DELETE FROM subscriptions WHERE endpoint = ?", (endpoint,))
                conn.commit()
                print(f"Removed expired subscription: {endpoint}")

scheduler = BackgroundScheduler()
scheduler.add_job(
    send_daily_motivations,
    'cron',
    hour=8, minute=0,
    timezone='America/New_York'
)
scheduler.start()
print("Daily scheduler started – pushes at 8:00 AM ET")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)