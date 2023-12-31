# -*- coding: utf-8 -*-
"""Flaviana Gomes - 232_P2_Alg_m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JtIgeuLRdNmSYq5pYkO7AqCWVrM0Dg5H

##**P2 - 2º. semestre/2023 -  Término: 11:00**
##HOJE EU NÃO VERIFICO A LÓGICA/PROGRAMAÇÃO, NEM ERROS DE CÓDIGO, POIS É UMA PROVA DE CONSULTA.
## É uma prova de consulta ao seu material, **apenas use os slides da disciplina de Algoritmo e as listas de exercícios do Colab da nossa aula**.
## **Apenas verificarei** o desenvolvimento dos exercícios de cada aluno, **EM OUTRO DIA**.

##Caso entregue atrasado não será aceita a prova. **O Classroom/Collab NÃO DEIXA ENTREGAR FORA DO PRAZO**.

##Depois de terminada a prova, você **NÃO PODE MAIS ALTERAR O ARQUIVO** DELA, essa ação fica registrada e assim a prova será anulada.

##**Não é permitido o acesso a qualquer outro site/aplicativo para o desenvolvimento da prova, ou seja, apenas poderão estar abertas e visíveis as guias (no navegador de internet) do Classroom e Colab.**
++++++++++++++++++++++++++++++++++++++++++++++++++++
##**P3** será dia **07/12**, no horário de aula.
##++++++++++++++++++++++++++++++++++++++++++++++++++++
#Não é permitido o uso do celular no dia da prova.

#CASO VERIFIQUE QUE O COLLAB TENHA ALGUM PROBLEMA, VÁ NO MENU, NA OPÇÃO DE AMBIENTE DE EXECUÇÃO, ESCOLHA A OPÇÃO REINICIAR AMBIENTE DE EXECUÇÃO, CLIQUE EM SIM E TENTE EXECUTAR NOVAMENTE O SEU PROGRAMA.
______________________________________________________

##**1.** [1,5 pontos - **Estrutura de repetição sem contador**] Desenvolva um programa utilizando a linguagem Python, que calcule e apresente a média de faturamentos de alguns meses de uma cooperativa. Não é informado a quantidade de meses, então use como critério de parada (condição da estrutura de repetição), digitar zero no valor do faturamento para sair.
"""

print('.'*100)
print("Programa para calcular a média do faturamento")
print('.'*100)
print("Vamos calcular a média do faturameento de alguns meses. Digite 0 para encerrar o programa")
soma_faturamento = 0
quantidade_inserida = 0
faturamento = float(input("Digite aqui o faturamento: "))
while faturamento != 0: #faturamento enquanto não for 0 pois o exercício não cita os números negativos como critério para encerrar, então não uso o >0
        soma_faturamento += faturamento
        quantidade_inserida += 1
        faturamento = float(input("Digite aqui o faturamento: "))
if quantidade_inserida > 0:
    media = soma_faturamento / quantidade_inserida
print(f"\nA média do faturamento dos meses inseridos é de {media:.2f}")

"""##**2.** [3,0 pontos - **Vetor**] Desenvolva um programa, utilizando a linguagem Python, que leia/armazene num vetor, o valor de faturamento bruto de 5 cooperativas.
##Sabe-se que as cooperativas possuem um desconto de 8% sobre o faturamento bruto, gerando assim, o faturamento líquido.
##Em um segundo vetor, calcule e armazene o faturamento líquido.
##Ao final apresente o vetor de faturamento líquido.

##Observação: Apenas podem ser utilizadas as funções append() e len()
"""

print('.'*100)
print("Programa para calcular o faturamento líquido")
print('.'*100)
faturamento_bruto = []
faturamento_liquido = []

for i in range(5):
    faturamento = float(input("Digite aqui o faturamento bruto: "))
    faturamento_bruto.append(faturamento)

for i in range(len(faturamento_bruto)):
    desconto = faturamento_bruto[i] * 0.08
    liquido = faturamento_bruto[i] - desconto
    faturamento_liquido.append(liquido)

print(f"\nO faturamento líquido de cada cooperativa, respectivamente, é: {faturamento_liquido}")

"""##**3.**  [2,5 pontos - **Matriz**] Desenvolva um programa utilizando a linguagem Python, que leia uma matriz 3 x 2, que representa preços de produtos. Encontre e maior preço e apresente: o valor, a linha e a coluna em que ele esta armazenado na matriz.
##ObObservação: Apenas podem ser utilizadas as funções append() e len()
"""

print('.'*100)
print("Programa para matriz de preços de produtos")
print('.'*100)
precos_matriz = []
for linha in range (3):
    linha_precos = []
    for coluna in range(2):
        preco = float(input(f"Digite o preço na linha {linha} e coluna {coluna}: "))
        linha_precos.append(preco)
    precos_matriz.append(linha_precos)

preco_maior = precos_matriz[0][0]
linha_preco_maior = 0
coluna_preco_maior = 0

for linha in range(len(precos_matriz)):
    for coluna in range(len(precos_matriz[0])):
        if precos_matriz[linha][coluna] > preco_maior:
            preco_maior = precos_matriz[linha][coluna]
            linha_preco_maior = linha
            coluna_preco_maior = coluna
print(f"\nO maior preço inserido na matriz é {preco_maior} em sua linha {linha_preco_maior} e coluna {coluna_preco_maior}")