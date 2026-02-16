# 🎓 AI-Based Smart Study Planner and Stress Management System

## 📁 Project Folder Structure

```
SmartStudyPlanner/
│
├── app.py                   ← Flask backend (AI logic + routes + database)
├── study_planner.db         ← SQLite database (auto-created on first run)
├── requirements.txt         ← Python dependencies
│
├── templates/
│   └── index.html           ← Frontend (HTML + CSS + JavaScript)
│
└── README.md                ← This file (setup + viva notes)
```

---

## ⚙️ Technology Stack

| Layer       | Technology        | Purpose                            |
|-------------|-------------------|------------------------------------|
| Frontend    | HTML, CSS, JS     | User Interface                     |
| Backend     | Python + Flask    | Routes, API endpoints              |
| Database    | SQLite            | Store study plans                  |
| AI Logic    | Python (Rule-Based Algorithm) | Smart scheduling       |

---

## 🚀 How to Install & Run (VS Code)

### Step 1 — Install Python
Make sure Python 3.7+ is installed:
```bash
python --version
```

### Step 2 — Open Project in VS Code
```
File → Open Folder → Select "SmartStudyPlanner"
```

### Step 3 — Open Terminal in VS Code
```
Terminal → New Terminal  (or press Ctrl + `)
```

### Step 4 — Install Flask
```bash
pip install flask
```
Or install all dependencies at once:
```bash
pip install -r requirements.txt
```

### Step 5 — Run the Application
```bash
python app.py
```

### Step 6 — Open in Browser
```
http://127.0.0.1:5000
```

---

## 🧠 How the AI Scheduling Algorithm Works

The **rule-based AI scheduler** follows these intelligent rules:

1. **Revision Rule**: Automatically reserves the last day as a full revision + practice day
2. **Progressive Distribution**: First half of days gets slightly more units (intensive phase), second half gets lighter load (consolidation phase)
3. **Intensity Detection**: Based on daily study hours, tasks are labeled as "Intensive", "Regular", or "Light Session"
4. **Overflow Protection**: Ensures unit count never exceeds total syllabus units
5. **Descriptive Naming**: Each task tells the student exactly which units to cover

**Example**: 10 units, 7 days, 3 hrs/day
- Days 1–3: ~1.57 units/day (intensive phase)
- Days 4–6: ~1.43 units/day (consolidation)
- Day 7:    Revision Day (full review)

---

## 📋 API Endpoints (for Viva)

| Method | Endpoint         | Description                       |
|--------|-----------------|-----------------------------------|
| GET    | `/`             | Serve main HTML page              |
| POST   | `/generate`     | Generate AI plan & save to DB     |
| GET    | `/plans`        | Fetch all saved plans             |
| POST   | `/update_status`| Mark task Completed/Pending       |
| POST   | `/delete_plan`  | Delete all tasks for a subject    |
| GET    | `/tips`         | Get random wellness tip           |

---

## 🗄️ Database Schema

```sql
CREATE TABLE IF NOT EXISTS study_plans (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    subject     TEXT NOT NULL,
    day         INTEGER NOT NULL,
    date_label  TEXT NOT NULL,
    task        TEXT NOT NULL,
    units       REAL NOT NULL,
    status      TEXT DEFAULT 'Pending',
    created_at  TEXT DEFAULT (datetime('now'))
);
```

---

## 🎓 Viva Q&A Preparation

**Q: What is the AI in this project?**
A: It uses a Rule-Based AI scheduling algorithm — a form of expert system that applies predefined rules to distribute syllabus units intelligently across available days.

**Q: Why not use machine learning?**
A: For study scheduling, rule-based AI is more predictable, explainable, and doesn't require training data. It's perfect for this deterministic problem.

**Q: What is Flask?**
A: Flask is a lightweight Python web framework used to create REST API endpoints that the frontend communicates with via fetch() calls.

**Q: How is data stored?**
A: SQLite is an embedded relational database. Data is stored in a `.db` file — no separate database server needed.

**Q: What is the Pomodoro Technique?**
A: A time management method where you study for 25 minutes, then take a 5-minute break. After 4 cycles, take a longer 20-minute break.

**Q: How does the stress management module help?**
A: It provides randomly-selected relaxation tips, focus reminders, break reminders, and an interactive Pomodoro timer — all based on evidence-backed productivity research.

---

## ✅ Features Checklist

- [x] User input form (subject, units, days, hours)
- [x] AI rule-based scheduling algorithm
- [x] Personalized daily timetable generation
- [x] SQLite database storage (auto-created)
- [x] Progress tracking (Pending / Completed)
- [x] Mark tasks as done / undo
- [x] Distraction focus reminders
- [x] Break reminders and relaxation tips
- [x] Pomodoro timer with break cycles
- [x] View all saved plans (history)
- [x] Delete plans
- [x] Clean dark-themed modern UI
- [x] Fully beginner-friendly code with comments
