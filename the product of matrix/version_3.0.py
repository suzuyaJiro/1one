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


def input_value(p):
    a = []
    c = []
    i = 0
    check = [x for x in range(p[1],p[1]*p[0]+1, p[1])]
    cnt = 0
    while cnt != max(check):
        cnt += 1
        i = input()
        if cnt not in check: 
            c += [int(i)]
        else: 
            c += [int(i)]
            a += [c]
            c = [] 
    return a


def r():
    return list(map(int, (input()).split(' ')))


print('Введите значение размерности A через пробел')
ra = r()
print('Введите значение матрицы A')
a = input_value(ra)

print('Введите значение размерности B через пробел')
rb = r()
print('Введите значение матрицы B')
b = input_value(rb)


f = prz(a,b) 
if type(f) != str:
    for i in f:
        for j in i:
            print(j, end=' ')
        print()
else: print(f)


# добавлен авто ввод значений матрицы
# 22