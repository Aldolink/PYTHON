# Escreva um programa que converta uma temperatura digitada em celsius em fahrenheit.

# Solicita a temperatura em celsius.
temperatura_celsius = float(input("Digite a temperatura em celsius: "))

temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"A temperatura em celsius e: {temperatura_celsius:.2f} C")
print(f"A temperatura convertida em fahrenheit e: {temperatura_fahrenheit:.2f} F")