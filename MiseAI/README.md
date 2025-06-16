# MiseAI Backend (FastAPI)

This is the backend system for MiseAI, built with FastAPI and SQLAlchemy.

## 🚀 Features
- Ingredient management
- Dish database
- Recipe-to-cost linking
- REST API endpoints for CRUD

## 🧱 Project Structure
```
miseai/
├── main.py
├── models/
├── schemas/
├── routers/
├── database.py
├── requirements.txt
└── README.md
```

## 📦 Installation
```bash
git clone https://github.com/MiseAI/MiseAI.git
cd MiseAI
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## 🗃️ Running the API
```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive API docs.
