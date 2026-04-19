import streamlit as st
import time

# ─── PAGE CONFIGURATION ────────────────────────────────────────────────
st.set_page_config(
    page_title="The Number Knight | Aryan's Math Adventure",
    page_icon="📖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── PITCH DECK DESIGN SYSTEM (CSS) ────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

    /* Variables extracted from pitch_deck_Main.html */
    :root {
      --ink: #0f0f1a;
      --ink3: #5a5a7a;
      --paper: #f8f7f4;
      --cream: #f0ebe0;
      --cream2: #e8e1d4;
      --r: #c0392b; 
    }

    /* Base application style */
    .stApp {
        background-color: var(--paper);
        color: var(--ink);
        font-family: 'Inter', sans-serif;
    }

    /* Headings Typography */
    h1, h2, h3, h4, h5 {
        font-family: 'Cormorant Garamond', serif !important;
        color: var(--ink) !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em;
    }

    /* Custom Hero Title styling */
    .hero-title {
        font-family: 'Cormorant Garamond', serif;
        font-size: clamp(42px, 6vw, 64px);
        font-weight: 700;
        color: var(--ink);
        line-height: 1.05;
        letter-spacing: -0.02em;
        margin-bottom: 10px;
    }
    .hero-title em {
        color: var(--r);
        font-style: normal;
    }

    /* Hide standard Streamlit chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Style the native Streamlit containers (st.container(border=True)) */
    [data-testid="stVerticalBlock"] > div > div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #fff;
        border: 1px solid var(--cream2);
        border-radius: 16px;
        padding: 10px;
        box-shadow: 0 4px 16px rgba(0,0,0,0.02);
    }

    /* Button styling (using the Red from your palette) */
    .stButton>button {
        background-color: var(--r);
        color: #fff;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #a02d22;
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(192,57,43,0.25);
        color: #fff;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent;
        border-bottom: 1px solid var(--cream2);
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        color: var(--ink3);
    }
    .stTabs [aria-selected="true"] {
        color: var(--r) !important;
        border-bottom-color: var(--r) !important;
    }

    /* Text Inputs */
    .stTextInput input, .stTextArea textarea {
        background-color: #fff;
        border: 1px solid var(--cream2);
        border-radius: 8px;
        color: var(--ink);
        font-family: 'Inter', sans-serif;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--r);
        box-shadow: 0 0 0 1px var(--r);
    }
