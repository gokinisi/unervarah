from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import bcrypt
import jwt
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Load env vars (or hardcode for local test)
MONGODB_URI = os.environ.get(
    'MONGODB_URI',
    'mongodb+srv://nervarah_db:Dr.Freedom2026$@cluster0.bl6ewar.mongodb.net/nervarah?retryWrites=true&w=majority'
)
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', '!DrFreedom2026$')

client = MongoClient(MONGODB_URI)
db = client['nervarah']
users = db['users']

print("Connected to MongoDB Atlas")

allowed_domains = ['aamu.edu', 'irsc.edu', 'fau.edu', 'gmail.com']

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    name = data.get('name', 'Anonymous')
    university = data.get('university')
    category = data.get('category')

    if not all([email, password, university, category]):
        return jsonify({'error': 'Missing required fields'}), 400

    domain = email.split('@')[-1].lower()
    if domain not in allowed_domains:
        return jsonify({'error': 'Email domain not allowed'}), 403

    if users.find_one({'email': email}):
        return jsonify({'error': 'Email already registered'}), 409

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = {
        'email': email,
        'password': hashed,
        'name': name,
        'university': university,
        'category': category,
        'logDates': [],
        'createdAt': datetime.utcnow()
    }

    users.insert_one(user)
    return jsonify({'success': True, 'message': 'Account created'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = users.find_one({'email': email})
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return jsonify({'error': 'Invalid credentials'}), 401

    token = jwt.encode({'email': email}, SECRET_KEY, algorithm='HS256')
    return jsonify({
        'success': True,
        'token': token,
        'user': {
            'email': email,
            'name': user['name'],
            'university': user['university'],
            'category': user['category'],
            'logDates': user['logDates']
        }
    })

@app.route('/log-view', methods=['POST'])
def log_view():
    # Simple version - add JWT auth later
    data = request.json
    email = data.get('email')
    today = datetime.utcnow().strftime('%Y-%m-%d')

    users.update_one({'email': email}, {'$addToSet': {'logDates': today}})
    return jsonify({'success': True})

@app.route('/matches', methods=['GET'])
def matches():
    university = request.args.get('university')
    category = request.args.get('category')

    if not university or not category:
        return jsonify({'error': 'Missing params'}), 400

    found = list(users.find({'university': university, 'category': category}, {'_id': 0, 'password': 0}))
    return jsonify(found)

@app.route('/admin/users', methods=['GET'])
def admin_users():
    auth = request.args.get('auth')
    if auth != ADMIN_PASSWORD:
        return jsonify({'error': 'Unauthorized'}), 401

    all_users = list(users.find({}, {'password': 0}))
    return jsonify(all_users)

@app.route('/admin/schools', methods=['GET'])
def admin_schools():
    auth = request.args.get('auth')
    if auth != ADMIN_PASSWORD:
        return jsonify({'error': 'Unauthorized'}), 401

    pipeline = [
        {'$group': {'_id': '$university', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}}
    ]
    stats = list(users.aggregate(pipeline))
    return jsonify(stats)

if __name__ == '__main__':
    print("Server starting...")
    app.run(debug=True, host='0.0.0.0', port=5000)
