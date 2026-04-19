import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="The Secret Kingdom of Numbers",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── 1. BOOK CONFIG & DATA ──────────────────────────────────────────────────────
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
            "text": "The old door was carved with a thousand spirals — each one a number, each number a secret. 'To enter,' said the Guardian, 'you must answer: what number is both everything and nothing?' Aryan smiled slowly. He already knew."
        },
        {
            "chapter": "Chapter 4",
            "title":   "The Fraction Forest",
            "emoji":   "🌳",
            "text": "Half the trees were tall, a quarter were golden, one-eighth glowed violet at night. The forest was a living fraction — always adding to one whole, no matter how you divided it. 'We are pieces,' whispered the Fraction Fairy. 'But together, we are complete.'"
        },
        {
            "chapter": "Chapter 9",
            "title":   "Zero's Secret",
            "emoji":   "⭕",
            "text": "Everyone laughed at Zero. 'You are nothing!' they said. But Zero just smiled and stepped beside One — and One became Ten. Then Hundred. Then Thousand. 'Nothing,' said Zero quietly, 'can become everything.'"
        },
    ],
    "physical_price": 299,
    "digital_price":  99,
    "upi_id":         "aryan@oksbi",       
    "whatsapp":       "919876543210",      
    "seller_email":   "aryan@example.com", 
}

RIDDLES = [
    {
        "q": "I am neither positive nor negative. What number am I?",
        "opts": ["One", "Zero", "Infinity", "Half"],
        "correct": 1,
        "fact": "Zero is the only number that is neither positive nor negative — and it can make any number ten times bigger just by standing beside it!",
    },
    {
        "q": "A fraction whose numerator equals its denominator always equals…?",
        "opts": ["Zero", "Two", "One", "Itself"],
        "correct": 2,
        "fact": "Any number divided by itself equals 1. That's why 4/4, 99/99 and 1000/1000 are all exactly 1!",
    }
]

# ── 2. SEPARATED CSS (No f-string bracket escaping needed) ──────────────────────
CSS = """
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500;600;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
<style>
#MainMenu, header, footer, .stDeployButton, .stToolbar, [data-testid="stDecoration"], [data-testid="stHeader"] { display: none !important; }
.main .block-container { padding: 0 !important; max-width: 100% !important; }
.main { padding: 0 !important; }
section[data-testid="stMain"] > div { padding: 0 !important; }

.bk * { margin:0; padding:0; box-sizing:border-box; }
.bk { line-height: 1.6; -webkit-font-smoothing: antialiased; }
.bk {
  --bg: #FAFAF8; --ink: #1C1C1C; --ink2: #4A4A4A; --ink3: #888;
  --border: #E4E0D8; --cream: #F5F0E8; --accent: #C8602A;
  --violet: #3D2B6E; --goldf: #F0D080; --green: #256A45; --red: #C0392B;
  --white: #FFFFFF; --sh: 0 2px 12px rgba(0,0,0,.07); --sh-lg: 0 14px 48px rgba(0,0,0,.14);
  --r: 12px; --rl: 20px; font-family: 'DM Sans', sans-serif; color: var(--ink); background: var(--bg);
}

.bk .wrap { max-width:1020px; margin:0 auto; padding:0 28px; }
.bk .section { padding:72px 0; }
.bk .lbl { display:inline-block; font-size:11px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; color:var(--accent); margin-bottom:12px; }
.bk h2 { font-family:'Playfair Display',serif; font-size:clamp(24px,3vw,38px); font-weight:900; line-height:1.15; color:var(--ink); margin-bottom:0; }

.bk .hero { background: var(--violet); padding: 60px 0 52px; position: relative; overflow: hidden; }
.bk .hero-grid { position:relative; z-index:1; display:grid; grid-template-columns: 1fr 300px; gap: 56px; align-items: center; }
.bk .hero h1 { font-family:'Playfair Display',serif; font-size:clamp(30px,4.2vw,50px); font-weight:900; color:#fff; line-height:1.12; margin-bottom:12px; }
.bk .hero h1 em { color:var(--goldf); font-style:normal; }
.bk .hero-desc { font-size:15px; color:rgba(255,255,255,.68); line-height:1.78; max-width:500px; margin-bottom:28px; }

.bk .btn-row { display:flex; gap:12px; flex-wrap:wrap; margin-top:20px; }
.bk .btn { display:inline-flex; align-items:center; gap:10px; padding:13px 22px; border-radius:var(--r); font-size:14px; font-weight:600; cursor:pointer; border:none; transition:transform .2s; }
.bk .btn:hover { transform:translateY(-2px); }
.bk .btn-solid { background:var(--accent); color:#fff; }
.bk .btn-ghost { background:rgba(255,255,255,.1); color:#fff; border:1px solid rgba(255,255,255,.22); }
.bk .btn-col { display:flex; flex-direction:column; line-height:1.25; text-align:left;}
.bk .btn-price { font-size:18px; font-weight:800; }
.bk .btn-sub { font-size:11px; opacity:.7; }

.bk .prev-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(255px,1fr)); gap:20px; margin-top:36px; }
.bk .prev-card { background:var(--white); border:1px solid var(--border); border-radius:var(--rl); padding:28px 24px; transition:transform .25s; }
.bk .prev-card:hover { transform:translateY(-5px); box-shadow:var(--sh-lg); }
.bk .prev-emoji { font-size:30px; margin-bottom:14px; display:block; }
.bk .prev-title { font-family:'Playfair Display',serif; font-size:17px; font-weight:700; margin-bottom:12px; }

/* Modal and Riddle CSS trimmed for brevity but fully functional */
.bk .riddle-box { background:var(--white); border:1px solid var(--border); border-radius:var(--rl); padding:40px 36px; max-width:640px; margin:40px auto 0; text-align:center; }
.bk .ropt { padding:10px 22px; border:2px solid var(--border); border-radius:50px; background:#fff; margin:5px; cursor:pointer; }
.bk .ropt.correct { border-color:var(--green); background:#E6F4ED; color:var(--green); }
.bk .ropt.wrong { border-color:var(--red); background:#FDECEA; color:var(--red); }

.bk-overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,.55); z-index:9999; align-items:center; justify-content:center; }
.bk-overlay.open { display:flex; }
.bk-modal { background:#fff; border-radius:20px; width:min(500px,92vw); max-height:90vh; overflow-y:auto; position:relative; }
.bk-modal-head { padding:26px 28px 18px; border-bottom:1px solid #E4E0D8; }
.bk-modal-body { padding:22px 28px 28px; }
.bk-input { width:100%; padding:11px 13px; border:1.5px solid #E4E0D8; border-radius:10px; margin-bottom:14px; }
.bk-btn-primary { background:#C8602A; color:#fff; width:100%; padding:14px; border:none; border-radius:10px; cursor:pointer; font-weight:bold;}
.bk-btn-wa { background:#25D366; color:#fff; width:100%; padding:14px; border:none; border-radius:10px; cursor:pointer; font-weight:bold; display:block; text-align:center; text-decoration:none; margin-bottom:15px;}
</style>
"""

