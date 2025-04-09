### Escreva um algoritmo 10 números e ao final da leitura escrever a soma total dos 10 numeros
soma=0
for x in range (10):
    numero = int(input("Escreva 10 numeros: "))
    soma = soma + numero
print(soma)