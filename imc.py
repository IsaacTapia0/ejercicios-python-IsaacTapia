# Programa para calcular el Índice de Masa Corporal (IMC)

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu Índice de Masa Corporal es: {imc}")