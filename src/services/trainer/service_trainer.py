from time import time
from uuid import uuid4
from src.repositories.mongo.repository_mongo import Repository_Mongo
from decouple import config

class Trainer_Service:

    repository = Repository_Mongo
    collection = config('trainers')  # Collection Mongo

    @classmethod
    def insert_trainer(cls, created_data: dict):
        _id = str(uuid4())
        time_now = time()
        created_data["created_dat"] = time_now
        created_data['unique_id'] = _id
        insert_in_db = cls.repository.insert_object(cls.collection, created_data)
        return f'{insert_in_db} User Created'

    @classmethod
    def get_id_trainer(cls, input):
        input_id = input["unique_id"]
        return_data = cls.repository.get_object(cls.collection, input_id)
        graphql_return_data = {
            "unique_id": return_data["unique_id"],
            "name_trainer": return_data["name_trainer"],
            "age": return_data["age"],
            "gender": return_data["gender"],
            "status": bool(return_data["status"]),
            "created_dat": int(return_data["created_dat"].timestamp()),
        }
        return graphql_return_data

    @classmethod
    def skip_limit_trainers(cls, skip, limit):
        repository_skip_limit = Repository_Mongo.skip_limit(cls.collection, skip, limit)
        return_skip = list(repository_skip_limit)
        final_list_pagination = []
        for trainer in return_skip:
            list_new = {
                "unique_id": trainer["unique_id"],
                "name": trainer["name"],
                "age": trainer["age"],
                "gender": trainer["gender"],
                "status": trainer["status"],
                "created_at": trainer["created_at"]
            }
            final_list_pagination.append(list_new)
        return_pagination = {"trainer": final_list_pagination}
        return return_pagination

    @classmethod
    def soft_delete_trainer(cls, unique_id, status):
        insert_id = {"unique_id": unique_id}
        insert_status = {"status": status}
        soft = cls.repository.update_object(cls.collection, insert_id, insert_status)
        return soft

    @classmethod
    def update_trainer(cls, update: dict):
        query = {"unique_id": update["unique_id"]}
        updated_user = dict()
        updated_user.update({"name": update['name'],
                             "gender": update['gender'],
                             "age": update['age'],
                             "status": update['status']})
        update = cls.repository.update_object(cls.collection, query, updated_user)
        return update



