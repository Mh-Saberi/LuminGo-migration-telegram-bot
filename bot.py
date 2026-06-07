from telegram.ext import Application, MessageHandler, filters, CommandHandler, CallbackQueryHandler
from config import TOKEN
from handlers.messages import handle_message
from handlers.commands import start, restart, clear_history
from handlers.buttons import button_handler

# --- main function ---
def main():
    # first we create the application with our bot token. This object will handle everything for us.
    app = Application.builder().token(TOKEN).build()


    # then we add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("restart", restart))
    app.add_handler(CommandHandler("clear", clear_history))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    

    print("OK!")
    app.run_polling() # this will start the bot and keep it running until we stop it manually. It will check for new messages and call the appropriate handlers.

if __name__ == "__main__":
    main()
