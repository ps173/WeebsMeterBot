from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from dotenv import load_dotenv
from apidata import required_stats
import requests
import os
import json

load_dotenv()

def start(update, context):
    update.message.reply_text('start command received')

def genstats(update, context):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    statsString = required_stats(query) 
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Weebo Meter',
            input_message_content=InputTextMessageContent(statsString)
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

def help(update, context):
    update.message.reply_text('help command received')

def error(update, context):
    update.message.reply_text('an error occured')

def text(update, context):
    update.message.reply_text(f'did you said "{text_received}" ?')

def main():
    TOKEN = os.getenv("BOT_TOKEN")

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CommandHandler("help", help))

    stats_handler = InlineQueryHandler(genstats)
    dispatcher.add_handler(stats_handler)

    dispatcher.add_handler(MessageHandler(Filters.text, text))

    dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
