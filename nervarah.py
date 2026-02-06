import streamlit as st
import sqlite3
import random
from datetime import datetime

# Sample messages – one per category (expand later)
MESSAGES = {
    "positive mindset": [
        "You already have the power to turn today around — take one kind act toward yourself right now (e.g., a hug, 10 min journaling, glass of water). I am worthy of my own love and care.",
        "You are not behind — you're exactly where the next breakthrough begins. Take one small step today. I am ready for what’s next."
    ],
    "exercise boost": [
        "Your body is ready — do 5 squats or a 30-second stretch right now. I am strong and getting stronger every day.",
        "One rep closer to the version of you that never quits. Start now. I am consistent and powerful."
    ],
    "healthy relationship": [
        "Love grows in small, kind moments — send one thoughtful message today. I give and receive love freely.",
        "You deserve healthy, respectful connection — speak your truth calmly today. I am worthy of real love."
    ],
    "healthy eating motivation": [
        "Your body thrives on good fuel — drink a full glass of water or eat one vegetable right now. I nourish myself with love.",
        "Every healthy choice is a vote for the future you — pick one nutritious snack today. I am healthy and energized."
    ]
}

# Database to store sign-ups
conn = sqlite3.connect('nervarah_users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (email TEXT PRIMARY KEY, category TEXT, signup_date TEXT)''')
conn.commit()

# ───────────────────────────────────────────────
# STREAMLIT UI
# ───────────────────────────────────────────────
st.set_page_config(page_title="Nervarah – Daily Motivation", layout="centered")

st.markdown("""
    <style>
    .main {background-color: #f8fafc;}
    .stButton > button {background-color: #6366f1; color: white; border-radius: 8px; padding: 0.75rem; font-weight: 600; width: 100%;}
    .stButton > button:hover {background-color: #4f46e5;}
    .card {background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
    h1 {color: #1e293b; text-align: center;}
    .subtitle {color: #64748b; text-align: center; font-size: 1.1rem;}
    .success {background: #ecfdf5; border: 1px solid #10b981; border-radius: 8px; padding: 1.5rem; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>✨ Nervarah</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">3 daily motivational messages – free to start</p>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    st.subheader("Sign Up for Daily Motivation")
    email = st.text_input("Your email address", placeholder="you@example.com")
    category = st.selectbox("Choose your daily focus", list(MESSAGES.keys()))

    if st.button("Sign Up – Free", type="primary", use_container_width=True):
        if "@" not in email or "." not in email.split("@")[-1]:
            st.error("Please enter a valid email.")
        else:
            try:
                signup_date = datetime.now().strftime("%Y-%m-%d %H:%M")
                c.execute("INSERT OR REPLACE INTO users (email, category, signup_date) VALUES (?, ?, ?)",
                          (email, category, signup_date))
                conn.commit()
                
                sample = random.choice(MESSAGES[category])
                
                st.markdown('<div class="success">', unsafe_allow_html=True)
                st.success("You're in! Here's your first motivation:")
                st.markdown(f"**{sample}**")
                st.markdown("Daily messages start tomorrow. Welcome to Nervarah! 🎉")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.balloons()
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Your email is used only for daily motivation. Unsubscribe anytime by replying STOP.")