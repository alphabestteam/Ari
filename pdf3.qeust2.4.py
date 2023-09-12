from  person import person
def adults():
    num_of_person = int(input("Enter the num of the person\n"))
    adults= [person() for x in range(num_of_person)]
    over_18 = [person for person in adults if person.get_age() >= 18]
    
    return over_18

if __name__ == "__main__":
    x = adults()
    for i in x:
       print(i)