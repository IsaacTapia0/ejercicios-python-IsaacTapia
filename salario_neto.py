# Programa para calcular el salario neto

salario_bruto = float(input("Ingresa el salario bruto: "))
porcentaje_impuestos = float(input("Ingresa el porcentaje de impuestos: "))
deducciones = float(input("Ingresa las deducciones: "))

impuestos = salario_bruto * (porcentaje_impuestos / 100)
salario_neto = salario_bruto - impuestos - deducciones

print(f"El salario neto es: {salario_neto}")