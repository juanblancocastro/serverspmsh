from .mongodb_base import MongoModel


class Users(MongoModel):

    _collection_name = 'consumptions'
