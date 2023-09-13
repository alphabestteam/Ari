class Point:

    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    def __eq__(self, point:object) -> bool:
        return f"the compare of two value of x is {p1._x == point._x} and the compare between y value is {p2._y == point._y}"
    
    def __str__(self, ) -> str:
        return f"x_value:{self._x} ,y_value:{self._y}" 
    
    def __add__(self, point) -> int:
        return f"add the two values of x will give us {self._x + point._x}\nthe add of y value will give {self._y + point._y}" 

if __name__ == "__main__":
    p1 = Point(x = 2, y = 4)
    p2 = Point(x = 2, y = 4)

    print(p1 == p2)
    print(p1, p2)
    print(p1 + p2)


#5.c
    # print(p1 == p2) its not working because he dont know how to compare tow objects.
    # print(p1, p2) it will print something the human not able to read. 
    # print(p1 + p2) its not working because he dont know how to add tow objects.
#5.d
    # to fix it we need to use the correct method - to compare: __eq__ method, to print: __str__ method, to add: __add__ method
