import random 
class person:
    def __init__(self):
        name_list =random.choice(["Ari", "Daniel", "Yalushka", "Hen", "Yhuda", "David", "Ezra", "Hadas", "michi", "Adi"])
        age_list = random.choice([11, 22, 33, 44, 55, 66, 77, 88, 99, 15])
        id_list = random.choice([123456789, 987654321, 212121121, 234987561, 192837465, 99999999, 111111111, 222222222, 444444444, 555555555])

        self.name = name_list
        self.age = age_list
        self.id = id_list

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name 

    def get_age(self):
        return self.age
    def set_name(self, age):
        self.age = age 
    
    def get_id(self):
        return self.id
    def set_id(self, id):
        self.id = id

    
    def __str__(self):
        return f"{self.name} {self.age} {self.id}"