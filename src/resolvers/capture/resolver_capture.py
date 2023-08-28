# third party
from ariadne import (QueryType, MutationType)
from decouple import config
# local
from src.services.capture.service_capture import Capture_Pokemons


capture_pokemon = MutationType()
get_capture_pokemon = QueryType()

# Collection Mongo
collectionPokemon = config('pokemons')
collectionCapture = config('capture')


@capture_pokemon.field("capture_pokemon")
def insert_pkm(obj, info, collection_capture: collectionCapture, collection_pokemon: collectionPokemon, name_pokemon, unique_id, number_pokemon):
    cap_created = Capture_Pokemons.capture_pokemon(collection_capture, collection_pokemon, name_pokemon, unique_id, number_pokemon)
    return cap_created

@get_capture_pokemon.field("find_captureds")
def get_pkm_cap(obj, info, collection: collectionCapture, input_capture):
    return_data = Capture_Pokemons.get_one_capture(collection, input_capture)
    return return_data

@get_capture_pokemon.field("page_capture")
def read_all3(obj, info, collection: collectionCapture, input_capture):
    return_data = Capture_Pokemons.get_all_pokemons(collection, input_capture)
    return return_data