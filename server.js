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

app.listen(3000, () => console.log("Server running on http://nervarah.com"));

  import express from "express";
import cookieParser from "cookie-parser";
import jwt from "jsonwebtoken";
import crypto from "crypto";
import pg from "pg";
import nodemailer from "nodemailer";

const app = express();
app.use(express.json());
app.use(cookieParser());

const { Pool } = pg;

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

const JWT_SECRET = process.env.JWT_SECRET;
if (!JWT_SECRET) throw new Error("Missing JWT_SECRET");

const APP_ORIGIN = process.env.APP_ORIGIN || "http://nervarah.com"; // where frontend lives
const FROM_EMAIL = process.env.FROM_EMAIL; // e.g. support@nervarah.com
if (!FROM_EMAIL) throw new Error("Missing FROM_EMAIL");

// --- Email transport (use your SMTP provider) ---
const transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: Number(process.env.SMTP_PORT || 587),
  secure: false,
  auth: { user: process.env.SMTP_USER, pass: process.env.SMTP_PASS },
});

// --- Helpers ---
function normalizeEmail(email) {
  return String(email || "").trim().toLowerCase();
}
function emailDomain(email) {
  return normalizeEmail(email).split("@")[1] || "";
}
function generateToken() {
  return crypto.randomBytes(32).toString("hex");
}
function hashToken(token) {
  return crypto.createHash("sha256").update(token).digest("hex");
}

function signSession(payload) {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: "7d" });
}

function getSession(req) {
  const token = req.cookies.session;
  if (!token) return null;
  try {
    return jwt.verify(token, JWT_SECRET);
  } catch {
    return null;
  }
}

function requireAuth(req, res, next) {
  const s = getSession(req);
  if (!s) return res.status(401).json({ error: "Not signed in" });
  req.session = s;
  next();
}

async function requireVerifiedAndPaid(req, res, next) {
  const { user_id } = req.session;
  const { rows } = await pool.query(
    `
    SELECT u.email_verified, s.paid_active, u.school_id
    FROM users u
    JOIN schools s ON s.id = u.school_id
    WHERE u.id = $1
    `,
    [user_id]
  );
  if (!rows[0]) return res.status(401).json({ error: "Invalid user" });
  if (!rows[0].email_verified) return res.status(403).json({ error: "Email not verified" });
  if (!rows[0].paid_active) return res.status(403).json({ error: "School not active" });
  req.school_id = rows[0].school_id;
  next();
}

// --- AUTH: Start (send magic link) ---
app.post("/api/auth/start", async (req, res) => {
  const email = normalizeEmail(req.body.email);
  if (!email.includes("@")) return res.status(400).json({ error: "Invalid email" });

  const domain = emailDomain(email);

  // find eligible school
  const schoolRes = await pool.query(
    `
    SELECT id, name, paid_active
    FROM schools
    WHERE $1 = ANY(allowed_domains)
    LIMIT 1
    `,
    [domain]
  );

  const school = schoolRes.rows[0];
  if (!school || !school.paid_active) {
    // Avoid leaking which domains are valid (good practice)
    return res.status(403).json({ error: "This email is not eligible for access." });
  }

  // upsert user
  const userRes = await pool.query(
    `
    INSERT INTO users (email, school_id, email_verified)
    VALUES ($1, $2, false)
    ON CONFLICT (email)
    DO UPDATE SET school_id = EXCLUDED.school_id
    RETURNING id
    `,
    [email, school.id]
  );

  const userId = userRes.rows[0].id;

  // create verification token
  const token = generateToken();
  const tokenHash = hashToken(token);

  await pool.query(
    `
    INSERT INTO email_verifications (user_id, token_hash, expires_at)
    VALUES ($1, $2, NOW() + interval '30 minutes')
    `,
    [userId, tokenHash]
  );

  const verifyUrl = `${process.env.API_ORIGIN || "http://localhost:3000"}/api/auth/verify?token=${token}`;

  // send email
  await transporter.sendMail({
    from: FROM_EMAIL,
    to: email,
    subject: "Your Nervarah sign-in link",
    text: `Click to sign in: ${verifyUrl}\nThis link expires in 30 minutes.`,
    html: `<p>Click to sign in:</p><p><a href="${verifyUrl}">Sign in to Nervarah</a></p><p>This link expires in 30 minutes.</p>`,
  });

  res.json({ ok: true });
});

// --- AUTH: Verify token, set session cookie, redirect ---
app.get("/api/auth/verify", async (req, res) => {
  const token = String(req.query.token || "");
  if (!token) return res.status(400).send("Missing token");

  const tokenHash = hashToken(token);

  const { rows } = await pool.query(
    `
    SELECT ev.id as ev_id, ev.user_id
    FROM email_verifications ev
    WHERE ev.token_hash = $1
      AND ev.used_at IS NULL
      AND ev.expires_at > NOW()
    LIMIT 1
    `,
    [tokenHash]
  );

  const ev = rows[0];
  if (!ev) return res.status(400).send("Invalid or expired link");

  // mark verification used + verify email
  await pool.query("BEGIN");
  try {
    await pool.query(
      `UPDATE email_verifications SET used_at = NOW() WHERE id = $1`,
      [ev.ev_id]
    );
    await pool.query(
      `UPDATE users SET email_verified = true WHERE id = $1`,
      [ev.user_id]
    );
    await pool.query("COMMIT");
  } catch (e) {
    await pool.query("ROLLBACK");
    throw e;
  }

  // issue session cookie
  const session = signSession({ user_id: ev.user_id });

  res.cookie("session", session, {
    httpOnly: true,
    sameSite: "lax",
    secure: false, // set true when using HTTPS in production
    maxAge: 7 * 24 * 60 * 60 * 1000,
  });

  return res.redirect(`${APP_ORIGIN}/meetup.html`);
});

