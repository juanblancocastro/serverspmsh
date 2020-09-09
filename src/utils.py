
def mongo_objectid_encoder(mongo_item):
    mongo_item['_id'] = str(mongo_item['_id'])

    return mongo_item
