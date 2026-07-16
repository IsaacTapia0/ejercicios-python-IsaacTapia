# Programa para calcular el salario neto

def main():
    print("=== Calculadora de Salario Neto ===\n")

    try:
        salario_bruto = float(input("Ingresa el salario bruto: $"))
        porcentaje_impuestos = float(input("Ingresa el porcentaje de impuestos: "))
        deducciones = float(input("Ingresa las deducciones: $"))

        if salario_bruto < 0:
            print("Error: El salario bruto no puede ser negativo.")
            return

        if porcentaje_impuestos < 0 or porcentaje_impuestos > 100:
            print("Error: El porcentaje de impuestos debe estar entre 0 y 100.")
            return

        if deducciones < 0:
            print("Error: Las deducciones no pueden ser negativas.")
            return

        impuestos = salario_bruto * (porcentaje_impuestos / 100)
        salario_neto = salario_bruto - impuestos - deducciones

        print(f"\nDesglose:")
        print(f"  Salario bruto:    ${salario_bruto:,.2f}")
        print(f"  Impuestos ({porcentaje_impuestos}%): -${impuestos:,.2f}")
        print(f"  Deducciones:      -${deducciones:,.2f}")
        print(f"  ─────────────────────────")
        print(f"  Salario neto:     ${salario_neto:,.2f}")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