// --- User Profile (create/update) ---
app.post("/api/profile", requireAuth, async (req, res) => {
  const { full_name } = req.body;
  await pool.query(`UPDATE users SET full_name = $1 WHERE id = $2`, [
    String(full_name || "").slice(0, 120),
    req.session.user_id,
  ]);
  res.json({ ok: true });
});

app.get("/api/profile", requireAuth, async (req, res) => {
  const { rows } = await pool.query(
    `SELECT email, full_name, email_verified FROM users WHERE id = $1`,
    [req.session.user_id]
  );
  res.json(rows[0] || null);
});

// --- Protected example: tips ---
app.get("/api/tips/today", requireAuth, requireVerifiedAndPaid, async (req, res) => {
  res.json({ tip: "Autonomy: choose one goal. Competence: one small win. Relatedness: one reach-out." });
});

// --- Meetups list for student's school ---
app.get("/api/meetups", requireAuth, requireVerifiedAndPaid, async (req, res) => {
  const { rows } = await pool.query(
    `
    SELECT id, title, starts_at, location_name, lat, lng
    FROM meetups
    WHERE school_id = $1 AND starts_at > NOW() - interval '1 day'
    ORDER BY starts_at ASC
    LIMIT 200
    `,
    [req.school_id]
  );
  res.json(rows);

  const express = require('express');
const { MongoClient } = require('mongodb');
const cors = require('cors');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const app = express();
app.use(cors());
app.use(express.json());

const uri = process.env.MONGODB_URI;
const client = new MongoClient(uri);
let db;

client.connect().then(() => {
  db = client.db("nervarah");
  console.log("Connected to MongoDB");
}).catch(err => console.error(err));

const SECRET_KEY = 'your_secret_key'; // Change to strong secret (add to Render env vars)

const allowedDomains = ['aamu.edu', 'irsc.edu', 'fau.edu']; // Expand as needed

// Signup
app.post('/signup', async (req, res) => {
  const { email, password, university, category } = req.body;
  const domain = email.split('@')[1];
  if (!allowedDomains.includes(domain)) return res.status(403).json({ error: 'Invalid school domain' });

  try {
    const hashedPass = await bcrypt.hash(password, 10);
    const newUser = { email, password: hashedPass, university, category, logDates: [] };
    await db.collection('users').insertOne(newUser);
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: 'Signup failed' });
  }
});

// Login
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await db.collection('users').findOne({ email });
    if (!user || !await bcrypt.compare(password, user.password)) return res.status(401).json({ error: 'Invalid credentials' });

    const token = jwt.sign({ email: user.email }, SECRET_KEY, { expiresIn: '1h' });
    res.json({ token, university: user.university, category: user.category, logDates: user.logDates });
  } catch (err) {
    res.status(500).json({ error: 'Login failed' });
  }
});

// Log daily view (authenticated)
app.post('/log-view', authenticateToken, async (req, res) => {
  const { email } = req.user;
  const today = new Date().toDateString();

  try {
    await db.collection('users').updateOne({ email }, { $addToSet: { logDates: today } });
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: 'Log failed' });
  }
});

// Get matches (authenticated)
app.get('/matches', authenticateToken, async (req, res) => {
  const { university, category } = req.query;
  try {
    const matches = await db.collection('users').find({ university, category, email: { $ne: req.user.email } }).toArray();
    res.json(matches.map(() => ({ message: 'Another student at your school with the same focus' }))); // Anonymized
  } catch (err) {
    res.status(500).json({ error: 'Fetch matches failed' });
  }
});

// Admin route (basic password for you)
app.get('/admin/profiles', (req, res) => {
  const { auth } = req.query;
  if (auth !== 'your_admin_password') return res.status(401).json({ error: 'Unauthorized' }); // Change password

  db.collection('users').find({}, { projection: { password: 0 } }).toArray() // Hide passwords
    .then(users => res.json(users))
    .catch(err => res.status(500).json({ error: 'Admin fetch failed' }));
});

function authenticateToken(req, res, next) {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'No token' });

  jwt.verify(token, SECRET_KEY, (err, user) => {
    if (err) return res.status(403).json({ error: 'Invalid token' });
    req.user = user;
    next();
  });
}

app.listen(process.env.PORT || 3000, () => console.log('Server running'));
});

app.listen(3000, () => console.log("API on nervarah.com"));


});

app.listen(3000, () => console.log('Server running'));
