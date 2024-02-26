lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$2,00", "R$5,00", "nao tem preço", "nao tem preço", "nao tem preço"]
#quero imprimir esses dois valores concatenando uma lista na outra

for numero, nome in zip(lista1, lista2):
    print(numero, nome, valor)
    """
    saida: 1 abacate R$2,00
           2 bola R$5,00
           3 cachorro nao tem preço
           4 dinheiro nao tem preço
           5 elefante nao tem preço
    
    """