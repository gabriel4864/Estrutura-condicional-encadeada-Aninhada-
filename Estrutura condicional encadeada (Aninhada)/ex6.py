# DESAFIO
Tipo = input("Digite sua profissão: ").upper().strip()
if Tipo in ["MILITAR", "CIENTISTA", "CIVIL", "HACKER ETICO"]:
    if Tipo == "MILITAR":
        Patente = input("Digite sua patente: ").upper().strip()
        if Patente == "GENERAL":
            print("Acesso permitido!")
        elif Patente == "SOLDADO":
            Missao = input("Está em uma missão especial? [S/N] ").upper().strip()
        if Tipo == "MILITAR" and Patente == "SOLDADO":
            if Missao == "S":
                print("Acesso permitido!")
            elif Missao == "N":
                print("Acesso negado, entre acompanhado de um supervisor")
    elif Tipo == "CIENTISTA":
        Senha1 = int(input("Digite a primeira senha: "))
        if Senha1 == 345:
            print("Primeira senha correta")
        else:
            print("Senha negada")
        Senha2 = int(input("Digite a segunda senha: "))
        if Senha2 == 456:
            print("Segunda senha correta")
        else:
            print("Senha negada")
        Senha3 = int(input("Digite a terceira senha: "))
        if Senha3 == 579:
            print("Terceira senha correta")
        else:
            print("Senha negada")
        Senha4 = int(input("Digite a quarta senha: "))
        if Senha4 == 122:
            print("Quarta senha correta")
        else:
            print("Senha negada")
        Senha5 = int(input("Digite a quinta senha: "))
        if Senha5 == 456:
            print("Quinta senha correta, acesso permitido!")
        else:
            print("Senha negada")
    elif Tipo == "CIVIL":
        Familiar = input("É familiar direto de um militar de alta patente? [S/N]").upper().strip()
        if Familiar == "S":
            print("Acesso permitido!")
        elif Familiar == "N":
            Dia = input("Qual é o dia da semana?: ").upper().strip()
        if Dia == "SEGUNDA" or Dia == "QUINTA":
            print("Acesso permitido!")
        else:
            print("Acesso negado")
    elif Tipo == "HACKER ETICO":
        Codigo = int(input("Digite o codigo de acesso: "))
        if Codigo == 54986:
            print("Acesso permitido!")
        elif Codigo != 54986:
            Acompanhante = input("Esta acompanhado por um militar de nivel superior? [S/N]").upper().strip()
        if Acompanhante == "S":
            print("Acesso permitido!")
        else:
            print("Acesso negado")