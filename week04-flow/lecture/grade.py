# program that readsa students percentage mark and
# print out grade

percentage = float(input("Please enter the percentage you attained: "))
# print percentage

if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100")

# list of results depending on percentage

if percentage <40:
    print ("fail")

elif percentage < 40:
    print ("pass")

elif percentage < 50:
    print ("Merit 2")

elif percentage < 60:
    print ("Merit 1")
    
elif percentage > 70:
    print ("Distinction")

