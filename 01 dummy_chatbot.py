from telegram.ext import Updater, MessageHandler, Filters
import openai

openai.api_key = ""
TELEGRAM_API_TOKEN = ""

def text_message(update, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "system", "content": "A humble woman"}] #personality of the chatbot
    )
    update.message.reply_text(response["choices"][0]["message"]["content"])


updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), text_message))
updater.start_polling()
updater.idle()