from graphql_pokemon_battle.src.infrastructures.mongo.infrastructure import MongoInfrastructure
class Pokemon_Repository:

    infrastructure = MongoInfrastructure
    db_name = "ProjetoCRUD"
    collection_name = "pokemons"

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
    def soft_delete_pokemon(cls, _id):
        collection = cls.get_collection()
        query = {"poke_id": _id}
        delete = {"$set": {"status": False}}
        delete_one = collection.update_one(query, delete)
        return delete_one

    @classmethod
    def get_object(cls, Id):
        collection = cls.get_collection()
        return collection.find_one(Id)

    @classmethod
    def get_all_pokemons(cls, skip, limit):
        collection = cls.get_collection()
        pokemon_skip = collection.find({}, {"status": True}).skip(skip).limit(limit)
        result = list(pokemon_skip)
        return result


    @classmethod
    def delete_pokemons(cls, deletar):
        collection = cls.get_collection()
        delete_onee = collection.delete_one(deletar)
        return delete_onee