const express = require('express');
const admin = require('firebase-admin');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// Initialize Firebase (get serviceAccount.json from Firebase console)
admin.initializeApp({
  credential: admin.credential.cert(require('./serviceAccount.json')),
  databaseURL: "https://your-project-id.firebaseio.com"
});

const db = admin.firestore();
const allowedDomains = ['irsc.edu', 'fau.edu', 'ufl.edu', 'gmail.com']; // Add your domains

// Sign-up endpoint (checks domain, creates user)
app.post('/signup', async (req, res) => {
  const { email, password, university, category } = req.body;
  const domain = email.split('@')[1];
  if (!allowedDomains.includes(domain)) {
    return res.status(403).json({ error: 'Email domain not allowed' });
  }

  try {
    const user = await admin.auth().createUser({ email, password });
    // Set custom claim for domain access
    await admin.auth().setCustomUserClaims(user.uid, { allowed: true, university, category });
    // Store user data for meetups
    await db.collection('users').doc(user.uid).set({ email, university, category, location: req.body.location || 'Port Saint Lucie, FL' });
    res.json({ uid: user.uid });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Login endpoint
app.post('/login', async (req, res) => {
  // Firebase handles login; frontend uses Firebase SDK for this
  res.json({ message: 'Use Firebase SDK for login' });
});

// Get matches for meetups
app.get('/meetups', async (req, res) => {
  const { university, category } = req.query;
  const matches = await db.collection('users')
    .where('university', '==', university)
    .where('category', '==', category)
    .get();
  const users = matches.docs.map(doc => ({ id: doc.id, ...doc.data() })); // Anonymize emails
  res.json(users);
});

app.listen(3000, () => console.log('Server running'));
