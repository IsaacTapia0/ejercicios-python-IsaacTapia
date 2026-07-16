# Programa para calcular el promedio de tres números

def main():
    print("=== Calculadora de Promedio ===\n")

    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        num3 = float(input("Ingresa el tercer número: "))

        promedio = (num1 + num2 + num3) / 3
        suma = num1 + num2 + num3

        print(f"\nResultados:")
        print(f"  Números ingresados: {num1}, {num2}, {num3}")
        print(f"  Suma: {suma:.2f}")
        print(f"  Promedio: {promedio:.2f}")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
