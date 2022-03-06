# Lab for testing types
#

# list of 5 variables
i = 3
fl = 3.5
isa = True
memo = "how now brown cow"
lots = [] 

# check for the type of variables listed above
print ("type of variable I is" + str(type(i)))
print ("type of variable fl is" + str(type(fl)))
print ("type of variable True is" + str(type(True)))
print ("type of variable memp is" + str(type(memo))) 
print ("type of variable lots is" + str(type(lots)))

# alternative method
print ("varable {} is of type: {} and value: {}" .format("i", type (i), i))
print ("varable {} is of type: {} and value: {}" .format("fl", type (fl), fl))
print ("varable {} is of type: {} and value: {}" .format("isa", type (isa), isa))
print ("varable {} is of type: {} and value: {}" .format("memo", type (memo), memo))
print ("varable {} is of type: {} and value: {}" .format("lots", type (lots), lots))
