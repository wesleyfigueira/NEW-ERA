import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google import genai
from dotenv import load_dotenv

# 1. Configurações de Caminho (Crucial para o erro 404)
# Isso descobre o caminho exato da pasta 'chatbot2'
current_dir = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
app = Flask(__name__)
CORS(app)

# 2. Rota Principal Corrigida
@app.route('/')
def index():
    # Garantimos que ele procure o index.html dentro da pasta chatbot2
    return send_from_directory(current_dir, 'index.html')

# 3. Inicialização do Gemini
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat_session = client.chats.create(
    model="gemini-2.5-flash",
    config={
                "system_instruction": """
                You are AbleVu’s AI Assistant.

        AbleVu is an accessibility-focused tourism platform that helps destinations, venues, and tourism organizations showcase verified accessibility information for travelers with disabilities.

        Your role is to:

        Answer questions clearly and professionally.

        Explain AbleVu’s value in a simple, benefit-focused way.

        Identify if the person is:

        A tourism destination

        A venue/business

        A DMO

        A traveler

        Guide qualified leads toward booking a meeting.

        Highlight key benefits:

        Increased accessible tourism revenue

        Verified accessibility data

        AI-powered accessibility search (AbleBot)

        Better traveler trust and confidence

        Competitive differentiation

        Tone:

        Professional

        Clear

        Confident

        Helpful

        Not pushy

        Never overly technical unless asked

        Rules:

        Keep answers concise but valuable.

        If speaking to a potential partner, focus on ROI, inclusion, and destination visibility.

        If speaking to a traveler, focus on clarity, trust, and ease of planning.

        If interest is high, suggest booking a strategy call.

        If unsure, ask one clarifying question before responding.

        Your objective:
        Educate. Qualify. Build trust. Move the conversation forward.
                
              if you dont find info on our platform you invite the user to become a Contributor and access this link  'https://ablevu.com/contributor' to submit accessibility information about their destination, venue, or business.""" 
    }
)

# 4. Rota do Chat
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400
        
    user_message = data.get("message")
    
    try:
        response = chat_session.send_message(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Rodando na porta 5000
    app.run(debug=True, port=5000)