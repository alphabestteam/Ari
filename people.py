class People:

    def __init__(self):
       self._list_people = []
    
    def add_person(self, name):
            self._list_people.append(name)
    
    def __iter__(self):
         self.index = 0
         return self

    def __next__(self):
        if self.index < len(self._list_people):
            person = self._list_people[self.index]
            del self._list_people[0]
            return person
        else:
           raise StopIteration

    
        
if __name__ == "__main__":
        p1 = People()
        p1.add_person("Ari")
        p1.add_person("Yael")
        p1.add_person("David")
        # print(p1._list_people)
        iter = iter(p1)
        for name in p1:
            print(name)         


