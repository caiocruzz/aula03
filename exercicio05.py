nota1= float(input("Digite a nota do aluno: "))
nota2= float(input("Digite a nota do aluno: "))
nota3= float(input("Digite a nota do aluno: "))
calculoMedia= (nota1+nota2+nota3) / 3
media= 7.0
if calculoMedia >= media :
    print(f"Aluno aprovado com média: {calculoMedia}")
else:
 if calculoMedia<=4 :
    print(f"Aluno em recuperação")
 else:
    print(f"Aluno reprovado com média: {calculoMedia}")