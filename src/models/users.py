from .mongodb_base import MongoModel


class Users(MongoModel):

    _collection_name = 'users'

    _name = ''

    _telegram_chat_id = ''

    _tlf = ''

    _nif = ''

    _direction = ''

    # def __init__(self, name: str, telegram_chat_id: str, tlf: str, nif: str, direction: str):
    #
    #     self._name = name
    #
    #     self._telegram_chat_id = telegram_chat_id
    #
    #     self._tlf = tlf
    #
    #     self._nif = nif
    #
    #     self._direction = direction
    #
    #     super().__init__()

