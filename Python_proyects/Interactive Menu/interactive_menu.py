while True:
    print(1, "calculate if a number is even or odd")
    print(2, "multiplication table of a number")
    print(3, "vowels of a word")
    print(4, "exit")
    option = int(input("choose an option (1-4): "))
    if option == 1:
        number = int(input("put a number: "))
        if number % 2 == 0:
            print("is a even")
        else:
            print("is a odd")
    elif option == 2:
        number = int(input("put a number: "))
        for n in range(1, 10+1):
            multiplication = number * n
            print(f"{number} * {n} is: {multiplication}")
    elif option == 3:
        word = input("put a word: ")
        vowels = 0
        for letter in word:
            if letter == "a":
                vowels += 1
            elif letter == "e":
                vowels += 1
            elif letter == "i":
                vowels += 1
            elif letter == "o":
                vowels += 1
            elif letter == "u":
                vowels += 1
        print(f"the amount of vowels are: {vowels}")
    elif option == 4:
        print("Goodbye")
        break