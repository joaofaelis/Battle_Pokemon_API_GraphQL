from trainer import insert_trainer
import names
from random import randint, choice


def generator(number_of_items: int):
    print("Inside generator function")
    for N in range(1, number_of_items):
        gender = choice(["Masculino", "Feminino"])
        insert_trainer(names.get_full_name(gender="male"), gender, randint(1, 80))


if __name__ == "__main__":
    generator(200)