# ── 3. SEPARATED JS (Using injected BK_DATA for safety) ────────────────────────
JS = """
<script>
// Logic strictly uses the injected BK_DATA object to prevent f-string crashes.
let bkRidIdx = 0;
let bkType = 'physical';

function bkLoadRiddle() {
  const r = BK_RIDDLES[bkRidIdx];
  document.getElementById('bkRiddleQ').textContent = r.q;
  const wrap = document.getElementById('bkRiddleOpts');
  wrap.innerHTML = '';
  document.getElementById('bkRiddleResult').innerHTML = '';
  r.opts.forEach((opt, i) => {
    const b = document.createElement('button');
    b.className = 'ropt';
    b.textContent = opt;
    b.onclick = () => bkCheckRiddle(i);
    wrap.appendChild(b);
  });
}

function bkCheckRiddle(idx) {
  const r = BK_RIDDLES[bkRidIdx];
  document.querySelectorAll('.ropt').forEach((b, i) => {
    if (i === r.correct) b.classList.add('correct');
    else if (i === idx)  b.classList.add('wrong');
    b.disabled = true;
  });
  const res = document.getElementById('bkRiddleResult');
  res.innerHTML = idx === r.correct
    ? '<strong style="color:#256A45">🎉 Correct!</strong> ' + r.fact
    : '<strong style="color:#C0392B">Not quite!</strong> ' + r.fact;
}

function bkOpen(type) {
  bkType = type;
  document.getElementById('bkS1').style.display = 'block';
  document.getElementById('bkS2').style.display = 'none';
  document.getElementById('bkS3').style.display = 'none';
  
  if (type === 'physical') {
    document.getElementById('bkModalTitle').textContent = '📦 Order Physical Copy';
    document.getElementById('bkModalSub').textContent   = `Delivered · ₹${BK_DATA.physical_price}`;
    document.getElementById('bkAddr').style.display = 'block';
  } else {
    document.getElementById('bkModalTitle').textContent = '⚡ Order Digital PDF';
    document.getElementById('bkModalSub').textContent   = `Emailed · ₹${BK_DATA.digital_price}`;
    document.getElementById('bkAddr').style.display = 'none';
  }
  document.getElementById('bkOverlay').classList.add('open');
}

function bkClose() { document.getElementById('bkOverlay').classList.remove('open'); }

function bkStep2() {
  document.getElementById('bkAmount').textContent = bkType === 'physical' ? `₹${BK_DATA.physical_price}` : `₹${BK_DATA.digital_price}`;
  document.getElementById('bkS1').style.display = 'none';
  document.getElementById('bkS2').style.display = 'block';
}

function bkStep3() {
  const name  = document.getElementById('bkName').value.trim() || 'Customer';
  const price = bkType === 'physical' ? `₹${BK_DATA.physical_price}` : `₹${BK_DATA.digital_price}`;
  
  // Create clean WhatsApp Message
  const msg = encodeURIComponent(
    `Hi! I just paid ${price} for *${BK_DATA.title}*.\n\nName: ${name}\n\nI will attach my payment screenshot to this chat right now!`
  );
  document.getElementById('bkWaLink').href = `https://wa.me/${BK_DATA.whatsapp}?text=${msg}`;

  document.getElementById('bkS2').style.display = 'none';
  document.getElementById('bkS3').style.display = 'block';
}

function bkSubmit() { bkClose(); alert("Order successfully registered! We will coordinate via WhatsApp."); }

setTimeout(bkLoadRiddle, 200);
</script>
"""

