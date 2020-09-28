import math
a = input("Введите 1-ую сторону: ")
a = float(a)
b = input("Введите 2-ую сторону: ")
b = float(b)
gr = input("Введите угол в градусах между этими сторонами: ")
gr = float(gr)
rad = (gr*math.pi*2)/360
c = math.sqrt(a**2+b**2-2*a*b*math.cos(rad))
print("Третья сторона равна: ", c)