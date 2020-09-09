import requests
from flask import Flask, request, jsonify
from src.models.devices import Devices
from src.utils import mongo_objectid_encoder

app = Flask(__name__)

BOT_TOKEN = '1302499196:AAGUtabUlDEk5Wusd1zJp8texO5r4iQLK0A'


@app.route('/insertDevice', methods=['POST'])
def inserting():
    """
    Inserts doc given in body request to corresponding database

    :return:
    """
    body = request.get_json()
    entity_returned = Devices().insert_doc(body)

    chat_id = 'https://api.telegram.org/bot{0}/sendMessage?chat_id=85806317&text=Probando'
    message = ''

    requests.post(
        url='https://api.telegram.org/bot{0}/sendMessage',
        data={'chat_id': chat_id, 'text': message}
    ).json()

    return jsonify(mongo_objectid_encoder(entity_returned))


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
