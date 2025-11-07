def prz_str(y,z):
    re = 0
    for i in range(len(y)):
        re += y[i]*z[i]
    return re

        
def prz(a,b):
    re = []
    for i in a:
        t = []
        for j in range(len(b[0])):
            l = [b[c][j] for c in range(len(b))]
            t += [ prz_str(i,l) ]
        re += t
    return re


a = [
    [6,1,9],
    [-3,8,1]
]

b = [
    [-2,-3],
    [2,0],
    [5,4]
]

if len(a[0]) == len(b):
    print( prz(a,b) )
else:
    print('Условие перемножения таблиц не соблюдено')