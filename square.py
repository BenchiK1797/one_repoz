# import math
#
# def _circle(r):
#     return math.pi*r**2

# import 10.10
# array = 10.10.generateList(100)
# array = 10.10.unique(array)
# print(array, 10.10.counter(array))
import random
def generateList(size):
    array = []
    for i in range(size):
        array.append(random.randint(1,20))
        return array
def unique(array:list):
    return list(set(array))
def counter(array):
    return len(array)