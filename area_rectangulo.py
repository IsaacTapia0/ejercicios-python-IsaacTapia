# Programa para calcular el área de un rectángulo

def main():
    print("=== Calculadora de Área de Rectángulo ===\n")

    try:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))

        if base <= 0 or altura <= 0:
            print("Error: La base y la altura deben ser valores positivos.")
            return

        area = base * altura

        print(f"\nResultados:")
        print(f"  Base: {base}")
        print(f"  Altura: {altura}")
        print(f"  Área: {area:.2f}")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
