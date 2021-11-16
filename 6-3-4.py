# Author: Nolan (AMDG) 11/15/2021
 
lst = list(input("Enter a list of numbers or letters seperated by spaces"))
numbers = list(lst)
length = len(numbers)
mid = int(length - 1)
end = int(length - 1)
choice = input("Do you want the middle or ends of your input? ")

if choice == "middle":
    print("The middle of your input is" + str(numbers[1:mid]) + '.')
if choice == "end":
    print("The end of your input is" + str(numbers[1:end]) + '.')
