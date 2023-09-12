from costumer import Costumer

class Register:
    num_costumers = 0
    def __init__(self):
        self._profit_amount = 0
        self._sales_list ={}

    def __str__(self):
        return f'profit amount: {self.profit_amount}, sales list: {self.sales_list}'
    
    @property
    def profit_amount(self):
        return self._profit_amount
    
    @property
    def sales_list(self):
        return self._sales_list
    
    def checkout_customer(self, new_costumer:Costumer):
        Register.num_costumers += 1
        self._profit_amount += new_costumer._total_amount
        self.sales_list.update({Register.num_costumers: {"name of the costumer":new_costumer.name_of_costumer,"total price":new_costumer.total_amount}})