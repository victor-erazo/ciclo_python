con_doble_asterisco = lambda ** variable : variable['a']

'''
dicc = {'a': 12}
print(con_doble_asterisco(** dicc))
'''

dicccionario = {'a':12,'b':3,'c':18}
con_doble_asterisco = lambda ** dic_args : sum(dic_args.values())

print(con_doble_asterisco(** dicccionario))