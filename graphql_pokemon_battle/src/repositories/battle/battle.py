from graphql_pokemon_battle.src.infrastructures.mongo.infrastructure import MongoInfrastructure
class battle_repository:

    infrastructure = MongoInfrastructure
    db = "ProjetoCRUD"
    collection = "capture"

    @classmethod
    def get_collection_battle(cls):
        infra = cls.infrastructure.get_client()
        database = infra[cls.db]
        collection = database[cls.collection]
        return collection

    @classmethod
    def get_one(cls, query: dict):
        collection = cls.get_collection_battle()
        return collection.find_one(query)

class start_battle:

    infrastructure = MongoInfrastructure
    db = "ProjetoCRUD"
    collection = "battle"

    @classmethod
    def get_collection_battle(cls):
        infra = cls.infrastructure.get_client()
        database = infra[cls.db]
        collection = database[cls.collection]
        return collection

    @classmethod
    def insert_one(cls, battle):
        collection = cls.get_collection_battle()
        return collection.insert_one(battle)