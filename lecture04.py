f = open('simple_numbers.txt', 'w')
n = input('Введите целое число n: ')
if n.isdigit():
    n = int(n)
    m = list(range(0, n+1)) #"Массив" от 0 до n, где индексы соответствуют значениям
    i = 2 #Начинаем со 2-ого элемента т.к это самое первое простое число
    while i<=n:
        j = i*i #Номер, с которого начинаем зачеркивать (с i^2 до n)
        while j <= n: #Цикл для зачеркивания. Если элемент = 0, то он зачеркнут.
            if (m[i]!=0)and(m[j]!=0)and(m[i] != m[j])and(m[j] % m[i]==0): #(Если элемент i или j не зачеркнут)(Если элементы друг другу не равны)(Если элемент j кратен эелементу i)
                m[j]=0 #Зачеркиваем
            j += 1
        if m[i] !=0:#Если элемент не зачеркнут
            f.write(str(m[i])+'\n')#Записываем в файл
        i+=1
else:
    print('Это не целое число')
try:
    pass
finally:
    f.close()
