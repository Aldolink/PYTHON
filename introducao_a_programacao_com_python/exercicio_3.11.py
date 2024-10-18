# Fazer um programa que solicita o valor de uma mercadoria e o percentual de desconto.
# Exibir o valor do desconto e o valor a pagar.

# Solicita o valor da mercadoria.
valor_mercadoria = float(input("Digite o valor atual da mercadoria: "))
# Solicita a porcentagem de desconto.
porcentual_desconto = float(input("Digite o porcentual de desconto da mercadoria: "))
# Calcula o valor do desconto.
valor_desconto = valor_mercadoria * (porcentual_desconto / 100)
# Calcula o valor final a pagar.
valor_a_pagar = valor_mercadoria - valor_desconto

# Exibe o valor do desconto e o valor final a pagar.
print(f"O porcentual de desconto e de R${valor_desconto:.2f}. ")
print(f"O valor a pagar e de R${valor_a_pagar:.2f}")
