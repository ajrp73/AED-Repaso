L0=[10, 2.0, True, 30, 40, ['A', 'B', 'C']]
L1_enteros= [L0[0]]
L1_enteros.extend(L0[3:5])
print("L1_enteros:", L1_enteros)


L2 =  list(L1_enteros)

L2.append(L0[5])

print("L1_enteros:", L1_enteros)
print("L2:", L2)

L2.extend(L0[5])
print("L2:", L2)
L2 = L2 + ['D', 'E', 'F']
print("L2:", L2)

L3= [10, 30, 40, ['A', 'B', 'C']]

print("Rango sublista:", L3[3][1:3])

L3= [i for i in range(10)]

L4= sorted(L3, reverse=True) #sorted ordena la lista sin modificarla (devuelve una nueva)
L5= sorted(L4)
print("L3:", L3)
print("L4:", L4)
print("L5:", L5)

L4.sort() #sort ordena la lista modificándola
print("L4:", L4)

L4.reverse() #de la vuelta a la lista modificándola
print("L4:", L4)

L6= list(reversed(L4))
print("L4:", L4)
print("L6:", L6)

print("L6:", L6[:-1])

print("L6:", L6[-1::-1])

dicc = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú': 'u'}
print("claves: ", dicc.keys())
print("valores: ", dicc.values())

print(dicc.get('á'))

for k, v in dicc.items():
    if v == 'i':
        print("clave", k)

print(dicc['í'])

def esPalindromo(cadena):
    cadSinEspacios= cad.replace(' ', '')
    cadSinTildes=''
    for c in cadSinEspacios:
        cadSinTildes += dicc.get(c, c)

    return cadSinTildes == cadSinTildes[::-1]
    
cad='ánita lava la tina'
print(f"es palindromo {cad}: {esPalindromo(cad)}")

