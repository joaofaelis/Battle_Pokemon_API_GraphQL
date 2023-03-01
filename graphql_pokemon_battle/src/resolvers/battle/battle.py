from ariadne import (QueryType,MutationType,gql,make_executable_schema,load_schema_from_path)
from graphql_pokemon_battle.src.services.battle.battle import capture

battle_pokemon = MutationType()
start_battle_pokemon = QueryType()


@battle_pokemon.field("start_Battle")
def insert_pkm(obj, info, input):
    btl_start = capture.insert_result_battle(input)
    return btl_start





