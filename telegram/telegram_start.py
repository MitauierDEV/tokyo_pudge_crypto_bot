from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from crypto_client.crypto_currency_client import get_crypto_currency_price

TOKEN = "7560347163:AAGSgNV4rIbTvQR7DwBNjrPvZ4xSWubTxDU"

async def start(update: Update, context):
    await update.message.reply_text("Привет! Введи свою крипто валюту")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    currency = await get_crypto_currency_price(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=currency.text)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

print("Bot is running...")
app.run_polling()