# messing with files
# Author: James Connolly

filename = "test.txt"
with open(filename, "w+t") as f:
    f.write("Hello World")
    f.seek(0)
    data = f.readline()
    print(data)

print ("done")

#filename = "testread.txt"
#with open(fileaname, "r") as f:
#   data = f.read()
#   print(data)

with open("messingWithFiles.py") as f:
    for line in f:
        # line[:1], removes the line in between
        # print("line: ", line[:-1])
        print(line, end="")