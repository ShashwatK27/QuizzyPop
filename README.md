# 🎯 QuizzyPop — Bursting with Brainpower!

QuizzyPop is a modern, highly interactive, and adaptive quiz platform designed specifically for Computer Science students and tech enthusiasts. Built with a robust Django REST API backend and a sleek, dynamic vanilla JavaScript frontend, QuizzyPop is designed to be a competitive, hackathon-ready project (perfect for events like the Smart India Hackathon).

## ✨ Key Features

* **True Adaptive Quiz Engine:** The game intelligently adjusts difficulty in real-time. Answer a question correctly, and the next one will be harder. Get it wrong, and it scales back to help you recover.
* **Weighted Scoring & Streak Multipliers:** Points scale with difficulty (Easy: 5, Medium: 10, Hard: 15). Consistently answering correctly builds a "Streak" that grants bonus points, rewarding true mastery.
* **🤖 AI Tutor Feedback:** When you get a question wrong, a custom AI Tutor modal provides a highly educational, context-aware explanation for the specific question to ensure continuous learning.
* **Player Analytics Dashboard:** A dedicated profile page featuring **Chart.js** visualizations. Track your "Subject Mastery" via radar charts and view your recent "Score Trends" over time to identify weak points.
* **Global & Subject Leaderboards:** Compete with others globally or within specific domains (Machine Learning, OS, DBMS, DAA, Software Engineering). Top scores are ranked by highest score and tie-broken by fastest time.
* **Stateless JWT Authentication:** Fully secured RESTful architecture using Django Rest Framework (DRF) and SimpleJWT.

## 🛠️ Technology Stack

* **Backend:** Python, Django, Django REST Framework (DRF)
* **Authentication:** JSON Web Tokens (JWT) via SimpleJWT
* **Database:** SQLite (Development) / PostgreSQL-ready
* **Frontend:** HTML5, Vanilla CSS (Neon Dark Theme), Vanilla JavaScript
* **Data Visualization:** Chart.js

## 🚀 Local Setup & Installation

Follow these steps to run QuizzyPop locally on your machine.

### 1. Clone the repository and set up a Virtual Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Environment Variables
Ensure you have a `.env` file in the root directory (alongside `manage.py`) with your secret key:
```env
SECRET_KEY=django-insecure-super-secret-key-for-development
```

### 4. Database Setup & Migrations
```bash
python manage.py migrate
```

### 5. Load the Question Bank
Populate the database with the pre-generated, intelligently mapped 125 computer science questions:
```bash
python manage.py loaddata quiz/fixtures/subject_questions.json
```
*(Optional: Run `python update_ai_tutor.py` to ensure all AI Tutor text is initialized).*

### 6. Create an Admin Account
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```

Navigate to `http://127.0.0.1:8000/` in your browser to start playing! You can manage the question bank by logging into `http://127.0.0.1:8000/admin/`.

---
*Developed as a high-tier hackathon submission.*
