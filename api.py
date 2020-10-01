from datetime import datetime

from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify
from bson import ObjectId

from src.models.devices import Devices
from src.models.consumptions import Consumptions
from src.models.users import Users
from src.utils import mongo_objectid_encoder, send_manual_message

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

    return jsonify(mongo_objectid_encoder(entity_returned))


@app.route('/insertConsumption', methods=['POST'])
def insert_consumption():
    """
    Inserts doc given in body request to corresponding collection

    :return:
    """
    body = request.get_json()

    timestamp = datetime.now()
    body['timestamp'] = timestamp
    body['deviceId'] = ObjectId(body['deviceId'])
    entity_returned = Consumptions().insert_doc(body)

    device_id = body['deviceId']

    query_db = {
        'deviceId': device_id
    }
    consumptions = Consumptions().get_docs_by_query(query_db)

    last_ten_avg = sum([doc['amperage'] for doc in consumptions[:10]]) / 10

    if abs(last_ten_avg - body['amperage']) > 0.017:
        query_db = {
            '_id': ObjectId(device_id)
        }
        device_data = Devices().get_one_doc(query_db)
        spmsh_user_id = device_data['userId']

        query_db = {
            '_id': spmsh_user_id
        }
        spmsh_user_data = Users().get_one_doc(query_db)
        user_chat_id = spmsh_user_data['chatId']
        send_text = '\U0001F6A8 ¡Alerta! Ponerse en contacto con ' \
                    + device_data['address']
        send_manual_message(user_chat_id, send_text)

    return jsonify(mongo_objectid_encoder(entity_returned))


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0')
