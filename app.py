import streamlit as st
import time

# ─── PAGE CONFIGURATION ────────────────────────────────────────────────
st.set_page_config(
    page_title="The Number Knight | Aryan's Math Adventure",
    page_icon="🗡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── CUSTOM LIGHTWEIGHT CSS ────────────────────────────────────────────
# Safe, native-friendly styling to make it pop without breaking layout
st.markdown("""
<style>
    /* Clean up the default Streamlit UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom button styling */
    .stButton>button {
        background-color: #6C63FF;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #574BDB;
        transform: scale(1.02);
    }
    
    /* Highlight text */
    .highlight {
        color: #6C63FF;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ─── SESSION STATE FOR INTERACTIVITY ───────────────────────────────────
if 'preview_unlocked' not in st.session_state:
    st.session_state.preview_unlocked = False

# ─── HERO SECTION ──────────────────────────────────────────────────────
st.title("🗡️ The Number Knight")
st.subheader("A magical adventure where Math is your only weapon.")

col1, col2 = st.columns([1, 1.2])

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
col3, col4 = st.columns([1, 3])
with col3:
    st.markdown("### 👦 About the Author")
    st.write("*(Photo here)*")
with col4:
    st.markdown("""
    **Aryan, 8th Grade Student & Math Explorer** Writing from Pune, Aryan believes that math doesn't have to be boring equations on a whiteboard. By combining his love for fantasy novels and puzzle-solving, he wrote *The Number Knight* to show kids that math is basically real-world magic.
    """)

st.divider()

# ─── SMART CHECKOUT SYSTEM ─────────────────────────────────────────────
st.header("🛒 Order Your Copy")
st.write("Select your format below. Payments are securely accepted via any UPI app (GPay, Paytm, PhonePe).")

tab1, tab2 = st.tabs(["📦 Physical Copy (₹299)", "⚡ Digital PDF (₹99)"])

# -- PHYSICAL COPY TAB --
with tab1:
    st.markdown("Delivered right to your doorstep within 3-5 working days.")
    with st.form("physical_order_form"):
        st.subheader("1. Shipping Details")
        p_name = st.text_input("Full Name *")
        p_phone = st.text_input("WhatsApp Number *")
        p_email = st.text_input("Email Address")
        p_address = st.text_area("Full Delivery Address with PIN Code *", placeholder="e.g., Flat 12, Tower A, Pimpri, Pune 411018")
        
        st.subheader("2. Payment (₹299)")
        st.info("Scan the QR code below with any UPI app. Once paid, enter the 12-digit UPI Transaction ID.")
        
        # Replace with the actual UPI QR code image generated for his account
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_monument_may_7_2013.jpg", width=200, caption="Aryan's UPI QR Code")
        st.write("**UPI ID:** aryan@upi")
        
        p_txn_id = st.text_input("UPI Transaction ID *", placeholder="e.g., 312345678901")
        
        p_submitted = st.form_submit_button("Place Order")
        if p_submitted:
            if not p_name or not p_phone or not p_address or not p_txn_id:
                st.error("Please fill in all required fields!")
            else:
                # Here you would add the logic to push to Firebase
                st.success(f"🎉 Thank you, {p_name}! We are verifying your payment of ₹299. We will update you on WhatsApp at {p_phone}!")
                st.balloons()

# -- DIGITAL COPY TAB --
with tab2:
    st.markdown("Sent directly to your email inbox immediately after payment confirmation.")
    with st.form("digital_order_form"):
        st.subheader("1. Digital Details")
        d_name = st.text_input("Full Name *", key="d_name")
        d_email = st.text_input("Email Address (where we will send the PDF) *", key="d_email")
        
        st.subheader("2. Payment (₹99)")
        st.info("Scan the QR code below with any UPI app. Once paid, enter the 12-digit UPI Transaction ID.")
        
        st.image("https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_monument_may_7_2013.jpg", width=200, caption="Aryan's UPI QR Code")
        st.write("**UPI ID:** aryan@upi")
        
        d_txn_id = st.text_input("UPI Transaction ID *", key="d_txn")
        
        d_submitted = st.form_submit_button("Send me the E-Book")
        if d_submitted:
            if not d_name or not d_email or not d_txn_id:
                st.error("Please fill in your name, email, and Transaction ID!")
            else:
                # Push to Firebase logic here
                st.success(f"🎉 Awesome, {d_name}! Once your ₹99 payment is verified, the PDF will be beamed to {d_email}.")
                st.snow()
