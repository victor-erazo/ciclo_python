# Funcion any y all


'''
print('Resultados de all')
print(all([True,False,True]))
print(all([3>1,True,'1'!= '']))
print(all([]))

print('Resultados de any')
print(any([True,False,True]))
print(any([3<1, False,'1' != '1']))
print(any([]))
'''

info = [ int(input()), input().split(' ') ]
print(info)

print('True' if all( list(map(lambda x: x>0, list(map(int,info[1])) )) )
and
any(list(map(lambda x: x[0] == x[1] or x[0] == '5',
list(zip(info[1],list(map(lambda x:x[-1:(len(x)+1)* -1:-1],info[1] )) )) )) )
else 'False'
)

'''
result_1 = list(map(int,info[1]))
print(result_1)

result_2 = all(list(map(lambda x: x>0, list(map(int,info[1])) )) )
print(result_2)

result_3 = any(list(map(lambda x: x[0] == x[1] or x[0] == '5',
list(zip(info[1],list(map(lambda x:x[-1:(len(x)+1)* -1:-1],info[1] )) )) )) )

result_3_1 = list(zip(info[1],list(map(lambda x:x[-1:(len(x)+1)* -1:-1],info[1] )) ))
print(result_3_1)
'''