import streamlit as st
import sqlite3
import os
from vonage import Client, Sms
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import random

# Vonage credentials (replace with your own from dashboard.nexmo.com)
VONAGE_API_KEY = os.getenv84a6d565
VONAGE_API_SECRET = os.getenvUAtokW9%PCZXo1o$w
VONAGE_BRAND_NAME = os.getenv("VONAGE_BRAND_NAME", "nervarah

")  # Your sender name

vonage_client = Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = Sms(vonage_client)

# Database setup
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (phone TEXT PRIMARY KEY, category TEXT)''')
conn.commit()

# Sample motivations (categorized – you can expand or replace with AI later)
motivations = {
    "positive mind": [
        "You are capable of amazing things.",
        "Every day is a new opportunity to grow.",
        "Your strength is greater than any challenge."
    ],
    "exercise motivation": [
        "Push through—your body is stronger than you think.",
        "One step at a time leads to great achievements.",
        "Feel the power in every movement."
    ],
    "mantra to meditate": [
        "I am at peace with myself and the world.",
        "Breathe in calm, exhale tension.",
        "I am present in this moment."
    ]
}

# Function to send daily motivation
def send_daily_motivations():
    c.execute("SELECT phone, category FROM users")
    users = c.fetchall()
    for phone, category in users:
        message = random.choice(motivations.get(category, motivations["positive mind"]))
        sms.send_message({
            "to": phone,
            "from": VONAGE_BRAND_NAME,
            "text": message
        })

# Schedule daily texts (e.g., 8:00 AM)
scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_motivations, 'cron', hour=8, minute=0)
scheduler.start()

# Streamlit app
st.title("Daily Motivation Sign-Up")
st.write("Enter your phone number to receive daily motivational texts!")

phone = st.text_input("Phone number (international format, e.g. +12025550123)")
category = st.selectbox(
    "Choose your daily motivation type:",
    ["positive mind", "exercise motivation", "mantra to meditate"]
)

if st.button("Sign Up"):
    if phone.startswith("+") and len(phone) >= 10:
        try:
            c.execute("INSERT OR REPLACE INTO users (phone, category) VALUES (?, ?)", (phone, category))
            conn.commit()
            st.success(f"Success! You'll receive daily {category} motivations starting tomorrow.")

            # Send welcome message
            sms.send_message({
                "to": phone,
                "from": VONAGE_BRAND_NAME,
                "text": f"Welcome! You'll get daily {category} motivations. Reply STOP to unsubscribe."
            })
        except Exception as e:
            st.error(f"Error saving your info: {e}")
    else:
        st.error("Please enter a valid international phone number starting with +")

st.markdown("---")
st.caption("Powered by Streamlit & Vonage • Your number is safe and will only be used for daimport streamlit as st
import sqlite3
import os
from vonage import Client, Sms
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import random

# Vonage credentials (replace with your own from dashboard.nexmo.com)
VONAGE_API_KEY = os.getenv("VONAGE_API_KEY", "your_api_key")
VONAGE_API_SECRET = os.getenv("VONAGE_API_SECRET", "your_api_secret")
VONAGE_BRAND_NAME = os.getenv("VONAGE_BRAND_NAME", "EmpathAI")  # Your sender name

vonage_client = Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = Sms(vonage_client)

# Database setup
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (phone TEXT PRIMARY KEY, category TEXT)''')
conn.commit()

# Sample motivations (categorized – you can expand or replace with AI later)
motivations = {
    "positive mind": [
        "You are capable of amazing things.",
        "Every day is a new opportunity to grow.",
        "Your strength is greater than any challenge."
    ],
    "exercise motivation": [
        "Push through—your body is stronger than you think.",
        "One step at a time leads to great achievements.",
        "Feel the power in every movement."
    ],
    "mantra to meditate": [
        "I am at peace with myself and the world.",
        "Breathe in calm, exhale tension.",
        "I am present in this moment."
    ]
}

# Function to send daily motivation
def send_daily_motivations():
    c.execute("SELECT phone, category FROM users")
    users = c.fetchall()
    for phone, category in users:
        message = random.choice(motivations.get(category, motivations["positive mind"]))
        sms.send_message({
            "to": phone,
            "from": VONAGE_BRAND_NAME,
            "text": message
        })

# Schedule daily texts (e.g., 8:00 AM)
scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_motivations, 'cron', hour=8, minute=0)
scheduler.start()

# Streamlit app
st.title("Daily Motivation Sign-Up")
st.write("Enter your phone number to receive daily motivational texts!")

phone = st.text_input("Phone number (international format, e.g. +12025550123)")
category = st.selectbox(
    "Choose your daily motivation type:",
    ["positive mind", "exercise motivation", "mantra to meditate"]
)

if st.button("Sign Up"):
    if phone.startswith("+") and len(phone) >= 10:
        try:
            c.execute("INSERT OR REPLACE INTO users (phone, category) VALUES (?, ?)", (phone, category))
            conn.commit()
            st.success(f"Success! You'll receive daily {category} motivations starting tomorrow.")

            # Send welcome message
            sms.send_message({
                "to": phone,
                "from": VONAGE_BRAND_NAME,
                "text": f"Welcome! You'll get daily {category} motivations. Reply STOP to unsubscribe."
            })
        except Exception as e:
            st.error(f"Error saving your info: {e}")
    else:
        st.error("Please enter a valid international phone number starting with +")

st.markdown("---")
st.caption("Powered by Streamlit & Vonage • Your number is safe and will only be used for daily motivations.")
