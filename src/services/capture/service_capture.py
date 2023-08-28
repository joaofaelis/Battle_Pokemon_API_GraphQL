from datetime import datetime
from uuid import uuid4
from src.repositories.mongo.repository_mongo import Repository_Mongo
from src.services.pokemons.service_pokemon import Pokemon_Service
from decouple import config
class Capture_Pokemons:

    repository = Repository_Mongo
    collectionPokemon = config('pokemons')  # Collection Mongo
    collectionCapture = config('capture')

    def capture_pokemon(cls, collection_capture: collectionCapture, collection_pokemon: collectionPokemon, name_pokemon, unique_id, number_pokemon):
        object_find = {'number_pokemon': number_pokemon}
        get_info: dict = cls.repository.get_object(collection_pokemon, object_find)
        if get_info is None:
            pokemon_objects: dict = Pokemon_Service.get_api_pokemon(number_pokemon)
            pokemon_objects.update({
                "unique_id": str(uuid4()),
                "trainer_id": unique_id,
                "pokemon_id": str(uuid4()),
                "number_pokemon": number_pokemon,
                "name_pokemon": name_pokemon,
                "weight": pokemon_objects['weight'],
                "experience": pokemon_objects['experience'],
                "captured_in": str(datetime.now()),
                "status": True,
                "created_at": str(datetime.now())

            })
            cls.repository.insert_object(collection_capture, pokemon_objects)
            return pokemon_objects
        else:
            get_info.update({
                "unique_id": str(uuid4()),
                "trainer_id": unique_id,
                "pokemon_id": get_info["unique_id"],
                "number_pokemon": get_info["number_pokemon"],
                "name_pokemon": name_pokemon,
                "weight": get_info['weight'],
                "experience": get_info['experience'],
                "captured_in": str(datetime.now())
            }
            )
            cls.repository.insert_object(collection_capture, get_info)
            return get_info

    @classmethod
    def get_one_capture(cls, collection_capture: collectionCapture, input: dict):
        get = input.get("input", input)
        get_object = cls.repository.get_object(collection_capture, get)
        return get_object

    @classmethod
    def get_all_pokemons(cls,collection_capture: collectionCapture, input):
        skip = input.get("skip")
        limit = input.get("limit")

        collection = cls.repository.skip_limit(collection_capture, skip, limit)
        list_data = list(collection)

        new_list_data = []

        for pkm_cap in list_data:
            capture_new_list = {
                "trainer_id": pkm_cap["trainer_id"],
                "poke_id": pkm_cap["poke_id"],
                "pokemon": pkm_cap["pokemon"],
                "number_pokemon": pkm_cap["number_pokemon"],
                "name_pokemon": pkm_cap["name_pokemon"],
                "weight": pkm_cap["weight"],
                "experience": pkm_cap["experience"],
                "captured_in": pkm_cap["captured_in"],
            }
            new_list_data.append(capture_new_list)

        return_obj = {"data": new_list_data}

        return return_obj