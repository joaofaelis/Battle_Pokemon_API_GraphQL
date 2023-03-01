from graphql_pokemon_battle.src.repositories.mongo.repository_pokemon import PokeRepository
import requests
from uuid import uuid4
from datetime import datetime
infra = PokeRepository

def insert_poke():
    ins = 1
    for ins in range(1,300):

        api = f'https://pokeapi.co/api/v2/pokemon/{ins}'
        list = requests.get(api)
        ret = list.json()
        for chave in ret.keys():
            new_list = {
        "poke_id": str(uuid4()),
        "pokemon": ret["name"],
        "weight": ret["weight"],
        "experience": ret["base_experience"],
         "status": True,
        "create_dat": str(datetime.now())
    }
        infra.insert_one(new_list)
        print(ret)


