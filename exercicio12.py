var = 0
numero = int(input("Digite um Numero para saber a tabuada dele: "))
for i in range (1,11,1):
    var = var + 1
    calculoTabuada = numero * var
    print(f"{numero} x {i} = {calculoTabuada}")

  # resposta do professor
num = int(input("Digite um número: "))
for x in range  (1,11):
    multi = x * num
    print(f"{x} * {num} = {multi}")