def main():
# question number 4
    sum = 0
    for x in range(1,101):
      sum += x
    print (sum)
    
# question number 5
import math
def factorial(number):
    return math.factorial(number)

print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))

# question number 12
def prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(prime(5))
print(prime(6))
print(prime(7))
print(prime(14))
print(prime(152))
print(prime(60693))


if __name__ == "__main__":
    main()