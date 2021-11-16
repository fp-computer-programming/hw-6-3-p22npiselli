# Author: Nolan (AMDG) 11/15/2021

lst = list(input("Enter a list of numbers: "))
lst2 = lst.copy()
lst2.sort()

if lst == lst2:
    print("this list is sorted ")
else:
    print("this list is not sorted")
