from src.repositories.mongo.repository_mongo import Repository_Mongo
import requests
from uuid import uuid4
from datetime import datetime
from decouple import config

class Pokemon_Service:

    repository = Repository_Mongo
    collection = config('pokemons')  # Collection Mongo

    @classmethod
    def get_api_pokemon(cls, input: dict):
        number_pokemon = input.get('number_pokemon')
        requests_api = f'https://pokeapi.co/api/v2/pokemon/{number_pokemon}'
        list_requests = requests.get(requests_api)
        result_in_json = list_requests.json()

        list_pokemons = {
            "number_pokemon": number_pokemon,
            "pokemon": result_in_json["name"],
            "weight": result_in_json["weight"],
            "experience": result_in_json["base_experience"],
        }

        return list_pokemons

    @classmethod
    def soft_delete_pokemon(cls, unique_id):
        query = {"unique_id": unique_id}
        delete = {"$set": {"status": False}}
        delete_pokemon = cls.repository.update_object(cls.collection, query, delete)
        return delete_pokemon

    @classmethod
    def skip_limit_pokemon(cls, input):
        skip = input.get("skip")
        limit = input.get("limit")
        repository_skip_limit = cls.repository.skip_limit(cls.collection, skip, limit)
        list_data = list(repository_skip_limit)
        new_list_data = []
        for pkm in list_data:
            new_list_pokemon = {
                "number_pokemon": pkm["number_pokemon"],
                "poke_id": pkm["poke_id"],
                "pokemon": pkm["pokemon"],
                "weight": pkm["weight"],
                "experience": pkm["experience"],
                "status": pkm["status"],
                "created_dat": pkm["created_dat"],
            }
            new_list_data.append(new_list_pokemon)
        return_obj = {"data_pokemon": new_list_data}
        return return_obj

    @classmethod
    def insert_pokemon(cls, insert_pokemon: dict):
        num_pokemon: int = insert_pokemon.get('number_pokemon')
        query: dict = {
            "number_pokemon": num_pokemon
        }
        pokemon_objects: dict = cls.repository.get_object(cls.collection, query)
        if pokemon_objects is None:
            pokemon_objects: dict = cls.get_api_pokemon(insert_pokemon)
            pokemon_objects.update({
               "poke_id": str(uuid4()),
               "status": True,
            "created_dat": str(datetime.now())

            })
            cls.repository.insert_object(cls.collection, pokemon_objects)
        return pokemon_objects



    @classmethod
    def delete_pokemon(cls, id):
        data_pokemon = {"poke_id": id}
        info_data = cls.repository.delete_object(cls.collection, data_pokemon)
        return f" {info_data} Dados deletados."















