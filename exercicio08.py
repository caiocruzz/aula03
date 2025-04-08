h1 = int(input("Digite a hora 1: "))
m1 = int(input("Digite a minuto 1: "))
h2 = int(input("Digite a hora 2: "))
m2 = int(input("Digite a minuto 2: "))

somaH = h1 + h2
somaM = m1 + m2
if somaM >= 59 :
    somaH = somaH +1
    somaM = somaM - 60
if somaH >=36 :
    somaH -=36
elif somaH >=24:
        somaH -=24
elif somaH >= 12:
    somaH = somaH - 12
print(somaH, somaM)