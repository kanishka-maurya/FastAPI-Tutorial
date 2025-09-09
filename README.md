 # 📌 Overview

This project is a tutorial-style demo showing how to:

- Build a backend API using FastAPI

- Connect it with a simple Streamlit frontend

- Pass user input → preprocess → send to ML model → get prediction

⚡ Note:
👉 This project is FastAPI-focused and not a heavy Machine Learning project.
The ML model is a simple pre-trained pipeline (stored in model.pkl) only for demonstration.
The main learning is how to integrate backend (FastAPI) with frontend (Streamlit).

# 🏥 Insurance Premium Classifier 

A simple **Machine Learning web application** where a trained pipeline predicts **insurance premium category** based on user details such as age, weight, height, city, income, occupation, and lifestyle factors.  

The project uses:  
- **FastAPI** → Backend API for model inference  
- **Streamlit** → Frontend UI for user interaction  
- **Pickle** → Model persistence  

---

## 🚀 Project Workflow  

1. **User enters details** (age, weight, height, city, income, occupation, smoker status) on the Streamlit frontend.  
2. The data is sent to the **FastAPI backend** (`/predict` endpoint).  
3. Backend computes features (`BMI`, `Age Group`, `Lifestyle Risk`, `City Tier`).  
4. Pre-trained ML model predicts the **insurance premium category**.  
5. Prediction is returned and displayed in the Streamlit app.  

---

## 🛠️ Tech Stack  

- **Python 3.9+**  
- **FastAPI** (Backend API)  
- **Streamlit** (Frontend UI)  
- **Pydantic v2** (Data validation)  
- **Pandas** (Data manipulation)  
- **scikit-learn / Pickle** (ML model serialization)  

---

1️⃣ Clone the Repository  

```bash
git clone https://github.com/kanishka-maurya/Insurance-Premium-Classifier.git
cd Insurance-Premium-Classifier
```

2️⃣ Create Virtual Environment

```bash
python -m venv env
source env/bin/activate   # On Mac/Linux
env\Scripts\activate      # On Windows
```

3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Run FastAPI Backend

```bash
uvicorn application:app --reload

API will be live at: http://127.0.0.1:8000

Interactive Swagger docs: http://127.0.0.1:8000/docs
```

5️⃣ Run Streamlit Frontend

```bash
streamlit run frontend.py
```
