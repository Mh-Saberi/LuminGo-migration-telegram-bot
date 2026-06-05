from telegram import Update
from telegram.ext import ContextTypes
from config import client, SYSTEM_PROMPT


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    # get the conversation history
    if "history" not in context.user_data:
        context.user_data["history"] = []
    history = context.user_data["history"]
    history.append({"role": "user", "content": user_text})

    thinking_msg = await update.message.reply_text("⏳ در حال فکر کردن...")

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            max_tokens=500
        )
        reply = response.choices[0].message.content

        # save only last 10 messages to avoid memory issues
        history.append({"role": "assistant", "content": reply})
        context.user_data["history"] = history[-5:]

    except Exception as e:
        print("EXCEPTION:", e)
        reply = "مشکل در اتصال به سرور."

    if not reply or reply.strip() == "":
        reply = "پاسخ نامعتبر دریافت شد."

    await thinking_msg.delete()

# Telegram has a message length limit, so we need to split long replies into parts
    MAX_LEN = 4000
    if len(reply) <= MAX_LEN:
        await update.message.reply_text(reply)
    else:
        parts = [reply[i:i+MAX_LEN] for i in range(0, len(reply), MAX_LEN)]
        for part in parts:
            await update.message.reply_text(part)
    