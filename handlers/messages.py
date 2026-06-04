from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# ------------------ Text -- Buttons ------------- Sorting Buttons
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler, CallbackQueryHandler
# ---------------------- The Core --- Text rcv ------ type --- def types --- /start -------- Buttons rcv
from config import client, SYSTEM_PROMPT


# For default text ⤵️
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
# wait -- name --------- event --------- other kind of data 
    user_text = update.message.text
#-- ---------- the user text 👆🏻

    thinking_msg = await update.message.reply_text("⏳ در حال فکر کردن...")
#-- sending req to open router ⤵️

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            max_tokens=1000
        )
        reply = response.choices[0].message.content
    # Code 200 = OK!
    except Exception as e:
        print("EXCEPTION:", e)
        reply = "مشکل در اتصال به سرور."

    
    if not reply or reply.strip() == "":
        reply = "پاسخ نامعتبر دریافت شد."

# ends & delete thinking message
    await thinking_msg.delete()
# async ends & message sent
    await update.message.reply_text(reply, parse_mode="Markdown")