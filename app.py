import streamlit as st
import streamlit.components.v1 as components

# ─── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="The Enchanted Book",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── BOOK DATA — edit these to match the real book ─────────────────────────────
BOOK = {
    "title": "The Secret Kingdom of Numbers",
    "subtitle": "A Mathematical Adventure Beyond Imagination",
    "author": "Aryan Sharma",
    "age": 13,
    "grade": "Class 8",
    "city": "Pune, India",
    "pages": 124,
    "genre": "Math · Adventure · Fantasy",
    "tagline": "What if every number had a superpower?",
    "description": (
        "Dive into a magical world where Prime Numbers guard ancient castles, "
        "Fractions build rainbow bridges, and the fearless hero Zero discovers "
        "that nothing can be the most powerful thing of all. Packed with real math "
        "tricks hidden inside an epic quest — this book makes you fall in love with "
        "numbers forever."
    ),
    "preview_pages": [
        {
            "title": "Chapter 1 · The Gate of Infinity",
            "text": (
                "The old wooden door was carved with a thousand spirals. "
                "Each spiral was a number, and each number whispered a secret. "
                "Aryan touched the door and felt a tingle — like electricity, "
                "but made of mathematics. 'To enter,' said the Guardian, "
                "'you must answer: what number is both odd and even?' "
                "Aryan smiled. He already knew the answer was hiding in plain sight..."
            ),
            "emoji": "🚪",
        },
        {
            "title": "Chapter 4 · The Fraction Forest",
            "text": (
                "Half the trees were tall, a quarter were golden, and one-eighth "
                "glowed violet at night. The forest itself was a living fraction — "
                "always adding up to one whole, no matter how you split it. "
                "'That's the beauty,' whispered the ancient Fraction Fairy. "
                "'We are pieces, but together we are complete. Just like you and your friends.'"
            ),
            "emoji": "🌳",
        },
        {
            "title": "Chapter 9 · Zero's Secret Power",
            "text": (
                "Everyone laughed at Zero. 'You are nothing!' they said. "
                "But Zero just smiled. With one quiet step, Zero stood beside One — "
                "and suddenly One became Ten. Then Hundred. Then Thousand. "
                "'Nothing,' said Zero, 'can become everything. That is my superpower.'"
            ),
            "emoji": "⭕",
        },
    ],
    "physical_price": 299,
    "digital_price": 99,
    "currency": "₹",
    "gpay_upi": "aryan@oksbi",   # ← replace with real UPI ID
    "seller_phone": "9876543210", # ← replace with real number
    "whatsapp": "9876543210",    # ← replace
    "cover_gradient": "linear-gradient(135deg, #1a1a2e 0%, #16213e 40%, #0f3460 70%, #533483 100%)",
    "star_count": 48,
}

# ─── INJECT FULL-PAGE MAGIC HTML ───────────────────────────────────────────────
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{BOOK['title']}</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&family=Nunito:wght@400;600;700;800&family=Crimson+Pro:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
/* ───────────── ROOT & RESET ───────────── */
:root{{
  --ink: #0d0d1a;
  --deep: #090915;
  --violet: #533483;
  --violet2: #7b52ab;
  --cyan: #00d4ff;
  --gold: #ffd700;
  --gold2: #ffb300;
  --rose: #ff6b9d;
  --cream: #fef9ec;
  --cream2: #fdf3d4;
  --text: #e8e0ff;
  --muted: rgba(232,224,255,0.55);
  --card-bg: rgba(255,255,255,0.04);
  --card-border: rgba(255,255,255,0.10);
  --glow: 0 0 40px rgba(83,52,131,0.6);
}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{
  font-family:'Nunito',sans-serif;
  background:var(--deep);
  color:var(--text);
  overflow-x:hidden;
  cursor:none;
}}

/* ───────────── MAGIC CURSOR ───────────── */
#cursor{{
  width:14px;height:14px;
  border-radius:50%;
  background:var(--gold);
  position:fixed;pointer-events:none;z-index:99999;
  mix-blend-mode:screen;
  transition:transform 0.15s ease,opacity 0.3s;
  box-shadow:0 0 16px var(--gold),0 0 32px rgba(255,215,0,0.4);
}}
#cursor-trail{{
  width:32px;height:32px;
  border-radius:50%;
  border:2px solid var(--violet2);
  position:fixed;pointer-events:none;z-index:99998;
  transition:all 0.12s ease;
  box-shadow:0 0 8px var(--violet);
}}

/* ───────────── STAR CANVAS ───────────── */
#starfield{{
  position:fixed;top:0;left:0;width:100%;height:100%;
  pointer-events:none;z-index:0;
}}

/* ───────────── HERO ───────────── */
.hero{{
  min-height:100vh;
  display:flex;
  align-items:center;
  justify-content:center;
  padding:60px 24px;
  position:relative;
  z-index:2;
  overflow:hidden;
}}
.hero-glow{{
  position:absolute;
  width:700px;height:700px;
  border-radius:50%;
  background:radial-gradient(circle,rgba(83,52,131,0.35) 0%,transparent 70%);
  top:50%;left:50%;
  transform:translate(-50%,-50%);
  pointer-events:none;
  animation:pulse 4s ease-in-out infinite;
}}
@keyframes pulse{{
  0%,100%{{transform:translate(-50%,-50%) scale(1);opacity:0.6;}}
  50%{{transform:translate(-50%,-50%) scale(1.15);opacity:1;}}
}}
.hero-inner{{
  display:flex;
  align-items:center;
  gap:80px;
  max-width:1100px;
  width:100%;
}}

