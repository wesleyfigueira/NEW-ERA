import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

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


        help the  travelers find accessible destinations, venues, and businesses based on their specific needs and preferences.


        Tone:

        Professional

        Clear

        Confident

        Helpful

        Not pushy

        Never overly technical unless asked

        Rules:

        Keep answers concise but valuable.

        If speaking to a traveler, focus on clarity, trust, and ease of planning.


        If unsure, ask one clarifying question before responding.

        Your objective:
        Show posible accessible places accordingly to the user needs and preferences, and if the user is a business or destination.
              if you dont find info on our platform you invite the user to become a Contributor and access this link  'https://ablevu.com/contributor' to submit accessibility information about their destination, venue, or business.""" 
    }
)

def chat_with_bot(prompt):
    try:
        
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Erro na requisição: {e}"

if __name__ == "__main__":
    print("Chatbot Gemini Ativo! (Digite 'exit' para sair)")
    while True:
        user_input = input("Você: ")

        if user_input.lower() in ["exit", "quit", "sair"]:
            print("Até logo!")
            break

        if not user_input.strip():
            continue

        response = chat_with_bot(user_input)
        print("Bot:", response)