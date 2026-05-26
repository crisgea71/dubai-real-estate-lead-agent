import os
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-on-render")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DEMO_PASSWORD = os.getenv("DEMO_PASSWORD")
FREE_MESSAGE_LIMIT = 14

if not GROQ_API_KEY:
    print("WARNING: GROQ_API_KEY is missing. Add it to your .env file.")

if not DEMO_PASSWORD:
    print("WARNING: DEMO_PASSWORD is missing. Add it to your .env file.")

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None


AGENCY_PROFILE = """
Agency name: Demo Dubai Real Estate
Market: Dubai / Middle East
Main areas: Dubai Marina, Downtown Dubai, Business Bay, Palm Jumeirah, JVC, Dubai Hills
Services: buying, renting, off-plan investment, luxury properties, commercial properties
Property types: apartment, villa, townhouse, office, retail, land
Tone: professional, short, helpful, luxury but not pushy
Goal: qualify the lead before a human real estate agent contacts them
"""


SYSTEM_PROMPT = f"""
You are an AI Lead Qualification Agent for this real estate agency:

{AGENCY_PROFILE}

Speak only in English.

Your job is to qualify property leads before a human real estate agent calls them.

Ask one question at a time.

You need to collect:
1. Buy or rent
2. Budget
3. Area
4. Property type
5. Timeline
6. Cash buyer or mortgage
7. Viewing interest
8. Name and phone/email

When you have all details, generate:

LEAD SUMMARY
Client name:
Buy/Rent:
Budget:
Area:
Property type:
Timeline:
Mortgage/Cash:
Viewing:
Contact:
Lead score:
Suggested next action:

Lead score rules:
Hot = clear budget, clear area, wants viewing, short timeline.
Warm = has budget and area, but not ready immediately.
Cold = vague budget, vague area, or just browsing.

Important rules:
- Do not invent available properties.
- Do not promise exact prices or availability.
- If the user asks for a specific property, say a human agent can verify current availability.
- Keep the conversation focused on qualification.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/unlock", methods=["POST"])
def unlock():
    data = request.get_json()
    password = data.get("password", "")

    if password == DEMO_PASSWORD:
        session["unlocked"] = True
        return jsonify({
            "success": True,
            "message": "Access unlocked. You can continue using the demo."
        })

    return jsonify({
        "success": False,
        "message": "Incorrect password."
    }), 401


@app.route("/chat", methods=["POST"])
def chat():
    try:
        if client is None:
            return jsonify({
                "reply": "Server error: GROQ_API_KEY is missing."
            }), 500

        unlocked = session.get("unlocked", False)
        message_count = session.get("message_count", 0)

        if not unlocked and message_count >= FREE_MESSAGE_LIMIT:
            return jsonify({
                "locked": True,
                "reply": "Demo limit reached. Please contact Cristina for full access."
            }), 403

        session["message_count"] = message_count + 1

        data = request.get_json()
        messages = data.get("messages", [])

        groq_messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        for message in messages:
            if message["role"] in ["user", "assistant"]:
                groq_messages.append({
                    "role": message["role"],
                    "content": message["content"]
                })

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=groq_messages,
            temperature=0.4,
            max_tokens=600
        )

        reply = response.choices[0].message.content

        return jsonify({
            "reply": reply,
            "remaining_free_messages": max(0, FREE_MESSAGE_LIMIT - session["message_count"]),
            "unlocked": unlocked
        })

    except Exception as e:
        return jsonify({
            "reply": "Something went wrong.",
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
