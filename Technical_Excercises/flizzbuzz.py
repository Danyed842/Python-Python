def Flizzbuzz():
    #a function who helps to verify if a number is multiple of diferent numbers
    number = int(input("put a number(1-100): "))
    if number % 3 == 0 and number % 5 == 0:
        print("FlizzBuzz")
    elif number % 3 == 0:
        print("Flizz")
    elif number % 5 == 0:
        print("Buzz")
Flizzbuzz()