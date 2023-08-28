#third party
from ariadne import (QueryType, MutationType)
#local
from src.services.battle.service_battle import Battle_Pokemons

battle_pokemon = MutationType()
start_battle_pokemon = QueryType()


@battle_pokemon.field("start_Battle")
def insert_pkm(obj, info, input_battle):
    btl_start = Battle_Pokemons.insert_result_battle(input_battle)
    return btl_start