/* FLOATING BOOK */
.book-wrap{{
  flex-shrink:0;
  position:relative;
  animation:float 6s ease-in-out infinite;
}}
@keyframes float{{
  0%,100%{{transform:translateY(0) rotateY(-8deg) rotateX(5deg);}}
  50%{{transform:translateY(-22px) rotateY(-8deg) rotateX(5deg);}}
}}
.book{{
  width:220px;height:300px;
  position:relative;
  transform-style:preserve-3d;
  perspective:1000px;
  filter:drop-shadow(0 30px 60px rgba(83,52,131,0.8));
}}
.book-cover{{
  width:220px;height:300px;
  border-radius:4px 16px 16px 4px;
  background:{BOOK['cover_gradient']};
  position:relative;
  overflow:hidden;
  border:1px solid rgba(255,215,0,0.3);
}}
.book-cover::before{{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(255,255,255,0.12) 0%,transparent 50%);
}}
.book-cover::after{{
  content:'';position:absolute;
  left:0;top:0;bottom:0;width:18px;
  background:linear-gradient(to right,rgba(0,0,0,0.4),rgba(83,52,131,0.3));
  border-radius:4px 0 0 4px;
}}
.book-spine-text{{
  position:absolute;left:0;top:0;bottom:0;width:18px;
  display:flex;align-items:center;justify-content:center;
  writing-mode:vertical-rl;
  font-size:9px;font-weight:800;
  color:rgba(255,255,255,0.4);
  letter-spacing:0.2em;
  text-transform:uppercase;
  z-index:2;
}}
.book-stars{{
  position:absolute;top:16px;right:16px;
  font-size:18px;
  animation:twinkle 2s ease-in-out infinite;
}}
@keyframes twinkle{{
  0%,100%{{opacity:1;transform:scale(1);}}
  50%{{opacity:0.6;transform:scale(0.9);}}
}}
.book-title-text{{
  position:absolute;
  bottom:0;left:0;right:0;
  padding:24px 16px 20px;
  background:linear-gradient(to top,rgba(0,0,0,0.9),transparent);
  font-family:'Cinzel Decorative',serif;
  font-size:11px;
  font-weight:700;
  color:var(--gold);
  line-height:1.4;
  text-align:center;
  letter-spacing:0.05em;
}}
.book-author-text{{
  font-family:'Nunito',sans-serif;
  font-size:9px;
  font-weight:600;
  color:rgba(255,255,255,0.5);
  margin-top:4px;
  letter-spacing:0.1em;
}}

/* Orbiting badge */
.orbit-badge{{
  position:absolute;
  top:-20px;right:-20px;
  width:64px;height:64px;
  background:var(--gold);
  border-radius:50%;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  font-size:9px;font-weight:900;
  color:#000;
  line-height:1.2;
  text-align:center;
  animation:spin-badge 8s linear infinite;
  box-shadow:0 0 24px rgba(255,215,0,0.6);
  text-transform:uppercase;
  letter-spacing:0.05em;
  z-index:5;
}}
@keyframes spin-badge{{
  0%{{transform:rotate(0deg);}}
  100%{{transform:rotate(360deg);}}
}}
.orbit-badge span{{
  display:inline-block;
  animation:spin-badge-reverse 8s linear infinite;
}}
@keyframes spin-badge-reverse{{
  0%{{transform:rotate(0deg);}}
  100%{{transform:rotate(-360deg);}}
}}

/* Book shadow */
.book-shadow{{
  width:180px;height:20px;
  background:radial-gradient(ellipse,rgba(83,52,131,0.6) 0%,transparent 70%);
  margin:16px auto 0;
  animation:shadow-pulse 6s ease-in-out infinite;
}}
@keyframes shadow-pulse{{
  0%,100%{{transform:scaleX(1);opacity:0.6;}}
  50%{{transform:scaleX(0.85);opacity:0.3;}}
}}

/* HERO RIGHT */
.hero-right{{flex:1;}}
.hero-badge{{
  display:inline-flex;align-items:center;gap:8px;
  padding:6px 16px;
  border:1px solid rgba(255,215,0,0.3);
  border-radius:40px;
  font-size:11px;font-weight:700;
  color:var(--gold);
  letter-spacing:0.15em;
  text-transform:uppercase;
  margin-bottom:24px;
  background:rgba(255,215,0,0.07);
}}
.hero-badge .dot{{
  width:6px;height:6px;border-radius:50%;
  background:var(--gold);
  animation:blink 1.5s ease-in-out infinite;
}}
@keyframes blink{{
  0%,100%{{opacity:1;}}50%{{opacity:0.3;}}
}}
.hero-h1{{
  font-family:'Cinzel Decorative',serif;
  font-size:clamp(28px,4vw,52px);
  font-weight:900;
  line-height:1.15;
  color:#fff;
  letter-spacing:-0.01em;
  margin-bottom:8px;
}}
.hero-h1 .accent{{color:var(--gold);}}
.hero-tagline{{
  font-size:18px;
  font-weight:600;
  color:var(--rose);
  margin-bottom:20px;
  font-style:italic;
}}
.hero-desc{{
  font-size:15px;
  color:var(--muted);
  line-height:1.85;
  max-width:480px;
  margin-bottom:36px;
  font-family:'Crimson Pro',serif;
  font-size:17px;
}}
.hero-meta{{
  display:flex;gap:24px;margin-bottom:36px;flex-wrap:wrap;
}}
.meta-pill{{
  display:flex;align-items:center;gap:6px;
  font-size:13px;font-weight:700;
  color:rgba(232,224,255,0.7);
}}
.meta-pill span{{font-size:16px;}}

