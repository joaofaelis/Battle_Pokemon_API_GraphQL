from datetime import datetime
from uuid import uuid4
from src.repositories.mongo.repository_mongo import Repository_Mongo
from decouple import config

class Battle_Pokemons:

    repository_capture = config('capture')
    repository_battle = config('battle')

    @classmethod
    def insert_result_battle(cls, result: dict):
        trainer_one = result.get("trainer_one_id")
        trainer_two = result.get("trainer_two_id")
        query_trainer_one: dict = {"trainer_id": trainer_one}
        query_trainer_two: dict = {"trainer_id": trainer_two}
        battle_object_one: dict = cls.repository_capture.get_one(query_trainer_one)
        battle_object_two: dict = cls.repository_capture.get_one(query_trainer_two)
        if battle_object_one["experience"] > battle_object_two["experience"]:
            trainer_winner_unique_id = trainer_one

            poke_battle = {
            "id_winner_battle": str(uuid4()),
            "trainer_winner_id": trainer_winner_unique_id,
            "poke_id": battle_object_one["poke_id"],
            "pokemon": battle_object_one["pokemon"],
            "number_pokemon": battle_object_one["number_pokemon"],
            "name_pokemon": battle_object_one["name_pokemon"],
            "weight": battle_object_one["weight"],
            "experience": battle_object_one["experiencie"],
            "date_battle": str(datetime.now()),
        }

        else:
            trainer_winner_unique_id = trainer_two
            poke_battle = {
            "id_winner_battle": str(uuid4()),
            "trainer_winner_id": trainer_winner_unique_id,
            "poke_id": battle_object_two["poke_id"],
            "pokemon": battle_object_two["pokemon"],
            "number_pokemon": battle_object_two["number_pokemon"],
            "name_pokemon": battle_object_two["name_pokemon"],
            "weight": battle_object_two["weight"],
            "experience": battle_object_two["experience"],
            "date_battle": str(datetime.now()),
            }


        battle = Repository_Mongo.insert_object(cls.repository_battle, poke_battle)
        return battle