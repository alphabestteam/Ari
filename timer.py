import time
import math


if __name__ == "__main__":
    def calculate_time(func):
        def inner1(*args, **kwargs):
            begin = time.time() 
            func(*args, **kwargs) # here we pass to the factorial function args and kwargs arguments 
            end = time.time()
            print(f"The time running of the factorial function {end - begin}")
        return inner1
 
@calculate_time
def factorial(num): # I choose to give an example on function that calculate factorial of number.
    print(math.factorial(num))
 
factorial(10)