#local
from src.infrastructure.mongo.infrastructure import MongoInfrastructure

class Repository_Mongo:

    @staticmethod
    def collection(select_collection: str):
        select_collection = MongoInfrastructure.get_collection(select_collection)
        return select_collection

    @classmethod
    def insert_object(cls, collection_mongo, object):
        insert_one = cls.collection(collection_mongo).insert_one(object)
        return insert_one

    @classmethod
    def get_object(cls, collection_mongo, unique_id):
        find_service = cls.collection(collection_mongo).find_one(unique_id)
        return find_service

    @classmethod
    def update_object(cls, collection_mongo, query, object_up):
        update_trainers = cls.collection(collection_mongo).update_one(query, object_up)
        return update_trainers

    @classmethod
    def delete_object(cls, collection_mongo, unique_id):
        delete_permanent = cls.collection(collection_mongo).delete_one(unique_id)
        return delete_permanent

    @classmethod
    def skip_limit(cls, collection_mongo, skip, limit):
        skip_limit = cls.collection(collection_mongo).find({}, {'status': True}).skip(skip).limit(limit)
        result = list(skip_limit)
        return result
