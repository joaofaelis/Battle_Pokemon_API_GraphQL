# API GraphQL Pokedex e Battle
Ultima mudança nesse projeto: 04/2023 

Como primeira ideia pessoal de projeto em Python, esse projeto teve como objetivo estudar
API em graphQl e o Apollo Server. Nesse projeto foi utilizado architecture Onion e um API openSource de Busca de Pokemons e suas informações, onde é feita as requisições
dentro da mesma e realizar um CRUD dentro do banco de dados.

 #### Todas as dependências necessárias para utilização desse projeto está listado no arquivo requirements.txt dentro do SRC.
## Tecnologias:

- Python3
- GraphQL
- Banco de dados NOSQL (MongoDB) - para armazenamento de dados em documentos.
- Utilização do Decouple - para ocultação de informação de conexão ao banco de dados.

# Funcionalidades do Projeto:

## Trainers/ Pokemons:
- ### CREATE trainers:
- (NOME, GENERO E IDADE)com date_time e Unique ID (Id Unico dentro do BD).
- ### CONSULT Pokemons:
- A API utilizada realiza a busca de pokemons através de numeros (codigos dos pokemons) que vai de 1 até o limite da API permitida.
pra isso tem o endpoit de GET de pokemons, para ser feita essa pesquisa e ai sim poder ter a certeza de qual armazenar ao banco de dados.
- ### CREATE Pokemons:
- Diferente dos trainers, a criação é feita informando os numeros dos pokemons, assim a API utilizada traz e armazena as informações no BD.
- ### GET trainers/Pokemons:
-  pegar informação de trainers/pokemons dentro do BD a partir do Unique ID.
- ### SKIP LIMIT:
- forma de paginação, para pesquisar mais de um trainers/pokemons ao mesmo tempo, informando quantos voce quer pular (skip) e o limite de pesquisa (limit).
- ### SOFT DELETE:
- Uma forma de deletar da paginação, é feito um update nos status de TRUE para FALSE, para que fique de forma inativa nas pesquisas.
- ### UPDATE:
- Selecionar o trainer a partir do Unique ID, para realizar update de informações.
- ### DELETE:
- Informar o Unique ID do Trainer/Pokemon para deletar do Banco de dados.

## CAPTURE:
Capture realiza a pesquisa do pokemon a partir do numero do mesmo, se ele ja estiver no banco de dados então é realizado um update para que haja o vinculo de um trainer a um pokemon, criando um documento com a informação de ambos em uma collection separada.
 Esse documento é utilizado para realizar as batalhas de trainers e seus pokemons.

## BATTLE:
É realizado uma comparação de informações de um documento de Capture á outro Capture indicando o Unique ID de cada documento, e aquele que tiver o pokemon com a maior experiencia, vence a batalha, armazenando o log de vitoria ao banco de dados.


