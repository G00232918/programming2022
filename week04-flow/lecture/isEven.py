# Request a user to enter a number and output if the number is odd or even
# Author: James Connolly

# requesting the user to enter the number to be processed
number = int(input("please enter an integer: "))

# using the modulus calculation confirm if the number is even
if (number % 2) == 0:
    print ("{} is an even number".format (number))

# print statement if the number is an odd
else:
    print ("{} is an odd number".format (number))