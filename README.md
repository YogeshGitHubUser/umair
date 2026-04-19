# 📖 The Secret Kingdom of Numbers — Book Store Website

A magical, children-friendly one-page book selling website built with Python + Streamlit.

---

## 🚀 Run Locally

```bash
pip install streamlit
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🌐 Deploy on Streamlit Cloud (Free)

1. Push this folder to a **GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New App** → connect your GitHub repo
4. Set main file: `app.py`
5. Click **Deploy** — your URL will be `your-app-name.streamlit.app` ✅

---

## ✏️ Customise the Book Details

Open `app.py` and edit the `BOOK` dictionary at the top:

| Field | What to change |
|-------|---------------|
| `title` | Your book's actual title |
| `author` | The student's name |
| `description` | Your book's description |
| `physical_price` | Price in ₹ for physical copy |
| `digital_price` | Price in ₹ for PDF |
| `gpay_upi` | Your real UPI ID (e.g. name@oksbi) |
| `whatsapp` | WhatsApp number for order confirmation |
| `preview_pages` | Up to 3 short excerpts from the book |

---

## ✨ Features

- 🌌 **Animated star field** background
- 📖 **3D floating book** with glowing effects
- 🔮 **Book Oracle** — AI chat powered by Claude, answers questions about the book & math
- 🧩 **Math Riddles** — 5 fun riddles from the Number Kingdom
- 💸 **QR Payment popup** — GPay, PhonePe, Paytm, Cash
- 📲 **WhatsApp confirmation** button
- ✨ **Magic cursor** with gold trail
- 📊 **Reading progress bar**
- 🎉 **Particle burst** on card click
- 📱 Fully **mobile responsive**

---

## 🔑 Notes on the Oracle (AI Feature)

The Book Oracle uses the Anthropic Claude API directly from the browser.
For production use, you should proxy this through a backend (Flask/FastAPI) to protect your API key.
For a school project / small scale use, it works as-is.

---

Made with ❤️ for a young author's first book!
