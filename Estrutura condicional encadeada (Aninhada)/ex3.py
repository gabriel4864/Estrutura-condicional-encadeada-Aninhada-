# Índice de Massa Corporal
KG = float(input("Digite seu peso: "))
M = float(input("Digite sua altura: "))
IMC = KG / M**2.
if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
else:
    print("Obesidade")