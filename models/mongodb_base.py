from pymongo import MongoClient


class MongoModel:

    _connection = None

    _database = 'spmsh'

    _collection_name = ''

    _collection = None

    _url = 'mongodb+srv://blancasdelmol:blancasdelmol@testingjuan.ed9pu.mongodb.net/'

    def __init__(self):

        if self._connection is None:
            self._connection = MongoClient(self._url)

        if self._collection is None:
            self._collection = self._connection[self._database][self._collection_name]

    def insert_doc(self, doc: dict):
        """Inserts given doc in corresponding database collection

        :param doc:
        :return:
        """

        returned_id = self._collection.insert(doc)

        inserted_doc = self.get_one_doc({'_id': returned_id})

        return inserted_doc

    def get_one_doc(self, query: dict):
        """Finds one doc by given query

        :param query:
        :return:
        """

        doc = self._collection.find_one(query)

        return doc


