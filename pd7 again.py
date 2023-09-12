# pdf 7

keep_going = True
sum_account = 0

the_shopping_list = []


while keep_going:
    the_option = int(
        input(
            "To add a product enter - 1, to delete a product enter  - 2, to finish the shopping enter - 3\n"
        )
    )
    in_shopping_list = False

    if the_option > 3 or the_option < 1:
        print("Enter only a number and only between 1 - 3")

    if the_option == 1:
        name = input("Enter the name of the product\n")
        cost = int(input("Enter the cost of the product\n"))
        amount = int(input("Enter the amount of a product\n"))
        sum_account += cost * amount

        for item in range(len(the_shopping_list)):
            if name in the_shopping_list[item]:
                the_shopping_list[item][name]["amount"] += amount
                in_shopping_list = True
                break

        if not in_shopping_list:
            the_shopping_list.append({name: {"cost": cost, "amount": amount}})
        print(the_shopping_list)
        print(f"Your total sum you need to pey is: {sum_account}")

    if the_option == 2 and len(the_shopping_list) != 0:
        name = input("Enter the name of the product\n")

        for item in range(len(the_shopping_list)):
            if name in the_shopping_list[item]:
                amount = int(input("Enter the amount of a product\n"))

                if the_shopping_list[item][name]["amount"] == 0:
                    del the_shopping_list[item]
                    print("Your dhopping list is empty")
                if the_shopping_list[item][name]["amount"] < 0:
                    print("You can't delete more amount then what you buy")
                the_shopping_list[item][name]["amount"] -= amount
                sum_account -= cost * amount
            else:
                print("You can't delete a product you don't buy")
        print(the_shopping_list)
        print(f"Your total sum you need to pey is: {sum_account}")

    if the_option == 3:
        keep_going = False


print(the_shopping_list)
print("Thank you have a good day!")
