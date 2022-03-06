import json
filename="testdict.json"
sample= dict(name="John", age=30, city="NewYork")

def writeDict(obj):
    with open(filename, "wt") as f:
        json.dump(obj,f)


writeDict(sample)

def readDict():
    with open(filename) as f:
        return json.load

someDict = readDict()
print(someDict)