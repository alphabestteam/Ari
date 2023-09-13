import json
from costumer import Costumer
from product import Product
from register import Register


def to_json(data: dict, num_of_costumer: int, costumer: Costumer):
    name = costumer.name_of_costumer
    cart = [product for product in costumer.shopping_list]
    total = costumer.total_amount
    data["summery"].append({"name": name, "cart": cart, "total": total })

def main():
    registers = [Register() for _ in range(1,4)]
    user_input = int(input("to add product enter - 1, to remove - 2, to quit enter - 3, to end the shopping and start a new one enter - 4\n"))
    name = input("Pleas enter your name\n")
    client = Costumer(name)

    while user_input != 3:
        data = {"summery": []}
        num_of_costumer = 1
        if user_input == 1:
            name_of_product = input("enter the product name\n")
            price = int(input("enter the product price\n"))
            amount = int(input("enter product amount\n"))
            prod = Product(name_of_product, price, amount)
            client.add_product(prod)

        elif user_input == 2 :
            name_of_product = input("enter the product name\n")
            price = int(input("enter the price of the product\n"))
            amount = int(input("enter the product amount\n"))
            prod = Product(name_of_product, price, amount)
            client.remove_product(prod)

        elif user_input == 4:
            choose_register = int(input("Choose your register between 1 - 4\n"))
            registers[choose_register].checkout_customer(client)
            to_json(data, num_of_costumer, client)
            num_of_costumer += 1
            name = input("To start a new shopping enter you name\n")
            client = Costumer(name)
        user_input = int(input("to add product enter - 1, to remove - 2, to quit enter - 3, to end the shopping and start a new one enter - 4\n"))

    if user_input == 3:
        choose_register = int(input("Choose register between 1 - 4\n"))
        registers[choose_register].checkout_customer(client)

    for _ in range(len(registers)):
        print(registers[_])

    with open("shopping_after_running.JSON", 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    main()