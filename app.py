import streamlit as st
import time

# ─── PAGE CONFIGURATION ────────────────────────────────────────────────
st.set_page_config(
    page_title="The Number Knight | Aryan's Math Adventure",
    page_icon="🗡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── PITCH DECK DESIGN SYSTEM + FANTASY BOOK THEME (CSS) ───────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

    :root {
      --ink: #0f0f1a;
      --ink3: #5a5a7a;
      --paper: #f8f7f4;
      --cream: #f0ebe0;
      --cream2: #e8e1d4;
      --r: #c0392b;   /* Deep Red */
      --b: #1a4a8a;   /* Royal Blue */
      --gold: #b8860b;
    }

    /* 1. Background: Subtle Math Grid & Paper Color */
    .stApp {
        background-color: var(--paper);
        background-image: 
            linear-gradient(var(--cream) 1px, transparent 1px),
            linear-gradient(90deg, var(--cream) 1px, transparent 1px);
        background-size: 40px 40px;
        font-family: 'Inter', sans-serif;
    }

    /* 2. Floating Magical Background Shapes (Pure CSS) */
    .magic-orb-1 {
        position: fixed; top: -10vw; right: -5vw; width: 40vw; height: 40vw;
        background: radial-gradient(circle, rgba(192,57,43,0.08) 0%, rgba(255,255,255,0) 70%);
        border-radius: 50%; z-index: -1; pointer-events: none;
    }
    .magic-orb-2 {
        position: fixed; bottom: -10vw; left: -10vw; width: 50vw; height: 50vw;
        background: radial-gradient(circle, rgba(26,74,138,0.06) 0%, rgba(255,255,255,0) 70%);
        border-radius: 50%; z-index: -1; pointer-events: none;
    }

    /* 3. Typography */
    h1, h2, h3, h4, h5 {
        font-family: 'Cormorant Garamond', serif !important;
        color: var(--ink) !important;
        font-weight: 700 !important;
    }
    
    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(48px, 8vw, 72px);
        font-weight: 700;
        color: var(--ink);
        line-height: 1.05;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 5px;
        text-shadow: 2px 2px 0px #fff;
    }
    .hero-title em { color: var(--r); font-style: italic; }
    
    .hero-subtitle {
        text-align: center; color: var(--ink3); font-size: 1.2rem;
        margin-bottom: 40px; font-weight: 500;
    }

    /* 4. Book Page Effect for Containers */
    [data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #ffffff;
        border: 1px solid var(--cream2) !important;
        /* Make it look like a book spine on the left edge */
        border-radius: 3px 15px 15px 3px !important; 
        box-shadow: -6px 0px 0px var(--b), 5px 10px 25px rgba(0,0,0,0.04) !important;
        padding: 30px !important;
        position: relative;
        transition: transform 0.3s ease;
    }
    [data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-2px);
    }

    /* 5. Button Styling (Themed) */
    .stButton>button {
        background-color: var(--r); color: #fff;
        font-family: 'Inter', sans-serif; font-weight: 600;
        border: none; border-radius: 6px; padding: 12px 28px;
        box-shadow: 0 4px 12px rgba(192,57,43,0.3);
        transition: all 0.2s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #a02d22; transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(192,57,43,0.4); color: #fff;
    }

    /* Decorative element */
    .separator {
        text-align: center; color: var(--gold); font-size: 24px;
        letter-spacing: 15px; margin: 30px 0; opacity: 0.6;
    }
</style>

