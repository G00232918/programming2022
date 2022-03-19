# testing how to show except
# Author: James Connolly

#filename = "data.txt"

import sys 

# print (sys.argv)

filename = sys.argv[1]

try:
    with open(filename)as f:
        print(f.read())
    var = 10/0

except FileNotFoundError as e:
    #print ("file does (", filename,") does not exist", sep= " ")
    print (e)
