from datetime import datetime
from uuid import uuid4
from pymongo.results import UpdateResult
from graphql_pokemon_battle.src.repositories.capture.capture import capture_repository
from graphql_pokemon_battle.src.repositories.mongo.repository_trainer import MongoRepository
from graphql_pokemon_battle.src.services.treinador.service_trainer import TrainerService
import requests
class Capture:

    repository = capture_repository

    @classmethod
    def capture_pokemon(cls, capture: dict):
        trainer = capture.get("trainer_id", capture)
        pokemon_number = capture.get("number_pokemon")
        api = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
        poke_list = requests.get(api)
        result = poke_list.json()

        pokemons_list = {

            "trainer_id": trainer,
            "poke_id": str(uuid4()),
            "pokemon": result["name"],
            "number_pokemon": pokemon_number,
            "name_pokemon": capture["name_pokemon"],
            "weight": result["weight"],
            "experience": result["base_experience"],
            "captured_in": datetime.now()
        }

        cls.repository.insert_one_capture(pokemons_list)
        return pokemons_list

    @classmethod
    def get_one(cls, input: dict):
        get = input.get("input", input)
        read = cls.repository.get_trainer_capture(get)
        return read

    @classmethod
    def get_all_pokemons(cls, input):
        skip = input.get("skip")
        limit = input.get("limit")

        collection = cls.repository.get_collection_capture()
        pokemon_skip = (
            collection.find({}).skip(skip).limit(limit)
        )
        raw_data = list(pokemon_skip)

        new_data = []

        for pkm_cap in raw_data:
            pokemon_novo_cap = {
                "trainer_id": pkm_cap["trainer_id"],
                "poke_id": pkm_cap["poke_id"],
                "pokemon": pkm_cap["pokemon"],
                "number_pokemon": pkm_cap["number_pokemon"],
                "name_pokemon": pkm_cap["name_pokemon"],
                "weight": pkm_cap["weight"],
                "experience": pkm_cap["experience"],
                "captured_in": pkm_cap["captured_in"],
            }
            new_data.append(pokemon_novo_cap)

        return_obj = {"data": new_data}

        return return_obj