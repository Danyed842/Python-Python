def calculator():
    #a function to do diferent oppers with 2 numbers
    num1 = int(input("Put a number to opper: "))
    opper = input("put an opperation (+, -, *, /): ")
    num2 = int(input("Put another number to opper: "))
    if opper == "+":
        print(num1 + num2)
    elif opper == "-":
        print(num1 - num2)
    elif opper == "*":
        print(num1 * num2)
    elif opper == "/":
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("can't divide by 0.")
    else:
        print("it isn't a opperation.")
def cop_to_usd():
    #a function who helps to convert cop to dollars
    cop = int(input("put a amount of cop(pesos colombianos): "))
    dollar = 4000
    usd = cop // dollar
    print(f"this amount of cop in usd is: {usd} usd.")
def to_100_years():
    #a function who helps what would be your age in 100 years
    age = int(input("put your age: "))
    hundred_years = age + 100
    print(f"in 100 years you would have {hundred_years}")