def even_or_odd():
    #this function ask for a number and check if is a even or odd
    number = int(input("put a number to verify if is even or odd: "))
    if number % 2 == 0:
        print("is a even.")
    else:
        print("is a odd.")
def vowels():
    #this function helps to count how many vowels has the word
    word = input("put a word: ")
    vowels = 0
    for letter in word:
        if letter == "a":
            vowels += 1
        elif letter == "e":
            vowels += 1
        elif letter == "o":
            vowels += 1
        elif letter == "i":
            vowels += 1
        elif letter == "u":
            vowels += 1
        print(f"the amount of vowels are: {vowels}")
def FlizzBuzz():
    #function who helps to verify if a number is a multiple of diferent numbers
    for n in range(1, 50+1):
        if n % 3 == 0 and n % 5 == 0:
            print("FlizzBuzz")
        elif n % 3 == 0:
            print("Flizz")
        elif n % 5 == 0:
            print("Buzz")
    print(n)
def prime():
    #function who helps to verify if a number is a prime or not
    number = int(input("put a number: "))
    dividers = 0
    for divider in range(1, number+1):
        if number % divider == 0:
            dividers += 1
    if dividers == 2:
        print("is a prime")
    else:
        print("isn't a prime")
def multiplication_table():
    #function who make the multiplication table of the number who the user puts
    number = int(input("put a number to make a multiplication table: "))
    for n in range(1, 10+1):
        multiplication = number * n
        print(f"{number} * {n} is : {multiplication}")
