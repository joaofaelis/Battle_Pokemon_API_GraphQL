
from ariadne import QueryType, gql, make_executable_schema, load_schema_from_path, MutationType
from ariadne.contrib.federation import make_federated_schema
from ariadne.asgi import GraphQL
from starlette.middleware.cors import CORSMiddleware
from starlette.applications import Starlette
import uvicorn

from resolvers.Pokemons.resolver_poke import mutation_pokemon, query_pokemon
from resolvers.trainers.resolver_treiner import query, mutation
from resolvers.capture import capture_pokemon, get_capture_pokemon
from resolvers.battle.battle import battle_pokemon, start_battle_pokemon


type_defs: str = load_schema_from_path("domain/schemas")
schema = make_federated_schema(type_defs, *[query, mutation, mutation_pokemon, query_pokemon,
                                            capture_pokemon, get_capture_pokemon, battle_pokemon, start_battle_pokemon ])
graphql_server = CORSMiddleware(
    GraphQL(
        schema,
        context_value={},
        debug=True,
    ),
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=("GET", "POST", "OPTIONS"),
)
app = Starlette(debug=True)
app.mount("/", graphql_server)
uvicorn.run(app, host="0.0.0.0", port=3333)



