while True:
    print(1, "add")
    print(2, "subtract")
    print(3, "multiply")
    print(4, "split")
    print(5, "exit")
    option = int(input("choose an option: "))
    if option == 1:
        num1 = int(input("put a nomber to add: "))
        num2 = int(input("put another number to add: "))
        print(num1 + num2)
    elif option == 2:
        num1 = int(input("put a number to subtract: "))
        num2 = int(input("put another number to subtract: "))
        print(num1 - num2)
    elif option == 3:
        num1 = int(input("put a number to mulltiply: "))
        num2 = int(input("put another number to multiply: "))
        print(num1 * num2)
    elif option == 4:
        num1 = int(input("put a number to split: "))
        num2 = int(input("put another number to split: "))
        try:
            num1 / num2
            print(num1 / num2)
        except ZeroDivisionError:
            print("isn't able to split by 0")
    elif option == 5:
        print("Goodbye")
        break 