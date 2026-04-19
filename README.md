# 📖 Book Store Website — Setup Guide

Built with **Python + Streamlit** · No backend needed · Free to deploy

---

## 🚀 Run Locally (30 seconds)

```bash
pip install streamlit
streamlit run app.py
```
Opens at → `http://localhost:8501`

---

## 🌐 Deploy Free on Streamlit Cloud

1. Create a free account at [share.streamlit.io](https://share.streamlit.io)
2. Push this folder to a GitHub repo
3. New App → point to `app.py` → Deploy
4. Your URL: `yourname-bookname.streamlit.app` ✅

---

## ✏️ Customise — Edit the `BOOK` dictionary in `app.py`

| Key | What to put |
|-----|-------------|
| `title` | Real book title |
| `author` | Student's name |
| `description` | Back-cover style description |
| `physical_price` | Price in ₹ |
| `digital_price` | Price in ₹ |
| `upi_id` | Your UPI ID (e.g. name@oksbi) |
| `whatsapp` | Country code + number (e.g. 919876543210) |
| `seller_email` | Your email where orders are notified |
| `preview` | 3 short excerpt objects from the book |
| `author_bio` | A short paragraph about the author |

**For the QR code:** Replace the SVG placeholder in the `<div class="qr-img">` section with an actual screenshot of your UPI QR (from GPay / PhonePe app). Save it as `qr.png` and change the SVG tag to `<img src="qr.png" width="144" height="144">`.

---

## 💸 How Payments Work (Zero Cost)

```
Customer fills form → sees QR → pays via GPay/Paytm/PhonePe
      → sends WhatsApp screenshot → you confirm
      → for digital: email the PDF manually
      → for physical: ship the book
```

**Why this works best for a student seller:**
- ₹0 platform fees
- No business registration needed
- Works on any device
- You stay in control

---

## ✨ Features

- Clean, professional design — no broken 3D
- Separate physical & digital order flows
- 3-step order modal: Details → Pay → Confirm
- Address collection for physical orders only
- Email collection for digital PDF delivery
- Auto-filled WhatsApp message with order details
- 5 Math Riddles from the book (interactive game)
- Book cover mockup with hover effect
- Fully mobile responsive
- Chapter preview section
- Author profile section

---

Made with ❤️ for a young author's first book — {BOOK_PLACEHOLDER}
