#desempacotar listas

lista = ['Jociano', 'Perin', 1, 2, 3]

n1, n2, *outralista, n3 = lista

print(n1, n2, outralista, n3)
print(outralista)
print(n3)