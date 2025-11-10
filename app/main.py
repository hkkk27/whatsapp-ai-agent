# app/main.py
from fastapi import FastAPI, Request
import os
import requests
from dotenv import load_dotenv
from app.notion_handler import save_to_notion
from app.ai_router import process_message
from datetime import datetime

load_dotenv()

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")

@app.get("/")
def home():
    return {"status": "WhatsApp AI Agent Running"}

# ✅ Webhook verification
@app.get("/webhook")
async def verify_token(request: Request):
    params = request.query_params
    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params.get("hub.challenge"))
    return {"error": "Invalid verification token"}

# ✅ Incoming WhatsApp message
@app.post("/message")
async def receive_message(request: Request):
    data = await request.json()
    print("📩 Incoming webhook JSON:", data)

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = message["from"]
        text = message["text"]["body"]
        print(f"💬 Message from {sender}: {text}")

        # Process message using AI
        corrected_text, intent, time_info = process_message(text)

        # Save to Notion
        save_to_notion(corrected_text, intent, time_info)

        # Reply message
        send_whatsapp_message(sender, f"✅ Your {intent} has been saved to Notion!")
        return {"status": "success"}

    except Exception as e:
        print("❌ Error:", e)
        return {"error": str(e)}

def send_whatsapp_message(to, text):
    url = "https://graph.facebook.com/v17.0/your_phone_number_id/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    response = requests.post(url, headers=headers, json=data)
    print("📤 WhatsApp API Response:", response.json())
