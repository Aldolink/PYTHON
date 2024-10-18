# Fazer um programa que calcula o aumento de um salario. Ele deve solicitar o valor
# do salario e a porcentagem do aumento. Exibir o valor do aumento e do novo salario

# Solicita o valor do salario atual.
salario_atual = float(input("Digite o salario atual: "))
# Solicita a porcentagem do aumento.
porcentagem_aumento = float(input("Digite a porcentagem do aumento: "))
# Caucula o valor do aumento.
valor_aumento = salario_atual * porcentagem_aumento / 100
# Caucula o novo salario apos o aumento.
novo_salario = salario_atual + valor_aumento
# Exibe o valor do aumento e o novo salario.
print(f"O aumento sera de R${valor_aumento:.2f}. ")
print(f"O novo salario sera de R${novo_salario:.2f}. ")
