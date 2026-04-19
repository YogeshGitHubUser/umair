import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="The Secret Kingdom of Numbers",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── HIDE STREAMLIT CHROME ──────────────────────────────────────────────────────
st.markdown("""
<style>
#MainMenu, header, footer, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { display: block; border: none; }
</style>
""", unsafe_allow_html=True)

# ── BOOK CONFIG — edit everything here ────────────────────────────────────────
BOOK = {
    "title":          "The Secret Kingdom of Numbers",
    "subtitle":       "A Mathematical Adventure Beyond Imagination",
    "author":         "Aryan Sharma",
    "age":            13,
    "grade":          "Class 8",
    "city":           "Pune, India",
    "pages":          124,
    "genre":          "Math · Adventure · Fantasy",
    "tagline":        "What if every number had a superpower?",
    "description": (
        "Dive into a world where Prime Numbers guard ancient castles, "
        "Fractions build rainbow bridges, and the fearless hero Zero discovers "
        "that nothing can be the most powerful thing of all. Packed with real "
        "math concepts hidden inside an epic quest — this book makes you fall "
        "in love with numbers forever."
    ),
    "author_bio": (
        "Aryan is a Class 8 student with a love for mathematics and an even "
        "bigger imagination. When his teacher told him numbers have personalities, "
        "he went home and wrote an entire fantasy world about them. "
        "This book proves that the best stories can come from the most curious minds — "
        "no matter how young."
    ),
    "preview": [
        {
            "chapter": "Chapter 1",
            "title":   "The Gate of Infinity",
            "emoji":   "🚪",
            "text": (
                "The old door was carved with a thousand spirals — each one a number, "
                "each number a secret. 'To enter,' said the Guardian, 'you must answer: "
                "what number is both everything and nothing?' Aryan smiled slowly. "
                "He already knew."
            ),
        },
        {
            "chapter": "Chapter 4",
            "title":   "The Fraction Forest",
            "emoji":   "🌳",
            "text": (
                "Half the trees were tall, a quarter were golden, one-eighth glowed "
                "violet at night. The forest itself was a living fraction — always "
                "adding to one whole, no matter how you divided it. "
                "'We are pieces,' whispered the Fraction Fairy. 'But together, we are complete.'"
            ),
        },
        {
            "chapter": "Chapter 9",
            "title":   "Zero's Secret",
            "emoji":   "⭕",
            "text": (
                "Everyone laughed at Zero. 'You are nothing!' they said. "
                "But Zero just smiled and stepped beside One — "
                "and One became Ten. Then Hundred. Then Thousand. "
                "'Nothing,' said Zero quietly, 'can become everything.'"
            ),
        },
    ],
    "physical_price": 299,
    "digital_price":  99,
    "upi_id":         "aryan@oksbi",          # ← replace with real UPI ID
    "whatsapp":       "919876543210",          # ← replace (country code + number)
    "seller_email":   "aryan@example.com",     # ← replace
    "seller_name":    "Aryan Sharma",
}

# ── RIDDLES DATA ───────────────────────────────────────────────────────────────
RIDDLES = [
    {
        "q": "I am neither positive nor negative. What number am I?",
        "opts": ["One", "Zero", "Infinity", "Half"],
        "correct": 1,
        "fact": "Zero (0) is the only number that is neither positive nor negative — and it has the power to make any number ten times bigger!"
    },
    {
        "q": "A fraction whose numerator equals its denominator always equals…?",
        "opts": ["Zero", "Two", "One", "Itself"],
        "correct": 2,
        "fact": "Any number ÷ itself = 1. That's why 4/4, 99/99, and 1000/1000 are all exactly equal to 1!"
    },
    {
        "q": "Which of these is NOT a prime number?",
        "opts": ["7", "11", "15", "13"],
        "correct": 2,
        "fact": "15 = 3 × 5, so it has factors other than 1 and itself. That disqualifies it from the Prime Guard!"
    },
    {
        "q": "The angles of ANY triangle always add up to…?",
        "opts": ["90°", "360°", "270°", "180°"],
        "correct": 3,
        "fact": "Every triangle — big, small, weird — always has angles that sum to exactly 180°. It's one of geometry's golden laws."
    },
    {
        "q": "Which number, when multiplied by anything, leaves it unchanged?",
        "opts": ["0", "2", "1", "10"],
        "correct": 2,
        "fact": "1 is the Multiplicative Identity. n × 1 = n, always. It's the quiet guardian of every equation."
    },
]

# ── BUILD THE PAGE ─────────────────────────────────────────────────────────────
riddles_json = str(RIDDLES).replace("'", '"').replace("True","true").replace("False","false")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{BOOK['title']}</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@400;500;600&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
<style>
/* ── RESET & ROOT ─────────────────────────────── */
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;font-size:16px;}}

:root{{
  --bg:       #FAFAF7;
  --ink:      #1A1A1A;
  --ink2:     #4A4A4A;
  --ink3:     #7A7A7A;
  --border:   #E4E0D8;
  --cream:    #F5F0E8;
  --accent:   #C8602A;       /* warm terracotta */
  --accent2:  #E8835A;
  --violet:   #3D2B6E;
  --violet2:  #5B4290;
  --gold:     #C8A84B;
  --gold2:    #F0D080;
  --green:    #2A6B4A;
  --white:    #FFFFFF;
  --shadow:   0 2px 12px rgba(0,0,0,0.08);
  --shadow-md:0 8px 32px rgba(0,0,0,0.12);
  --shadow-lg:0 16px 48px rgba(0,0,0,0.16);
  --r:12px;
  --r-lg:20px;
}}

