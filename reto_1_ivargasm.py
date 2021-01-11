"""
Dada la siguiente lista [12,23,5,29,92,64]

1,Elimina el último y añadelo al principio
2, mueve el segundo elemento a la última posición
3, añade el número 14 al comienzo de la lista
4, suma todos los números de la lista y añade el resultado al final de la lista
5, combina la lista actual con la siguiente: [4,11,32]
6, elimina todos los números impares de la lista
7, ordena los números de la lista de forma ascendente
8, vacía la lista
"""

lista = [12,23,5,29,92,64]

# 1
ultimo = lista.pop()
lista.insert(0,ultimo)
print(lista)

#2
elemento2 = lista.pop(1)
lista.append(elemento2)
print(lista)

#3
lista.insert(0,14)
print(lista)

#4
suma=0
for i in lista:
    suma += i
lista.append(suma)
print(lista)

#5
lista2 = [4,11,32]
lista += lista2
print(lista)

#6
for impar in lista[:]:
    if impar%2 != 0:
        indice = lista.index(impar)
        lista.pop(indice)
print(lista)

#7
lista.sort()
print(lista)

#8
del lista[:]
print(lista) 