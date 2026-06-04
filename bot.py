from openai import OpenAI
# For AI connection

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# ------------------ Text -- Buttons ------------- Sorting Buttons
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler, CallbackQueryHandler
# ---------------------- The Core --- Text rcv ------ type --- def types --- /start -------- Buttons rcv

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get("TOKEN")
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

# AI client setup
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


SYSTEM_PROMPT = """تو یک دستیار مهاجرت دوستانه و حرفه‌ای هستی. به کاربران کمک می‌کنی بهترین مسیر مهاجرتی رو بر اساس شرایط شخصیشون پیدا کنن — چه تحصیلی، چه کاری، چه اقامت دائم.

                    اگه کاربر سوال کلی پرسید، جواب کلی بده. فقط وقتی کاربر خودش خواست مسیر شخصی‌سازی شده بدونه، اطلاعاتش رو بپرس:
                    - سن
                    - مدرک تحصیلی و معدل
                    - سابقه کاری
                    - سطح زبان (آیلتس، تافل و غیره)
                    - کشور مقصد
                    - بودجه

                    بر اساس پروفایل کاربر:
                    - مناسب‌ترین مسیرهای مهاجرتی رو پیشنهاد بده
                    - برای مهاجرت تحصیلی، دانشگاه‌ها و رشته‌هایی که با شانس کاربر تناسب دارن رو معرفی کن
                    - هزینه‌ها، مدارک لازم، زمان‌بندی و چالش‌های هر مسیر رو توضیح بده
                    - درباره شانس واقعی صادق باش — هیچ‌وقت پذیرش، ویزا یا اقامت رو تضمین نکن
                    - خودت رو وکیل یا مشاور رسمی مهاجرت معرفی نکن

                      لحنت گرم، شفاف و حمایتگر باشه — مثل یه دوست آگاه که واقعاً میخواد کمک کنه. همیشه به زبانی که کاربر باهات صحبت میکنه جواب بده. از جواب دادن به سوالات غیرمرتبط خودداری کن.
                     پاسخ‌هات رو با Markdown فرمت کن:
                     از # برای هدر استفاده نکن.     
                    - برای تیتر از *تیتر* استفاده کن
                    - برای لیست از - استفاده کن
                    - برای متن مهم از *متن* استفاده کن
                    - برای کد از `کد` استفاده کن"""
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

# first message of user : /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 راهنما", callback_data="guide")],
        [InlineKeyboardButton("❓ سوالات متداول", callback_data="faq")],
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard) # telegram knows this!

    welcome_text = (
        """خوش آمدید 👋
          من دستیار مهاجرت شما هستم. کمک می‌کنم بهترین مسیرهای تحصیلی، کاری یا اقامت دائم را بر اساس شرایط شما پیدا کنید.
            برای شروع، کمی درباره خودتان بگویید."""
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# restart conversation without /start
async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مکالمه جدید شروع شد! 🔄")

# Buttons 
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # stops flicker telegram needs this one

    data = query.data # callback_data
    if data == "guide":
        text = (
            """📘 راهنمای سریع 
            1️⃣ شرایط خود را بگویید: سن، تحصیلات، سابقه کاری، زبان و کشور مقصد.
            2️⃣ من مسیرهای مناسب را پیشنهاد می‌کنم: تحصیلی، کاری یا اقامت دائم.
            3️⃣ برای هر مسیر، دانشگاه‌ها، هزینه‌ها، مدارک و چالش‌ها را توضیح می‌دهم.
            4️⃣ سوالات خود را بپرسید، من پاسخ می‌دهم!"""
        )
    elif data == "faq":
        text = (
            """❓ سوالات متداول دانشجویان
            1️⃣ بهترین کشور برای مهاجرت تحصیلی کدام است؟
            2️⃣ چطور شانس پذیرش در دانشگاه‌ها را افزایش دهم؟
            3️⃣ هزینه‌های مهاجرت چقدر است؟
            4️⃣ چه مدارکی برای ویزا نیاز دارم؟
           """
        )
    elif data == "support":
        text = (
            """📞 پشتیبانی
            برای سوالات بیشتر یا کمک، لطفاً با پشتیبانی ما تماس بگیرید:
            📧 ایمیل: saberimahtab2002@gmail.com
            📞 تلفن: 09375607637"""
        )
    else:
        text = "دکمه ناشناخته!"

    await query.edit_message_text(text)  # جایگزینی پیام قبلی با پاسخ
    # اگر نمی‌خواهید پیام قبلی عوض شود، می‌توانید از query.message.reply_text استفاده کنید.

# --- تابع اصلی ---
def main():
    app = Application.builder().token(TOKEN).build()
# اول یه اپلیکیشن می‌سازیم با استفاده از توکن ربات. این شیء همه کارهای ربات رو راه می‌ندازه.


    # هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("restart", restart))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    

    print("OK!")
    app.run_polling() # همش سوال میپرسه

if __name__ == "__main__":
    main()

# python bot.py ==> __name__ --> "__main__"
# iport bot ==> __name__ --> bot
# Why == | Run directly? 
# main() runs!