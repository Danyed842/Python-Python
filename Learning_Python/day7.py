numbers = [50, 200, 100, 30, 20]
print(f"the sum of the list is: {sum(numbers)}")
print("------")
numbers = [1, 1, 2, 2, 3, 3, 4, 4]
print(f"The list without duplicates: {set(numbers)}")
print("------")
words = [ ]
word1 = input("put a word: ")
word2 = input("put another word: ")
word3 = input("put another word: ")
word4 = input("put another word: ")
word5 = input("put a last word: ")
words.append(word1)
words.append(word2)
words.append(word3)
words.append(word4)
words.append(word5)
for word in (words):
    cant_letters = len(word)
    larger_word = max(words)
print(f"the word with more letters have: {cant_letters} letters and the word are:{larger_word}")
print("------")
students = {"David": 3.4,
            "Jose": 3.9,
            "Joshua": 4.2
}
for name, grade in students.items():
    print(f"The name of the student is: {name} and the grade is: {grade}")
prom = sum(students.values()) / len(students)
print(prom)
print("------")
inventory = {

}
while True:
    print(1, "add products")
    print(2, "update quantity")
    print(3, "show inventory")
    print(4, "exit")
    option = int(input("choose an option: "))
    if option == 1:
        product = input("put the name of the product: ")
        quantity = int(input("put the quantity of products: "))
        inventory[product] = quantity
    elif option == 2:
        quantity = int(input("put the quantity of products: "))
        inventory[product] = quantity
    elif option == 3:
        print(inventory)
    elif option == 4:
        print("goodbye")
        break
    else:
        print("isn't a valide option")