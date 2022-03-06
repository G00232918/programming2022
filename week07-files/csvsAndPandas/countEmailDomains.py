# this script will count each email domain from
# employee.csv file
# Author : James Connolly

import csv
fileName = "employees.csv"
domainCount {}

# use longer filenames easier to read
with open(filename, "rt") as employeeFile:
    csvReader = csv.reader(employeeFile, delimiter = ",")
    firstline = True
    count = 0
    for line in csvReader:
        if firstLine:
            if firstLine = False
            continue
        email = line[8]
        start = email.find('@')
        domain = email[start+1:]
        if domain not in domainCount:
            domainCount[domain] = 0
        else:
            domainCount[domain] += 1


for key, value in domainCount.items():
    print(key, "\t\t", value)

