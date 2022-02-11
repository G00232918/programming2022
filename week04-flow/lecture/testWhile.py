#testing with while loops
# Author: James Connoly

# while conditions
#   statements

# counter controlled examples
count = 0 
while count < 10:
    print(count)
    count += 1

count = 10 
while count >= 0:
    print(count)
    count -= 1
print ("blast off")

# sentinel controlled examples
val = input("enter something (q to quit):")
while val != 'q':
    print("you said: ")
    val = input("q to quit):")
print ("goodbye")

