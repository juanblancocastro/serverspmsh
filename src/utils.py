import requests
import os
from bson import ObjectId


def mongo_objectid_encoder(mongo_item: dict):
    for k, v in mongo_item.items():
        if isinstance(v, ObjectId):
            mongo_item[k] = str(v)
    # mongo_item['_id'] = str(mongo_item['_id'])

    return mongo_item


def send_manual_message(chat_id, message):
    """Using python library requests sends a telegram message to
    user by telegram chat_id

    :param chat_id:
    :param message:
    """
    requests.post(
        url='https://api.telegram.org/bot{0}/sendMessage'.format(os.getenv('BOT_TOKEN')),
        data={'chat_id': chat_id, 'text': message}
    ).json()