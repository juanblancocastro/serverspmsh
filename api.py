import requests
import datetime

from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify

from src.models.devices import Devices
from src.models.consumptions import Consumptions
from src.utils import mongo_objectid_encoder

app = Flask(__name__)
load_dotenv(find_dotenv())


@app.route('/insertDevice', methods=['POST'])
def insert_device():
    """
    Inserts doc given in body request to corresponding database

    :return:
    """
    body = request.get_json()
    entity_returned = Devices().insert_doc(body)

    # chat_id = 'https://api.telegram.org/bot{0}/sendMessage?chat_id=85806317&text=Probando'
    # message = ''
    #
    # requests.post(
    #     url='https://api.telegram.org/bot{0}/sendMessage',
    #     data={'chat_id': chat_id, 'text': message}
    # ).json()

    return jsonify(mongo_objectid_encoder(entity_returned))


@app.route('/insertConsumption', methods=['POST'])
def insert_consumption():
    """
    Inserts doc given in body request to corresponding collection

    :return:
    """
    body = request.get_json()

    timestamp = datetime.datetime.now()
    body['timestamp'] = timestamp
    entity_returned = Consumptions().insert_doc(body)

    # chat_id = 'https://api.telegram.org/bot{0}/sendMessage?chat_id=85806317&text=Probando'
    # message = ''
    #
    # requests.post(
    #     url='https://api.telegram.org/bot{0}/sendMessage',
    #     data={'chat_id': chat_id, 'text': message}
    # ).json()

    return jsonify(mongo_objectid_encoder(entity_returned))


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0')
