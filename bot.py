import os
import logging

from bson import ObjectId
from dotenv import load_dotenv, find_dotenv
from src.models.devices import Devices

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())


def start(update, context):
    keyboard = [[InlineKeyboardButton("Option 1", callback_data='1'),
                 InlineKeyboardButton("Option 2", callback_data='2')],

                [InlineKeyboardButton("Option 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == '3':
        device = Devices().get_one_doc({'_id': ObjectId('5f59162308a2e0adcdcad4e2')})
        query.edit_message_text(text="Dispositivo: {}".format(device['campoDePrueba']))

    elif query.data == '2':
        send_text = 'Datos consumo día de hoy para \n' \
                    'dispositivo 5213098123098: \n' \
                    'Potencia: 543W \n' \
                    'Intensidad: 34A'

        query.edit_message_text(text=send_text)

    elif query.data == '1':
        send_text = '\U0001F6A8 ¡Alerta! Ponerse en contacto con' \
                    'dirección: C/ Toro 65, 2ºC      '
        query.edit_message_text(text=send_text)

    else:
        query.edit_message_text(text="Selected option: {}".format(query.data))


def help_command(update, context):
    update.message.reply_text("Use /start to test this bot.")


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary

    bot_token = os.getenv('BOT_TOKEN')
    updater = Updater(bot_token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()