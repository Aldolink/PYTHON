# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos
# do usuario. Calcule o total em segundos.

# Solicitando os valores de dias, horas, minutos e segundos
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))
# Convertendo tudo para segundos
total_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos 
# Exibe o total em segundos
print(f"O total em segundos e : {total_segundos}")


