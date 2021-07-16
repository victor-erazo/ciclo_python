'''
t = 'a','b','c','d','e'
print(type(t))
print(t)

t = ('es una cadena','a','b','c')
print(t)
print(t[0])
'''

'''
t = ('a')
print(type(t))
t = ('a',)
print(type(t))

t = tuple('lupines')
print(t)

print(t[3:6])

# t[0] = 'J'
t = ('J',) + t[1:]
print(t)
'''
# print((0,1,2) < (0,3,4))
# print((0,1,200000) < (0,3,4))

txt = 'but soft what light in yonder windows breaks'
palabra = txt.split()
# print(palabra)
l = list() # forma alternativa lista = [] 
# Creamos un ciclo
for subcadena in palabra:
    l.append((len(subcadena),subcadena))

# print(l)
l.sort(reverse=True)
print(l)

res = list()
res_l = list()

for longitud,palabra_f in l:
    res.append(palabra_f)
    res_l.append(longitud)
    # res.append(len(palabra))

print(res)
print(res_l)