body{{
  font-family:'DM Sans',sans-serif;
  background:var(--bg);
  color:var(--ink);
  line-height:1.6;
  -webkit-font-smoothing:antialiased;
}}

/* ── TYPOGRAPHY ───────────────────────────────── */
.serif      {{ font-family:'Playfair Display',serif; }}
.serif-body {{ font-family:'DM Serif Display',serif; }}
h1,h2,h3   {{ font-family:'Playfair Display',serif; line-height:1.15; }}

/* ── LAYOUT ───────────────────────────────────── */
.container {{ max-width:1000px;margin:0 auto;padding:0 24px; }}
.section    {{ padding:72px 0; }}
.section-sm {{ padding:48px 0; }}
hr.divider  {{ border:none;border-top:1px solid var(--border);margin:0; }}

/* ── LABELS ───────────────────────────────────── */
.label{{
  display:inline-block;
  font-size:11px;font-weight:600;
  letter-spacing:.18em;text-transform:uppercase;
  color:var(--accent);
  margin-bottom:12px;
}}

/* ─────────────────────────────────────────────────
   HERO
───────────────────────────────────────────────── */
.hero{{
  background:var(--violet);
  color:#fff;
  padding:64px 0 56px;
  position:relative;
  overflow:hidden;
}}
/* subtle texture overlay */
.hero::before{{
  content:'';
  position:absolute;inset:0;
  background:
    radial-gradient(ellipse 60% 80% at 80% 50%, rgba(200,96,42,.18) 0%, transparent 70%),
    radial-gradient(ellipse 40% 60% at 20% 20%, rgba(255,255,255,.04) 0%, transparent 60%);
  pointer-events:none;
}}
.hero-inner{{
  position:relative;z-index:1;
  display:grid;
  grid-template-columns:1fr 340px;
  gap:56px;
  align-items:center;
}}
/* left */
.hero-eyebrow{{
  display:inline-flex;align-items:center;gap:8px;
  border:1px solid rgba(255,255,255,.2);
  border-radius:40px;padding:5px 14px;
  font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;
  color:rgba(255,255,255,.6);
  margin-bottom:22px;
}}
.hero-eyebrow .dot{{
  width:6px;height:6px;border-radius:50%;background:var(--gold2);
  animation:blink 1.6s ease-in-out infinite;
}}
@keyframes blink{{0%,100%{{opacity:1;}}50%{{opacity:.3;}}}}
.hero h1{{
  font-size:clamp(32px,4.5vw,52px);
  font-weight:900;color:#fff;
  margin-bottom:10px;
  letter-spacing:-.02em;
}}
.hero h1 em{{color:var(--gold2);font-style:normal;}}
.hero-tagline{{
  font-family:'DM Serif Display',serif;
  font-size:18px;font-style:italic;
  color:rgba(255,255,255,.65);
  margin-bottom:20px;
}}
.hero-desc{{
  font-size:15px;color:rgba(255,255,255,.7);
  line-height:1.75;max-width:520px;margin-bottom:32px;
}}
.hero-meta{{display:flex;gap:20px;flex-wrap:wrap;margin-bottom:32px;}}
.meta-chip{{
  display:flex;align-items:center;gap:6px;
  font-size:13px;color:rgba(255,255,255,.55);font-weight:500;
}}
.meta-chip .ic{{font-size:15px;}}

/* BUY BUTTONS */
.btn-group{{display:flex;gap:12px;flex-wrap:wrap;}}
.btn{{
  display:inline-flex;align-items:center;gap:10px;
  padding:14px 24px;border-radius:var(--r);
  font-size:14px;font-weight:600;
  cursor:pointer;border:none;text-decoration:none;
  transition:transform .2s,box-shadow .2s,filter .2s;
  font-family:'DM Sans',sans-serif;
  white-space:nowrap;
}}
.btn:hover{{transform:translateY(-2px);}}
.btn-primary{{
  background:var(--accent);color:#fff;
  box-shadow:0 4px 16px rgba(200,96,42,.4);
}}
.btn-primary:hover{{box-shadow:0 8px 24px rgba(200,96,42,.5);}}
.btn-secondary{{
  background:rgba(255,255,255,.1);color:#fff;
  border:1px solid rgba(255,255,255,.25);
}}
.btn-secondary:hover{{background:rgba(255,255,255,.18);}}
.btn-price{{font-size:17px;font-weight:700;}}
.btn-sub{{font-size:11px;opacity:.7;}}
.btn-col{{display:flex;flex-direction:column;line-height:1.2;}}

