# testing with OS
# Author: James Connolly

import os 
filename = "test.txt"
if os.path.exists(filename):
    print(filename, "already exists")
else:
    print(filename, "does not exist do you want do you want to create it")

os.remove(filename)