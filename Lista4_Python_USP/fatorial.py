""" Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída. """

""" n=int(input('Digite um número'))
cont=1
for n in range (n, 0, -1):
    cont*=n-1

print('O fatorial de ', n,'é',cont) """

n=int(input('Digite um número'))
cont=n
while n >= cont:
    n=n-1
    print(n*(n-1))