# Demonstrate raising an exception
# This program prompts the user for a number and 
# return that number multiplied by 2
# Author: James Connolly

try:
    inputVar = input("enter a numbr: ")
    number = int(inputVar)
    if (number<0):
        raise ValueError("negative value entered")
    print ("Number multiploed by 2 is", number * 2)
except ValueError as e:
    print("please enter a number")
    print (e)