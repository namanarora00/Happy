
import logging
from conversation import Conversation
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

HANDLERS = {}


def get_handler(uid):
    if not HANDLERS.get(uid, None):
        HANDLERS[uid] = Conversation()
    return HANDLERS[uid]


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def on_message(update, context):
    """Echo the user message."""

    uid = update.effective_user.id
    handler = get_handler(uid)
    reply = handler.response(update.message.text)
    update.message.reply_text(reply)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    API_KEY = os.environ.get('API_TELEGRAM', None)
    if not API_KEY:
        print("Please define API_KEY in the environment")
        exit(0)

    """Start the bot."""
    updater = Updater(API_KEY, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, on_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
