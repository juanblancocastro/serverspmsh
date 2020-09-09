from flask import Flask, request
from src.models.devices import Devices
import json
from bson import ObjectId
import datetime

app = Flask(__name__)


# Create a URL route in our application for "/"
@app.route('/insertDevice', methods=['POST'])
def inserting():
    """
    Inserts doc given in body request to corresponding database

    :return:
    """
    body = request.get_json()
    entity_returned = Devices().insert_doc(body)
    return mongo_encoder(entity_returned)


def mongo_encoder(mongo_item):
    mongo_item['_id'] = str(mongo_item['_id'])

    return mongo_item


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
