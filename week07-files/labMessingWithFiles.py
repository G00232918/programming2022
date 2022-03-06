# a program that counts how many times it runs

filename = "count.txt"

def readNumber():
    with open(filename) as f:
        # read the integer from the text file created
        number = int(f.read())
        return number

num =readNumber()
print (num)

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

writeNumber(3)

# main program
num = readNumber()
num += 1
print ("you have run this program {}".format (num))
writeNumber(num)