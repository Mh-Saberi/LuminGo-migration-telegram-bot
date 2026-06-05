from telegram import Update
from telegram.ext import ContextTypes
from config import client, SYSTEM_PROMPT


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    if "history" not in context.user_data:
        context.user_data["history"] = []
    history = context.user_data["history"]
    history.append({"role": "user", "content": user_text})

    thinking_msg = await update.message.reply_text("⏳ در حال فکر کردن...")

    reply = None
    try:
        response = client.chat.completions.create(
            model="google/gemini-2.0-flash-exp:free",  # ✅ مدل درست
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            max_tokens=800
        )
        reply = response.choices[0].message.content

        history.append({"role": "assistant", "content": reply})
        context.user_data["history"] = history[-10:]

    except Exception as e:
        print("EXCEPTION:", type(e).__name__, e)
        err = str(e)
        if "429" in err:
            reply = "⚠️ سرور شلوغه، چند ثانیه صبر کن و دوباره امتحان کن."
        elif "401" in err or "403" in err:
            reply = "❌ مشکل در API Key."
        elif "404" in err:
            reply = "❌ مدل در دسترس نیست."
        else:
            reply = f"⚠️ خطا: {type(e).__name__}"

    if not reply or reply.strip() == "":
        reply = "پاسخ نامعتبر دریافت شد."

    await thinking_msg.delete()

    # ✅ تقسیم پیام اگه طولانی بود
    MAX_LEN = 4000
    if len(reply) <= MAX_LEN:
        await update.message.reply_text(reply, parse_mode="Markdown")
    else:
        parts = [reply[i:i+MAX_LEN] for i in range(0, len(reply), MAX_LEN)]
        for part in parts:
            await update.message.reply_text(part, parse_mode="Markdown")