/* BUY BUTTONS */
.buy-group{{
  display:flex;gap:14px;flex-wrap:wrap;
}}
.btn-buy{{
  display:flex;align-items:center;gap:10px;
  padding:16px 28px;
  border-radius:14px;
  font-size:15px;font-weight:800;
  cursor:pointer;
  border:none;
  text-decoration:none;
  transition:all 0.25s ease;
  position:relative;
  overflow:hidden;
  letter-spacing:0.02em;
}}
.btn-buy::before{{
  content:'';
  position:absolute;inset:0;
  background:rgba(255,255,255,0.12);
  opacity:0;
  transition:opacity 0.2s;
}}
.btn-buy:hover::before{{opacity:1;}}
.btn-buy:hover{{transform:translateY(-3px);}}
.btn-physical{{
  background:linear-gradient(135deg,var(--gold) 0%,var(--gold2) 100%);
  color:#000;
  box-shadow:0 8px 30px rgba(255,215,0,0.35);
}}
.btn-digital{{
  background:linear-gradient(135deg,var(--violet) 0%,var(--violet2) 100%);
  color:#fff;
  box-shadow:0 8px 30px rgba(83,52,131,0.4);
}}
.btn-physical:hover{{box-shadow:0 12px 40px rgba(255,215,0,0.55);}}
.btn-digital:hover{{box-shadow:0 12px 40px rgba(83,52,131,0.6);}}
.price-tag{{font-size:20px;font-weight:900;}}
.price-sub{{font-size:11px;font-weight:600;opacity:0.75;display:block;line-height:1;}}

/* ───────────── SECTION WRAPPER ───────────── */
.section{{
  max-width:1100px;
  margin:0 auto;
  padding:80px 24px;
  position:relative;
  z-index:2;
}}
.section-label{{
  font-size:11px;font-weight:800;
  letter-spacing:0.25em;text-transform:uppercase;
  color:var(--cyan);
  margin-bottom:12px;
}}
.section-title{{
  font-family:'Cinzel Decorative',serif;
  font-size:clamp(26px,3.5vw,40px);
  font-weight:700;
  color:#fff;
  margin-bottom:40px;
  line-height:1.2;
}}

/* ───────────── PREVIEW ───────────── */
.preview-bg{{
  background:linear-gradient(180deg,var(--deep) 0%,rgba(83,52,131,0.12) 50%,var(--deep) 100%);
  position:relative;
}}
.preview-cards{{
  display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
  gap:20px;
}}
.prev-card{{
  background:var(--card-bg);
  border:1px solid var(--card-border);
  border-radius:20px;
  padding:28px 24px;
  position:relative;
  overflow:hidden;
  cursor:pointer;
  transition:all 0.3s ease;
}}
.prev-card::before{{
  content:'';
  position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(83,52,131,0.15),transparent);
  opacity:0;
  transition:opacity 0.3s;
}}
.prev-card:hover{{
  border-color:rgba(255,215,0,0.3);
  transform:translateY(-6px);
  box-shadow:0 20px 60px rgba(83,52,131,0.4);
}}
.prev-card:hover::before{{opacity:1;}}
.prev-emoji{{font-size:36px;margin-bottom:12px;display:block;}}
.prev-chapter{{
  font-size:10px;font-weight:800;
  letter-spacing:0.2em;text-transform:uppercase;
  color:var(--cyan);margin-bottom:6px;
}}
.prev-text{{
  font-family:'Crimson Pro',serif;
  font-size:15px;line-height:1.75;
  color:var(--muted);
  font-style:italic;
  position:relative;
}}
.prev-text::before{{
  content:'"';
  font-size:48px;
  color:rgba(255,215,0,0.15);
  font-family:'Cinzel Decorative',serif;
  position:absolute;
  top:-10px;left:-8px;
  line-height:1;
}}
.card-glow{{
  position:absolute;
  bottom:-30px;right:-30px;
  width:100px;height:100px;
  border-radius:50%;
  background:radial-gradient(circle,rgba(83,52,131,0.4),transparent);
  pointer-events:none;
}}

/* ───────────── AUTHOR ───────────── */
.author-bg{{background:rgba(255,255,255,0.02);border-top:1px solid var(--card-border);border-bottom:1px solid var(--card-border);}}
.author-inner{{
  display:flex;
  align-items:center;
  gap:60px;
  max-width:900px;
  margin:0 auto;
  padding:80px 24px;
}}
.author-avatar{{
  flex-shrink:0;
  width:160px;height:160px;
  border-radius:50%;
  background:linear-gradient(135deg,var(--violet) 0%,var(--violet2) 100%);
  display:flex;align-items:center;justify-content:center;
  font-size:72px;
  position:relative;
  box-shadow:0 0 0 6px rgba(83,52,131,0.3),0 0 60px rgba(83,52,131,0.4);
  animation:author-pulse 4s ease-in-out infinite;
}}
@keyframes author-pulse{{
  0%,100%{{box-shadow:0 0 0 6px rgba(83,52,131,0.3),0 0 60px rgba(83,52,131,0.4);}}
  50%{{box-shadow:0 0 0 12px rgba(83,52,131,0.15),0 0 80px rgba(83,52,131,0.6);}}
}}
.author-details{{flex:1;}}
.author-name{{
  font-family:'Cinzel Decorative',serif;
  font-size:28px;font-weight:700;
  color:#fff;margin-bottom:4px;
}}
.author-grade{{
  font-size:13px;font-weight:700;
  color:var(--gold);margin-bottom:16px;
  letter-spacing:0.08em;
}}
.author-bio{{
  font-family:'Crimson Pro',serif;
  font-size:17px;line-height:1.8;
  color:var(--muted);
  margin-bottom:20px;
}}
.author-stats{{display:flex;gap:24px;flex-wrap:wrap;}}
.astat{{text-align:center;}}
.astat-num{{
  font-family:'Cinzel Decorative',serif;
  font-size:28px;font-weight:700;color:var(--cyan);line-height:1;
}}
.astat-lbl{{font-size:11px;color:var(--muted);margin-top:2px;}}

