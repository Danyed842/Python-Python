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
print(f"the word with more letters have: {cant_letters} letters")