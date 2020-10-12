def ismydigital(a): # аналог S.isdigital(), но учитывает дробные значения и знак минус
    dlin = len(a)
    i = 0
    yslovie = 1
    c1 = 0
    c2 = 0
    while (yslovie != 0) and (i != dlin):
        if (a[i] != '0') and (a[i] != '1') and (a[i] != '2') and (a[i] != '3') and (a[i] != '4') and (a[i] != '5') and (
                a[i] != '6') and (a[i] != '7') and (a[i] != '8') and (a[i] != '9') and (a[i] != '.') and (a[i] != '-'):
            yslovie = 0
        if a[i] == '.':
            c1 += 1
        if c1 > 1:
            yslovie = 0
        if a[i] == '-':
            c2 += 1
        if c2 > 1:
            yslovie = 0
        if a[0]=='.':
            yslovie = 0
        if a[dlin-1]=='.':
            yslovie = 0
        if (a[i]=='-')and(i!=0):
            yslovie = 0
        i += 1
    return yslovie

a = input("Введите градусы цельсия или фаренгейта (например, 1.1С или -25F): ")
dlin = len(a)
if a.find('C', 0, dlin)==dlin-1 and (a.find('F', 0, dlin))<0 :
    if ismydigital(a[:dlin-1])==1: #Введенное значение это число?
        b = float(a[:dlin-1])
        b = 9/5*b+32
        b = round(b,2)
        b = str(b)
        print(a, '=', b + 'F')
    else:
        print('Перед знаком С, должны быть числа')
elif a.find('C', 0, dlin)<0 and (a.find('F', 0 ,dlin))==dlin-1 :
    if ismydigital(a[:dlin-1])==1:
        b = float(a[:dlin - 1])
        b = 5/9*(b-32)
        b = round(b, 2)
        b = str(b)
        print(a,'=',b+'C')
    else:
        print('Перед знаком F, должны быть числа')
elif a.find('C', 0, dlin)>=0 and (a.find('F', 0, dlin))<0 :
    print('Градусы должны быть в конце')
elif a.find('C', 0, dlin)<0 and (a.find('F', 0, dlin))>=0:
    print('Градусы должны быть в конце')
elif a.find('C', 0, dlin)>=0 and (a.find('F', 0, dlin))>=0 :
    print('Введите либо градусы цельсия либо фаренгейты')
elif a.find('c', 0, dlin)>=0 or (a.find('f', 0, dlin))>=0 :
    print('Введите градусы c большой буквы')
else:
    print('Введите только числовое значение, а затем символ обозначающий градусы цельсия или фаренгейта')