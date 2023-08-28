# third party
from ariadne import QueryType, MutationType
# local
from src.services.pokemons.service_pokemon import Pokemon_Service


query_pokemon = QueryType()
mutation_pokemon = MutationType()


@mutation_pokemon.field("insert_pokemon")
def insert_poke(obj, info, input_pokemon):
    create_data = Pokemon_Service.insert_pokemon(input_pokemon)
    return create_data

@mutation_pokemon.field("soft_delete_pokemon")
def soft(obj, info, input_pokemon):
    soft_delete = Pokemon_Service.soft_delete_pokemon(input_pokemon)
    return soft_delete

@query_pokemon.field('page_pokemons')
def skiplimit(obj, info, input_pokemon):
    pagination = Pokemon_Service.skip_limit_pokemon(input_pokemon)
    return pagination

@mutation_pokemon.field("deletePokemon")
def del_pkm(obj, info, input_pokemon):
    delete = input_pokemon.get("poke_id")
    poke_delete = Pokemon_Service.delete_pokemon(delete)
    return poke_delete

