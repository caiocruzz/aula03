# DOIS TIMES, QUEM VENCEU DE ACORDO COM O SALDO DE GOLS
timeCasa= input("Digite o nome do time")
timeCasaGol= int(input(f"Quantos gols o {timeCasa} fez?: "))
timeFora= input("Digite o nome do time")
timeForaGol= int(input(f"Quantos gols o {timeFora} fez?: "))
if timeCasaGol == timeForaGol:
    print("EMPATE")
else:
    if timeCasaGol>timeForaGol:
     print(f"{timeCasa} Vencedor")
    else:
        print(f"{timeFora} Vencedor")