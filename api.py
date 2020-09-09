import requests
from flask import Flask, request, jsonify
from src.models.devices import Devices
from src.utils import mongo_objectid_encoder

app = Flask(__name__)

BOT_TOKEN = '1302499196:AAGUtabUlDEk5Wusd1zJp8texO5r4iQLK0A'


# Create a URL route in our application for "/"
@app.route('/insertDevice', methods=['POST'])
def inserting():
    """
    Inserts doc given in body request to corresponding database

    :return:
    """
    body = request.get_json()
    entity_returned = Devices().insert_doc(body)

    bot_url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id=85806317&text=Probando'

    requests.post(
        url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
        data={'chat_id': 12345, 'text': 'hello friend'}
    ).json()

    'https://api.telegram.org/bot{}/sendMessage?chat_id=<group chat id >&text=<our text>'
    return jsonify(mongo_objectid_encoder(entity_returned))


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
