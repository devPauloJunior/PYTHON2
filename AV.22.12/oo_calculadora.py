#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# utilizar as classes CalculadoraMM(Super), Adicao, Subtracao, Multiplicacao, Divisao e Equacao para elas faça:
# faça herança quando julgar necessária
# sua calculadora deve trabalha com strings validando as operações Ex: "2+2" "16*140" "2x-10=9"
# crie os padrões e faça as validações
# utilize as expressões regulares para as validações
# OBS: Veja a possibilidade de utilizar os métodos mágicos
# OBS: Faça todas as validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça as impressões necessárias
import re

rd = re.compile('[0-9]{1,4}\+[0-9]{1,4}')
soma = "111+11"
if rd.match(soma):
    num = re.split('\+',soma)
    num1 = num[0]
    num2 = num[1]
    resultado = int(num1) + int(num2)
    print(resultado)
else:
    print("tchau")
