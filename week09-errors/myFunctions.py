# a module of useful functions
# Author: James Connolly

"""
functions that retrns the factorial number of an int
ie
7! = 7x6x6x5x4x3x2x1 = 5040
"""
def factorial(num):
    if num == 1:
        return 1
    factorial = 1
    num +=1
    # when the range is set to one it goes to one less than
    # selected
    for i in range(1, num):
        # print("before mult ", factorial, "by", i)
        factorial *= i
        # print("after mult ", factorial)
    return factorial

if __name__ == "__main__":
    print ("in my functions",__name__)
    assert factorial(7) == 5040