<div class="magic-orb-1"></div>
<div class="magic-orb-2"></div>
""", unsafe_allow_html=True)

# ─── SESSION STATE FOR INTERACTIVITY ───────────────────────────────────
if 'preview_unlocked' not in st.session_state:
    st.session_state.preview_unlocked = False

# ─── HERO SECTION ──────────────────────────────────────────────────────
st.markdown("<div class='hero-title'>The Number <em>Knight</em></div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>✧ A magical adventure where Math is your only weapon ✧</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    # A placeholder for the actual book cover image
    st.image("https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=600&q=80", caption="Available in Physical & Digital")

with col2:
    st.markdown("### ⬢ The Story")
    st.markdown("""
    **What if every equation was a spell?** Dive into a fantastical world where Prime Numbers are ancient guardians, Fractions build bridges over bottomless pits, and the fearless hero, Zero, discovers the ultimate power.
    
    * 📖 **120 Pages of Adventure**
    * 🧩 **Hidden Math Puzzles**
    * 🎯 **Ages 9 to 14**
    """)
    
    st.markdown("### ₹299 Physical | ₹99 Digital")
    st.info("👇 Scroll down to secure your copy!")

st.markdown("<div class='separator'>✦ ✦ ✦</div>", unsafe_allow_html=True)

# ─── FUTURISTIC INTERACTIVITY: THE VAULT ───────────────────────────────
st.header("🔐 Unlock the Secret Grimoire")
st.write("Most books just *give* you a preview. This one makes you earn it. Solve the Sphinx's riddle to unlock a secret sneak peek of Chapter 1.")

if not st.session_state.preview_unlocked:
    puzzle_container = st.container(border=True)
    with puzzle_container:
        st.markdown("### △ The Sphinx's Challenge")
        st.markdown("*\"I am an odd number. Take away one letter, and I become even. What number am I?\"*")
        
        guess = st.text_input("Type your answer below:", key="puzzle_guess").strip().lower()
        
        if st.button("Unlock The Vault"):
            if guess == "seven":
                st.session_state.preview_unlocked = True
                st.success("Correct! The magical seals are breaking...")
                time.sleep(1)
                st.rerun()
            elif guess != "":
                st.error("The Sphinx shakes her head. Try again!")
else:
    st.success("✨ The Grimoire is Unlocked!")
    unlocked_container = st.container(border=True)
    with unlocked_container:
        st.markdown("### Chapter 1: The Hollow Zero")
        st.markdown("> *The heavy iron doors of the Polygon Keep slammed shut. Aria looked at the glowing equation etched into her wrist. It was fading. She needed a Prime, and she needed it fast. 'Zero!' she yelled into the echoing hall. 'I need you to multiply!' But Zero just stood there, smiling calmly. 'You forget, Aria,' Zero whispered. 'When I multiply, everything disappears.'*")

st.markdown("<div class='separator'>✦ ✦ ✦</div>", unsafe_allow_html=True)

# ─── AUTHOR PROFILE ────────────────────────────────────────────────────
author_container = st.container(border=True)
with author_container:
    col3, col4 = st.columns([1, 3], gap="medium")
    with col3:
        st.markdown("### 👦 About the Author")
        st.write("*(Photo here)*")
    with col4:
        st.markdown("""
        **Aryan, Class 8 Student & Math Explorer** Writing from his classroom in Pune, Aryan believes that math doesn't have to be boring equations on a whiteboard. By combining his love for fantasy novels and puzzle-solving, he wrote *The Number Knight* to show kids that math is basically real-world magic.
        """)

st.markdown("<div class='separator'>✦ ✦ ✦</div>", unsafe_allow_html=True)

# ─── SMART CHECKOUT SYSTEM ─────────────────────────────────────────────
st.header("🛒 Secure Your Copy")
st.write("Select your preferred format below. Payments are securely accepted via any UPI app.")

tab1, tab2 = st.tabs(["📦 Physical Book (₹299)", "⚡ Digital PDF (₹99)"])

# -- PHYSICAL COPY TAB --
with tab1:
    with st.container(border=True):
        st.markdown("#### 📬 Home Delivery")
        st.write("Delivered right to your doorstep within 3-5 working days.")
        
        p_name = st.text_input("Full Name *")
        p_phone = st.text_input("WhatsApp Number *")
        p_address = st.text_area("Full Delivery Address with PIN Code *", placeholder="e.g., Flat 12, Tower A, Pimpri, Pune 411018")
        
        st.markdown("#### 💳 Payment (₹299)")
        st.info("Scan the QR code below with GPay, Paytm, or PhonePe. Once paid, enter the 12-digit UPI Transaction ID.")
        
        # Replace with the actual UPI QR code image
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_monument_may_7_2013.jpg", width=150)
        st.write("**UPI ID:** aryan@upi")
        
        p_txn_id = st.text_input("UPI Transaction ID *", placeholder="e.g., 312345678901")
        
        if st.button("Submit Order for Physical Copy"):
            if not p_name or not p_phone or not p_address or not p_txn_id:
                st.error("Please fill in all required fields!")
            else:
                st.success(f"🎉 Thank you, {p_name}! We are verifying your payment of ₹299. We will update you on WhatsApp at {p_phone}!")
                st.balloons()

# -- DIGITAL COPY TAB --
with tab2:
    with st.container(border=True):
        st.markdown("#### 📧 Instant Digital Access")
        st.write("Sent directly to your email inbox immediately after payment confirmation.")
        
        d_name = st.text_input("Full Name *", key="d_name")
        d_email = st.text_input("Email Address (where we will send the PDF) *", key="d_email")
        
        st.markdown("#### 💳 Payment (₹99)")
        st.info("Scan the QR code below with any UPI app. Once paid, enter the 12-digit UPI Transaction ID.")
        
        # Replace with the actual UPI QR code image
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_monument_may_7_2013.jpg", width=150)
        st.write("**UPI ID:** aryan@upi")
        
        d_txn_id = st.text_input("UPI Transaction ID *", key="d_txn")
        
        if st.button("Submit Order for Digital Copy"):
            if not d_name or not d_email or not d_txn_id:
                st.error("Please fill in your name, email, and Transaction ID!")
            else:
                st.success(f"🎉 Awesome, {d_name}! Once your ₹99 payment is verified, the PDF will be beamed to {d_email}.")
                st.snow()
