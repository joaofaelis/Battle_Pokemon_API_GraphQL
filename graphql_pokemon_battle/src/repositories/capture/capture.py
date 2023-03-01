from graphql_pokemon_battle.src.infrastructures.mongo.infrastructure import MongoInfrastructure

class capture_repository:
    infrastructure = MongoInfrastructure
    db = "ProjetoCRUD"
    collection = "capture"

    @classmethod
    def get_collection_capture(cls):
        infra = cls.infrastructure.get_client()
        database = infra[cls.db]
        collection = database[cls.collection]
        return collection

    @classmethod
    def insert_one_capture(cls, create):
        collection = cls.get_collection_capture()
        return collection.insert_one(create)

    @classmethod
    def get_trainer_capture(cls, pokemons):
        collection = cls.get_collection_capture()
        return collection.find_one(pokemons)

    @classmethod
    def get_all_capture(cls, skip, limit):
        collection = cls.get_collection_capture()
        pokemons_skip = collection.find({}).skip(skip).limit(limit)
        result = list(pokemons_skip)
        return result
