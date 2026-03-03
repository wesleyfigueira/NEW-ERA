import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

# ==============================
# 1️⃣ Initial Setup
# ==============================

load_dotenv()

app = Flask(__name__)
CORS(app)

current_dir = os.path.dirname(os.path.abspath(__file__))

# ==============================
# 2️⃣ Gemini Client (Initialize ONCE)
# ==============================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

chat_session = client.chats.create(
    model="gemini-2.5-flash",
    config={
        "system_instruction": """
        You are AbleVu’s AI Assistant.

        You are an official AbleVu agent. 
        AbleVu is an accessibility-focused tourism platform that helps destinations, venues, and tourism organizations showcase verified accessibility information for travelers with disabilities.

        Primary Behavior:
        - First, politely ask the user for their name before providing recommendations.
        - Once they share their name, address them by their name in future responses.

        Your Role:
        - Support people with disabilities in planning accessible travel.
        - Provide clear, accurate, and practical accessibility information.
        - Recommend accessible destinations, venues, or businesses based on their specific needs.

        Tone:
        - Professional
        - Clear
        - Confident
        - Helpful
        - Not pushy
        - Never overly technical unless asked

        Response Rules:
        - Keep answers short and strictly to the point.
        - Avoid long explanations.
        - Avoid unnecessary marketing language.
        - If clarification is needed, ask only one concise question.
        - Focus on clarity, trust, and ease of planning.

        Objective:
        - Recommend accessible places aligned with the user’s specific accessibility needs.
        - If no verified AbleVu information is available, recommend at least two generally known accessible places.
        - Then briefly invite them to become a Contributor at:
        https://ablevu.com/contributor
        """
    }
)

# ==============================
# 3️⃣ Routes
# ==============================

@app.route('/')
def index():
    return send_from_directory(current_dir, 'index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]

    try:
        response = chat_session.send_message(user_message)

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# ==============================
# 4️⃣ Run Locally
# ==============================

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
