import streamlit as st
import json

st.set_page_config(
    page_title="The Secret Kingdom of Numbers",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── BOOK CONFIG ────────────────────────────────────────────────────────────────
BOOK = {
    "title":         "The Secret Kingdom of Numbers",
    "author":        "Aryan Sharma",
    "age":           13,
    "grade":         "Class 8",
    "city":          "Pune, India",
    "pages":         124,
    "genre":         "Math · Adventure · Fantasy",
    "tagline":       "What if every number had a superpower?",
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
        "This book proves that the best stories can come from the most curious "
        "minds — no matter how young."
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
                "violet at night. The forest was a living fraction — always adding to "
                "one whole, no matter how you divided it. 'We are pieces,' whispered "
                "the Fraction Fairy. 'But together, we are complete.'"
            ),
        },
        {
            "chapter": "Chapter 9",
            "title":   "Zero's Secret",
            "emoji":   "⭕",
            "text": (
                "Everyone laughed at Zero. 'You are nothing!' they said. "
                "But Zero just smiled and stepped beside One — and One became Ten. "
                "Then Hundred. Then Thousand. "
                "'Nothing,' said Zero quietly, 'can become everything.'"
            ),
        },
    ],
    "physical_price": 299,
    "digital_price":  99,
    "upi_id":         "aryan@oksbi",       # ← replace with real UPI ID
    "whatsapp":       "919876543210",      # ← replace: country code + number, no +
    "seller_email":   "aryan@example.com", # ← replace
}

# ── RIDDLES ────────────────────────────────────────────────────────────────────
RIDDLES = [
    {
        "q":       "I am neither positive nor negative. What number am I?",
        "opts":    ["One", "Zero", "Infinity", "Half"],
        "correct": 1,
        "fact":    "Zero is the only number that is neither positive nor negative — and it can make any number ten times bigger just by standing beside it!",
    },
    {
        "q":       "A fraction whose numerator equals its denominator always equals…?",
        "opts":    ["Zero", "Two", "One", "Itself"],
        "correct": 2,
        "fact":    "Any number divided by itself equals 1. That's why 4/4, 99/99 and 1000/1000 are all exactly 1!",
    },
    {
        "q":       "Which of these is NOT a prime number?",
        "opts":    ["7", "11", "15", "13"],
        "correct": 2,
        "fact":    "15 = 3 × 5, so it has factors besides 1 and itself. Primes can only be divided by 1 and themselves — 7, 11 and 13 all pass the test!",
    },
    {
        "q":       "The angles of ANY triangle always add up to…?",
        "opts":    ["90°", "360°", "270°", "180°"],
        "correct": 3,
        "fact":    "Every triangle — no matter how big, small or lopsided — has angles that sum to exactly 180°. It's one of geometry's golden laws.",
    },
    {
        "q":       "Which number, when multiplied by anything, leaves it unchanged?",
        "opts":    ["0", "2", "1", "10"],
        "correct": 2,
        "fact":    "1 is the Multiplicative Identity. n × 1 = n, always. It's the quiet guardian of every equation in the Kingdom.",
    },
]

# ── GENERATE HTML SNIPPETS FROM PYTHON DATA ────────────────────────────────────
preview_cards_html = ""
for p in BOOK["preview"]:
    preview_cards_html += f"""
    <div class="prev-card">
      <span class="prev-emoji">{p['emoji']}</span>
      <div class="prev-ch">{p['chapter']}</div>
      <div class="prev-title">{p['title']}</div>
      <p class="prev-text">{p['text']}</p>
    </div>"""

riddles_js = json.dumps(RIDDLES)

# ── FULL PAGE HTML ─────────────────────────────────────────────────────────────
# We inject this via st.markdown so it lives directly in the Streamlit DOM
# — no iframe, no fixed height, scrolls naturally.

