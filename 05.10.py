import math

zapros1 = input("выберите необходимую фигуру или напишите  выход ")
zapros2 = input("вычислить площадь или периметр")

def sTreugolnika():
         a = int(input("введите сторону а"))
         b = int(input("введите сторону в"))
         result = (a * b)/2
         return result
print(sTreugolnika())

def sPramougolnika():
    a = int(input("введите сторону а"))
    b = int(input("введите сторону в"))
    result = a * b
    return result
print(sPramougolnika)

while True:
    zapros1 = input("выберите необходимую фигуру или напишите  выход ")
    zapros2 = input("вычислить площадь или периметр")

    if zapros1 == "треугольник" and zapros2 == "площадь":
        result = sTreugolnika()

    elif zapros1 == "прямоугольник" and zapros2 == "площадь":
        print(sPramougolnika())


# sTreugolnika = (a*b)/2
# sPramougolnika = a*b
# pPramougolnika = a+a+b+b
# sKruga = math.pi*r^2
# pKruga = 2*math.pi*r
# sTrapecii = ((a+b)*h)/2
# pTrapecii = a+b+c+d

