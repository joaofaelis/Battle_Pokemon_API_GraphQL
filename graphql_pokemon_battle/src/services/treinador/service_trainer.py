from time import time
from uuid import uuid4
from graphql_pokemon_battle.src.repositories.mongo.repository_trainer import MongoRepository

class TrainerService:
    repository = MongoRepository

    @classmethod
    def get_id_trainer(cls, input: str):
        input_id = input["id"]
        return_data = cls.repository.get_object(input_id)
        graphql_return_data = {
            "id": return_data["id"],
            "name": return_data["name"],
            "age": return_data["age"],
            "gender": return_data["gender"],
            "status": bool(return_data["status"]),
            "created_dat": int(return_data["created_dat"].timestamp()),
        }
        return graphql_return_data


    @classmethod
    def skip_limit_trainer(cls, input):
        skip = input.get("skip")
        limit = input.get("limit")
        collection = cls.repository.get_collection()
        trainer_skip = (
            collection.find({"status": True}, {"_id": False}).skip(skip).limit(limit)
        )
        list_data = list(trainer_skip)
        new_list_data = []
        for data in list_data:
            trainer_new = {
                "id": data["id"],
                "name": data["name"],
                "gender": data["gender"],
                "age": data["age"],
                "created_dat": data["created_dat"],
                "status": data["status"],

            }
            new_list_data.append(trainer_new)
        return_obj = {"data": new_list_data}
        return return_obj


    @classmethod
    def insert_trainer(cls, created: dict):
        _id = str(uuid4())
        create = time()
        created["created_dat"] = create
        created['id'] = _id
        insert = cls.repository.insert_one(created)
        return f'{insert} User Created'


    @classmethod
    def soft_delete_trainer(cls, id, status):
        insert = {"id": id}
        insert_status = {"status": status}
        soft = cls.repository.soft_delete(insert, insert_status)
        return soft


    @classmethod
    def update_trainer(cls, update: dict):
        query = {"id": update["id"]}
        updated_user = dict()
        updated_user.update({"name": update['name'],
                             "gender": update['gender'],
                             "age": update['age'],
                             "status": update['status']})
        update = cls.repository.update(query, updated_user )
        return update



