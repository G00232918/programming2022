# Uses a variable to greet
#Author: James Connolly

name = "James"
print ('hello' + name )

# this won't work
age = 34
#print ('Your age is' + age)
print ('your age is ' + str(age))
print ('Hello {} \tyour age is {}'.format(name, age))