/* right — book card */
.book-card{{
  background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.12);
  border-radius:var(--r-lg);
  padding:28px 24px;
  text-align:center;
}}
.book-cover{{
  width:160px;height:220px;
  margin:0 auto 20px;
  border-radius:4px 12px 12px 4px;
  background:linear-gradient(160deg,#2D1B5E 0%,#3D2B6E 40%,#C8602A 100%);
  box-shadow:
    -4px 0 0 rgba(0,0,0,.3),
    var(--shadow-lg);
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  position:relative;overflow:hidden;
  transition:transform .3s,box-shadow .3s;
  cursor:default;
}}
.book-cover:hover{{
  transform:perspective(600px) rotateY(-8deg) translateY(-4px);
  box-shadow:-6px 8px 32px rgba(0,0,0,.4),var(--shadow-lg);
}}
.book-cover::before{{
  content:'';position:absolute;
  left:0;top:0;bottom:0;width:16px;
  background:linear-gradient(to right,rgba(0,0,0,.35),rgba(0,0,0,.05));
}}
.book-cover-inner{{padding:20px 16px;text-align:center;position:relative;z-index:1;}}
.book-emoji{{font-size:36px;margin-bottom:8px;display:block;}}
.book-cover-title{{
  font-family:'Playfair Display',serif;
  font-size:11px;font-weight:700;color:var(--gold2);
  line-height:1.4;margin-bottom:6px;
  letter-spacing:.02em;
}}
.book-cover-author{{font-size:9px;color:rgba(255,255,255,.5);letter-spacing:.08em;}}
.book-card-label{{
  font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;
  color:rgba(255,255,255,.35);margin-bottom:6px;
}}
.book-card-title{{font-size:14px;font-weight:600;color:#fff;margin-bottom:4px;}}
.book-card-sub{{font-size:12px;color:rgba(255,255,255,.45);}}

/* ─────────────────────────────────────────────────
   PREVIEW
───────────────────────────────────────────────── */
.preview-grid{{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(260px,1fr));
  gap:20px;
  margin-top:40px;
}}
.preview-card{{
  background:var(--white);
  border:1px solid var(--border);
  border-radius:var(--r-lg);
  padding:28px 24px;
  transition:box-shadow .25s,transform .25s,border-color .25s;
  cursor:default;
  position:relative;overflow:hidden;
}}
.preview-card::after{{
  content:'';
  position:absolute;bottom:0;left:0;right:0;height:3px;
  background:linear-gradient(to right,var(--violet),var(--accent));
  opacity:0;
  transition:opacity .25s;
}}
.preview-card:hover{{
  box-shadow:var(--shadow-lg);
  transform:translateY(-4px);
  border-color:transparent;
}}
.preview-card:hover::after{{opacity:1;}}
.preview-emoji{{font-size:32px;margin-bottom:14px;display:block;}}
.preview-ch{{font-size:10px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-bottom:4px;}}
.preview-title{{font-size:16px;font-weight:700;margin-bottom:12px;color:var(--ink);}}
.preview-text{{
  font-family:'DM Serif Display',serif;
  font-size:15px;line-height:1.75;color:var(--ink2);font-style:italic;
}}

/* ─────────────────────────────────────────────────
   AUTHOR
───────────────────────────────────────────────── */
.author-band{{background:var(--cream);}}
.author-inner{{
  display:grid;
  grid-template-columns:auto 1fr;
  gap:40px;align-items:center;
}}
.author-avatar{{
  width:120px;height:120px;
  border-radius:50%;
  background:linear-gradient(135deg,var(--violet) 0%,var(--accent) 100%);
  display:flex;align-items:center;justify-content:center;
  font-size:52px;
  flex-shrink:0;
  box-shadow:var(--shadow-md);
}}
.author-name{{font-size:26px;font-weight:900;margin-bottom:4px;}}
.author-tag{{font-size:13px;color:var(--accent);font-weight:600;margin-bottom:14px;}}
.author-bio{{font-size:15px;color:var(--ink2);line-height:1.75;max-width:560px;}}
.author-stats{{display:flex;gap:32px;margin-top:20px;flex-wrap:wrap;}}
.astat-num{{font-family:'Playfair Display',serif;font-size:28px;font-weight:700;color:var(--violet);line-height:1;}}
.astat-lbl{{font-size:11px;color:var(--ink3);margin-top:2px;}}

/* ─────────────────────────────────────────────────
   RIDDLE
───────────────────────────────────────────────── */
.riddle-box{{
  background:var(--white);
  border:1px solid var(--border);
  border-radius:var(--r-lg);
  padding:40px;
  max-width:660px;margin:40px auto 0;
  text-align:center;
  box-shadow:var(--shadow);
}}
.riddle-counter{{
  font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink3);margin-bottom:20px;
}}
.riddle-q{{
  font-family:'Playfair Display',serif;
  font-size:20px;color:var(--ink);
  margin-bottom:28px;line-height:1.45;
}}
.riddle-opts{{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:20px;}}
.riddle-opt{{
  padding:11px 24px;
  border:2px solid var(--border);
  border-radius:50px;
  background:#fff;color:var(--ink);
  font-size:15px;font-weight:600;
  cursor:pointer;
  transition:all .2s;
  font-family:'DM Sans',sans-serif;
}}
.riddle-opt:hover:not(:disabled){{border-color:var(--violet);color:var(--violet);}}
.riddle-opt.correct{{border-color:var(--green);background:#E8F5ED;color:var(--green);}}
.riddle-opt.wrong{{border-color:#C0392B;background:#FDECEC;color:#C0392B;}}
.riddle-opt:disabled{{cursor:default;}}
.riddle-result{{
  min-height:40px;font-size:14px;line-height:1.6;
  color:var(--ink2);padding:0 8px;
  transition:all .3s;
}}
.riddle-next{{
  margin-top:16px;
  padding:10px 22px;
  border-radius:50px;
  border:1px solid var(--border);
  background:#fff;color:var(--ink2);
  font-size:13px;font-weight:600;cursor:pointer;
  font-family:'DM Sans',sans-serif;
  transition:all .2s;
}}
.riddle-next:hover{{border-color:var(--violet);color:var(--violet);}}

/* ─────────────────────────────────────────────────
   ORDER MODAL
───────────────────────────────────────────────── */
.overlay{{
  display:none;
  position:fixed;inset:0;
  background:rgba(0,0,0,.55);
  z-index:2000;
  align-items:center;justify-content:center;
  backdrop-filter:blur(4px);
}}
.overlay.open{{display:flex;}}

.modal{{
  background:#fff;
  border-radius:var(--r-lg);
  width:min(520px,92vw);
  max-height:90vh;overflow-y:auto;
  box-shadow:0 24px 64px rgba(0,0,0,.25);
  position:relative;
  animation:modal-in .25s ease;
}}
@keyframes modal-in{{
  from{{opacity:0;transform:translateY(16px);}}
  to{{opacity:1;transform:none;}}
}}
.modal-close{{
  position:absolute;top:16px;right:20px;
  background:none;border:none;cursor:pointer;
  font-size:22px;color:var(--ink3);
  line-height:1;padding:4px;
  transition:color .2s;
}}
.modal-close:hover{{color:var(--ink);}}

.modal-header{{
  padding:28px 32px 20px;
  border-bottom:1px solid var(--border);
}}
.modal-title{{font-size:20px;font-weight:700;margin-bottom:4px;}}
.modal-sub{{font-size:13px;color:var(--ink3);}}

.modal-body{{padding:24px 32px;}}

/* Step tabs */
.steps{{display:flex;gap:0;margin-bottom:28px;border:1px solid var(--border);border-radius:var(--r);overflow:hidden;}}
.step-tab{{
  flex:1;padding:10px 4px;text-align:center;
  font-size:12px;font-weight:600;color:var(--ink3);
  background:#fff;position:relative;
  transition:all .2s;
}}
.step-tab.active{{background:var(--violet);color:#fff;}}
.step-tab .step-num{{
  display:block;font-size:16px;font-weight:700;margin-bottom:2px;
}}

/* Forms */
.form-field{{margin-bottom:16px;}}
.form-label{{font-size:12px;font-weight:600;color:var(--ink2);margin-bottom:6px;display:block;}}
.form-input{{
  width:100%;padding:11px 14px;
  border:1.5px solid var(--border);border-radius:var(--r);
  font-size:14px;font-family:'DM Sans',sans-serif;color:var(--ink);
  transition:border-color .2s;outline:none;
  background:#fff;
}}
.form-input:focus{{border-color:var(--violet);}}
.form-row{{display:grid;grid-template-columns:1fr 1fr;gap:12px;}}

/* QR section */
.qr-section{{
  background:var(--cream);
  border-radius:var(--r);
  padding:24px;text-align:center;
  margin-bottom:20px;
}}
.qr-amount{{
  font-family:'Playfair Display',serif;
  font-size:32px;font-weight:700;color:var(--ink);margin-bottom:4px;
}}
.qr-upi{{font-size:13px;color:var(--ink3);margin-bottom:16px;}}
.qr-img{{
  width:160px;height:160px;
  border:1px solid var(--border);border-radius:var(--r);
  background:#fff;margin:0 auto 12px;
  display:flex;align-items:center;justify-content:center;
  padding:8px;
}}
.qr-img svg{{width:100%;height:100%;}}
.pay-methods{{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;}}
.pay-chip{{
  padding:6px 14px;background:#fff;
  border:1px solid var(--border);border-radius:8px;
  font-size:12px;font-weight:600;color:var(--ink2);
}}
.confirm-note{{
  font-size:13px;color:var(--ink3);
  line-height:1.65;margin-top:16px;
  padding:12px 16px;
  background:#F8F4FF;
  border-left:3px solid var(--violet);
  border-radius:0 var(--r) var(--r) 0;
}}

/* Screenshot upload */
.upload-area{{
  border:2px dashed var(--border);
  border-radius:var(--r);
  padding:28px;text-align:center;
  cursor:pointer;
  transition:border-color .2s,background .2s;
  margin-bottom:16px;
}}
.upload-area:hover{{border-color:var(--violet);background:#F8F4FF;}}
.upload-area input{{display:none;}}
.upload-icon{{font-size:32px;margin-bottom:8px;}}
.upload-label{{font-size:14px;font-weight:600;color:var(--ink2);}}
.upload-sub{{font-size:12px;color:var(--ink3);margin-top:4px;}}

.btn-full{{
  width:100%;justify-content:center;padding:15px;font-size:15px;
}}
.btn-whatsapp{{
  display:flex;align-items:center;gap:8px;
  padding:13px 20px;border-radius:var(--r);
  background:#25D366;color:#fff;font-weight:600;font-size:14px;
  text-decoration:none;font-family:'DM Sans',sans-serif;
  transition:filter .2s;margin-bottom:12px;
  justify-content:center;
}}
.btn-whatsapp:hover{{filter:brightness(.92);}}

/* success */
.success-box{{
  text-align:center;padding:20px 0;display:none;
}}
.success-icon{{font-size:56px;margin-bottom:16px;}}
.success-title{{font-size:22px;font-weight:700;margin-bottom:8px;}}
.success-sub{{font-size:14px;color:var(--ink3);line-height:1.65;}}

/* ─────────────────────────────────────────────────
   CTA STRIP
───────────────────────────────────────────────── */
.cta-strip{{
  background:var(--ink);
  padding:56px 0;
  text-align:center;
  color:#fff;
}}
.cta-strip h2{{color:#fff;font-size:clamp(24px,3vw,36px);margin-bottom:8px;}}
.cta-strip p{{font-size:16px;color:rgba(255,255,255,.55);margin-bottom:32px;}}

/* ─────────────────────────────────────────────────
   RESPONSIVE
───────────────────────────────────────────────── */
@media(max-width:700px){{
  .hero-inner{{grid-template-columns:1fr;}}
  .book-card{{display:none;}}
  .author-inner{{grid-template-columns:1fr;text-align:center;}}
  .author-avatar{{margin:0 auto;}}
  .author-stats{{justify-content:center;}}
  .form-row{{grid-template-columns:1fr;}}
  .modal-body,.modal-header{{padding-left:20px;padding-right:20px;}}
}}
@media(max-width:500px){{
  .btn{{padding:12px 18px;}}
  .section{{padding:52px 0;}}
}}
</style>
</head>
<body>

<!-- ══════════════════════════════════════════════
     HERO
═══════════════════════════════════════════════ -->
<section class="hero">
  <div class="container">
    <div class="hero-inner">

      <!-- LEFT -->
      <div class="hero-left">
        <div class="hero-eyebrow">
          <span class="dot"></span> Now Available · Physical &amp; Digital
        </div>
        <h1>The Secret<br><em>Kingdom</em> of Numbers</h1>
        <p class="hero-tagline">"{BOOK['tagline']}"</p>
        <p class="hero-desc">{BOOK['description']}</p>
        <div class="hero-meta">
          <div class="meta-chip"><span class="ic">📚</span> {BOOK['pages']} pages</div>
          <div class="meta-chip"><span class="ic">🎭</span> {BOOK['genre']}</div>
          <div class="meta-chip"><span class="ic">🏷️</span> Ages 8–14</div>
          <div class="meta-chip"><span class="ic">📍</span> {BOOK['city']}</div>
        </div>
        <div class="btn-group">
          <button class="btn btn-primary" onclick="openOrder('physical')">
            <span>📦</span>
            <span class="btn-col">
              <span class="btn-price">₹{BOOK['physical_price']}</span>
              <span class="btn-sub">Physical Copy</span>
            </span>
          </button>
          <button class="btn btn-secondary" onclick="openOrder('digital')">
            <span>⚡</span>
            <span class="btn-col">
              <span class="btn-price">₹{BOOK['digital_price']}</span>
              <span class="btn-sub">Digital PDF</span>
            </span>
          </button>
        </div>
      </div>

      <!-- RIGHT — book mockup -->
      <div class="book-card">
        <div class="book-cover">
          <div class="book-cover-inner">
            <span class="book-emoji">🏰✨</span>
            <div class="book-cover-title">{BOOK['title']}</div>
            <div class="book-cover-author">— {BOOK['author']} —</div>
          </div>
        </div>
        <div class="book-card-label">Written by</div>
        <div class="book-card-title">{BOOK['author']}</div>
        <div class="book-card-sub">{BOOK['grade']} · {BOOK['age']} years · {BOOK['city']}</div>
      </div>

    </div>
  </div>
</section>

<hr class="divider">

<!-- ══════════════════════════════════════════════
     PREVIEW
═══════════════════════════════════════════════ -->
<section class="section">
  <div class="container">
    <div class="label">👀 Sneak Peek</div>
    <h2 style="font-size:clamp(26px,3.5vw,38px);">A glimpse inside the Kingdom</h2>
    <div class="preview-grid">
      {''.join(f"""
      <div class="preview-card">
        <span class="preview-emoji">{p['emoji']}</span>
        <div class="preview-ch">{p['chapter']}</div>
        <div class="preview-title">{p['title']}</div>
        <p class="preview-text">{p['text']}</p>
      </div>
      """ for p in BOOK['preview'])}
    </div>
  </div>
</section>

<hr class="divider">

<!-- ══════════════════════════════════════════════
     AUTHOR
═══════════════════════════════════════════════ -->
<div class="author-band">
<section class="section-sm">
  <div class="container">
    <div class="author-inner">
      <div class="author-avatar">🧒</div>
      <div>
        <div class="label">✍️ About the Author</div>
        <div class="author-name">{BOOK['author']}</div>
        <div class="author-tag">{BOOK['grade']} · {BOOK['age']} years old · {BOOK['city']}</div>
        <p class="author-bio">{BOOK['author_bio']}</p>
        <div class="author-stats">
          <div class="astat">
            <div class="astat-num">1st</div>
            <div class="astat-lbl">Published Book</div>
          </div>
          <div class="astat">
            <div class="astat-num">{BOOK['age']}</div>
            <div class="astat-lbl">Years Young</div>
          </div>
          <div class="astat">
            <div class="astat-num">{BOOK['pages']}</div>
            <div class="astat-lbl">Pages Written</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
</div>

<hr class="divider">

<!-- ══════════════════════════════════════════════
     RIDDLE GAME
═══════════════════════════════════════════════ -->
<section class="section">
  <div class="container" style="text-align:center;">
    <div class="label">🧩 Number Kingdom Challenge</div>
    <h2 style="font-size:clamp(24px,3vw,36px);margin-bottom:8px;">Can you solve a riddle from the book?</h2>
    <p style="color:var(--ink3);font-size:15px;max-width:480px;margin:0 auto;">
      Every chapter hides a mathematical secret. Try yours below.
    </p>
    <div class="riddle-box">
      <div class="riddle-counter" id="riddleCounter"></div>
      <div class="riddle-q" id="riddleQ"></div>
      <div class="riddle-opts" id="riddleOpts"></div>
      <div class="riddle-result" id="riddleResult"></div>
      <button class="riddle-next" onclick="nextRiddle()">Next riddle →</button>
    </div>
  </div>
</section>

<!-- ══════════════════════════════════════════════
     CTA STRIP
═══════════════════════════════════════════════ -->
<div class="cta-strip">
  <div class="container">
    <h2>Ready to enter the Kingdom?</h2>
    <p>Every great mathematician started with a great story.</p>
    <div class="btn-group" style="justify-content:center;">
      <button class="btn btn-primary" onclick="openOrder('physical')" style="font-size:16px;padding:16px 28px;">
        <span>📦</span>
        <span class="btn-col">
          <span class="btn-price">₹{BOOK['physical_price']}</span>
          <span class="btn-sub">Physical Copy · Delivered</span>
        </span>
      </button>
      <button class="btn" onclick="openOrder('digital')" style="background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.25);font-size:16px;padding:16px 28px;">
        <span>⚡</span>
        <span class="btn-col">
          <span class="btn-price">₹{BOOK['digital_price']}</span>
          <span class="btn-sub">Digital PDF · Emailed</span>
        </span>
      </button>
    </div>
  </div>
</div>


<!-- ══════════════════════════════════════════════
     ORDER MODAL
═══════════════════════════════════════════════ -->
<div class="overlay" id="overlay" onclick="overlayClick(event)">
  <div class="modal" id="modal">
    <button class="modal-close" onclick="closeModal()">✕</button>

    <div class="modal-header">
      <div class="modal-title" id="modalTitle">Order your copy</div>
      <div class="modal-sub" id="modalSub"></div>
    </div>

    <div class="modal-body">

      <!-- STEP INDICATOR -->
      <div class="steps">
        <div class="step-tab active" id="tab1"><span class="step-num">1</span>Your Details</div>
        <div class="step-tab" id="tab2"><span class="step-num">2</span>Pay</div>
        <div class="step-tab" id="tab3"><span class="step-num">3</span>Confirm</div>
      </div>

      <!-- STEP 1: DETAILS -->
      <div id="step1">
        <div class="form-field">
          <label class="form-label">Full Name *</label>
          <input class="form-input" id="f_name" type="text" placeholder="e.g. Priya Mehta">
        </div>
        <div class="form-field">
          <label class="form-label">Email Address *</label>
          <input class="form-input" id="f_email" type="email" placeholder="e.g. priya@gmail.com">
          <div style="font-size:11px;color:var(--ink3);margin-top:4px;" id="emailNote"></div>
        </div>
        <div class="form-field">
          <label class="form-label">WhatsApp / Phone *</label>
          <input class="form-input" id="f_phone" type="tel" placeholder="e.g. 9876543210">
        </div>
        <div id="addressFields">
          <div class="form-field">
            <label class="form-label">Delivery Address *</label>
            <input class="form-input" id="f_addr" type="text" placeholder="Flat / House No., Building, Street">
          </div>
          <div class="form-row">
            <div class="form-field">
              <label class="form-label">City *</label>
              <input class="form-input" id="f_city" type="text" placeholder="Pune">
            </div>
            <div class="form-field">
              <label class="form-label">PIN Code *</label>
              <input class="form-input" id="f_pin" type="text" placeholder="411001" maxlength="6">
            </div>
          </div>
        </div>
        <button class="btn btn-primary btn-full" onclick="goToStep2()">Continue to Payment →</button>
      </div>

      <!-- STEP 2: PAY -->
      <div id="step2" style="display:none;">
        <div class="qr-section">
          <div class="qr-amount" id="payAmount"></div>
          <div class="qr-upi">UPI ID: <strong>{BOOK['upi_id']}</strong></div>
          <div class="qr-img">
            <!-- Functional-looking QR placeholder — replace with real UPI QR image -->
            <svg viewBox="0 0 144 144" xmlns="http://www.w3.org/2000/svg">
              <rect width="144" height="144" fill="white"/>
              <!-- Top-left finder -->
              <rect x="8" y="8" width="42" height="42" rx="4" fill="none" stroke="#111" stroke-width="4"/>
              <rect x="16" y="16" width="26" height="26" rx="2" fill="#111"/>
              <!-- Top-right finder -->
              <rect x="94" y="8" width="42" height="42" rx="4" fill="none" stroke="#111" stroke-width="4"/>
              <rect x="102" y="16" width="26" height="26" rx="2" fill="#111"/>
              <!-- Bottom-left finder -->
              <rect x="8" y="94" width="42" height="42" rx="4" fill="none" stroke="#111" stroke-width="4"/>
              <rect x="16" y="102" width="26" height="26" rx="2" fill="#111"/>
              <!-- Center logo -->
              <rect x="56" y="56" width="32" height="32" rx="6" fill="#3D2B6E"/>
              <text x="72" y="78" font-size="18" text-anchor="middle" fill="white">📖</text>
              <!-- Data modules (decorative) -->
              <rect x="58" y="8" width="6" height="6" fill="#111"/><rect x="68" y="8" width="6" height="6" fill="#111"/>
              <rect x="78" y="8" width="6" height="6" fill="#111"/><rect x="58" y="18" width="6" height="6" fill="#111"/>
              <rect x="78" y="18" width="6" height="6" fill="#111"/><rect x="68" y="28" width="6" height="6" fill="#111"/>
              <rect x="58" y="38" width="6" height="6" fill="#111"/><rect x="68" y="38" width="6" height="6" fill="#111"/>
              <rect x="78" y="38" width="6" height="6" fill="#111"/>
              <rect x="8" y="58" width="6" height="6" fill="#111"/><rect x="18" y="68" width="6" height="6" fill="#111"/>
              <rect x="28" y="58" width="6" height="6" fill="#111"/><rect x="38" y="68" width="6" height="6" fill="#111"/>
              <rect x="8" y="78" width="6" height="6" fill="#111"/><rect x="28" y="78" width="6" height="6" fill="#111"/>
              <rect x="8" y="88" width="6" height="6" fill="#111"/>
              <rect x="98" y="58" width="6" height="6" fill="#111"/><rect x="108" y="68" width="6" height="6" fill="#111"/>
              <rect x="128" y="58" width="6" height="6" fill="#111"/><rect x="98" y="78" width="6" height="6" fill="#111"/>
              <rect x="118" y="78" width="6" height="6" fill="#111"/><rect x="128" y="88" width="6" height="6" fill="#111"/>
              <rect x="58" y="98" width="6" height="6" fill="#111"/><rect x="78" y="98" width="6" height="6" fill="#111"/>
              <rect x="68" y="108" width="6" height="6" fill="#111"/><rect x="58" y="118" width="6" height="6" fill="#111"/>
              <rect x="78" y="118" width="6" height="6" fill="#111"/>
            </svg>
          </div>
          <div class="pay-methods">
            <span class="pay-chip">📱 GPay</span>
            <span class="pay-chip">💳 PhonePe</span>
            <span class="pay-chip">🔵 Paytm</span>
            <span class="pay-chip">💵 Cash</span>
          </div>
        </div>
        <div class="confirm-note" id="payNote"></div>
        <div style="display:flex;gap:10px;margin-top:16px;">
          <button class="btn" style="background:#fff;color:var(--ink);border:1px solid var(--border);flex:1;" onclick="goToStep(1)">← Back</button>
          <button class="btn btn-primary" style="flex:2;" onclick="goToStep3()">I have paid →</button>
        </div>
      </div>

      <!-- STEP 3: CONFIRM -->
      <div id="step3" style="display:none;">
        <p style="font-size:14px;color:var(--ink2);margin-bottom:16px;line-height:1.65;">
          Please send your payment screenshot via WhatsApp to confirm your order.
          Once confirmed, <span id="deliveryNote"></span>
        </p>
        <a class="btn-whatsapp" id="whatsappLink" href="#" target="_blank">
          <span>📲</span> Send Screenshot on WhatsApp
        </a>
        <div class="upload-area" onclick="document.getElementById('screenshotInput').click()">
          <input type="file" id="screenshotInput" accept="image/*" onchange="fileSelected(this)">
          <div class="upload-icon">📸</div>
          <div class="upload-label" id="uploadLabel">Upload Payment Screenshot</div>
          <div class="upload-sub">JPG, PNG · Optional — WhatsApp is faster</div>
        </div>
        <div class="confirm-note">
          📧 <strong id="digitalNote"></strong>
        </div>
        <button class="btn btn-primary btn-full" style="margin-top:16px;" onclick="submitOrder()">✓ Submit my Order</button>
        <div style="display:flex;gap:10px;margin-top:10px;">
          <button class="btn" style="background:#fff;color:var(--ink);border:1px solid var(--border);flex:1;" onclick="goToStep(2)">← Back</button>
        </div>
      </div>

      <!-- SUCCESS -->
      <div class="success-box" id="successBox">
        <div class="success-icon">🎉</div>
        <div class="success-title">Order Submitted!</div>
        <p class="success-sub" id="successMsg"></p>
      </div>

    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════
     SCRIPTS
═══════════════════════════════════════════════ -->
<script>
// ── RIDDLES ────────────────────────────────────────────────────────────────────
const RIDDLES = {riddles_json};
let ridIdx = 0;

function loadRiddle() {{
  const r = RIDDLES[ridIdx];
  document.getElementById('riddleCounter').textContent =
    'Riddle ' + (ridIdx+1) + ' of ' + RIDDLES.length;
  document.getElementById('riddleQ').textContent = r.q;
  document.getElementById('riddleResult').innerHTML = '';
  const opts = document.getElementById('riddleOpts');
  opts.innerHTML = '';
  r.opts.forEach((o, i) => {{
    const b = document.createElement('button');
    b.className = 'riddle-opt';
    b.textContent = o;
    b.onclick = () => checkRiddle(i);
    opts.appendChild(b);
  }});
}}
function checkRiddle(idx) {{
  const r = RIDDLES[ridIdx];
  document.querySelectorAll('.riddle-opt').forEach((b, i) => {{
    if (i === r.correct) b.classList.add('correct');
    else if (i === idx) b.classList.add('wrong');
    b.disabled = true;
  }});
  const res = document.getElementById('riddleResult');
  res.innerHTML = (idx === r.correct)
    ? '<strong style="color:var(--green)">🎉 Correct!</strong> ' + r.fact
    : '<strong style="color:#C0392B">Not quite!</strong> ' + r.fact;
}}
function nextRiddle() {{
  ridIdx = (ridIdx + 1) % RIDDLES.length;
  loadRiddle();
}}
loadRiddle();

// ── ORDER MODAL ────────────────────────────────────────────────────────────────
let orderType = 'physical';

function openOrder(type) {{
  orderType = type;
  // reset to step 1
  goToStep(1);
  document.getElementById('step1').style.display = 'block';
  document.getElementById('step2').style.display = 'none';
  document.getElementById('step3').style.display = 'none';
  document.getElementById('successBox').style.display = 'none';
  document.querySelectorAll('.step-tab').forEach((t,i) => t.classList.toggle('active', i===0));

  if (type === 'physical') {{
    document.getElementById('modalTitle').textContent = '📦 Order Physical Copy';
    document.getElementById('modalSub').textContent = 'Delivered to your doorstep · ₹{BOOK['physical_price']}';
    document.getElementById('addressFields').style.display = 'block';
    document.getElementById('emailNote').textContent = 'Order confirmation will be sent here.';
  }} else {{
    document.getElementById('modalTitle').textContent = '⚡ Order Digital PDF';
    document.getElementById('modalSub').textContent = 'Emailed after payment confirmation · ₹{BOOK['digital_price']}';
    document.getElementById('addressFields').style.display = 'none';
    document.getElementById('emailNote').textContent = '📧 The PDF will be sent to this email after we confirm your payment.';
  }}

  document.getElementById('overlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}}

function closeModal() {{
  document.getElementById('overlay').classList.remove('open');
  document.body.style.overflow = '';
}}
function overlayClick(e) {{
  if (e.target === document.getElementById('overlay')) closeModal();
}}
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closeModal(); }});

function goToStep(n) {{
  [1,2,3].forEach(i => {{
    document.getElementById('step'+i).style.display = (i===n) ? 'block' : 'none';
    document.getElementById('tab'+i).classList.toggle('active', i===n);
  }});
}}

function goToStep2() {{
  // basic validation
  const name  = document.getElementById('f_name').value.trim();
  const email = document.getElementById('f_email').value.trim();
  const phone = document.getElementById('f_phone').value.trim();
  if (!name || !email || !phone) {{
    alert('Please fill in your name, email, and phone number.');
    return;
  }}
  if (orderType === 'physical') {{
    const addr = document.getElementById('f_addr').value.trim();
    const city = document.getElementById('f_city').value.trim();
    const pin  = document.getElementById('f_pin').value.trim();
    if (!addr || !city || !pin) {{
      alert('Please fill in your delivery address.');
      return;
    }}
  }}

  const price = orderType === 'physical' ? '₹{BOOK['physical_price']}' : '₹{BOOK['digital_price']}';
  document.getElementById('payAmount').textContent = price;

  const note = orderType === 'physical'
    ? 'After we confirm your payment, your physical book will be dispatched within 1–2 working days.'
    : 'After we confirm your payment screenshot, the PDF will be emailed to you within a few hours.';
  document.getElementById('payNote').textContent = note;

  goToStep(2);
}}

function goToStep3() {{
  const name  = document.getElementById('f_name').value.trim();
  const phone = document.getElementById('f_phone').value.trim();
  const email = document.getElementById('f_email').value.trim();
  const price = orderType === 'physical' ? '₹{BOOK['physical_price']}' : '₹{BOOK['digital_price']}';
  const typeStr = orderType === 'physical' ? 'Physical Copy' : 'Digital PDF';

  const msg = encodeURIComponent(
    `Hi! I just paid *${{price}}* for *{BOOK['title']}* (${{typeStr}}).\\n\\nName: ${{name}}\\nPhone: ${{phone}}\\nEmail: ${{email}}\\n\\nScreenshot attached! Please confirm my order 🙏`
  );
  document.getElementById('whatsappLink').href =
    'https://wa.me/{BOOK['whatsapp']}?text=' + msg;

  if (orderType === 'digital') {{
    document.getElementById('deliveryNote').textContent =
      'the PDF will be emailed to ' + email + ' once payment is confirmed.';
    document.getElementById('digitalNote').textContent =
      'Digital book: we will email your PDF to ' + email + ' after confirming your payment.';
  }} else {{
    document.getElementById('deliveryNote').textContent =
      'your book will be dispatched within 1–2 working days.';
    document.getElementById('digitalNote').textContent =
      'Your order confirmation will be sent to ' + email + '.';
  }}

  goToStep(3);
}}

function fileSelected(input) {{
  if (input.files && input.files[0]) {{
    document.getElementById('uploadLabel').textContent = '✅ ' + input.files[0].name;
  }}
}}

function submitOrder() {{
  // Hide all steps, show success
  [1,2,3].forEach(i => document.getElementById('step'+i).style.display = 'none');
  document.querySelectorAll('.step-tab').forEach(t => t.classList.remove('active'));
  document.getElementById('successBox').style.display = 'block';

  const name = document.getElementById('f_name').value.trim();
  const email = document.getElementById('f_email').value.trim();
  const msg = orderType === 'digital'
    ? `Thank you, ${{name}}! 🎉 Once we confirm your payment, the PDF will be sent to ${{email}}. We'll WhatsApp you too!`
    : `Thank you, ${{name}}! 🎉 Your book will be dispatched in 1–2 days. We'll WhatsApp you with the tracking update!`;
  document.getElementById('successMsg').textContent = msg;
}}
</script>
</body>
</html>"""

components.html(html, height=6000, scrolling=False)
