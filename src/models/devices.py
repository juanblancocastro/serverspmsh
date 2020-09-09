from bson import ObjectId

from .mongodb_base import MongoModel


class Devices(MongoModel):

    _direction = ''

    _responsible_id = None

    _collection_name = 'devices'

    # def __init__(self, direction: str, responsible_id: ObjectId):
    #
    #     self._direction = direction
    #
    #     self._responsible_id = responsible_id
    #
    #     super().__init__()
