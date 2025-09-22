def anagram():
    #a function who helps to know if 2 words are anagram
    word1 = input("put the 1rst word: ")
    word2 = input("put the 2nd word to verify if they are anagrams: ")
    if sorted(word1) == sorted(word2):
        print("is an anagram")
    else:
        print("isn't a anagram")
anagram()