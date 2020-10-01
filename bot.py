import os
import logging

from bson import ObjectId
from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv
from src.models.devices import Devices
from src.models.consumptions import Consumptions
from src.models.users import Users

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv(find_dotenv())


def start(update, context):
    keyboard = [[InlineKeyboardButton("\U0001F4A1 Datos de consumo", callback_data='1')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Seleccionar:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    query.answer()

    if query.data == '3':
        device = Devices().get_one_doc({'_id': ObjectId('5f59162308a2e0adcdcad4e2')})
        query.edit_message_text(text="Dispositivo: {}".format(device['campoDePrueba']))

    elif query.data == '1':
        user_chat_id = query.from_user.id
        query_db = {
            'chatId': user_chat_id
        }
        spmsh_user_data = Users().get_one_doc(query_db)
        spmsh_user_id = spmsh_user_data['_id']

        query_db = {
            'userId': spmsh_user_id
        }
        device_data = Devices().get_one_doc(query_db)
        device_id = device_data['_id']

        query_db = {
            'deviceId': device_id
        }

        consumptions = Consumptions().get_docs_by_query(query_db)

        consumptions = [doc for doc in consumptions if doc['timestamp'] > datetime.now() - timedelta(days=2)]
        avg_consumptions = sum([doc['amperage'] for doc in consumptions]) / len(consumptions)

        send_text = 'Datos consumo medio de hoy y de ayer para el ' \
                    'dispositivo de ' + device_data['address'] + ': \n' \
                    'Intensidad media: ' + str(avg_consumptions) + ' Amperios'

        query.edit_message_text(text=send_text)

    elif query.data == '2':
        send_text = '\U0001F6A8 ¡Alerta! Ponerse en contacto con' \
                    'dirección: C/ Toro 65, 2ºC      '
        query.edit_message_text(text=send_text)

    else:
        query.edit_message_text(text="Selected option: {}".format(query.data))


def help_command(update, context):
    update.message.reply_text("Use /start to test this bot.")


def main():
    bot_token = os.getenv('BOT_TOKEN')
    updater = Updater(bot_token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()