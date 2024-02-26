#recebe uma lista e retorna um única valor a essa lista
#ex de uso: obter a soma dos valores dos elementos de uma lista
from functools import reduce

def soma(x, y):
    return x+y
lista = [1, 3,5,10, 20] #quero obter a soma de todos os valores dessa lista

soma = reduce(soma, lista)
print(soma)
#saida: 39