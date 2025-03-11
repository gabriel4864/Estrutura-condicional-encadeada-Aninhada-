# Bônus de um funcionário
Salario = float(input("Digite seu salario: "))
Tempo = int(input("Digite quantosanos de servico: "))
if Tempo < 1:
    print("Sem bonus")
elif Tempo >= 1 and Tempo <= 3:
    Salario_Final = (Salario * 0.05) + Salario
    print("Salario com o bonus: ", Salario_Final)
elif Tempo >= 3 and Tempo <= 5:
    Salario_Final = (Salario * 0.1) + Salario
    print("Salario com o bonus: ", Salario_Final)
else:
    Salario_Final = (Salario * 0.15) + Salario
    print("Salario com o bonus: ", Salario_Final)