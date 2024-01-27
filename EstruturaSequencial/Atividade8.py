"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
   Calcule e mostre o total do seu salário no referido mês."""

horas_ganho = float(input("Digite quanto você ganha por hora: "))
mes_trabalho = int(input("Digite quantas horas você trabalhou nesse mês: "))

salario = horas_ganho * mes_trabalho

print(f"Seu salario será R$ {salario}")