/* ───────────── INTERACTIVE: BOOK ORACLE ───────────── */
.oracle-bg{{
  background:radial-gradient(ellipse at center,rgba(83,52,131,0.2) 0%,transparent 70%);
  border-top:1px solid var(--card-border);
}}
.oracle-wrap{{
  max-width:700px;
  margin:0 auto;
  text-align:center;
}}
.oracle-crystal{{
  font-size:80px;
  display:block;
  margin:0 auto 24px;
  animation:crystal-spin 10s linear infinite;
  cursor:pointer;
  filter:drop-shadow(0 0 20px rgba(83,52,131,0.8));
  transition:transform 0.3s;
}}
.oracle-crystal:hover{{transform:scale(1.15) rotate(10deg);}}
@keyframes crystal-spin{{
  0%{{filter:drop-shadow(0 0 20px rgba(83,52,131,0.8)) hue-rotate(0deg);}}
  100%{{filter:drop-shadow(0 0 20px rgba(0,212,255,0.8)) hue-rotate(360deg);}}
}}
.oracle-title{{
  font-family:'Cinzel Decorative',serif;
  font-size:26px;color:#fff;margin-bottom:8px;
}}
.oracle-sub{{
  font-size:14px;color:var(--muted);margin-bottom:30px;
  font-family:'Crimson Pro',serif;font-size:16px;
}}
.oracle-btn{{
  display:inline-flex;align-items:center;gap:10px;
  padding:16px 36px;
  background:linear-gradient(135deg,var(--violet) 0%,var(--cyan) 100%);
  color:#fff;border:none;border-radius:50px;
  font-size:15px;font-weight:800;
  cursor:pointer;
  letter-spacing:0.05em;
  box-shadow:0 8px 30px rgba(83,52,131,0.5);
  transition:all 0.3s;
  font-family:'Nunito',sans-serif;
}}
.oracle-btn:hover{{transform:translateY(-3px);box-shadow:0 14px 40px rgba(83,52,131,0.7);}}
.oracle-output{{
  margin-top:28px;
  background:var(--card-bg);
  border:1px solid var(--card-border);
  border-radius:20px;
  padding:28px 32px;
  text-align:left;
  display:none;
}}
.oracle-output.visible{{display:block;animation:fade-in 0.6s ease;}}
@keyframes fade-in{{from{{opacity:0;transform:translateY(10px);}}to{{opacity:1;transform:none;}}}}
.oracle-answer{{
  font-family:'Crimson Pro',serif;
  font-size:18px;line-height:1.8;
  color:var(--text);
}}
.oracle-char{{
  display:inline;
  opacity:0;
  animation:char-appear 0.03s ease forwards;
}}

