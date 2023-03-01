from ariadne import (QueryType,MutationType,gql,make_executable_schema,load_schema_from_path)
from graphql_pokemon_battle.src.services.capture.capture import Capture

capture_pokemon = MutationType()
get_capture_pokemon = QueryType()


@capture_pokemon.field("capture_pokemon")
def insert_pkm(obj, info, input):
    cap_created = Capture.capture_pokemon(input)
    return cap_created

@get_capture_pokemon.field("find_captureds")
def get_pkm_cap(obj, info, input):
    read_cap = Capture.get_one(input)
    return read_cap

@get_capture_pokemon.field("page_capture")
def read_all3(obj, info, input):
    return_data = Capture.get_all_pokemons(input)
    return return_data