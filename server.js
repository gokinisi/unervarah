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
  import express from "express";
import cookieParser from "cookie-parser";
import jwt from "jsonwebtoken";

const app = express();
app.use(express.json());
app.use(cookieParser());

const JWT_SECRET = process.env.JWT_SECRET || "dev-secret-change-me";

// ---- Mock DB (replace with real DB) ----
const schools = [
  { id: "asu", name: "Albany State University", paid_active: true, allowed_domains: ["asurams.edu"] },
  { id: "demo", name: "Demo University", paid_active: false, allowed_domains: ["demouni.edu"] },
];

const meetups = [
  {
    id: "m1",
    school_id: "asu",
    title: "Sunset Walk + Journaling",
    starts_at: "2026-03-05T18:00:00-05:00",
    location_name: "Campus Green",
    lat: 31.576, lng: -84.139,
  },
];

const users = []; // { id, email, school_id, email_verified }

// ---- Helpers ----
function getUserFromReq(req) {
  const token = req.cookies.session;
  if (!token) return null;
  try {
    return jwt.verify(token, JWT_SECRET);
  } catch {
    return null;
  }
}

function requireAuth(req, res, next) {
  const u = getUserFromReq(req);
  if (!u) return res.status(401).json({ error: "Not signed in" });
  req.user = u;
  next();
}

function requirePaidSchool(req, res, next) {
  const school = schools.find(s => s.id === req.user.school_id);
  if (!school?.paid_active) return res.status(403).json({ error: "School not active" });
  next();
}

// ---- Auth: Email access gating (MVP) ----
// In production, you will:
// 1) send a verification link to the email
// 2) verify token
// 3) then create session cookie

app.post("/api/auth/start", (req, res) => {
  const { email } = req.body;
  if (!email || !email.includes("@")) return res.status(400).json({ error: "Invalid email" });

  const domain = email.split("@")[1].toLowerCase();
  const school = schools.find(s => s.allowed_domains.includes(domain));

  if (!school || !school.paid_active) {
    // IMPORTANT: don’t leak which domains are valid in production; for now keep it explicit.
    return res.status(403).json({ error: "Your university is not currently enrolled." });
  }

  // MVP: treat as verified immediately (NOT OK for real)
  // Replace with email magic-link verification
  const user = { id: crypto.randomUUID(), email, school_id: school.id, email_verified: true };
  users.push(user);

  const sessionPayload = { user_id: user.id, email: user.email, school_id: user.school_id };
  const token = jwt.sign(sessionPayload, JWT_SECRET, { expiresIn: "7d" });

  res.cookie("session", token, { httpOnly: true, sameSite: "lax", secure: false });
  res.json({ ok: true, school: { id: school.id, name: school.name } });
});

app.post("/api/auth/logout", (req, res) => {
  res.clearCookie("session");
  res.json({ ok: true });
});

// ---- Schools (only show paid/eligible schools if you prefer) ----
app.get("/api/schools", requireAuth, (req, res) => {
  // return only paid schools OR only user’s school; pick one:
  const mySchool = schools.find(s => s.id === req.user.school_id);
  res.json(mySchool ? [mySchool] : []);
});

// ---- Meetups listing (restricted to the user’s school) ----
app.get("/api/meetups", requireAuth, requirePaidSchool, (req, res) => {
  const schoolId = req.query.school_id;

  // enforce: user can only view their own school’s meetups
  if (schoolId && schoolId !== req.user.school_id) {
    return res.status(403).json({ error: "Forbidden" });
  }

  const list = meetups
    .filter(m => m.school_id === req.user.school_id)
    .sort((a, b) => new Date(a.starts_at) - new Date(b.starts_at));

  res.json(list);
});

// ---- Create meetup (admin only in real life) ----
app.post("/api/meetups", requireAuth, requirePaidSchool, (req, res) => {
  // TODO: check role/admin
  const { title, starts_at, location_name, lat, lng } = req.body;

  if (!title || !starts_at) return res.status(400).json({ error: "title and starts_at required" });

  const m = {
    id: crypto.randomUUID(),
    school_id: req.user.school_id,
    title,
    starts_at,
    location_name: location_name || "",
    lat: typeof lat === "number" ? lat : null,
    lng: typeof lng === "number" ? lng : null,
  };

  meetups.push(m);
  res.json({ ok: true, meetup: m });
});

// ---- Motivation tips gated route ----
app.get("/api/tips/today", requireAuth, requirePaidSchool, (req, res) => {
  res.json({
    tip: "Today: choose one goal you can own (autonomy), one small win you can complete (competence), and one person you can connect with (relatedness).",
  });
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));

});

app.listen(3000, () => console.log('Server running'));
