# Leitor de velocidade
Velocidade = float(input("Digite a velocidade: "))
if Velocidade <= 40:
    print("Baixa velocidade")
elif Velocidade >= 41 and Velocidade <= 80:
    print("Velocidade moderada")
elif Velocidade >= 81 and Velocidade <= 120:
    print("Velocidade alta")
else:
    print("Velocidade muito alta")