# testing reading a csv
# Author: James Connolly

import csv

filename = "test.csv"

with open(filename, "rt") as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")
    firstLine = True
    for line in csvReader:
        if firstLine:
           firstLine = False
           continue 
        print(line[2])
