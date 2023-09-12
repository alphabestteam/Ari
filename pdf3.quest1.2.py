def main():
    try:
      your_first_num = int(input("Enter the first number\n"))
      print(your_first_num)
    except:
      print("Your input is not supported")

    try:
      your_second_num = int(input("Enter the second number\n"))
      print(your_second_num)
    except:
      print("Your input is not supported!")
    
    finally:
       print("Finished Running!")
   
      
if __name__ == "__main__":
   main()