# ── 4. HTML CONSTRUCTION & INJECTION ───────────────────────────────────────────
preview_html = "".join([
    f"""<div class="prev-card"><span class="prev-emoji">{p['emoji']}</span>
    <div class="prev-title">{p['title']}</div><p>{p['text']}</p></div>""" 
    for p in BOOK["preview"]
])

HTML = f"""
<script>
  const BK_DATA = {json.dumps(BOOK)};
  const BK_RIDDLES = {json.dumps(RIDDLES)};
</script>

<div class="bk">
  <section class="hero">
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <h1>The Secret <em>Kingdom</em><br>of Numbers</h1>
          <p class="hero-desc">{BOOK['description']}</p>
          <div class="btn-row">
            <button class="btn btn-solid" onclick="bkOpen('physical')">
              <span class="btn-col">
                <span class="btn-price">₹{BOOK['physical_price']}</span><span class="btn-sub">Physical Copy</span>
              </span>
            </button>
            <button class="btn btn-ghost" onclick="bkOpen('digital')">
              <span class="btn-col">
                <span class="btn-price">₹{BOOK['digital_price']}</span><span class="btn-sub">Digital PDF</span>
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section"><div class="wrap">
    <h2>A glimpse inside the Kingdom</h2>
    <div class="prev-grid">{preview_html}</div>
  </div></section>

  <section class="section"><div class="wrap" style="text-align:center">
    <h2>Can you solve a riddle from the book?</h2>
    <div class="riddle-box">
      <div id="bkRiddleQ" style="font-weight:bold; font-size:1.2rem; margin-bottom:15px;"></div>
      <div id="bkRiddleOpts" style="margin-bottom:15px;"></div>
      <div id="bkRiddleResult"></div>
      <button onclick="bkLoadRiddle()" style="margin-top:15px; padding: 5px 15px; cursor: pointer;">Next Riddle</button>
    </div>
  </div></section>
</div>

<div class="bk-overlay" id="bkOverlay">
  <div class="bk-modal" id="bkModal">
    <div class="bk-modal-head">
      <h3 id="bkModalTitle"></h3>
      <p id="bkModalSub"></p>
    </div>
    <div class="bk-modal-body">
      <div id="bkS1">
        <input class="bk-input" id="bkName" type="text" placeholder="Full Name *">
        <input class="bk-input" id="bkAddr" type="text" placeholder="Delivery Address *">
        <button class="bk-btn-primary" onclick="bkStep2()">Continue to Payment →</button>
      </div>
      <div id="bkS2" style="display:none; text-align:center;">
        <h2 id="bkAmount" style="margin-bottom: 5px;"></h2>
        <p>UPI ID: <strong>{BOOK['upi_id']}</strong></p>
        <button class="bk-btn-primary" style="margin-top:15px;" onclick="bkStep3()">I have paid →</button>
      </div>
      <div id="bkS3" style="display:none; text-align:center;">
        <p style="margin-bottom: 20px;">Click below to open WhatsApp. <strong>Don't forget to attach your screenshot</strong> in the chat!</p>
        <a id="bkWaLink" class="bk-btn-wa" target="_blank">📲 Open WhatsApp to Confirm</a>
        <button class="bk-btn-primary" onclick="bkSubmit()" style="background:#4A4A4A;">Close Window</button>
      </div>
    </div>
  </div>
</div>
"""

# Combine all parts
full_page = CSS + HTML + JS

# Render everything cleanly inside a dedicated HTML component
components.html(full_page, height=1000, scrolling=True)
