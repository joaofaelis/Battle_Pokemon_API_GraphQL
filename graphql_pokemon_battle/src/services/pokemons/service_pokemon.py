from graphql_pokemon_battle.src.repositories.mongo.repository_pokemon import Pokemon_Repository
import requests
from uuid import uuid4
from datetime import datetime

class pokemon_service:

    repository = Pokemon_Repository

    @classmethod
    def soft_delete_poke(cls, delete: str):
        insert = delete["id"]
        soft = cls.repository.soft_delete_pokemon(insert)
        return soft

    @classmethod
    def skip_limit_pokemon(cls, input):
        skip = input.get("skip")
        limit = input.get("limit")
        collection = cls.repository.get_collection()
        pokemon_skip = (
            collection.find({"status": True}, {"_id": False}).skip(skip).limit(limit)
        )
        raw_data = list(pokemon_skip)
        new_data = []
        for pkm in raw_data:
            pokemon_novo = {
                "number_pokemon": pkm["number_pokemon"],
                "poke_id": pkm["poke_id"],
                "pokemon": pkm["pokemon"],
                "weight": pkm["weight"],
                "experience": pkm["experience"],
                "status": pkm["status"],
                "created_dat": pkm["created_dat"],
            }
            new_data.append(pokemon_novo)
        return_obj = {"data": new_data}
        return return_obj

    @classmethod
    def insert_pokemon(cls, insert: dict):
        num_pokemon: int = insert.get('number_pokemon')
        query: dict = {
            "number_pokemon": num_pokemon
        }
        pokemon_objects: dict = cls.repository.get_object(query)
        if pokemon_objects is None:
            pokemon_objects: dict = cls.get_api_pokemon(insert)
            pokemon_objects.update({
               "poke_id": str(uuid4()),
               "status": True,
            "created_dat": str(datetime.now())

            })
            cls.repository.insert_one(pokemon_objects)
        return pokemon_objects

    @classmethod
    def get_api_pokemon(cls, input: dict):
        number_pokemon = input.get('number_pokemon')
        api = f'https://pokeapi.co/api/v2/pokemon/{number_pokemon}'
        list = requests.get(api)
        result = list.json()

        new_list = {
            "number_pokemon": number_pokemon,
            "pokemon": result["name"],
            "weight": result["weight"],
            "experience": result["base_experience"],
        }

        return new_list

    @classmethod
    def delete_pokemon(cls, id):
        data = {"poke_id": id}
        dt = cls.repository.delete_pokemons(data)
        return f" {dt} Dados deletados."















