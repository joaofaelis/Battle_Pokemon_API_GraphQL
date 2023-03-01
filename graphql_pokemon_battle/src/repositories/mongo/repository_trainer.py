from graphql_pokemon_battle.src.infrastructures.mongo.infrastructure import MongoInfrastructure
class MongoRepository:

    infrastructure = MongoInfrastructure
    db_name = "ProjetoCRUD"
    collection_name = "trainers"

    @classmethod
    def get_collection(cls):
        client = cls.infrastructure.get_client()
        database = client[cls.db_name]
        collection = database[cls.collection_name]
        return collection

    @classmethod
    def insert_one(cls, create):
        collection = cls.get_collection()
        return collection.insert_one(create)

    @classmethod
    def update(cls, query, object_up):
        collection = cls.get_collection()
        update_obj = {"$set": object_up}
        update = collection.update_one(query, update_obj)
        return update

    @classmethod
    def soft_delete(cls, _id, atualizar):
        collection = cls.get_collection()
        delete = {"$set": atualizar}
        delete_one = collection.update_one(_id, delete)
        return delete_one

    @classmethod
    def get_object(cls, Id):
        collection = cls.get_collection()
        query = {"id": Id}
        return collection.find_one(query)

    @classmethod
    def get_all(cls, skip, limit):
        collection = cls.get_collection()
        trainer_skip = collection.find({}, {"status": True}).skip(skip).limit(limit)
        result = list(trainer_skip)
        return result
