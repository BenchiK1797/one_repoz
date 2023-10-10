# from square import _circle
#
# print(_circle(10))

# import random
# array = []
# for i in range(100):
#     array.append(random.randint(1,20))
# mno = set(array)
# array1 = list(mno)
# cont = len(array1)
# print(array1,cont)

import square
array = square.generateList(100)
array = square.unique(array)
print(array, square.counter(array))

# import random
# def generateList(size):
#     array = []
#     for i in range(size):
#         array.append(random.randint(1,20))
#         return array
# def unique(array:list):
#     return list(set(array))
# def counter(array):
#     return len(array)