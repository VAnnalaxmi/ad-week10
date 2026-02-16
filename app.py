# ============================================================
# AI-Based Smart Study Planner and Stress Management System
# Backend: Flask + SQLite + Rule-Based AI Scheduling Algorithm
# ============================================================

from flask import Flask, render_template, request, jsonify
import sqlite3
import math
import random
from datetime import datetime, timedelta

app = Flask(__name__)
DB_NAME = "study_planner.db"

# ─────────────────────────────────────────────
# DATABASE SETUP
# ─────────────────────────────────────────────

def init_db():
    """Create database tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_plans (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            subject   TEXT NOT NULL,
            day       INTEGER NOT NULL,
            date_label TEXT NOT NULL,
            task      TEXT NOT NULL,
            units     REAL NOT NULL,
            status    TEXT DEFAULT 'Pending',
            created_at TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ─────────────────────────────────────────────
# AI RULE-BASED SCHEDULING ALGORITHM
# ─────────────────────────────────────────────

RELAXATION_TIPS = [
    "🌿 Take a 5-minute walk outside. Fresh air boosts brain power!",
    "🧘 Try box breathing: Inhale 4s → Hold 4s → Exhale 4s → Hold 4s.",
    "💧 Drink a glass of water. Hydration improves focus by up to 30%.",
    "🎵 Listen to lo-fi music for 10 minutes to reset your mind.",
    "✍️ Write down 3 things you're grateful for right now.",
    "🌸 Do 10 slow neck rolls to release tension from studying.",
    "😴 A 20-minute power nap can boost memory consolidation.",
    "🍎 Snack on nuts or fruit — avoid sugar crash before exams!",
]

FOCUS_REMINDERS = [
    "🔕 Phone away! Your future self will thank you.",
    "🎯 One topic at a time. Deep focus beats scattered effort.",
    "⏰ Set a 25-min Pomodoro timer. Go!",
    "💡 You've got this. Every page you study is progress.",
    "🚀 Eliminate distractions now — success requires sacrifice.",
]

def ai_schedule(subject, total_units, total_days, daily_hours):
    """
    Rule-Based AI Scheduling Algorithm:
    - Reserves last day as revision day
    - Distributes units progressively (harder units first, lighter near exam)
    - Accounts for daily available hours
    - Labels tasks descriptively
    """
    schedule = []

    if total_days <= 0 or total_units <= 0:
        return schedule

    # Rule 1: If only 1 day, cram everything
    if total_days == 1:
        schedule.append({
            "day": 1,
            "task": f"Complete all {total_units} units of {subject} (Intensive Session)",
            "units": total_units
        })
        return schedule

    # Rule 2: Reserve last day for revision
    study_days = total_days - 1 if total_days > 2 else total_days
    revision_day = total_days if total_days > 2 else None

    # Rule 3: Distribute units — more coverage early, lighter closer to exam
    # Weight: early days get slightly more units (70%) vs later (30%)
    units_per_day = total_units / study_days
    units_per_hour = units_per_day / daily_hours if daily_hours > 0 else units_per_day

    unit_counter = 0
    for d in range(1, study_days + 1):
        # Progressive adjustment: first half gets +10%, second half gets -10%
        midpoint = study_days / 2
        if d <= midpoint:
            day_units = round(units_per_day * 1.1, 2)
        else:
            day_units = round(units_per_day * 0.9, 2)

        # Clamp to remaining units
        remaining = round(total_units - unit_counter, 2)
        if remaining <= 0:
            break
        day_units = min(day_units, remaining)
        day_units = round(day_units, 2)

        unit_start = round(unit_counter + 0.01, 2) if unit_counter > 0 else 1
        unit_end   = round(unit_counter + day_units, 2)

        task = f"Study {subject} — Units {unit_start:.0f} to {unit_end:.0f} ({daily_hours}hrs)"
        if daily_hours >= 6:
            task += " 🔥 Intensive"
        elif daily_hours <= 2:
            task += " 📖 Light Session"

        schedule.append({"day": d, "task": task, "units": day_units})
        unit_counter += day_units

    # Rule 4: Add revision day
    if revision_day:
        schedule.append({
            "day": revision_day,
            "task": f"🔄 Revision Day — Review all {total_units} units of {subject} + Practice Questions",
            "units": round(total_units * 0.5, 2)
        })

    return schedule

# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate_plan():
    """Generate AI study plan and store in database."""
    data = request.get_json()

    subject     = data.get("subject", "").strip()
    total_units = float(data.get("total_units", 0))
    total_days  = int(data.get("total_days", 0))
    daily_hours = float(data.get("daily_hours", 2))

    if not subject or total_units <= 0 or total_days <= 0:
        return jsonify({"error": "Please fill all fields correctly."}), 400

    # Run AI scheduling
    schedule = ai_schedule(subject, total_units, total_days, daily_hours)

    # Save to database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Delete existing plan for same subject (optional: allows re-generation)
    cursor.execute("DELETE FROM study_plans WHERE subject = ?", (subject,))

    start_date = datetime.today()
    rows = []
    for item in schedule:
        day_date = start_date + timedelta(days=item["day"] - 1)
        date_label = day_date.strftime("%A, %d %b %Y")
        cursor.execute(
            "INSERT INTO study_plans (subject, day, date_label, task, units, status) VALUES (?, ?, ?, ?, ?, ?)",
            (subject, item["day"], date_label, item["task"], item["units"], "Pending")
        )
        rows.append({
            "id": cursor.lastrowid,
            "day": item["day"],
            "date_label": date_label,
            "task": item["task"],
            "units": item["units"],
            "status": "Pending"
        })

    conn.commit()
    conn.close()

    tip    = random.choice(RELAXATION_TIPS)
    focus  = random.choice(FOCUS_REMINDERS)

    return jsonify({
        "message": f"Study plan for '{subject}' generated successfully!",
        "schedule": rows,
        "relaxation_tip": tip,
        "focus_reminder": focus,
        "total_days": total_days,
        "total_units": total_units
    })


@app.route("/plans", methods=["GET"])
def get_all_plans():
    """Fetch all stored study plans from database."""
    conn = get_db_connection()
    rows = conn.execute(
        "SELECT * FROM study_plans ORDER BY subject, day"
    ).fetchall()
    conn.close()

    plans = [dict(r) for r in rows]
    return jsonify({"plans": plans})


@app.route("/update_status", methods=["POST"])
def update_status():
    """Toggle task status between Pending and Completed."""
    data   = request.get_json()
    row_id = data.get("id")
    status = data.get("status")

    if row_id is None or status not in ("Pending", "Completed"):
        return jsonify({"error": "Invalid data."}), 400

    conn = get_db_connection()
    conn.execute(
        "UPDATE study_plans SET status = ? WHERE id = ?", (status, row_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Status updated.", "id": row_id, "status": status})


@app.route("/delete_plan", methods=["POST"])
def delete_plan():
    """Delete all tasks for a given subject."""
    data    = request.get_json()
    subject = data.get("subject", "")

    conn = get_db_connection()
    conn.execute("DELETE FROM study_plans WHERE subject = ?", (subject,))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Plan for '{subject}' deleted."})


@app.route("/tips", methods=["GET"])
def get_tips():
    """Return a random relaxation tip and focus reminder."""
    return jsonify({
        "relaxation_tip": random.choice(RELAXATION_TIPS),
        "focus_reminder": random.choice(FOCUS_REMINDERS)
    })


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    print("=" * 55)
    print("  🎓 Smart Study Planner — Server Starting")
    print("  📍 Open: http://127.0.0.1:5000")
    print("=" * 55)
    app.run(debug=True)
