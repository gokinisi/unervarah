{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
import requests\
import base64\
import json\
\
app = Flask(__name__)\
\
# REPLACE WITH YOUR KEYS\
VAPID_PRIVATE_KEY = "YOUR_PRIVATE_VAPID_KEY"\
VAPID_PUBLIC_KEY = "YOUR_PUBLIC_VAPID_KEY"\
VAPID_CLAIMS = \{"sub": "mailto:your-email@example.com"\}\
\
subscriptions = []  # In-memory for MVP \'96 use database later\
\
def send_push(subscription, title, body):\
    headers = \{\
        "Authorization": f"VAPID t=\{base64.urlsafe_b64encode(VAPID_PUBLIC_KEY.encode()).decode()\}, k=\{base64.urlsafe_b64encode(VAPID_PRIVATE_KEY.encode()).decode()\}",\
        "Content-Type": "application/json",\
        "TTL": "2419200"  # 28 days\
    \}\
    payload = json.dumps(\{\
        "title": title,\
        "body": body\
    \})\
    response = requests.post(\
        subscription['endpoint'],\
        data=payload,\
        headers=headers\
    )\
    print("Push response:", response.status_code)\
\
@app.route('/subscribe', methods=['POST'])\
def subscribe():\
    data = request.json\
    subscription = data['subscription']\
    category = data['category']\
    subscriptions.append(\{'subscription': subscription, 'category': category\})\
    print("New subscription:", subscription['endpoint'])\
    return jsonify(\{"status": "subscribed"\})\
\
@app.route('/test-push')\
def test_push():\
    if not subscriptions:\
        return "No subscribers"\
    for sub in subscriptions:\
        send_push(sub['subscription'], "Nervarah Test", "This is a test motivation!")\
    return "Test push sent!"\
\
if __name__ == '__main__':\
    app.run(port=5000)}