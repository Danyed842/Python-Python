print("numbers 1-10:")
for i in range(1, 10+1):
    print(i)
print("------")
print("even numbers in 1-20:")
for i in range(1, 20+1):
    if i % 2 != 0:
        continue
    print(i)
print("------")
number = int(input("put a number: "))
add = 0
for n in range(1, number+1):
    add += n
print(f"the addition of the first {number} natural numbers is: {add}")
print("------")
word = input("put a word: ")
print("the letters of the word on separate lines: ")
for letter in word:
    print(letter)
print("------")
number = int(input("put a number to make her multiplication table: "))
for n in range(1, 10+1):
    multiplication = number * n
    print(f"{number} * {n}: {multiplication}")
print("------")
import random
num = random.randint(1, 100)
while True: 
 number = int(input("guess the number 1-100: "))
 if number == num:
     print("¡You win!")
     break
 elif number < num:
     print("too lower, try higher")
 elif number > num:
     print("too higher, try lower")
print("------")
trys = 3
password = "python123"
while True:
    password2 = input(f"put the password({trys} trys left): ")
    if password2 == password:
        print("the password are right")
        break
    else:
        trys -= 1
        if trys == 0:
            print("you have no more attempts")
            break
    
    