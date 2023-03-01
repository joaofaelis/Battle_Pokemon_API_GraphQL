from random import randint
import names
from pymongo import MongoClient
import os
from uuid import uuid4
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client["ProjetoCRUD"]


def insert_trainer(name, genero, idade):
    bd = db.trainers.insert_one(
        {
            "id": str(uuid4()),
            "name": name,
            "gender": genero,
            "age": idade,
            "created_dat": datetime.now(),
            "status": True,
        }
    )


# caracteres_permitidos = "i,I,l,L,a,A,U,u"
# print("Criação de treinador")
#
# while True:
#     if __name__ == "__main__":
#         option_start = input("[I]nserir, [L]istar, [A]pagar [U]pdate: ")
#
#     if option_start not in caracteres_permitidos:
#         print("Coloque uma letra permitida.")
#         continue
#
#     if option_start == "i" or option_start == "I":
#         name = input("Nome: ")
#         genero = input("Genero: ")
#         idade = input("Idade: ")
#         bd = db.Trainer.insert_one(
#             {
#                 "Id": str(uuid4()),
#                 "Nome": name,
#                 "Genero": genero,
#                 "Idade": idade,
#                 "created_at": datetime.now(),
#                 "status": "ativo",
#             }
#         )
#
#     elif option_start in ["l", "L"]:
#         os.system("clear")
#         limit = input("Quantos treinadores por pagina?:")
#         skip = input("Qual skip: ")
#         resultado = db.Trainer.find().skip(int(skip)).limit(int(limit))
#         for dado in resultado:
#             print(dado)
#
#     elif option_start in ["a", "A"]:
#         _id = input("Digite o id do documento a ser apagado: ")
#         update_obj = {"$set": {"status": "Inativo"}}
#         query = {"Id": _id}
#         update = db.Trainer.update_one(query, update_obj, upsert=False)
#
#     # #TODO soft delete
#     # delete = db.Trainer.delete_one({"Id": _id})
#
#     elif option_start == "u" or option_start == "U":
#         unique_id = input("Digite o id do documeto a ser alterado: ")
#         escolha = input("Alterar o [n]ome, [g]enero ou [i]dade? : ")
#         objeto = input("Digite o novo: ")
#         choice_dict = {"n": "Nome", "g": "Genero", "i": "Idade"}
#
#         mapping = choice_dict.get(escolha, "Nome")
#         update_obj = {"$set": {mapping: objeto}}
#         query = {"Id": unique_id}
#         update = db.Trainer.update_one(query, update_obj, upsert=False)
#         print(update)
#         print(update.matched_count)
#         print(update.modified_count)