</style>
""", unsafe_allow_html=True)

# ─── SESSION STATE FOR INTERACTIVITY ───────────────────────────────────
if 'preview_unlocked' not in st.session_state:
    st.session_state.preview_unlocked = False

# ─── HERO SECTION ──────────────────────────────────────────────────────
st.markdown("<div class='hero-title'>The Number <em>Knight</em></div>", unsafe_allow_html=True)
st.subheader("A magical adventure where Math is your only weapon.")
st.write("") # Spacer

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    # A placeholder for the actual book cover image
    st.image("https://images.unsplash.com/photo-1512820200504-83970f81b433?auto=format&fit=crop&w=400&q=80", caption="Physical & Digital Editions Available")

with col2:
    st.markdown("""
    **What if every equation was a spell?** Dive into a fantastical world where Prime Numbers are ancient guardians, Fractions build bridges over bottomless pits, and the fearless hero, Zero, discovers the ultimate power.
    
    * 📖 **120 Pages of Adventure**
    * 🧩 **Hidden Math Puzzles**
    * 🎯 **Ages 9 to 14**
    """)
    
    st.markdown("### ₹299 Physical | ₹99 Digital")
    st.write("Scroll down to secure your copy!")

st.divider()

# ─── FUTURISTIC INTERACTIVITY: THE VAULT ───────────────────────────────
st.header("🔐 Unlock the Secret Chapter")
st.write("Most books just *give* you a preview. This one makes you earn it. Solve the riddle to unlock a secret sneak peek of Chapter 1.")

if not st.session_state.preview_unlocked:
    puzzle_container = st.container(border=True)
    with puzzle_container:
        st.markdown("**The Sphinx's Challenge:**")
        st.markdown("*I am an odd number. Take away a letter and I become even. What number am I?*")
        
        guess = st.text_input("Type your answer below:", key="puzzle_guess").strip().lower()
        
        if st.button("Unlock Vault"):
            if guess == "seven":
                st.session_state.preview_unlocked = True
                st.success("Correct! The vault is opening...")
                time.sleep(1)
                st.rerun()
            elif guess != "":
                st.error("The Sphinx shakes her head. Try again!")
else:
    st.success("✨ Vault Unlocked!")
    unlocked_container = st.container(border=True)
    with unlocked_container:
        st.markdown("### Chapter 1: The Hollow Zero")
        st.markdown("> *The heavy iron doors of the Polygon Keep slammed shut. Aria looked at the glowing equation etched into her wrist. It was fading. She needed a Prime, and she needed it fast. 'Zero!' she yelled into the echoing hall. 'I need you to multiply!' But Zero just stood there, smiling calmly. 'You forget, Aria,' Zero whispered. 'When I multiply, everything disappears.'*")

st.divider()

# ─── AUTHOR PROFILE ────────────────────────────────────────────────────
col3, col4 = st.columns([1, 3], gap="large")
with col3:
    st.markdown("### 👦 About the Author")
    st.write("*(Photo here)*")
with col4:
    st.markdown("""
    **Aryan, Class 8 Student & Math Explorer** Writing from his classroom in Pune, Aryan believes that math doesn't have to be boring equations on a whiteboard. By combining his love for fantasy novels and puzzle-solving, he wrote *The Number Knight* to show kids that math is basically real-world magic.
    """)

st.divider()

# ─── SMART CHECKOUT SYSTEM ─────────────────────────────────────────────
st.header("🛒 Order Your Copy")
st.write("Select your format below. Payments are securely accepted via any UPI app.")

tab1, tab2 = st.tabs(["📦 Physical Copy (₹299)", "⚡ Digital PDF (₹99)"])

# -- PHYSICAL COPY TAB --
with tab1:
    st.write("Delivered right to your doorstep within 3-5 working days.")
    with st.form("physical_order_form"):
        st.subheader("1. Shipping Details")
        p_name = st.text_input("Full Name *")
        p_phone = st.text_input("WhatsApp Number *")
        p_address = st.text_area("Full Delivery Address with PIN Code *", placeholder="e.g., Flat 12, Tower A, Pimpri, Pune 411018")
        
        st.subheader("2. Payment (₹299)")
        st.info("Scan the QR code below with GPay, Paytm, or PhonePe. Once paid, enter the 12-digit UPI Transaction ID.")
        
        # Replace with the actual UPI QR code image generated for his account
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_monument_may_7_2013.jpg", width=180, caption="Aryan's UPI QR Code")
        st.write("**UPI ID:** aryan@upi")
        
        p_txn_id = st.text_input("UPI Transaction ID *", placeholder="e.g., 312345678901")
        
        p_submitted = st.form_submit_button("Place Order")
        if p_submitted:
            if not p_name or not p_phone or not p_address or not p_txn_id:
                st.error("Please fill in all required fields!")
            else:
                st.success(f"🎉 Thank you, {p_name}! We are verifying your payment of ₹299. We will update you on WhatsApp at {p_phone}!")
                st.balloons()

# -- DIGITAL COPY TAB --
with tab2:
    st.write("Sent directly to your email inbox immediately after payment confirmation.")
    with st.form("digital_order_form"):
        st.subheader("1. Digital Details")
        d_name = st.text_input("Full Name *", key="d_name")
        d_email = st.text_input("Email Address (where we will send the PDF) *", key="d_email")
        
        st.subheader("2. Payment (₹99)")
        st.info("Scan the QR code below with any UPI app. Once paid, enter the 12-digit UPI Transaction ID.")
        
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_monument_may_7_2013.jpg", width=180, caption="Aryan's UPI QR Code")
        st.write("**UPI ID:** aryan@upi")
        
        d_txn_id = st.text_input("UPI Transaction ID *", key="d_txn")
        
        d_submitted = st.form_submit_button("Send me the E-Book")
        if d_submitted:
            if not d_name or not d_email or not d_txn_id:
                st.error("Please fill in your name, email, and Transaction ID!")
            else:
                st.success(f"🎉 Awesome, {d_name}! Once your ₹99 payment is verified, the PDF will be beamed to {d_email}.")
                st.snow()
