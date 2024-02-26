#OBTENDO O QUADRADO DE CADA NÚMERO



x = [1,2,3,4,5]
y = [i**2 for i in x] # valor = i**/  #laço = for i in x
print (y)
#saída: [1, 4, 9, 16, 25] 


#####################################
#adicionando apenas os numeros impares de x
x = [1,2,3,4,5]
z = [i for i in x if i%2==1]
print(z)
#saida: [1,3,5]



#A list comprehension é uma poderosa ferramenta oferecida pela linguagem de programação 
# Python que permite criar listas de forma concisa e eficiente. 
# Com ela, é possível realizar operações em uma única linha de código, 
# evitando a necessidade de utilizar loops tradicionais.

# valor = i**2 
#laço = for i in x
# condição if i%2==1