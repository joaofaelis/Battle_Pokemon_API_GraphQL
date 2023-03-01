from datetime import datetime
from uuid import uuid4
from pymongo.results import UpdateResult
from graphql_pokemon_battle.src.repositories.battle.battle import battle_repository, start_battle
import requests
class capture:

    repository_one = battle_repository
    repository_two = start_battle

    @classmethod
    def insert_result_battle(cls, result: dict):
        trainer_one = result.get("trainer_one_id")
        trainer_two = result.get("trainer_two_id")
        query_trainer_one: dict = {"trainer_id": trainer_one}
        query_trainer_two: dict = {"trainer_id": trainer_two}
        battle_object_one: dict = cls.repository_one.get_one(query_trainer_one)
        battle_object_two: dict = cls.repository_one.get_one(query_trainer_two)
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


        cls.repository_two.insert_one(poke_battle)
        return poke_battle