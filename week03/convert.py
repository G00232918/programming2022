# A program that takes in a float amount of dollars and 
# returns that absolute amount in cent
# Author: James Connolly

# Setup the variable to show what is needed
amount = float(input("amount of dollars to return in cents: "))

# The calculation for cents
absoluteValueInCents = abs(amount*100)

# Formula to calculate the amount of cents and how the results show
print ("amount in dollars {} converts into {} cents".format(amount, absoluteValueInCents))

