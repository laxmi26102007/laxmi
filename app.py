from flask import Flask, request, jsonify
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ------------------ Advice Function ------------------
def get_advice(h, a, m):
    advice = []

    if h < 3:
        advice.append("📚 Study at least 4–5 hours daily")
    if a < 75:
        advice.append("📊 Maintain minimum 75% attendance")
    if m < 50:
        advice.append("📝 Revise basics and practice questions")
    if h > 6 and m > 70:
        advice.append("🔥 You are doing great! Keep consistency")

    return " | ".join(advice) if advice else "Excellent performance!"

# ------------------ Home Route ------------------
@app.route("/")
def home():
    return "AI Student API Running"

# ------------------ Prediction Route ------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    h = float(data['hours'])
    a = float(data['attendance'])
    m = float(data['marks'])

    # 🎯 RULE-BASED RESULT (ACCURATE)
    if m >= 40 and a >= 75:
        result = "Pass"
    else:
        result = "Fail"

    # 🎯 ELIGIBILITY
    if a >= 75:
        eligibility = "Eligible"
    else:
        eligibility = "Not Eligible"

    return jsonify({
        "result": result,
        "eligibility": eligibility,
        "advice": get_advice(h, a, m)
    })

# ------------------ Smart Timetable ------------------
@app.route("/timetable", methods=["POST"])
def timetable():
    data = request.json
    h = float(data['hours'])

    if h < 3:
        plan = """📅 Study Plan:
Increase study time to 5 hours daily
Morning: Basics
Afternoon: Practice
Evening: Revision"""
    else:
        plan = """📅 Study Plan:
Maintain your routine
Add mock tests on weekends
Daily revision is important"""

    return jsonify({"plan": plan})

# ------------------ Chatbot ------------------
@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    if any(word in msg for word in ["study", "learn", "read"]):
        reply = "📚 Study 4–5 hours daily with focus and no distractions."

    elif any(word in msg for word in ["attendance", "college", "class"]):
        reply = "📊 Maintain at least 75% attendance to avoid issues."

    elif any(word in msg for word in ["marks", "score", "exam"]):
        reply = "📝 Practice previous year papers and revise daily."

    elif any(word in msg for word in ["fail", "low", "bad"]):
        reply = "⚠️ Don't worry! Start small, stay consistent, and improve daily."

    elif any(word in msg for word in ["time", "schedule", "plan"]):
        reply = "📅 Follow a timetable: Study → Practice → Revision daily."

    else:
        reply = "💡 Tip: Study regularly, maintain attendance, and revise."

    return jsonify({"reply": reply})

# ------------------ Run App ------------------
if __name__ == "__main__":
    app.run(port=5003)