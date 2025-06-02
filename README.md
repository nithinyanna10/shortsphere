# 🔗 ShortSphere — Smart URL Shortener with Analytics

**ShortSphere** is a lightweight, privacy-respecting URL shortener built entirely in Python using **FastAPI** and **Streamlit** — with real-time click tracking, geolocation, and dashboard analytics.

---

## 🚀 Features

- ✅ Generate short links for any long URL
- 🔁 Automatically redirect to original URLs
- 📊 Track click events (IP, geolocation, device)
- 🌍 Analytics dashboard with:
  - Total clicks
  - Country distribution
  - User agent breakdown
  - Exportable raw logs
- 💾 Zero database: uses Redis or JSON-based file logging
- 🧩 Modular code (easy to extend, deploy, or add auth)

---

## 🛠 Tech Stack

| Layer      | Technology       |
|------------|------------------|
| Backend    | [FastAPI](https://fastapi.tiangolo.com) |
| Frontend   | [Streamlit](https://streamlit.io)       |
| Storage    | Redis *(or in-memory fallback)*          |
| Logging    | JSON file-based event logs               |
| IP Lookup  | ip-api.com *(free tier, no key needed)* |

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/shortsphere.git
cd shortsphere

# Backend
cd backend
pip install -r requirements.txt

# (Optional) Redis setup
# docker run -d -p 6379:6379 redis

# Frontend
cd ../frontend/streamlit_ui
pip install -r requirements.txt

cd backend
uvicorn main:app --reload
# Runs at http://localhost:8000

cd frontend/streamlit_ui
streamlit run app.py
# Opens at http://localhost:8501
