# Programa para calcular el Índice de Masa Corporal (IMC)

def obtener_clasificacion(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("=== Calculadora de IMC ===\n")

    try:
        peso = float(input("Ingresa tu peso en kilogramos: "))
        altura = float(input("Ingresa tu altura en metros: "))

        if peso <= 0:
            print("Error: El peso debe ser un valor positivo.")
            return

        if altura <= 0:
            print("Error: La altura debe ser un valor positivo.")
            return

        imc = peso / (altura ** 2)
        clasificacion = obtener_clasificacion(imc)

        print(f"\nResultados:")
        print(f"  Peso: {peso} kg")
        print(f"  Altura: {altura} m")
        print(f"  IMC: {imc:.2f}")
        print(f"  Clasificación: {clasificacion}")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
