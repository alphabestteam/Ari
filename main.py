from costumer import Costumer
from product import Product
from register import Register

def main():
    registers = [Register() for _ in range(1,4)]
    user_input = int(input("to add product enter - 1, to remove - 2, to quit enter - 3, to end the shopping and start a new one enter - 4\n"))
    name = input("Pleas enter your name\n")
    client = Costumer(name)

    while user_input != 3:
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
            name = input("To start a new shopping enter you name\n")
            client = Costumer(name)
        user_input = int(input("to add product enter - 1, to remove - 2, to quit enter - 3, to end the shopping and start a new one enter - 4\n"))

    if user_input == 3:
        choose_register = int(input("Choose register between 1 - 4\n"))
        registers[choose_register].checkout_customer(client)

    for _ in range(len(registers)):
        print(registers[_])

if __name__ == '__main__':
    main()