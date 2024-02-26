n1 = int(input("digite o primeiro numero"))
sinal = input("digite o sinal: ")
n2 = int(input("digite o segundo numero: "))

if sinal == "+":
    conta = n1 + n2
elif sinal == "-":
    conta = n1 - n2
elif sinal == "*":
    conta = n1 * n2
elif sinal == "/":
    conta = n1 / n2
else:
    print("digite um sinal válido")
    
print(conta)