from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

class TelegramBot:
    def init(self, token: str):
        """Initialize the bot with your token."""
        self.application = Application.builder().token(token).build()
        
        # Add handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when the command /start is issued."""
        await update.message.reply_text('Hello! Welcome to your Telegram bot. Use /help to see available commands.')
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Send a message when the command /help is issued."""
        help_text = """
        Available commands:
        /start - Start the bot
        /help - Show this help message
        
        You can also send any message and I'll echo it back!
        """
        await update.message.reply_text(help_text)
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Echo the user message."""
        await update.message.reply_text(f"You said: {update.message.text}")
    
    def run(self):
        """Start the bot."""
        print("Bot is starting...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

def main():
    # Replace 'YOUR_BOT_TOKEN' with the token you got from BotFather
    bot_token = "7821181761:AAEwwuh4gqkuRvL2yJ_YQZMm64tfTGZWIx4"
    bot = TelegramBot(bot_token)
    bot.run()

if __name__ == '_main_':
    main()
