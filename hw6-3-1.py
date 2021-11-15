# Author: Nolan (AMDG) 11/15/2021

w1 = list(input("Enter a word: "))
w2 = list(input("Enter a word: "))

w1.sort()
w2.sort()

if w1 == w2:
    print("These words are anagrams")
else:
    print("These words are not anagrams")