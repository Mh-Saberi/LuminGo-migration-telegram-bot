from telegram import Update
from telegram.ext import ContextTypes

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
            4️⃣ سوالات خود را بپرسید، من پاسخ می‌دهم!
            """
        )
    elif data == "faq":
        text = (
            """❓ سوالات متداول
            1️⃣ بهترین کشور برای مهاجرت تحصیلی کدام است؟
            2️⃣ چطور شانس پذیرش در دانشگاه‌ها را افزایش دهم؟
            3️⃣ هزینه‌های مهاجرت چقدر است؟
            4️⃣ چه مدارکی برای ویزا نیاز دارم؟
           """
        )
    elif data == "support":
        text = (
            """
            📞 پشتیبانی
            برای سوالات بیشتر یا کمک، لطفاً با پشتیبانی ما تماس بگیرید:
            📧 ایمیل: saberimahtab2002@gmail.com
            📞 تلفن: 09375607637
            """
        )
    else:
        text = "دکمه ناشناخته!"

    await query.edit_message_text(text)  