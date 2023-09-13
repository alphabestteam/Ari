
from product import Product

def exist_product(name_of_product,shopping_list:dict):
    if name_of_product in shopping_list:
        return True
    return False

def print_item(shopping_list:dict):
    for product in shopping_list:
        print(product)

class Costumer:
    def __init__(self,name_of_costumer):
        self._name_of_costumer = name_of_costumer
        self._shopping_list = {}
        self._total_amount = 0

    def _str_(self) -> str:
        return f'name : {self._name_of_costumer}, shopping list : {self._shopping_list}, purchase amount : {self._purchase_amount}'
    
    @property
    def name_of_costumer(self):
        return self._name_of_costumer
    
    @property
    def shopping_list(self):
        return self._shopping_list
    
    @property
    def total_amount(self):
        return self._total_amount

    
    @name_of_costumer.setter
    def name_of_costumer(self,new_name_of_costumer:str):
        self._name_of_costumer = new_name_of_costumer

    @total_amount.setter
    def total_amount(self,new_total_amount:int):
        self._total_amount = new_total_amount

    def add_product(self,new_product:Product):
        if exist_product(new_product.name_of_product,self.shopping_list):
            self._shopping_list[new_product.name_of_product].amount = new_product.amount
            self._shopping_list[new_product.name_of_product].total_price = new_product.amount * self._shopping_list[new_product.name_of_product].price
            self._total_amount += new_product.amount * self._shopping_list[new_product.name_of_product].price
        else:
            self._shopping_list[new_product.name_of_product]= new_product
            self._total_amount += new_product.total_price

    def remove_product(self,new_product:Product):
        if exist_product(new_product.name_of_product,self.shopping_list):
            if new_product.amount >= self._shopping_list[new_product.name_of_product].amount:
                self._total_amount -= self._shopping_list[new_product.name_of_product].amount * self._shopping_list[new_product.name_of_product].price
                self._shopping_list.pop(new_product.name_of_product)
            else:
                self._shopping_list[new_product.name_of_product].amount =-new_product.amount
                self._shopping_list[new_product.name_of_product].total_price =-(new_product.amount * self._shopping_list[new_product.name_of_product].price)
                self._total_amount -= new_product.amount * self._shopping_list[new_product.name_of_product].price
        else:
            print("you can't remove item that you don't buy")
    
   