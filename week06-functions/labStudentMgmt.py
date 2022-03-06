# student management program lab
# Author: James Connolly

# Display the menu for user the options to select
def displayMenu ():
    print ("what would you like to do")
    print ("\t (a) Add a new student")
    print ("\t (v) View students")
    print ("\t (q) Quit")
    # .strip removes characters or white spaces from beginning or end of string
    choice = (input("type in one letter (a/v/q):")).strip()
    return choice

def doAdd(students):
    # function to add a new student
    currentStudent = {}
    currentStudent["name"] = input("Enter name: ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)
    
def readModules():
    # function to add the modules
    modules = []
    moduleName = (input("enter the first module name (blank to quit:")).strip()
    
    while moduleName !="":
        module = {}
        module ["name"] = moduleName
        module ["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = (input("\tEnter the next module name (blank to quit:")).strip()
        
    return modules

# this function is to the display the list of modules entered with the grade
def displayModules(modules):
    print ("\tName"     "\tGrade")
    for module in modules:
        print ("\t{}\t{}".format(module["name"], module["grade"]))

# function to show the student with the entered modules
def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

# This is to call the functions based on the chosen option
students = []
choice = displayMenu ()
while (choice != "q"):
    if choice == "a":
        doAdd (students)

    elif choice == "v":
        doView(students)

    elif choice != "q":
        print("please select a relevant letter - a, v, or q")
    choice = displayMenu ()


