# version 1.0
# def prz_str(y,z):
#     re = 0
#     for i in range(len(y)):
#         re += y[i]*z[i]
#     return re

        
# def prz(a,b):
#     re = []
#     for i in a:
#         t = []
#         for j in range(len(b[0])):
#             l = [b[c][j] for c in range(len(b))]
#             t += [ prz_str(i,l) ]
#         re += t
#     return re


# a = [
#     [6,1,9],
#     [-3,8,1]
# ]

# b = [
#     [-2,-3],
#     [2,0],
#     [5,4]
# ]

# if len(a[0]) == len(b):
#     print( prz(a,b) )
# else:
#     print('Условие перемножения таблиц не соблюдено')



# # version 2.0
# def prz_str(y,z):
#     return sum([y[i]*z[i] for i in range(len(y))])

        
# def prz(a,b):
#     if len(a[0]) == len(b):
#         re = []
#         for i in a:
#             t = []
#             for j in range(len(b[0])):
#                 l = [x[j] for x in b]
#                 t += [ prz_str(i,l) ]
#             re += [t]
#         return re
#     else:
#         return('Условие перемножения таблиц не соблюдено')


# def input_value():
#     a = []
#     c = []
#     i = 0
#     while i != '-':
#         i = input()
#         if i not in {'+','-'}: 
#             c += [int(i)]
#         else: 
#             a += [c]
#             c = []
#     return a


# print('Введите значение матрицы A')
# a = input_value()
# print(a)
# print('Введите значение матрицы B')
# b = input_value()
# print(b)


# f = prz(a,b) 
# if type(f) != str:
#     for i in f:
#         for j in i:
#             print(j, end=' ')
#         print()
# else: print(f)


# # с точки зрения кода первая функция имеет меньше строк но менее читабельна и легка в понимании
# # добавлен ввод значений в терминале(чтобы ввести значение матрицы вводите значение начиная с первого элемента первой строки, если нужно перейти на следующую строку, то используйте +, если значение матрицы заполнено то используйте -)
# # рекомендации по улучшению: чтобы постоянно не использовать + для перехода к новой строке можно вначале писать размерность матрицы и ориентуриясь на эти значения в коде будет автоматическое перестроение на следующую строку



# # version 2.0
# def prz_str(y,z):
#     return sum([y[i]*z[i] for i in range(len(y))])

        
# def prz(a,b):
#     if len(a[0]) == len(b):
#         re = []
#         for i in a:
#             t = []
#             for j in range(len(b[0])):
#                 l = [x[j] for x in b]
#                 t += [ prz_str(i,l) ]
#             re += [t]
#         return re
#     else:
#         return('Условие перемножения таблиц не соблюдено')


# def input_value(p):
#     a = []
#     c = []
#     i = 0
#     check = [x for x in range(p[1],p[1]*p[0]+1, p[1])]
#     cnt = 0
#     while cnt != max(check):
#         cnt += 1
#         i = input()
#         if cnt not in check: 
#             c += [int(i)]
#         else: 
#             c += [int(i)]
#             a += [c]
#             c = [] 
#     return a


# def r():
#     return list(map(int, (input()).split(' ')))


# print('Введите значение размерности A через пробел')
# ra = r()
# print('Введите значение матрицы A')
# a = input_value(ra)

# print('Введите значение размерности B через пробел')
# rb = r()
# print('Введите значение матрицы B')
# b = input_value(rb)


# f = prz(a,b) 
# if type(f) != str:
#     for i in f:
#         for j in i:
#             print(j, end=' ')
#         print()
# else: print(f)


# # добавлен авто ввод значений матрицы



# version 2.0
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




# def f(b): return b + 1

# b = [1,2]
# print(f(1))

# check = [x for x in range(p[1],p[1]*p[0]+1, p[1])]


