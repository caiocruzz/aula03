nome= input("Insira seu nome: ")
idade= int(input("Qual sua idade ? "))
salario= float(input("Quanto voce recebe? "))
aumentoSalarial= float(input("Quanto voce recebeu de aumento? "))
valorReal = (aumentoSalarial * salario)/100
salarioAtual = salario + valorReal

print(f"Meu nome é: {nome}  Minha idade é: {idade} Meu salário é {salario}\n"
      f"e seu sálario é R${salario:.2f} e você recebeu\n"
      f"R${valorReal:.2f} de aumento e seu novo salário"
      f"é R${salarioAtual:.2f}")



