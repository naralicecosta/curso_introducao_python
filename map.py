# pegar uma função e aplicar a todos elementos de uma lista

def dobro(x):
    return x*2
valor = [1, 3, 4, 4, 5]

valor_dobrado = (map(dobro, valor)) #recebe dois argumentos, o primeiro a função que quer chamar e o segundo é a lista que quero aplicar

valor_dobrado = list(valor_dobrado) #convertendo o resultado em uma lista
print(valor_dobrado)

#saida: [2, 4, 6, 8,10]