# using an init program that intializes the file

filename = "count.txt"

def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))
writeNumber (0)

import os.path
filename = "count.txt"
if not os.path.isfile(filename):
    print ("File does not exist")
    #initialise file here
    WriteNumber(0)