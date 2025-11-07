def prz_str(y,z):
    return sum([y[i]*z[i] for i in range(len(y))])

        
def prz(a,b):
    if len(a[0]) == len(b):
        re = []
        for i in a:
            t = []
            for j in range(len(b[0])):
                l = [x[j] for x in b]
                t += [ prz_str(i,l) ]
            re += [t]
        return re
    else:
        return('Условие перемножения таблиц не соблюдено')


def input_value(r):
    a = []
    for _ in range(r):
        a.append(list(map(int, (input()).split(' '))))
    return a


print('Введите количество строк A')
ra = int(input())
print('Введите значение матрицы A построчно, значения строки через пробел')
a = input_value(ra)

print('Введите количество строк B')
rb = int(input())
print('Введите значение матрицы B построчно, значения строки через пробел')
b = input_value(rb)

print()
print('Ответ:')
f = prz(a,b) 
if type(f) != str:
    for i in f:
        for j in i:
            print(j, end=' ')
        print()
else: print(f)
 
# Добавлен другой формат ввода, код стал проще
