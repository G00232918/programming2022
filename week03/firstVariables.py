# messing around with variable types
# author: James Connolly

ageOfPatient = {}
age = "3"

# we need to convert the type to str so we can conate it to the message
print ("type of ageOfPatient is :" + str(type(ageOfPatient)))
print ("type of age is:" + str(type(age)))

# show how you convert a str to int and in to str
print ("you are " + str(age))
nextYear = int(age) + 1
print ("next year you will be " + str(nextYear))