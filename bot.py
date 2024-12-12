from transformers import pipeline
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Initialize Hugging Face pipeline (e.g., GPT-2 or other conversational models)
qa_pipeline = pipeline("text-generation", model="gpt2")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! I can help you with math problems or general questions. Just type your query!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.strip()

    try:
        # Use Hugging Face for general questions
        response = ask_huggingface(user_message)
    except Exception as e:
        response = f"Sorry, I couldn’t process your query. Error: {e}"
    
    await update.message.reply_text(response)

def ask_huggingface(question: str) -> str:
    """
    Query Hugging Face pipeline for general doubt solving.
    """
    try:
        result = qa_pipeline(question, max_length=150, num_return_sequences=1, temperature=0.7)
        return result[0]["generated_text"]
    except Exception as e:
        return f"Error in processing your query: {e}"

if __name__ == "__main__":
    # Replace 'your_telegram_bot_token' with your actual Telegram bot token
    app = ApplicationBuilder().token("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").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
    #check the code 
