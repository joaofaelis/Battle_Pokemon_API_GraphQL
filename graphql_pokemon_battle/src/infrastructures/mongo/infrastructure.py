from pymongo import MongoClient


class MongoInfrastructure:
    client = None
    uri = "mongodb://localhost:27017"

    @classmethod
    def get_client(cls):
        if cls.client is None:
            cls.client = MongoClient(cls.uri)
        return cls.client


