from flask import Flask, request, jsonify, send_from_directory
import sqlite3
import json
from pywebpush import webpush, WebPushException
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import random

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

# Sample messages (fallback if ML is removed)
MESSAGES = {
    "positive mindset": [
        "You already have the power to turn today around — take one kind act toward yourself right now. I am worthy of my own love and care.",
        "You are not behind — you're exactly where the next breakthrough begins. I am ready for what’s next."
    ],
    "exercise boost": [
        "Your body is ready — do 5 squats or a 30-second stretch right now. I am strong and getting stronger every day.",
        "One rep closer to the version of you that never quits. I am consistent and powerful."
    ],
    "healthy relationship": [
        "Love grows in small, kind moments — send one thoughtful message today. I give and receive love freely.",
        "You deserve healthy, respectful connection. I am worthy of real love."
    ],
    "healthy eating motivation": [
        "Your body thrives on good fuel — drink a full glass of water or eat one vegetable right now. I nourish myself with love.",
        "Every healthy choice is a vote for the future you. I am healthy and energized."
    ]
}

def get_motivation(category):
    return random.choice(MESSAGES.get(category, MESSAGES["positive mindset"]))

def clean_uplifting_message(message):
    message = message.strip()
    junk_patterns = ['---', '–––', '…', '�', '\n', '\r', '  ']
    for junk in junk_patterns:
        message = message.replace(junk, ' ')
    negative_starters = ["don't", "stop", "never", "can't", "but", "however", "no", "not"]
    words = message.split()
    if words and words[0].lower() in negative_starters:
        message = ' '.join(words[1:]).strip()
    if not message.endswith(('.', '!', '?')):
        message += "!"
    if "I am" not in message and random.random() < 0.5:
        message += " I am worthy of joy and growth."
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

# Test push endpoint
@app.route('/send-test')
def send_test():
    c.execute("SELECT endpoint, auth, p256dh, category FROM subscriptions")
    subs = c.fetchall()
    if not subs:
        return "No subscribers yet"
    sent_count = 0
    for endpoint, auth, p256dh, category in subs:
        message = get_motivation(category)
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


const response = await fetch('https://unervarah.onrender.com/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    subscription: subscription.toJSON(),
    category: selectedCategory,
    email: document.getElementById('email').value.trim()
  })
});

const registration = await navigator.serviceWorker.register('https://nervarah-backend.onrender.com/sw.js');

# Daily scheduler
def send_daily_motivations():
    c.execute("SELECT endpoint, auth, p256dh, category FROM subscriptions")
    subs = c.fetchall()
    if not subs:
        print("No subscribers for daily send")
        return
    print(f"Starting daily send to {len(subs)} subscribers at {datetime.now()}")
    for endpoint, auth, p256dh, category in subs:
        message = get_motivation(category)
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