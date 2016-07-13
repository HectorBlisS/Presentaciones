from random import sample

# Le pido al usuario un numero de elemntos
n = int(input('Dame un numero de elementos: '))

#Genero mi lista y la desordeno
lista = range(n)
lista = sample(lista,n)
print(lista)

#comenzar la comparacion
num = len(lista)
for i in range(num):
	for j in range(num):
		if lista[i]<lista[j]:
			tmp = lista[i]
			lista[i] = lista[j]
			lista[j] = tmp
# imprimo la lista ya ordenada
print(lista)




