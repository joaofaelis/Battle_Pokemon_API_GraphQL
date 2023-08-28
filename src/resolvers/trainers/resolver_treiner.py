# third party
from ariadne import QueryType, MutationType
# local
from src.services.trainer.service_trainer import Trainer_Service


query = QueryType()
mutation = MutationType()


@query.field("find_trainer")
def get_trainer(obj, info, input_trainer):
    return_data = Trainer_Service.get_id_trainer(input_trainer)
    return return_data


@query.field("page_trainers")
def get_all(obj, info, skip, limit):
    get_all_trainer = Trainer_Service.skip_limit_trainers(skip, limit)
    return get_all_trainer


@mutation.field("insert_trainer")
def insert_trainer(obj, info, input_trainer):
    created = Trainer_Service.insert_trainer(input_trainer)
    return created


@mutation.field("soft_delete_trainer")
def soft_delete(obj, info, input_trainer):
    unique_id = input_trainer.get("id")
    status = input_trainer.get("status")
    service = Trainer_Service.soft_delete_trainer(unique_id, status)
    return service


@mutation.field("Update_trainer")
def update(obj, info, input_trainer):
    Trainer_Service.update_trainer(input_trainer)
    return "Sucess"

