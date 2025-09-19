def max_of_three(num1, num2, num3):
    #function who recieve 3 values and return the higher 
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    elif num3>num1 and num3>num2:
        return num3
def palindrome(word):
    #function who recieve a word and return True if is palindrome
    if word == word[::-1]:
        print("is a palindrome")
    else:
        print("isn't a palindrome")
def factorial(number):
    #function who recieve a number and return
        factorial2 = 1
        for x in range(1, number+1):
            factorial2 *= x
        print(f"The factorial of {number} is: {factorial2}")
def convertor(celsius):
    #function who recieve celsius and convert to farenheit
    farenheit = (celsius * 1.8) + 32
    print(f"the celsius in farenheit are: {farenheit}")
def reverse_string(string):
    #function who recieve a string and reverse the string
        print(string[::-1])

