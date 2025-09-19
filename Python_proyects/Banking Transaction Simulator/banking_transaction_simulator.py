salary = 1000000
while True:
    print(1, "check balance")
    print(2, "deposit")
    print(3, "withdraw")
    print(4, "exit")
    option = int(input("put a number to choose: "))
    if option == 1:
        print(salary)
    elif option == 2:
        deposit = int(input("put the number of money that you want to deposit: "))
        print("¡the money was deposited!")
        salary += deposit
    elif option == 3:
        withdraw = int(input("put the number of money that you want to withdraw: "))
        if withdraw <= salary:
            print("money withdrawed")
            salary -= withdraw
        else:
            print("no enought money")
    elif option == 4:
        print("Goodbye")
        break
