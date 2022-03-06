# program that reads in two numbers and 
# output the integer answer and remainder
# Author: James Connolly

x = int(input("Enter first number: "))
y = int(input("Enter the number you want yo divide by:"))
answer= int(x/y) # // gives the division
remainder = x%y # % gives the remainder

print ("{} divided by {} is {} with remainder {}".format ( x, y, answer, remainder))

