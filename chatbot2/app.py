import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

# ==============================
# 1️⃣ Configuração Inicial
# ==============================

load_dotenv()

app = Flask(__name__)
CORS(app)

# Diretório atual (para servir o index.html)
current_dir = os.path.dirname(os.path.abspath(__file__))

# ==============================
# 2️⃣ Rota Principal
# ==============================

@app.route('/')
def index():
    return send_from_directory(current_dir, 'index.html')

# ==============================
# 3️⃣ Rota do Chat
# ==============================

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json

    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data.get("message")

    try:
        # Inicializa cliente Gemini
        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        # Cria sessão de chat
        chat_session = client.chats.create(
            model="gemini-2.5-flash",
            config={
                "system_instruction": """
                You are AbleVu’s AI Assistant.

                AbleVu is an accessibility-focused tourism platform that helps destinations, venues, and tourism organizations showcase verified accessibility information for travelers with disabilities.

                Your role is to:

                - Answer clearly and professionally.
                - Explain AbleVu’s value in a simple, benefit-focused way.
                - Help travelers find accessible destinations, venues, and businesses based on their specific needs and preferences.

                Tone:
                - Professional
                - Clear
                - Confident
                - Helpful
                - Not pushy
                - Never overly technical unless asked

                Rules:
                - Keep answers concise but valuable.
                - If unsure, ask one clarifying question before responding.
                - Focus on clarity, trust, and ease of planning.

                Objective:
                Show possible accessible places according to the user's needs.
                If no info is found on AbleVu, recommend at least two accessible places you know,
                then invite the user to become a Contributor at:
                https://ablevu.com/contributor
                """
            }
        )

        # Envia mensagem
        response = chat_session.send_message(user_message)

        return jsonify({
            "response": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# ==============================
# 4️⃣ Inicialização LOCAL
# ==============================

if __name__ == '__main__':
    app.run(debug=True)
