# round a number
# eg 4.5 round to 4
# but 5.5 rounds to 6
# so do not use it accuracy is essential
# Author: James Connolly

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print ('{} rounded is {}'.format(numberToRound, roundedNumber))