/* ───────────── ACTIVITY: RIDDLE ───────────── */
.riddle-wrap{{
  background:var(--card-bg);
  border:1px solid var(--card-border);
  border-radius:24px;
  padding:40px;
  margin-top:60px;
  text-align:center;
  position:relative;
  overflow:hidden;
}}
.riddle-wrap::before{{
  content:'🔢';
  position:absolute;
  font-size:200px;
  opacity:0.03;
  top:50%;left:50%;
  transform:translate(-50%,-50%);
  pointer-events:none;
}}
.riddle-title{{font-size:20px;font-weight:800;color:var(--gold);margin-bottom:8px;}}
.riddle-q{{
  font-family:'Crimson Pro',serif;
  font-size:19px;color:var(--text);margin-bottom:24px;font-style:italic;
}}
.riddle-options{{
  display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-bottom:20px;
}}
.riddle-opt{{
  padding:12px 28px;
  border:2px solid var(--card-border);
  border-radius:50px;
  background:transparent;
  color:var(--text);
  font-size:16px;font-weight:700;
  cursor:pointer;
  transition:all 0.2s;
  font-family:'Nunito',sans-serif;
}}
.riddle-opt:hover{{border-color:var(--cyan);color:var(--cyan);}}
.riddle-opt.correct{{border-color:var(--gold);background:rgba(255,215,0,0.15);color:var(--gold);}}
.riddle-opt.wrong{{border-color:#ff4757;background:rgba(255,71,87,0.1);color:#ff4757;}}
.riddle-result{{
  font-size:16px;font-weight:700;
  min-height:28px;
  transition:all 0.3s;
}}

/* ───────────── PAYMENT MODAL ───────────── */
.overlay{{
  position:fixed;inset:0;
  background:rgba(0,0,0,0.85);
  z-index:1000;
  display:flex;align-items:center;justify-content:center;
  opacity:0;pointer-events:none;
  transition:opacity 0.3s;
  backdrop-filter:blur(8px);
}}
.overlay.active{{opacity:1;pointer-events:all;}}
.pay-modal{{
  background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);
  border:1px solid rgba(255,215,0,0.3);
  border-radius:28px;
  padding:40px;
  width:min(480px,90vw);
  position:relative;
  box-shadow:0 30px 80px rgba(0,0,0,0.6);
  text-align:center;
}}
.pay-modal h2{{
  font-family:'Cinzel Decorative',serif;
  font-size:22px;color:var(--gold);margin-bottom:6px;
}}
.pay-modal .pay-type{{
  font-size:13px;color:var(--muted);margin-bottom:28px;
}}
.qr-box{{
  width:200px;height:200px;
  background:#fff;
  border-radius:16px;
  margin:0 auto 20px;
  display:flex;align-items:center;justify-content:center;
  padding:12px;
  box-shadow:0 0 40px rgba(255,215,0,0.2);
}}
.qr-box svg{{width:100%;height:100%;}}
.pay-amount{{
  font-family:'Cinzel Decorative',serif;
  font-size:36px;font-weight:700;color:#fff;margin-bottom:4px;
}}
.pay-upi{{
  font-size:13px;color:var(--cyan);margin-bottom:20px;
  font-family:'Crimson Pro',serif;
}}
.pay-methods{{
  display:flex;gap:8px;justify-content:center;margin-bottom:24px;flex-wrap:wrap;
}}
.pay-m{{
  padding:8px 16px;
  background:rgba(255,255,255,0.07);
  border:1px solid var(--card-border);
  border-radius:10px;
  font-size:12px;font-weight:700;
  color:var(--text);
}}
.pay-note{{font-size:12px;color:var(--muted);line-height:1.6;margin-bottom:20px;}}
.pay-close{{
  position:absolute;top:16px;right:20px;
  background:none;border:none;cursor:pointer;
  color:rgba(255,255,255,0.4);
  font-size:24px;line-height:1;
  transition:color 0.2s;
}}
.pay-close:hover{{color:#fff;}}
.btn-whatsapp{{
  display:inline-flex;align-items:center;gap:8px;
  padding:14px 28px;
  background:#25d366;
  color:#fff;border:none;border-radius:12px;
  font-size:14px;font-weight:800;
  cursor:pointer;text-decoration:none;
  transition:all 0.2s;
  font-family:'Nunito',sans-serif;
}}
.btn-whatsapp:hover{{background:#20ba5a;transform:translateY(-2px);}}

/* ───────────── PARTICLE BURST ───────────── */
.particle{{
  position:fixed;pointer-events:none;
  border-radius:50%;z-index:9999;
  animation:particle-fly 1s ease-out forwards;
}}
@keyframes particle-fly{{
  0%{{opacity:1;transform:scale(1);}}
  100%{{opacity:0;transform:scale(0) translate(var(--tx),var(--ty));}}
}}

/* ───────────── READING PROGRESS BAR ───────────── */
#progress-bar{{
  position:fixed;top:0;left:0;height:3px;
  background:linear-gradient(90deg,var(--violet),var(--cyan),var(--gold));
  z-index:9000;
  width:0%;
  transition:width 0.1s;
  box-shadow:0 0 10px var(--cyan);
}}

/* ───────────── RESPONSIVE ───────────── */
@media(max-width:768px){{
  .hero-inner{{flex-direction:column;gap:40px;text-align:center;}}
  .hero-desc{{max-width:100%;}}
  .hero-meta{{justify-content:center;}}
  .buy-group{{justify-content:center;}}
  .author-inner{{flex-direction:column;text-align:center;gap:32px;}}
  .author-stats{{justify-content:center;}}
  .book-wrap{{order:-1;}}
}}
</style>
</head>
<body>

<!-- Cursor -->
<div id="cursor"></div>
<div id="cursor-trail"></div>

<!-- Progress bar -->
<div id="progress-bar"></div>

<!-- Starfield -->
<canvas id="starfield"></canvas>

<!-- Payment Overlay -->
<div class="overlay" id="payOverlay" onclick="closeIfOutside(event,'payOverlay')">
  <div class="pay-modal">
    <button class="pay-close" onclick="closePay()">×</button>
    <h2 id="payTitle">Get Your Copy</h2>
    <p class="pay-type" id="payTypeLabel"></p>
    <div class="qr-box">
      <!-- Placeholder QR — in production, replace with actual UPI QR image/generated QR -->
      <svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
        <!-- Styled QR-like placeholder -->
        <rect width="200" height="200" fill="white"/>
        <rect x="10" y="10" width="60" height="60" fill="none" stroke="#000" stroke-width="4"/>
        <rect x="20" y="20" width="40" height="40" fill="#000"/>
        <rect x="130" y="10" width="60" height="60" fill="none" stroke="#000" stroke-width="4"/>
        <rect x="140" y="20" width="40" height="40" fill="#000"/>
        <rect x="10" y="130" width="60" height="60" fill="none" stroke="#000" stroke-width="4"/>
        <rect x="20" y="140" width="40" height="40" fill="#000"/>
        <!-- Center pattern -->
        <rect x="80" y="10" width="8" height="8" fill="#000"/>
        <rect x="96" y="10" width="8" height="8" fill="#000"/>
        <rect x="112" y="10" width="8" height="8" fill="#000"/>
        <rect x="80" y="26" width="8" height="8" fill="#000"/>
        <rect x="112" y="26" width="8" height="8" fill="#000"/>
        <rect x="88" y="42" width="8" height="8" fill="#000"/>
        <rect x="104" y="42" width="8" height="8" fill="#000"/>
        <!-- More pattern -->
        <rect x="80" y="80" width="40" height="40" rx="4" fill="#533483"/>
        <text x="100" y="107" font-family="Arial" font-size="22" fill="white" text-anchor="middle" font-weight="bold">📖</text>
        <rect x="80" y="130" width="8" height="8" fill="#000"/>
        <rect x="96" y="130" width="8" height="8" fill="#000"/>
        <rect x="112" y="130" width="8" height="8" fill="#000"/>
        <rect x="88" y="146" width="8" height="8" fill="#000"/>
        <rect x="104" y="146" width="8" height="8" fill="#000"/>
        <rect x="80" y="162" width="8" height="8" fill="#000"/>
        <rect x="96" y="162" width="8" height="8" fill="#000"/>
        <rect x="112" y="162" width="8" height="8" fill="#000"/>
        <rect x="130" y="80" width="8" height="8" fill="#000"/>
        <rect x="146" y="80" width="8" height="8" fill="#000"/>
        <rect x="162" y="80" width="8" height="8" fill="#000"/>
        <rect x="130" y="96" width="8" height="8" fill="#000"/>
        <rect x="162" y="96" width="8" height="8" fill="#000"/>
        <rect x="138" y="112" width="8" height="8" fill="#000"/>
        <rect x="154" y="112" width="8" height="8" fill="#000"/>
        <rect x="130" y="128" width="8" height="8" fill="#000"/>
        <rect x="146" y="128" width="8" height="8" fill="#000"/>
        <rect x="162" y="128" width="8" height="8" fill="#000"/>
        <rect x="130" y="144" width="8" height="8" fill="#000"/>
        <rect x="162" y="144" width="8" height="8" fill="#000"/>
        <rect x="138" y="160" width="8" height="8" fill="#000"/>
        <rect x="154" y="160" width="8" height="8" fill="#000"/>
      </svg>
    </div>
    <div class="pay-amount" id="payAmount">{BOOK['currency']}299</div>
    <div class="pay-upi">UPI: {BOOK['gpay_upi']}</div>
    <div class="pay-methods">
      <div class="pay-m">📱 GPay</div>
      <div class="pay-m">💳 PhonePe</div>
      <div class="pay-m">🔵 Paytm</div>
      <div class="pay-m">💵 Cash</div>
    </div>
    <p class="pay-note">Scan the QR above with any UPI app · After payment, WhatsApp your screenshot to confirm your order!</p>
    <a class="btn-whatsapp" href="https://wa.me/{BOOK['whatsapp']}?text=Hi! I just paid for the book 📖" target="_blank">
      <span>📲</span> Confirm on WhatsApp
    </a>
  </div>
</div>

<!-- ══ HERO ══════════════════════════════════════════════════════════ -->
<section class="hero">
  <div class="hero-glow"></div>
  <div class="hero-inner">
    <!-- Book -->
    <div class="book-wrap">
      <div class="orbit-badge">
        <span>✨ By<br>a Kid<br>13 yrs</span>
      </div>
      <div class="book">
        <div class="book-cover">
          <div class="book-spine-text">{BOOK['author']}</div>
          <div class="book-stars">✨🌟⭐</div>
          <!-- Decorative elements inside cover -->
          <div style="position:absolute;top:30px;left:24px;right:24px;">
            <div style="font-size:40px;text-align:center;margin-bottom:12px;">🔢✨🌌</div>
            <div style="width:100%;height:1px;background:linear-gradient(to right,transparent,rgba(255,215,0,0.4),transparent);"></div>
          </div>
          <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;">
            <div style="font-size:52px;">🏰</div>
          </div>
          <div class="book-title-text">
            {BOOK['title']}<br>
            <div class="book-author-text">— {BOOK['author']} —</div>
          </div>
        </div>
      </div>
      <div class="book-shadow"></div>
    </div>

    <!-- Right -->
    <div class="hero-right">
      <div class="hero-badge"><span class="dot"></span> Now Available · Limited Print Run</div>
      <h1 class="hero-h1">
        {BOOK['title'].split()[0]} <span class="accent">{' '.join(BOOK['title'].split()[1:])}</span>
      </h1>
      <div class="hero-tagline">"{BOOK['tagline']}"</div>
      <p class="hero-desc">{BOOK['description']}</p>
      <div class="hero-meta">
        <div class="meta-pill"><span>📚</span> {BOOK['pages']} Pages</div>
        <div class="meta-pill"><span>🎭</span> {BOOK['genre']}</div>
        <div class="meta-pill"><span>🏆</span> Age 8–14</div>
        <div class="meta-pill"><span>📍</span> {BOOK['city']}</div>
      </div>
      <div class="buy-group">
        <button class="btn-buy btn-physical" onclick="openPay('physical')">
          <span>📦</span>
          <span>
            <span class="price-tag">{BOOK['currency']}{BOOK['physical_price']}</span>
            <span class="price-sub">Physical Book</span>
          </span>
        </button>
        <button class="btn-buy btn-digital" onclick="openPay('digital')">
          <span>📱</span>
          <span>
            <span class="price-tag">{BOOK['currency']}{BOOK['digital_price']}</span>
            <span class="price-sub">Digital PDF</span>
          </span>
        </button>
      </div>
    </div>
  </div>
</section>

<!-- ══ PREVIEW ══════════════════════════════════════════════════════ -->
<div class="preview-bg">
<div class="section">
  <div class="section-label">👀 Sneak Peek</div>
  <h2 class="section-title">Peek Inside the Magic</h2>
  <div class="preview-cards">
    {''.join(f"""
    <div class="prev-card" onclick="burst(event)">
      <span class="prev-emoji">{p['emoji']}</span>
      <div class="prev-chapter">{p['title']}</div>
      <p class="prev-text">{p['text']}</p>
      <div class="card-glow"></div>
    </div>
    """ for p in BOOK['preview_pages'])}
  </div>
</div>
</div>

<!-- ══ AUTHOR ══════════════════════════════════════════════════════ -->
<div class="author-bg">
<div class="author-inner">
  <div class="author-avatar">🧒</div>
  <div class="author-details">
    <div class="section-label">✍️ The Author</div>
    <div class="author-name">{BOOK['author']}</div>
    <div class="author-grade">{BOOK['grade']} · {BOOK['age']} years old · {BOOK['city']}</div>
    <p class="author-bio">
      {BOOK['author']} is a Class 8 student with a wild imagination and a love for 
      mathematics. When his math teacher told him that numbers have personalities, 
      he went home and wrote an entire fantasy world about them. 
      This book is proof that the best stories come from the most curious minds — 
      no matter how young they are. 🌟
    </p>
    <div class="author-stats">
      <div class="astat"><div class="astat-num">1st</div><div class="astat-lbl">Published Book</div></div>
      <div class="astat"><div class="astat-num">13</div><div class="astat-lbl">Years Young</div></div>
      <div class="astat"><div class="astat-num">∞</div><div class="astat-lbl">Imagination</div></div>
    </div>
  </div>
</div>
</div>

<!-- ══ ORACLE + RIDDLE ══════════════════════════════════════════════ -->
<div class="oracle-bg">
<div class="section">
  <div class="oracle-wrap">
    <div class="section-label" style="text-align:center;">🔮 Book Oracle</div>
    <h2 class="section-title" style="text-align:center;">Ask the Book a Question</h2>
    <p style="font-family:'Crimson Pro',serif;font-size:17px;color:var(--muted);margin-bottom:28px;">
      The magic crystal knows everything inside the story. Ask it anything about math, 
      the characters, or the kingdom…
    </p>
    <span class="oracle-crystal" id="crystalEmoji">🔮</span>
    
    <div style="display:flex;gap:10px;max-width:500px;margin:0 auto 16px;">
      <input id="oracleInput" 
        style="flex:1;padding:14px 20px;background:var(--card-bg);border:1px solid var(--card-border);
               border-radius:12px;color:#fff;font-size:15px;font-family:'Nunito',sans-serif;
               outline:none;transition:border-color 0.3s;" 
        placeholder="What is Zero's superpower? …"
        onkeydown="if(event.key==='Enter')askOracle()"
        onfocus="this.style.borderColor='var(--cyan)'"
        onblur="this.style.borderColor='var(--card-border)'"
      />
      <button class="oracle-btn" onclick="askOracle()" style="padding:14px 24px;">Ask ✨</button>
    </div>
    
    <div class="oracle-output" id="oracleOutput">
      <div class="oracle-answer" id="oracleAnswer"></div>
    </div>
  </div>

  <!-- RIDDLE -->
  <div class="riddle-wrap" id="riddleSection">
    <div class="riddle-title">🧩 Number Kingdom Riddle</div>
    <p class="riddle-q" id="riddleQ">Loading your riddle from the Kingdom…</p>
    <div class="riddle-options" id="riddleOpts"></div>
    <div class="riddle-result" id="riddleResult"></div>
    <button onclick="nextRiddle()" 
      style="margin-top:16px;padding:10px 24px;background:var(--card-bg);
             border:1px solid var(--card-border);border-radius:50px;
             color:var(--muted);font-size:13px;font-weight:700;cursor:pointer;
             font-family:'Nunito',sans-serif;transition:all 0.2s;"
      onmouseover="this.style.borderColor='var(--cyan)'"
      onmouseout="this.style.borderColor='var(--card-border)'"
    >Next Riddle 🎲</button>
  </div>
</div>
</div>

<!-- ══ FINAL CTA ════════════════════════════════════════════════════ -->
<div style="text-align:center;padding:80px 24px 100px;position:relative;z-index:2;">
  <div style="font-size:48px;margin-bottom:20px;">📖✨</div>
  <h2 style="font-family:'Cinzel Decorative',serif;font-size:clamp(22px,3vw,36px);color:#fff;margin-bottom:12px;">
    Ready to Enter the Kingdom?
  </h2>
  <p style="font-family:'Crimson Pro',serif;font-size:18px;color:var(--muted);margin-bottom:36px;">
    Every great mathematician started with a great story.
  </p>
  <div class="buy-group" style="justify-content:center;">
    <button class="btn-buy btn-physical" onclick="openPay('physical')" style="font-size:17px;padding:18px 36px;">
      <span>📦</span>
      <span>
        <span class="price-tag">{BOOK['currency']}{BOOK['physical_price']}</span>
        <span class="price-sub">Physical Book · Free Delivery</span>
      </span>
    </button>
    <button class="btn-buy btn-digital" onclick="openPay('digital')" style="font-size:17px;padding:18px 36px;">
      <span>⚡</span>
      <span>
        <span class="price-tag">{BOOK['currency']}{BOOK['digital_price']}</span>
        <span class="price-sub">Instant Digital PDF</span>
      </span>
    </button>
  </div>
</div>

<script>
// ─── CURSOR ───────────────────────────────────────────
const cur = document.getElementById('cursor');
const trail = document.getElementById('cursor-trail');
let mx=0,my=0,tx=0,ty=0;
document.addEventListener('mousemove',(e)=>{{
  mx=e.clientX; my=e.clientY;
  cur.style.left=(mx-7)+'px'; cur.style.top=(my-7)+'px';
  setTimeout(()=>{{
    trail.style.left=(mx-16)+'px'; trail.style.top=(my-16)+'px';
  }},60);
}});

// ─── READING PROGRESS ─────────────────────────────────
window.addEventListener('scroll',()=>{{
  const total = document.body.scrollHeight - window.innerHeight;
  const pct = (window.scrollY / total)*100;
  document.getElementById('progress-bar').style.width = pct+'%';
}});

// ─── STARFIELD ────────────────────────────────────────
const canvas = document.getElementById('starfield');
const ctx = canvas.getContext('2d');
let stars=[], W, H;
function resize(){{ W=canvas.width=window.innerWidth; H=canvas.height=window.innerHeight; }}
resize(); window.addEventListener('resize',resize);
for(let i=0;i<{BOOK['star_count']*3};i++){{
  stars.push({{
    x:Math.random()*2000, y:Math.random()*1200,
    r:Math.random()*1.5+0.2,
    o:Math.random(), sp:Math.random()*0.008+0.002,
    dx:(Math.random()-0.5)*0.1
  }});
}}
function drawStars(){{
  ctx.clearRect(0,0,W,H);
  stars.forEach(s=>{{
    s.o += s.sp; if(s.o>1||s.o<0) s.sp*=-1;
    s.x += s.dx; if(s.x<0) s.x=W; if(s.x>W) s.x=0;
    ctx.beginPath();
    ctx.arc(s.x % W, s.y % H, s.r,0,Math.PI*2);
    ctx.fillStyle=`rgba(255,255,255,${{s.o}})`;
    ctx.fill();
  }});
  requestAnimationFrame(drawStars);
}}
drawStars();

// ─── PARTICLE BURST ───────────────────────────────────
function burst(e){{
  const emojis=['✨','⭐','🌟','💫','🔢','📐','➕','✖️','🎉'];
  for(let i=0;i<14;i++){{
    const p=document.createElement('div');
    p.className='particle';
    const angle=Math.random()*360;
    const dist=60+Math.random()*80;
    const tx=Math.cos(angle*Math.PI/180)*dist+'px';
    const ty=Math.sin(angle*Math.PI/180)*dist+'px';
    p.style.cssText=`
      left:${{e.clientX-10}}px;top:${{e.clientY-10}}px;
      width:20px;height:20px;font-size:16px;
      text-align:center;line-height:20px;
      --tx:${{tx}};--ty:${{ty}};
      background:none;
      animation-delay:${{Math.random()*0.2}}s;
    `;
    p.textContent=emojis[Math.floor(Math.random()*emojis.length)];
    document.body.appendChild(p);
    setTimeout(()=>p.remove(),1200);
  }}
}}

// ─── PAYMENT MODAL ────────────────────────────────────
function openPay(type){{
  const overlay=document.getElementById('payOverlay');
  const title=document.getElementById('payTitle');
  const label=document.getElementById('payTypeLabel');
  const amount=document.getElementById('payAmount');
  if(type==='physical'){{
    title.textContent='📦 Physical Book Order';
    label.textContent='Delivered to your doorstep in 3-5 days';
    amount.textContent='{BOOK['currency']}{BOOK['physical_price']}';
  }} else {{
    title.textContent='⚡ Digital Book Order';
    label.textContent='Instant PDF delivery via WhatsApp';
    amount.textContent='{BOOK['currency']}{BOOK['digital_price']}';
  }}
  overlay.classList.add('active');
}}
function closePay(){{
  document.getElementById('payOverlay').classList.remove('active');
}}
function closeIfOutside(e,id){{
  if(e.target.id===id) document.getElementById(id).classList.remove('active');
}}
document.addEventListener('keydown',(e)=>{{ if(e.key==='Escape') closePay(); }});

// ─── RIDDLES ──────────────────────────────────────────
const riddles = [
  {{
    q:"I am a number that is neither positive nor negative. What am I?",
    opts:["Zero","One","Infinity","-1"],correct:0,
    explain:"Zero (0) is the only number that is neither positive nor negative!"
  }},
  {{
    q:"I am a fraction. My numerator equals my denominator. What is my value?",
    opts:["0","Infinity","1","1/2"],correct:2,
    explain:"Any number divided by itself equals 1. That's the unity fraction!"
  }},
  {{
    q:"Prime numbers can only be divided by 1 and themselves. Which of these is NOT prime?",
    opts:["7","11","15","13"],correct:2,
    explain:"15 = 3 × 5, so it's not prime. 7, 11, 13 are all prime!"
  }},
  {{
    q:"What happens when you add all angles of any triangle?",
    opts:["90°","360°","180°","270°"],correct:2,
    explain:"Every triangle's angles always add up to exactly 180°. Magic!"
  }},
  {{
    q:"I multiply any number and keep it the same. What number am I?",
    opts:["0","2","1","-1"],correct:2,
    explain:"1 is the Multiplicative Identity! n × 1 = n always."
  }},
];
let currentRiddle=0;
function loadRiddle(){{
  const r=riddles[currentRiddle];
  document.getElementById('riddleQ').textContent=r.q;
  document.getElementById('riddleResult').textContent='';
  document.getElementById('riddleResult').style.color='';
  const opts=document.getElementById('riddleOpts');
  opts.innerHTML='';
  r.opts.forEach((o,i)=>{{
    const btn=document.createElement('button');
    btn.className='riddle-opt'; btn.textContent=o;
    btn.onclick=()=>checkRiddle(i);
    opts.appendChild(btn);
  }});
}}
function checkRiddle(idx){{
  const r=riddles[currentRiddle];
  const btns=document.querySelectorAll('.riddle-opt');
  btns.forEach((b,i)=>{{
    if(i===r.correct) b.classList.add('correct');
    else if(i===idx && idx!==r.correct) b.classList.add('wrong');
    b.onclick=null;
  }});
  const res=document.getElementById('riddleResult');
  if(idx===r.correct){{
    res.textContent='🎉 Brilliant! '+r.explain;
    res.style.color='var(--gold)';
  }} else {{
    res.textContent='💡 Not quite! '+r.explain;
    res.style.color='var(--rose)';
  }}
}}
function nextRiddle(){{
  currentRiddle=(currentRiddle+1)%riddles.length;
  loadRiddle();
}}
loadRiddle();

// ─── BOOK ORACLE (Claude API) ─────────────────────────
async function askOracle(){{
  const input=document.getElementById('oracleInput');
  const output=document.getElementById('oracleOutput');
  const answer=document.getElementById('oracleAnswer');
  const crystal=document.getElementById('crystalEmoji');
  const q=input.value.trim();
  if(!q) return;
  
  crystal.style.animation='none';
  crystal.textContent='⏳';
  output.classList.add('visible');
  answer.innerHTML='<em style="color:var(--muted)">The crystal is thinking… ✨</em>';
  
  try{{
    const resp=await fetch('https://api.anthropic.com/v1/messages',{{
      method:'POST',
      headers:{{'Content-Type':'application/json'}},
      body:JSON.stringify({{
        model:'claude-sonnet-4-20250514',
        max_tokens:300,
        system:`You are the Book Oracle for a children's fantasy book called "${{'{BOOK['title']}'}}" by ${{'{BOOK['author']}'}}, a 13-year-old Class 8 student from Pune. 
The book is about a magical kingdom where numbers have superpowers — primes guard castles, fractions build bridges, zero discovers its true power, etc.
Answer questions about the book, math concepts in it, or the author in a MAGICAL, CHILD-FRIENDLY way using simple language, wonder, and occasional emojis. 
Keep answers to 2-3 sentences. If the question is unrelated to math or the book, gently redirect back to the kingdom.`,
        messages:[{{role:'user',content:q}}]
      }})
    }});
    const data=await resp.json();
    const text=data.content?.[0]?.text || "The crystal clouds… try again!";
    answer.innerHTML='';
    let i=0;
    function typeChar(){{
      if(i<text.length){{
        answer.innerHTML+=text[i];
        i++; setTimeout(typeChar,18);
      }}
    }}
    typeChar();
    crystal.style.animation='crystal-spin 10s linear infinite';
    crystal.textContent='🔮';
  }} catch(err){{
    answer.innerHTML='<em style="color:var(--rose)">The crystal needs a moment… please try again! ✨</em>';
    crystal.style.animation='crystal-spin 10s linear infinite';
    crystal.textContent='🔮';
  }}
  input.value='';
}}
</script>
</body>
</html>
"""

components.html(html, height=10000, scrolling=False)
