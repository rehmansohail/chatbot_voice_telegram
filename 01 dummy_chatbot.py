from telegram.ext import Updater, MessageHandler, Filters
import openai

openai.api_key = ""     #place your openai api key here
TELEGRAM_API_TOKEN = ""     #place your telegram token here

def text_message(update, context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "system", "content": "A jester"}] #personality of the chatbot
    )
    update.message.reply_text(response["choices"][0]["message"]["content"])


updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), text_message))
updater.start_polling()
updater.idle()