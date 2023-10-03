# def delSecondElement(array:list):
#
#     return  array[::2]# по умолчанию [начало листа:конец листа:шаг]
# print(delSecondElement([1,2,3,4,5,6,7,8,9]))

# def fibonachi(n):
#     if n==0 or n==1:
#         return  n
#     print(fibonachi(n-1)+fibonachi(n-2))
#     return fibonachi(n-1)+fibonachi(n-2)
# print(fibonachi(7))


# def vozvrat(n):
#     if n==-2 or n==-3:
#         return n
#     print(vozvrat(n-2) + vozvrat(n-1))
#     return vozvrat(n-2)+vozvrat(n-1)
# print(vozvrat(1))


import math
a = int(input("ведите количество скторов"))
r = int(input("задайте радиус круга"))
def ploshadSect():
    ploshad = (math.pi*r**2)/a
    return ploshad
print(ploshadSect())

