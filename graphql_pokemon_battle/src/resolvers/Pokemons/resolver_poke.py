from graphql_pokemon_battle.src.services.pokemons.service_pokemon import pokemon_service
from ariadne import QueryType, gql, make_executable_schema, load_schema_from_path, MutationType

query_pokemon = QueryType()
mutation_pokemon = MutationType()


@mutation_pokemon.field("insert_pokemon")
def insert_poke(obj, info, input):
    create = pokemon_service.insert_pokemon(input)
    return create

@mutation_pokemon.field("soft_delete_pokemon")
def soft(obj, info, input):
    soft_delete = pokemon_service.soft_delete_poke(input)
    return soft_delete

@query_pokemon.field('page_pokemons')
def skiplimit(obj, info, input):
    var = pokemon_service.skip_limit_pokemon(input)
    return var

@mutation_pokemon.field("deletePokemon")
def del_pkm(obj, info, input):
    delet = input.get("poke_id")
    poke_delete = pokemon_service.delete_pokemon(delet)
    return poke_delete

