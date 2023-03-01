import requests
# from graphql_pokemon_battle.src.infrastructures.mongo.infrastructure import MongoInfrastructure
# class PokeRepository:
#     infrastructure= MongoInfrastructure
#     db_name= "ProjetoGru"
#     collection_name= "pokemons"
# #
# infra = PokeRepository

# get = input("Codigo pokemon: ")
# api = f'https://pokeapi.co/api/v2/pokemon-form/{get}'
# list = requests.get(api)
# ret = list.json()
# print (ret)
# print(ret.keys())
# if 'pokemon' in ret:
#     print("AAAAAAAAAAAAAAAAAAAAAAAA")
# print((ret.values()))
# for chave in ret.keys():
#     print(f'Chave = {chave} e valor = {ret[chave]}')
#
# var1 = []
#
#
# new_list = {
#             "pokemon": ret ["name"],
#             "habilidade": ret ["weight"],
#             "Experiência": trainer["base_experience"],
#             # "genero": trainer["genero"],
#             # "status": trainer["status"],
#         }
# var1.append(new_list)
# return_obj = {"data": var1}
# print(return_obj)

#
# api = f'https://pokeapi.co/api/v2/pokemon/charizard'
# list = requests.get(api)
# ret = list.json()
# print (ret)
# print(ret.keys())
# print((ret.values()))
# for chave in ret.keys():
#     print(f'Chave = {chave} e valor = {ret[chave]}')
#
# var1 = []
#
#
# new_list = {
#             "pokemon": ret ["name"],
#             "peso": ret ["weight"],
#             "Experiencia": ret ["base_experience"],
#             # "genero": trainer["genero"],
#             # "status": trainer["status"],
#         }
# var1.append(new_list)
# return_obj = {"data": var1}
# print(return_obj)
#
#
# @classmethod
# def insert_poke(cls):
#     insert = cls.infra.insert_one(return_obj)
#     print("Sucesso!")


# @classmethod
# def create_trainer(cls):
#     name = input("nome: ")
#     genero = input("genero: ")
#     idade = input("idade: ")
#     objeto = {
#         "id": str(uuid4()),
#         "nome": name,
#         "genero": genero,
#         "idade": idade,
#         "created_at": datetime.now(),
#         "status": True,
#     }
#     _ = cls.repository.insert_one(objeto)
#     print("sucess!")
#
# @classmethod
# def skip_limit(cls):
#     os.system("clear")
#     limit = input("Quantos treinadores por pagina?:")
#     skip = input("Qual skip: ")
#     result = cls.repository.get_all_objects(int(skip), int(limit))
#     for dado in result:
#         print(dado)
#
# @classmethod
# def update(cls):
#     unique_id = input("Digite o id do documeto a ser alterado: ")
#     escolha = input("Alterar o [n]ome, [g]enero ou [i]dade? : ")
#     objeto = input("Digite o novo: ")
#     choice_dict = {"n": "Nome", "g": "Genero", "i": "Idade"}
#     mapping = choice_dict.get(escolha, "Nome")
#     internal_obj = {mapping: objeto}
#     query = {"Id": unique_id}
#     update = cls.repository.update(query, internal_obj)
#     print(update)
#     print(update.matched_count)
#     print(update.modified_count)
#
# @classmethod
# def soft_delete(cls):
#     _id = input("Digite o id do documento a ser apagado: ")
#     update = cls.repository.soft_delete(_id)
#     print(update)
#
# @classmethod
# def get_trainer(cls):
#     os.system("clear")
#     Id = input("Coloque o Id para pesquisa: ")
#     recebe = cls.repository.get_object(Id)
#     print(recebe)

# Daqui para baixo: Serviços para o GraphQL