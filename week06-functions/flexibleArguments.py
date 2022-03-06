# flexible arguments
# Author: James Connolly

# print ("hi", 55, 343, [], {}, sep=":")

# * reflects a tuple

def flex1(*args):
    print (type(args))
    for x in args:
        print (x)


#flex1(1,2,3,"hi", [])

# keyword arguments
# ** reflects as a list
def flex2(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} is {value}")

# flex2(age = 23, title= "hi")

def ave(*args):
    sumofNumbers = sum(args)
    lenght = len(args)
    return sumofNumbers/lenght, sumofNumbers

average , sumof = ave(3,4,5,6)
print("average is", average, "sums is", sumof)