page_html = f"""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">

<style>
/* ── STREAMLIT CHROME REMOVAL ─────────────────── */
#MainMenu, header, footer,
.stDeployButton, .stToolbar,
[data-testid="stDecoration"],
[data-testid="stHeader"] {{
  display: none !important;
}}
.main .block-container {{
  padding: 0 !important;
  max-width: 100% !important;
}}
.main {{
  padding: 0 !important;
}}
section[data-testid="stMain"] > div {{
  padding: 0 !important;
}}

/* ── RESET ────────────────────────────────────── */
.bk * {{ margin:0; padding:0; box-sizing:border-box; }}
.bk {{ line-height: 1.6; -webkit-font-smoothing: antialiased; }}

/* ── DESIGN TOKENS ────────────────────────────── */
.bk {{
  --bg:        #FAFAF8;
  --ink:       #1C1C1C;
  --ink2:      #4A4A4A;
  --ink3:      #888;
  --border:    #E4E0D8;
  --cream:     #F5F0E8;
  --accent:    #C8602A;
  --violet:    #3D2B6E;
  --violet2:   #5B4290;
  --gold:      #C8A84B;
  --goldf:     #F0D080;
  --green:     #256A45;
  --red:       #C0392B;
  --white:     #FFFFFF;
  --sh:        0 2px 12px rgba(0,0,0,.07);
  --sh-md:     0 6px 28px rgba(0,0,0,.11);
  --sh-lg:     0 14px 48px rgba(0,0,0,.14);
  --r:         12px;
  --rl:        20px;
  font-family: 'DM Sans', sans-serif;
  color: var(--ink);
  background: var(--bg);
}}

/* ── LAYOUT ───────────────────────────────────── */
.bk .wrap    {{ max-width:1020px; margin:0 auto; padding:0 28px; }}
.bk .section {{ padding:72px 0; }}
.bk .sec-sm  {{ padding:52px 0; }}
.bk .divider {{ border:none; border-top:1px solid var(--border); margin:0; }}

/* ── SHARED LABEL ─────────────────────────────── */
.bk .lbl {{
  display:inline-block;
  font-size:11px; font-weight:700;
  letter-spacing:.2em; text-transform:uppercase;
  color:var(--accent); margin-bottom:12px;
}}
.bk h2 {{
  font-family:'Playfair Display',serif;
  font-size:clamp(24px,3vw,38px);
  font-weight:900; line-height:1.15;
  color:var(--ink); margin-bottom:0;
}}

/* ════════════════════════════════════════════════
   HERO
═══════════════════════════════════════════════ */
.bk .hero {{
  background: var(--violet);
  padding: 60px 0 52px;
  position: relative;
  overflow: hidden;
}}
.bk .hero::after {{
  content:'';
  position:absolute; inset:0;
  background:
    radial-gradient(ellipse 55% 70% at 85% 50%, rgba(200,96,42,.2) 0%, transparent 65%),
    radial-gradient(ellipse 40% 50% at 15% 30%, rgba(255,255,255,.04) 0%, transparent 60%);
  pointer-events:none;
}}
.bk .hero-grid {{
  position:relative; z-index:1;
  display:grid;
  grid-template-columns: 1fr 300px;
  gap: 56px;
  align-items: center;
}}
/* eyebrow pill */
.bk .eyebrow {{
  display:inline-flex; align-items:center; gap:8px;
  border:1px solid rgba(255,255,255,.2);
  border-radius:40px; padding:5px 14px;
  font-size:11px; font-weight:600;
  letter-spacing:.14em; text-transform:uppercase;
  color:rgba(255,255,255,.6);
  margin-bottom:20px;
}}
.bk .eyebrow .dot {{
  width:6px; height:6px; border-radius:50%;
  background: var(--goldf);
  animation: bk-blink 1.6s ease-in-out infinite;
}}
@keyframes bk-blink {{ 0%,100%{{opacity:1}} 50%{{opacity:.25}} }}

.bk .hero h1 {{
  font-family:'Playfair Display',serif;
  font-size:clamp(30px,4.2vw,50px);
  font-weight:900; color:#fff;
  letter-spacing:-.02em;
  line-height:1.12;
  margin-bottom:12px;
}}
.bk .hero h1 em {{ color:var(--goldf); font-style:normal; }}
.bk .hero-tagline {{
  font-family:'DM Serif Display',serif;
  font-size:17px; font-style:italic;
  color:rgba(255,255,255,.6);
  margin-bottom:18px;
}}
.bk .hero-desc {{
  font-size:15px; color:rgba(255,255,255,.68);
  line-height:1.78; max-width:500px;
  margin-bottom:28px;
}}
.bk .hero-chips {{
  display:flex; gap:16px; flex-wrap:wrap;
  margin-bottom:30px;
}}
.bk .chip {{
  display:flex; align-items:center; gap:5px;
  font-size:13px; color:rgba(255,255,255,.52);
  font-weight:500;
}}
/* buy buttons */
.bk .btn-row {{ display:flex; gap:12px; flex-wrap:wrap; }}
.bk .btn {{
  display:inline-flex; align-items:center; gap:10px;
  padding:13px 22px; border-radius:var(--r);
  font-size:14px; font-weight:600;
  cursor:pointer; border:none;
  font-family:'DM Sans',sans-serif;
  transition:transform .2s, box-shadow .2s, filter .2s;
  white-space:nowrap;
}}
.bk .btn:hover {{ transform:translateY(-2px); }}
.bk .btn-solid {{
  background:var(--accent); color:#fff;
  box-shadow:0 4px 18px rgba(200,96,42,.38);
}}
.bk .btn-solid:hover {{ box-shadow:0 8px 26px rgba(200,96,42,.5); }}
.bk .btn-ghost {{
  background:rgba(255,255,255,.1); color:#fff;
  border:1px solid rgba(255,255,255,.22);
}}
.bk .btn-ghost:hover {{ background:rgba(255,255,255,.18); }}
.bk .btn-price {{ font-size:18px; font-weight:800; }}
.bk .btn-sub   {{ font-size:11px; opacity:.7; }}
.bk .btn-col   {{ display:flex; flex-direction:column; line-height:1.25; }}

/* book mockup */
.bk .book-mockup {{
  background:rgba(255,255,255,.07);
  border:1px solid rgba(255,255,255,.12);
  border-radius:var(--rl);
  padding:28px 22px;
  text-align:center;
}}
.bk .book-cover {{
  width:148px; height:206px;
  margin:0 auto 18px;
  border-radius:3px 12px 12px 3px;
  background:linear-gradient(155deg,#2A1A5C 0%,#3D2B6E 45%,#C8602A 100%);
  box-shadow: -5px 4px 0 rgba(0,0,0,.3), var(--sh-lg);
  display:flex; flex-direction:column;
  align-items:center; justify-content:center;
  position:relative; overflow:hidden;
  transition:transform .35s, box-shadow .35s;
}}
.bk .book-cover:hover {{
  transform:perspective(500px) rotateY(-10deg) translateY(-4px);
  box-shadow:-8px 10px 28px rgba(0,0,0,.42), var(--sh-lg);
}}
.bk .book-cover::before {{
  content:'';
  position:absolute; left:0;top:0;bottom:0; width:14px;
  background:linear-gradient(to right,rgba(0,0,0,.38),transparent);
}}
.bk .book-inner {{
  position:relative; z-index:1;
  padding:16px 12px; text-align:center;
}}
.bk .book-emoji {{ font-size:32px; margin-bottom:8px; display:block; }}
.bk .book-title-sm {{
  font-family:'Playfair Display',serif;
  font-size:10px; font-weight:700;
  color:var(--goldf); line-height:1.4;
  margin-bottom:6px;
}}
.bk .book-author-sm {{
  font-size:8px; color:rgba(255,255,255,.45);
  letter-spacing:.08em;
}}
.bk .mock-lbl {{ font-size:10px; font-weight:600; letter-spacing:.12em; text-transform:uppercase; color:rgba(255,255,255,.32); margin-bottom:4px; }}
.bk .mock-name {{ font-size:14px; font-weight:700; color:#fff; margin-bottom:3px; }}
.bk .mock-sub  {{ font-size:11px; color:rgba(255,255,255,.4); }}

/* ════════════════════════════════════════════════
   PREVIEW
═══════════════════════════════════════════════ */
.bk .prev-grid {{
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(255px,1fr));
  gap:20px;
  margin-top:36px;
}}
.bk .prev-card {{
  background:var(--white);
  border:1px solid var(--border);
  border-radius:var(--rl);
  padding:28px 24px;
  position:relative; overflow:hidden;
  transition:box-shadow .25s, transform .25s, border-color .25s;
}}
.bk .prev-card::after {{
  content:'';
  position:absolute; bottom:0;left:0;right:0; height:3px;
  background:linear-gradient(to right,var(--violet),var(--accent));
  opacity:0; transition:opacity .25s;
}}
.bk .prev-card:hover {{ box-shadow:var(--sh-lg); transform:translateY(-5px); border-color:transparent; }}
.bk .prev-card:hover::after {{ opacity:1; }}
.bk .prev-emoji {{ font-size:30px; margin-bottom:14px; display:block; }}
.bk .prev-ch    {{ font-size:10px; font-weight:700; letter-spacing:.18em; text-transform:uppercase; color:var(--accent); margin-bottom:4px; }}
.bk .prev-title {{ font-family:'Playfair Display',serif; font-size:17px; font-weight:700; color:var(--ink); margin-bottom:12px; }}
.bk .prev-text  {{ font-family:'DM Serif Display',serif; font-size:15px; line-height:1.78; color:var(--ink2); font-style:italic; }}

/* ════════════════════════════════════════════════
   AUTHOR
═══════════════════════════════════════════════ */
.bk .author-band {{ background:var(--cream); }}
.bk .author-grid {{
  display:grid;
  grid-template-columns:auto 1fr;
  gap:40px; align-items:center;
}}
.bk .author-avatar {{
  width:108px; height:108px; border-radius:50%;
  background:linear-gradient(135deg,var(--violet) 0%,var(--accent) 100%);
  display:flex; align-items:center; justify-content:center;
  font-size:48px; flex-shrink:0;
  box-shadow:var(--sh-md);
}}
.bk .author-name {{ font-family:'Playfair Display',serif; font-size:26px; font-weight:900; margin-bottom:4px; }}
.bk .author-tag  {{ font-size:13px; color:var(--accent); font-weight:600; margin-bottom:14px; }}
.bk .author-bio  {{ font-size:15px; color:var(--ink2); line-height:1.78; max-width:560px; margin-bottom:18px; }}
.bk .a-stats     {{ display:flex; gap:32px; flex-wrap:wrap; }}
.bk .astat-num   {{ font-family:'Playfair Display',serif; font-size:26px; font-weight:700; color:var(--violet); line-height:1; }}
.bk .astat-lbl   {{ font-size:11px; color:var(--ink3); margin-top:2px; }}

/* ════════════════════════════════════════════════
   RIDDLE
═══════════════════════════════════════════════ */
.bk .riddle-box {{
  background:var(--white);
  border:1px solid var(--border);
  border-radius:var(--rl);
  padding:40px 36px;
  max-width:640px; margin:40px auto 0;
  text-align:center;
  box-shadow:var(--sh);
}}
.bk .riddle-counter {{
  font-size:11px; font-weight:700; letter-spacing:.16em;
  text-transform:uppercase; color:var(--ink3); margin-bottom:18px;
}}
.bk .riddle-q {{
  font-family:'Playfair Display',serif;
  font-size:20px; color:var(--ink);
  margin-bottom:26px; line-height:1.45;
}}
.bk .riddle-opts {{
  display:flex; flex-wrap:wrap; gap:10px;
  justify-content:center; margin-bottom:18px;
}}
.bk .ropt {{
  padding:10px 22px;
  border:2px solid var(--border); border-radius:50px;
  background:#fff; color:var(--ink);
  font-size:15px; font-weight:600; cursor:pointer;
  font-family:'DM Sans',sans-serif;
  transition:border-color .18s, color .18s, background .18s;
}}
.bk .ropt:hover:not(:disabled) {{ border-color:var(--violet); color:var(--violet); }}
.bk .ropt.correct {{ border-color:var(--green); background:#E6F4ED; color:var(--green); }}
.bk .ropt.wrong   {{ border-color:var(--red);   background:#FDECEA; color:var(--red); }}
.bk .ropt:disabled {{ cursor:default; }}
.bk .riddle-result {{
  min-height:44px; font-size:14px; line-height:1.65;
  color:var(--ink2); padding:0 4px;
}}
.bk .riddle-next {{
  margin-top:16px; padding:10px 24px;
  border-radius:50px; border:1px solid var(--border);
  background:#fff; color:var(--ink2);
  font-size:13px; font-weight:600;
  cursor:pointer; font-family:'DM Sans',sans-serif;
  transition:border-color .18s, color .18s;
}}
.bk .riddle-next:hover {{ border-color:var(--violet); color:var(--violet); }}

/* ════════════════════════════════════════════════
   CTA STRIP
═══════════════════════════════════════════════ */
.bk .cta-strip {{
  background:var(--ink);
  padding:60px 0;
  text-align:center;
}}
.bk .cta-strip h2 {{ color:#fff; margin-bottom:8px; }}
.bk .cta-strip p  {{ font-size:16px; color:rgba(255,255,255,.48); margin-bottom:32px; }}
.bk .cta-btn-row  {{ display:flex; gap:14px; justify-content:center; flex-wrap:wrap; }}

/* ════════════════════════════════════════════════
   ORDER MODAL
═══════════════════════════════════════════════ */
.bk-overlay {{
  display:none;
  position:fixed; inset:0;
  background:rgba(0,0,0,.55);
  z-index:9999;
  align-items:center; justify-content:center;
  backdrop-filter:blur(5px);
}}
.bk-overlay.open {{ display:flex; animation:bk-fade-in .2s ease; }}
@keyframes bk-fade-in {{ from{{opacity:0}} to{{opacity:1}} }}

.bk-modal {{
  background:#fff;
  border-radius:20px;
  width:min(500px,92vw);
  max-height:90vh; overflow-y:auto;
  box-shadow:0 24px 64px rgba(0,0,0,.26);
  position:relative;
  animation:bk-slide-up .25s ease;
  font-family:'DM Sans',sans-serif;
  color:#1C1C1C;
}}
@keyframes bk-slide-up {{ from{{opacity:0;transform:translateY(18px)}} to{{opacity:1;transform:none}} }}

.bk-modal-close {{
  position:absolute; top:14px; right:18px;
  background:none; border:none; cursor:pointer;
  font-size:22px; color:#888; line-height:1;
  transition:color .15s;
}}
.bk-modal-close:hover {{ color:#1C1C1C; }}

.bk-modal-head {{
  padding:26px 28px 18px;
  border-bottom:1px solid #E4E0D8;
}}
.bk-modal-head h3 {{
  font-family:'Playfair Display',serif;
  font-size:19px; font-weight:900; margin-bottom:3px;
}}
.bk-modal-head p {{ font-size:13px; color:#888; }}

.bk-modal-body {{ padding:22px 28px 28px; }}

/* step tabs */
.bk-steps {{
  display:flex; border:1px solid #E4E0D8;
  border-radius:10px; overflow:hidden;
  margin-bottom:24px;
}}
.bk-step {{
  flex:1; padding:10px 6px; text-align:center;
  font-size:12px; font-weight:600; color:#888;
  background:#fff; transition:all .2s;
}}
.bk-step.active {{ background:#3D2B6E; color:#fff; }}
.bk-step-num {{ display:block; font-size:15px; font-weight:800; margin-bottom:1px; }}

/* form */
.bk-field {{ margin-bottom:14px; }}
.bk-label {{
  display:block; font-size:12px; font-weight:600;
  color:#4A4A4A; margin-bottom:5px;
}}
.bk-input {{
  width:100%; padding:11px 13px;
  border:1.5px solid #E4E0D8; border-radius:10px;
  font-size:14px; font-family:'DM Sans',sans-serif; color:#1C1C1C;
  transition:border-color .2s; outline:none; background:#fff;
}}
.bk-input:focus {{ border-color:#3D2B6E; }}
.bk-row {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; }}
.bk-hint {{ font-size:11px; color:#888; margin-top:4px; }}

/* pay section */
.bk-pay-box {{
  background:#F5F0E8; border-radius:12px;
  padding:22px; text-align:center; margin-bottom:18px;
}}
.bk-pay-amount {{
  font-family:'Playfair Display',serif;
  font-size:30px; font-weight:900; color:#1C1C1C; margin-bottom:3px;
}}
.bk-pay-upi {{ font-size:13px; color:#888; margin-bottom:14px; }}
.bk-qr {{
  width:152px; height:152px;
  border:1px solid #E4E0D8; border-radius:10px;
  background:#fff; margin:0 auto 12px;
  display:flex; align-items:center; justify-content:center;
  padding:8px;
}}
.bk-qr svg {{ width:100%; height:100%; }}
.bk-pay-chips {{ display:flex; gap:8px; justify-content:center; flex-wrap:wrap; }}
.bk-chip {{
  padding:5px 13px; background:#fff;
  border:1px solid #E4E0D8; border-radius:8px;
  font-size:12px; font-weight:600; color:#4A4A4A;
}}
.bk-note {{
  font-size:13px; color:#4A4A4A; line-height:1.65;
  padding:11px 14px;
  background:#F0EBFF;
  border-left:3px solid #3D2B6E;
  border-radius:0 10px 10px 0;
  margin-bottom:16px;
}}

/* buttons inside modal */
.bk-btn {{
  display:inline-flex; align-items:center; justify-content:center; gap:8px;
  padding:12px 20px; border-radius:10px;
  font-size:14px; font-weight:600; cursor:pointer;
  border:none; font-family:'DM Sans',sans-serif;
  transition:filter .2s, transform .2s;
  text-decoration:none;
}}
.bk-btn:hover {{ transform:translateY(-1px); filter:brightness(.94); }}
.bk-btn-primary {{ background:#C8602A; color:#fff; width:100%; justify-content:center; padding:14px; font-size:15px; }}
.bk-btn-back    {{ background:#fff; color:#4A4A4A; border:1px solid #E4E0D8; flex:1; }}
.bk-btn-wa      {{ background:#25D366; color:#fff; width:100%; margin-bottom:10px; }}
.bk-btn-row2    {{ display:flex; gap:10px; margin-top:10px; }}

/* upload area */
.bk-upload {{
  border:2px dashed #E4E0D8; border-radius:10px;
  padding:24px; text-align:center; cursor:pointer;
  transition:border-color .2s, background .2s;
  margin-bottom:14px;
}}
.bk-upload:hover {{ border-color:#3D2B6E; background:#F8F4FF; }}
.bk-upload input {{ display:none; }}
.bk-upload-icon  {{ font-size:28px; margin-bottom:6px; }}
.bk-upload-lbl   {{ font-size:14px; font-weight:600; color:#4A4A4A; }}
.bk-upload-sub   {{ font-size:11px; color:#888; margin-top:3px; }}

/* success */
.bk-success {{ text-align:center; padding:20px 0; display:none; }}
.bk-success-icon  {{ font-size:52px; margin-bottom:14px; }}
.bk-success-title {{ font-family:'Playfair Display',serif; font-size:22px; font-weight:900; margin-bottom:8px; }}
.bk-success-sub   {{ font-size:14px; color:#4A4A4A; line-height:1.65; }}

/* ── RESPONSIVE ───────────────────────────────── */
@media(max-width:700px) {{
  .bk .hero-grid   {{ grid-template-columns:1fr; }}
  .bk .book-mockup {{ display:none; }}
  .bk .author-grid {{ grid-template-columns:1fr; text-align:center; }}
  .bk .author-avatar {{ margin:0 auto; }}
  .bk .a-stats     {{ justify-content:center; }}
  .bk .riddle-box  {{ padding:28px 18px; }}
  .bk-modal-body, .bk-modal-head {{ padding-left:18px; padding-right:18px; }}
  .bk-row          {{ grid-template-columns:1fr; }}
}}
</style>

<!-- ════════════ ORDER MODAL ════════════ -->
<div class="bk-overlay" id="bkOverlay" onclick="bkOverlayClick(event)">
  <div class="bk-modal" id="bkModal">
    <button class="bk-modal-close" onclick="bkClose()">✕</button>
    <div class="bk-modal-head">
      <h3 id="bkModalTitle">Order your copy</h3>
      <p id="bkModalSub"></p>
    </div>
    <div class="bk-modal-body">

      <!-- step tabs -->
      <div class="bk-steps">
        <div class="bk-step active" id="bkTab1"><span class="bk-step-num">1</span>Details</div>
        <div class="bk-step"        id="bkTab2"><span class="bk-step-num">2</span>Pay</div>
        <div class="bk-step"        id="bkTab3"><span class="bk-step-num">3</span>Confirm</div>
      </div>

      <!-- STEP 1 -->
      <div id="bkS1">
        <div class="bk-field">
          <label class="bk-label">Full Name *</label>
          <input class="bk-input" id="bkName" type="text" placeholder="e.g. Priya Mehta">
        </div>
        <div class="bk-field">
          <label class="bk-label">Email Address *</label>
          <input class="bk-input" id="bkEmail" type="email" placeholder="e.g. priya@gmail.com">
          <div class="bk-hint" id="bkEmailHint"></div>
        </div>
        <div class="bk-field">
          <label class="bk-label">WhatsApp / Phone *</label>
          <input class="bk-input" id="bkPhone" type="tel" placeholder="e.g. 9876543210">
        </div>
        <div id="bkAddrBlock">
          <div class="bk-field">
            <label class="bk-label">Delivery Address *</label>
            <input class="bk-input" id="bkAddr" type="text" placeholder="Flat / House No., Building, Street">
          </div>
          <div class="bk-row">
            <div class="bk-field">
              <label class="bk-label">City *</label>
              <input class="bk-input" id="bkCity" type="text" placeholder="Pune">
            </div>
            <div class="bk-field">
              <label class="bk-label">PIN Code *</label>
              <input class="bk-input" id="bkPin" type="text" placeholder="411001" maxlength="6">
            </div>
          </div>
        </div>
        <button class="bk-btn bk-btn-primary" onclick="bkStep2()">Continue to Payment →</button>
      </div>

      <!-- STEP 2 -->
      <div id="bkS2" style="display:none">
        <div class="bk-pay-box">
          <div class="bk-pay-amount" id="bkAmount"></div>
          <div class="bk-pay-upi">UPI ID: <strong>{BOOK['upi_id']}</strong></div>
          <div class="bk-qr">
            <svg viewBox="0 0 144 144" xmlns="http://www.w3.org/2000/svg">
              <rect width="144" height="144" fill="white"/>
              <rect x="8"  y="8"  width="42" height="42" rx="3" fill="none" stroke="#111" stroke-width="4"/>
              <rect x="16" y="16" width="26" height="26" rx="1" fill="#111"/>
              <rect x="94" y="8"  width="42" height="42" rx="3" fill="none" stroke="#111" stroke-width="4"/>
              <rect x="102" y="16" width="26" height="26" rx="1" fill="#111"/>
              <rect x="8"  y="94" width="42" height="42" rx="3" fill="none" stroke="#111" stroke-width="4"/>
              <rect x="16" y="102" width="26" height="26" rx="1" fill="#111"/>
              <rect x="56" y="56" width="32" height="32" rx="5" fill="#3D2B6E"/>
              <text x="72" y="78" font-size="16" text-anchor="middle" fill="white">📖</text>
              <rect x="58" y="8"  width="6" height="6" fill="#111"/>
              <rect x="68" y="8"  width="6" height="6" fill="#111"/>
              <rect x="78" y="8"  width="6" height="6" fill="#111"/>
              <rect x="58" y="18" width="6" height="6" fill="#111"/>
              <rect x="78" y="18" width="6" height="6" fill="#111"/>
              <rect x="68" y="28" width="6" height="6" fill="#111"/>
              <rect x="58" y="38" width="6" height="6" fill="#111"/>
              <rect x="78" y="38" width="6" height="6" fill="#111"/>
              <rect x="8"  y="58" width="6" height="6" fill="#111"/>
              <rect x="28" y="58" width="6" height="6" fill="#111"/>
              <rect x="18" y="68" width="6" height="6" fill="#111"/>
              <rect x="8"  y="78" width="6" height="6" fill="#111"/>
              <rect x="28" y="78" width="6" height="6" fill="#111"/>
              <rect x="98" y="58" width="6" height="6" fill="#111"/>
              <rect x="128" y="58" width="6" height="6" fill="#111"/>
              <rect x="108" y="68" width="6" height="6" fill="#111"/>
              <rect x="118" y="68" width="6" height="6" fill="#111"/>
              <rect x="98" y="78" width="6" height="6" fill="#111"/>
              <rect x="128" y="78" width="6" height="6" fill="#111"/>
              <rect x="58" y="98" width="6" height="6" fill="#111"/>
              <rect x="78" y="98" width="6" height="6" fill="#111"/>
              <rect x="68" y="108" width="6" height="6" fill="#111"/>
              <rect x="58" y="118" width="6" height="6" fill="#111"/>
              <rect x="78" y="118" width="6" height="6" fill="#111"/>
              <rect x="98" y="98" width="6" height="6" fill="#111"/>
              <rect x="128" y="98" width="6" height="6" fill="#111"/>
              <rect x="108" y="108" width="6" height="6" fill="#111"/>
              <rect x="98" y="118" width="6" height="6" fill="#111"/>
              <rect x="118" y="118" width="6" height="6" fill="#111"/>
              <rect x="128" y="128" width="6" height="6" fill="#111"/>
            </svg>
          </div>
          <div class="bk-pay-chips">
            <span class="bk-chip">📱 GPay</span>
            <span class="bk-chip">💳 PhonePe</span>
            <span class="bk-chip">🔵 Paytm</span>
            <span class="bk-chip">💵 Cash</span>
          </div>
        </div>
        <div class="bk-note" id="bkPayNote"></div>
        <div class="bk-btn-row2">
          <button class="bk-btn bk-btn-back" onclick="bkGoStep(1)">← Back</button>
          <button class="bk-btn bk-btn-primary" style="flex:2;" onclick="bkStep3()">I have paid →</button>
        </div>
      </div>

      <!-- STEP 3 -->
      <div id="bkS3" style="display:none">
        <p style="font-size:14px;color:#4A4A4A;line-height:1.65;margin-bottom:16px;">
          Please send your payment screenshot on WhatsApp to confirm your order.
          Once confirmed, <span id="bkDeliveryNote"></span>
        </p>
        <a class="bk-btn bk-btn-wa" id="bkWaLink" href="#" target="_blank">
          📲 &nbsp;Send Screenshot on WhatsApp
        </a>
        <div class="bk-upload" onclick="document.getElementById('bkFileInput').click()">
          <input type="file" id="bkFileInput" accept="image/*" onchange="bkFileSelected(this)">
          <div class="bk-upload-icon">📸</div>
          <div class="bk-upload-lbl" id="bkUploadLbl">Upload Payment Screenshot</div>
          <div class="bk-upload-sub">JPG / PNG · Optional — WhatsApp is faster</div>
        </div>
        <div class="bk-note" id="bkDigiNote"></div>
        <button class="bk-btn bk-btn-primary" onclick="bkSubmit()" style="margin-top:14px;">✓ Submit Order</button>
        <div class="bk-btn-row2">
          <button class="bk-btn bk-btn-back" onclick="bkGoStep(2)">← Back</button>
        </div>
      </div>

      <!-- SUCCESS -->
      <div class="bk-success" id="bkSuccess">
        <div class="bk-success-icon">🎉</div>
        <div class="bk-success-title">Order Submitted!</div>
        <p class="bk-success-sub" id="bkSuccessMsg"></p>
      </div>

    </div>
  </div>
</div>

<!-- ════════════════════════════════════════════════
     PAGE BODY  (wrapped in .bk for scoped CSS)
═══════════════════════════════════════════════ -->
<div class="bk">

  <!-- HERO -->
  <section class="hero">
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <div class="eyebrow"><span class="dot"></span> Now Available · Physical &amp; Digital</div>
          <h1>The Secret <em>Kingdom</em><br>of Numbers</h1>
          <p class="hero-tagline">"{BOOK['tagline']}"</p>
          <p class="hero-desc">{BOOK['description']}</p>
          <div class="hero-chips">
            <span class="chip">📚 {BOOK['pages']} pages</span>
            <span class="chip">🎭 {BOOK['genre']}</span>
            <span class="chip">🏷️ Ages 8–14</span>
            <span class="chip">📍 {BOOK['city']}</span>
          </div>
          <div class="btn-row">
            <button class="btn btn-solid" onclick="bkOpen('physical')">
              <span>📦</span>
              <span class="btn-col">
                <span class="btn-price">₹{BOOK['physical_price']}</span>
                <span class="btn-sub">Physical Copy</span>
              </span>
            </button>
            <button class="btn btn-ghost" onclick="bkOpen('digital')">
              <span>⚡</span>
              <span class="btn-col">
                <span class="btn-price">₹{BOOK['digital_price']}</span>
                <span class="btn-sub">Digital PDF</span>
              </span>
            </button>
          </div>
        </div>
        <div class="book-mockup">
          <div class="book-cover">
            <div class="book-inner">
              <span class="book-emoji">🏰✨</span>
              <div class="book-title-sm">{BOOK['title']}</div>
              <div class="book-author-sm">— {BOOK['author']} —</div>
            </div>
          </div>
          <div class="mock-lbl">Written by</div>
          <div class="mock-name">{BOOK['author']}</div>
          <div class="mock-sub">{BOOK['grade']} · {BOOK['age']} yrs · {BOOK['city']}</div>
        </div>
      </div>
    </div>
  </section>

  <hr class="divider">

  <!-- PREVIEW -->
  <section class="section">
    <div class="wrap">
      <div class="lbl">👀 Sneak Peek</div>
      <h2>A glimpse inside the Kingdom</h2>
      <div class="prev-grid">
        {preview_cards_html}
      </div>
    </div>
  </section>

  <hr class="divider">

  <!-- AUTHOR -->
  <div class="author-band">
    <section class="sec-sm">
      <div class="wrap">
        <div class="author-grid">
          <div class="author-avatar">🧒</div>
          <div>
            <div class="lbl">✍️ About the Author</div>
            <div class="author-name">{BOOK['author']}</div>
            <div class="author-tag">{BOOK['grade']} · {BOOK['age']} years old · {BOOK['city']}</div>
            <p class="author-bio">{BOOK['author_bio']}</p>
            <div class="a-stats">
              <div>
                <div class="astat-num">1st</div>
                <div class="astat-lbl">Published Book</div>
              </div>
              <div>
                <div class="astat-num">{BOOK['age']}</div>
                <div class="astat-lbl">Years Young</div>
              </div>
              <div>
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

  <!-- RIDDLE -->
  <section class="section">
    <div class="wrap" style="text-align:center">
      <div class="lbl">🧩 Number Kingdom Challenge</div>
      <h2>Can you solve a riddle from the book?</h2>
      <p style="color:#888;font-size:15px;max-width:460px;margin:10px auto 0">
        Every chapter hides a mathematical secret. Try one below.
      </p>
      <div class="riddle-box">
        <div class="riddle-counter" id="bkRiddleCounter"></div>
        <div class="riddle-q"       id="bkRiddleQ"></div>
        <div class="riddle-opts"    id="bkRiddleOpts"></div>
        <div class="riddle-result"  id="bkRiddleResult"></div>
        <button class="riddle-next" onclick="bkNextRiddle()">Next riddle →</button>
      </div>
    </div>
  </section>

  <!-- CTA -->
  <div class="cta-strip">
    <div class="wrap">
      <h2>Ready to enter the Kingdom?</h2>
      <p>Every great mathematician started with a great story.</p>
      <div class="cta-btn-row">
        <button class="btn btn-solid" onclick="bkOpen('physical')" style="font-size:16px;padding:15px 26px">
          <span>📦</span>
          <span class="btn-col">
            <span class="btn-price">₹{BOOK['physical_price']}</span>
            <span class="btn-sub">Physical Copy · Delivered</span>
          </span>
        </button>
        <button class="btn" onclick="bkOpen('digital')" style="background:rgba(255,255,255,.1);color:#fff;border:1px solid rgba(255,255,255,.22);font-size:16px;padding:15px 26px">
          <span>⚡</span>
          <span class="btn-col">
            <span class="btn-price">₹{BOOK['digital_price']}</span>
            <span class="btn-sub">Digital PDF · Emailed</span>
          </span>
        </button>
      </div>
    </div>
  </div>

</div><!-- /.bk -->

<script>
// ── RIDDLES ────────────────────────────────────────────
const BK_RIDDLES = {riddles_js};
let bkRidIdx = 0;

function bkLoadRiddle() {{
  const r = BK_RIDDLES[bkRidIdx];
  document.getElementById('bkRiddleCounter').textContent =
    'Riddle ' + (bkRidIdx + 1) + ' of ' + BK_RIDDLES.length;
  document.getElementById('bkRiddleQ').textContent = r.q;
  document.getElementById('bkRiddleResult').innerHTML = '';
  const wrap = document.getElementById('bkRiddleOpts');
  wrap.innerHTML = '';
  r.opts.forEach((opt, i) => {{
    const b = document.createElement('button');
    b.className = 'ropt';
    b.textContent = opt;
    b.onclick = () => bkCheckRiddle(i);
    wrap.appendChild(b);
  }});
}}
function bkCheckRiddle(idx) {{
  const r = BK_RIDDLES[bkRidIdx];
  document.querySelectorAll('.ropt').forEach((b, i) => {{
    if (i === r.correct) b.classList.add('correct');
    else if (i === idx)  b.classList.add('wrong');
    b.disabled = true;
  }});
  const res = document.getElementById('bkRiddleResult');
  res.innerHTML = idx === r.correct
    ? '<strong style="color:#256A45">🎉 Correct!</strong> ' + r.fact
    : '<strong style="color:#C0392B">Not quite!</strong> ' + r.fact;
}}
function bkNextRiddle() {{
  bkRidIdx = (bkRidIdx + 1) % BK_RIDDLES.length;
  bkLoadRiddle();
}}
bkLoadRiddle();

// ── MODAL ──────────────────────────────────────────────
let bkType = 'physical';

function bkOpen(type) {{
  bkType = type;
  bkGoStep(1);
  document.getElementById('bkS1').style.display = 'block';
  document.getElementById('bkS2').style.display = 'none';
  document.getElementById('bkS3').style.display = 'none';
  document.getElementById('bkSuccess').style.display = 'none';

  if (type === 'physical') {{
    document.getElementById('bkModalTitle').textContent = '📦 Order Physical Copy';
    document.getElementById('bkModalSub').textContent   = 'Delivered to your doorstep · ₹{BOOK['physical_price']}';
    document.getElementById('bkAddrBlock').style.display = 'block';
    document.getElementById('bkEmailHint').textContent   = 'Order confirmation will be sent here.';
  }} else {{
    document.getElementById('bkModalTitle').textContent = '⚡ Order Digital PDF';
    document.getElementById('bkModalSub').textContent   = 'Emailed after payment confirmation · ₹{BOOK['digital_price']}';
    document.getElementById('bkAddrBlock').style.display = 'none';
    document.getElementById('bkEmailHint').textContent   = '📧 Your PDF will be sent here after we confirm payment.';
  }}

  document.getElementById('bkOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}}

function bkClose() {{
  document.getElementById('bkOverlay').classList.remove('open');
  document.body.style.overflow = '';
}}
function bkOverlayClick(e) {{
  if (e.target.id === 'bkOverlay') bkClose();
}}
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') bkClose(); }});

function bkGoStep(n) {{
  [1,2,3].forEach(i => {{
    document.getElementById('bkTab' + i).classList.toggle('active', i === n);
  }});
}}

function bkStep2() {{
  const name  = document.getElementById('bkName').value.trim();
  const email = document.getElementById('bkEmail').value.trim();
  const phone = document.getElementById('bkPhone').value.trim();
  if (!name || !email || !phone) {{
    alert('Please fill in your name, email and phone number.');
    return;
  }}
  if (bkType === 'physical') {{
    const addr = document.getElementById('bkAddr').value.trim();
    const city = document.getElementById('bkCity').value.trim();
    const pin  = document.getElementById('bkPin').value.trim();
    if (!addr || !city || !pin) {{
      alert('Please fill in your delivery address.');
      return;
    }}
  }}
  const price = bkType === 'physical' ? '₹{BOOK['physical_price']}' : '₹{BOOK['digital_price']}';
  document.getElementById('bkAmount').textContent = price;
  document.getElementById('bkPayNote').textContent = bkType === 'physical'
    ? 'After we confirm your payment, your physical book will be dispatched within 1–2 working days.'
    : 'After we confirm your payment screenshot, the PDF will be emailed to you within a few hours.';
  document.getElementById('bkS1').style.display = 'none';
  document.getElementById('bkS2').style.display = 'block';
  bkGoStep(2);
}}

function bkStep3() {{
  const name  = document.getElementById('bkName').value.trim();
  const email = document.getElementById('bkEmail').value.trim();
  const phone = document.getElementById('bkPhone').value.trim();
  const price = bkType === 'physical' ? '₹{BOOK['physical_price']}' : '₹{BOOK['digital_price']}';
  const typeStr = bkType === 'physical' ? 'Physical Copy' : 'Digital PDF';

  const msg = encodeURIComponent(
    'Hi! I just paid ' + price + ' for *{BOOK['title']}* (' + typeStr + ').\\n\\n' +
    'Name: ' + name + '\\nPhone: ' + phone + '\\nEmail: ' + email + '\\n\\n' +
    'Screenshot attached! Please confirm my order 🙏'
  );
  document.getElementById('bkWaLink').href = 'https://wa.me/{BOOK['whatsapp']}?text=' + msg;

  if (bkType === 'digital') {{
    document.getElementById('bkDeliveryNote').textContent =
      'the PDF will be emailed to ' + email + ' once we confirm payment.';
    document.getElementById('bkDigiNote').textContent =
      '📧 Digital book: your PDF will be emailed to ' + email + ' after payment is confirmed.';
  }} else {{
    document.getElementById('bkDeliveryNote').textContent =
      'your book will be dispatched within 1–2 working days.';
    document.getElementById('bkDigiNote').textContent =
      '📬 Order confirmation will be sent to ' + email + '.';
  }}

  document.getElementById('bkS2').style.display = 'none';
  document.getElementById('bkS3').style.display = 'block';
  bkGoStep(3);
}}

function bkFileSelected(input) {{
  if (input.files && input.files[0])
    document.getElementById('bkUploadLbl').textContent = '✅ ' + input.files[0].name;
}}

function bkSubmit() {{
  const name  = document.getElementById('bkName').value.trim();
  const email = document.getElementById('bkEmail').value.trim();
  ['bkS1','bkS2','bkS3'].forEach(id => document.getElementById(id).style.display = 'none');
  [1,2,3].forEach(i => document.getElementById('bkTab'+i).classList.remove('active'));
  const box = document.getElementById('bkSuccess');
  box.style.display = 'block';
  box.innerHTML = `
    <div class="bk-success-icon">🎉</div>
    <div class="bk-success-title">Order Submitted!</div>
    <p class="bk-success-sub">${{
      bkType === 'digital'
        ? 'Thank you, ' + name + '! Once we confirm your payment, the PDF will be sent to ' + email + '. We will WhatsApp you too!'
        : 'Thank you, ' + name + '! Your book will be dispatched in 1–2 days. We will WhatsApp you with updates!'
    }}</p>`;
}}
</script>
"""

st.markdown(page_html, unsafe_allow_html=True)
