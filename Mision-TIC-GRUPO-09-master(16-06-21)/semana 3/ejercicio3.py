'''
s = {1,2,3,4}
print(s)
s = {True,3.14,None,False,"Hola Python",(1,2)}
print(s)

# s = {[1,2]}

s = {}
print(type(s))

s = set()
print(type(s))

s1 = set([1,2,3,4])
s2 = set(range(10))
print(s1)
print(s2)
'''

'''
c = {1,3,2,9,3,1}
print(c)

a = set('Hola Pythonista')
print(a)

unidos = set([3,5,6,1,5])
print(unidos)
'''

'''
mi_conjunto = {1,3,2,9,3,1}
print(mi_conjunto)
for mi_c in mi_conjunto:
    print(mi_c)
'''

'''
set_mutable1 = set([4,3,11,7,5,2,1,4])
print(set_mutable1)
set_mutable1.add(22.00001)
set_mutable1.add(9)
print(set_mutable1)

set_mutable1.clear()
print(set_mutable1)

set_mutable = set([4.01,"Carro",True])
print(set_mutable)
otro_set_mutable = set_mutable.copy()
print(otro_set_mutable)
'''

'''
set_mutable1 = set([4,3,11,7,5,2,4,1])
set_mutable2 = set([11,5,9,2,4,8])

print(set_mutable1)
print(set_mutable2)

print(set_mutable1.difference(set_mutable2))
print(set_mutable2.difference(set_mutable1))
'''

'''
print({1,2,3} == {3,2,1})
print({1,2,3} == {1,2,6})
'''


'''
proyecto1 = {'python','zope2','ZODB3','pytz'}
print(proyecto1)

proyecto2 = {'python','plone','diazo'}
print(proyecto2)

proyecto1.difference_update(proyecto2)
print(proyecto1)
'''

'''
paquetes = {'python','zope','plone','django'}
print(paquetes)

paquetes.discard('django')
print(paquetes)
'''

'''
set_mutable1 = set([4,3,11,7,5,2,4,1])
set_mutable2 = set([11,5,9,2,4,8])

print(set_mutable1)
print(set_mutable2)

print(set_mutable1.intersection(set_mutable2))
print(set_mutable2.intersection(set_mutable1))
'''

'''
proyecto1 = {'python','zope2','pytz'}
print(proyecto1)

proyecto2 = {'python','plone','diazo','z3c.form'}
print(proyecto2)

proyecto3 = {'python','django','django-filter'}
print(proyecto3)

proyecto3.intersection_update(proyecto1,proyecto2)
print(proyecto3)
'''

'''
set_mutable1 = set([4,3,11,7,5,2,4,1])
set_mutable2 = set([11,5,9,2,4,8])

print(set_mutable1)
print(set_mutable2)
print(set_mutable1.isdisjoint(set_mutable2))
'''



'''
set_mutable1 = set([4,3,11,7,5,2,4,1])
set_mutable2 = set([11,5,9,2,4,8])
set_mutable3 = set([11,5,2,4])

print(set_mutable1)
print(set_mutable2)
print(set_mutable3)

print(set_mutable2.issubset(set_mutable1))
print(set_mutable3.issubset(set_mutable1))

print(set_mutable1.issuperset(set_mutable2))
print(set_mutable1.issuperset(set_mutable3))

# print(set_mutable1[:2])
'''

paquetes = {'python','zope2','pytz', 'django'}

print('valor aleatorio devuesto es : ', paquetes.pop())
print(paquetes)

paquetes.remove('django')
print(paquetes)
