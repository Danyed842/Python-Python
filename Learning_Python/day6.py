age = int(input("put your age to verify if you can enter to the discotect: "))
if age <= 18:
    print("you can't go to the discotect")
else:
    print("you can go to the discotect")
print("------")
number = int(input("put a number to verify if is positive, negative or zero: "))
if number == 0:
    print("is zero")
elif number < 0:
    print("is negative")
else:
    print("is positive")
print("------")
grade = int(input("put a grade(0-100): "))
if grade >= 90:
    print("A")
elif grade >= 80 and grade <= 89:
    print("B")
elif grade >= 70 and grade <= 79:
    print("C")
elif grade >= 60 and grade <= 69:
    print("D")
else:
    print("F")
print("------")
income = int(input("put your salary to calculate your taxes: "))
if income <= 1000000:
    print("exempt")
elif income >= 1000000 <= 3000000:
    print("low tax")
elif income >= 3000000 <= 6000000:
    print("mid tax")
else:
    print("high tax") 
print("------")
user = "admin"
password = "1234"
trys = 3
while True:
    user_try = input(f"put the correct username({trys} trys left): ")
    password_try = input(f"put the correct password({trys} trys left): ")
    if user_try != user:
        trys -= 1
        if trys <= 0:
            print("Blocked")
            break
    elif password_try != password:
        trys -= 1
    else: 
        print("¡Welcome!")
        break
print("------")
print("let's play rock paper scissors shoot.")
print(1, "paper")
print(2, "rock")
print(3, "scissors")
import random
computer = random.randint(1, 3)
choose = int(input("what do you choose?: "))
if computer == 2 and choose == 1:
    print("you win")
elif computer == 1 and choose == 3:
    print("you win")
elif computer == 3 and choose == 2:
    print("you win")
elif computer == 1 and choose == 1:
    print("draw")
elif computer == 2 and choose == 2:
    print("draw")
elif computer == 3 and choose == 3:
    print("draw")
else:
    print("computer win")