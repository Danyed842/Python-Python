fruits = ["banana", "apple", "cherry", "watermelon", "pear"]
print(f"the first fruit of the list is: {fruits[0]}")
print(f"the last fruit of the list is: {fruits[-1]}")
print(f"the lenght of the list of fruits is: {len(fruits)}")
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.remove(1)
print(numbers)
aleatory_numbers = [2, 5, 9, 3, 1, 4, 10, 8, 6, 7]
print(sorted(aleatory_numbers))
print(f"the higher value in this list is: {max(aleatory_numbers)}")
print(f"the lower value in this list is: {min(aleatory_numbers)}")
coord = (10.5, 25.2, 100, 50)
for cord in coord:
    print(f"the coords are: {cord}")