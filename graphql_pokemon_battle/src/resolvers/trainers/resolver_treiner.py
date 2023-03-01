from time import time
from uuid import uuid4
from graphql_pokemon_battle.src.services.treinador.service_trainer import TrainerService
from ariadne import QueryType, gql, make_executable_schema, load_schema_from_path, MutationType

query = QueryType()
mutation = MutationType()


@query.field("find_trainer")
def get_trainer(obj, info, input):
    return_data = TrainerService.get_id_trainer(input)
    return return_data


@query.field("page_trainers")
def get_all(obj, info, input):
    get_all_trainer = TrainerService.skip_limit_trainer(input)
    return get_all_trainer


@mutation.field("insert_trainer")
def insert_trainer(obj, info, input):
    created = TrainerService.insert_trainer(input)
    return created


@mutation.field("soft_delete_trainer")
def soft_delete(obj, info, input):
    unique_id = input.get("id")
    status = input.get("status")
    service =TrainerService.soft_delete_trainer(unique_id, status)
    return service


@mutation.field("Update_trainer")
def update(obj, info, input):
    TrainerService.update_trainer(input)
    return "Sucess"

