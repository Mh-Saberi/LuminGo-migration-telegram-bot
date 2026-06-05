from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackQueryHandler
from config import TOKEN, WEBHOOK_URL, PORT
from handlers.messages import handle_message
from handlers.commands import start, restart, clear_history
from handlers.buttons import button_handler

# --- تابع اصلی ---
def main():
    app = Application.builder().token(TOKEN).build()
# اول یه اپلیکیشن می‌سازیم با استفاده از توکن ربات. این شیء همه کارهای ربات رو راه می‌ندازه.


    # هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("restart", restart))
    app.add_handler(CommandHandler("clear", clear_history))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    

    print("OK!")
    app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=WEBHOOK_URL
        )

if __name__ == "__main__":
    main()

# python bot.py ==> __name__ --> "__main__"
# iport bot ==> __name__ --> bot
# Why == | Run directly? 
# main() runs!