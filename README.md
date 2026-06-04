<div align="center">

# 🌍 LuminGo — Migration Assistant Bot

**A smart AI-powered Telegram bot for immigration guidance**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram)](https://t.me/Lumininini)
[![OpenRouter](https://img.shields.io/badge/AI-OpenRouter-orange)](https://openrouter.ai)
[![Railway](https://img.shields.io/badge/Deployed-Railway-purple)](https://railway.app)

</div>

---

## ✨ Features

- 🎓 Academic immigration guidance (universities, programs, requirements)
- 💼 Work-based immigration pathways
- 🏡 Permanent residency information
- 🧠 AI-powered responses with conversation memory
- 🌐 Persian language support

---

## 🚀 Try It

Open Telegram and search for [@Lumininini](https://t.me/Lumininini) and start chatting!

---

## 📁 Project Structure
```
LuminGo/
├── handlers/
│   ├── messages.py   # AI message handling + memory
│   ├── commands.py   # /start, /restart, /clear
│   └── buttons.py    # Inline keyboard buttons
├── bot.py            # App entry point
├── config.py         # Settings & AI client
└── requirements.txt
```

---

## 🛠️ Self-Hosting

If you want to run your own instance:

### Requirements
- Python 3.10+
- Telegram bot token from [@BotFather](https://t.me/BotFather)
- OpenRouter API key from [openrouter.ai](https://openrouter.ai)

### Installation

```bash
git clone https://github.com/Mh-Saberi/LuminGo-migration-telegram-bot.git
cd LuminGo-migration-telegram-bot
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```bash
TOKEN=your_telegram_token
OPENROUTER_API_KEY=your_openrouter_key
```

### Run

```bash
python bot.py
```

---

## ☁️ Deploy on Railway

1. Connect your repo to [Railway](https://railway.app)
2. Add `TOKEN` and `OPENROUTER_API_KEY` in Railway → Variables
3. Deploy! 🚀

---

## 📞 Contact

📧 saberimahtab2002@gmail.com
