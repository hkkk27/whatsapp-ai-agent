
# 🤖 WhatsApp AI Agent — with Notion & OpenRouter Integration

A smart **AI-powered WhatsApp agent** that understands natural messages, classifies them (notes, reminders, to-dos), and automatically **stores or schedules them in Notion**.
Built using **FastAPI**, **Twilio WhatsApp API**, **Notion API**, and **OpenRouter AI models**.

---

## 🚀 Features

* 📲 **WhatsApp Integration** — Chat directly with your AI agent via WhatsApp.
* 🧠 **AI Message Understanding** — Detects whether a message is a note, task, or reminder.
* 📅 **Smart Time Recognition** — Understands natural time inputs like “remind me tomorrow at 5 pm.”
* 🗂️ **Notion Sync** — Automatically saves classified data into separate Notion databases:

  * Notes
  * Reminders
  * To-Do list
* ⚡ **FastAPI Backend** — Built for performance, scalability, and clarity.
* 🔐 **Environment-based Configuration** — Secure token and ID management via `.env`.

---

## 🧩 Tech Stack

| Component                              | Description                                                 |
| -------------------------------------- | ----------------------------------------------------------- |
| **Python (FastAPI)**                   | Web framework to handle WhatsApp messages                   |
| **Twilio API**                         | To send/receive WhatsApp messages                           |
| **OpenRouter API (GPT/Claude models)** | For AI message understanding                                |
| **Notion API**                         | To store notes, reminders, and tasks                        |
| **dateparser**                         | To parse natural language dates (“tomorrow”, “next Monday”) |

---

## ⚙️ Folder Structure

```
whatsapp-ai-agent/
│
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── notion_handler.py    # Handles Notion API interactions
│   ├── ai_router.py         # Connects OpenRouter AI for classification
│   ├── utils.py             # Helper functions
│   ├── test_notion.py       # Simple Notion API test
│
├── .env.example             # Example environment file
├── requirements.txt         # Python dependencies
├── README.md                # You are here 🚀
```

---

## 🔑 Environment Variables (`.env.example`)

```bash
# Twilio WhatsApp
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

# Notion API
NOTION_TOKEN=your_notion_secret_key
NOTION_DB_NOTES=your_notes_database_id
NOTION_DB_REMINDERS=your_reminders_database_id
NOTION_DB_TODOS=your_todos_database_id

# OpenRouter API
OPENROUTER_API_KEY=your_openrouter_key
```

---

## 🧠 How It Works

1. **User sends a WhatsApp message** → e.g.

   > “Remind me to pay bills tomorrow at 6 pm”

2. **FastAPI receives the message** from Twilio’s webhook.

3. **AI Router (OpenRouter)** analyzes and classifies the message:

   * `type`: reminder
   * `content`: "pay bills"
   * `time`: "tomorrow 6 pm"

4. **Notion Handler** stores it in the correct database.

5. **Bot replies** on WhatsApp:

   > “✅ Reminder saved in Notion for tomorrow at 6 PM.”

---

## 🧰 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/whatsapp-ai-agent.git
cd whatsapp-ai-agent
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` File

```bash
cp .env.example .env
```

Then, fill in your credentials.

### 5️⃣ Run the App

```bash
uvicorn app.main:app --reload
```

### 6️⃣ Expose to the Internet (for Twilio)

Use [ngrok](https://ngrok.com/) to expose your local server:

```bash
ngrok http 8000
```

Set your Twilio WhatsApp webhook URL to:

```
https://<your-ngrok-url>/webhook
```

---

## 📈 Example Conversation

**User (WhatsApp):**

> Take a note – AI project documentation due next week.

**Bot:**

> ✅ Saved as a Note in Notion.

**User:**

> Remind me to buy groceries tomorrow at 5 PM

**Bot:**

> ⏰ Reminder added to Notion for tomorrow at 5 PM.

---

## 🧾 Resume Description Example

> **WhatsApp AI Agent (Python, FastAPI, Twilio, Notion API, OpenRouter)**
>
> * Built an AI-powered WhatsApp assistant that classifies messages as notes, reminders, or to-dos.
> * Integrated Notion API for structured data storage and Twilio WhatsApp API for real-time messaging.
> * Implemented OpenRouter GPT-based model for natural language understanding and time parsing.
> * Deployed FastAPI backend with modular architecture and environment-based configuration.
> * Published project on GitHub to demonstrate applied AI + API integration skills.

---

## 💡 Future Enhancements

* ✅ Google Calendar or Outlook integration
* ✅ Web dashboard to visualize notes & reminders
* ✅ Voice message support
* ✅ Multi-user authentication system

---

## 🧑‍💻 Author

**Harshit Singh**
📧 [[harshitkumarsingh04@gmail.com](mailto:harshitkumarsingh04@gmail.com)]
🌐 [GitHub Profile](https://github.com/hkkk27)

