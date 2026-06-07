from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# first message of user : /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 راهنما", callback_data="guide")],
        [InlineKeyboardButton("❓ سوالات متداول", callback_data="faq")],
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard) # telegram knows this!

    welcome_text = (
        """
        خوش آمدید 👋 
        من دستیار مهاجرت شما هستم. کمک می‌کنم بهترین مسیرهای تحصیلی، کاری یا اقامت دائم را بر اساس شرایط شما پیدا کنید.
        برای شروع، کمی درباره خودتان بگویید.
        مثلا: "من 25 ساله هستم، لیسانس کامپیوتر دارم، 3 سال سابقه کاری دارم، انگلیسی بلدم و می‌خوام به کانادا مهاجرت کنم."
        """
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# restart conversation with /start
async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)  # just call start again
    await update.message.reply_text("مکالمه جدید شروع شد! 🔄")

async def clear_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["history"] = []
    await update.message.reply_text("تاریخچه مکالمه پاک شد! 🗑️")
