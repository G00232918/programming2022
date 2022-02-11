# This program reads numbers until the user enters a 0
# it sill then print them back out again and their average

numbers = []

# enter the first numberand check if not 0 in the while loop
number = int(input("enter a number(0 is to quit): "))
while number != 0:
    numbers.append(number)

# read the next number and check if 0
    number = int(input("enter more numbers(0 is to quit): "))

# print out the values
for value in numbers:
    print (value)

# average to be a float
average = float(sum(numbers))/len(numbers)
print("The average of the set of numbers is {}".format(average))


