# -*- coding: utf-8 -*-
"""Flaviana Gomes - 232_P1_Alg_m.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dxDk79i24q6OKz8yCni8DvlHkaIIm3Uv

##**P1 - 2º. semestre/2023 -  Término: 10:40**
##HOJE EU NÃO VERIFICO A LÓGICA/PROGRAMAÇÃO, NEM ERROS DE CÓDIGO, POIS É UMA PROVA DE CONSULTA.

## É uma prova de consulta ao seu material, **apenas use os slides da disciplina de Algoritmo e as listas de exercícios do Colab da nossa aula**.

## **Apenas verificarei** o desenvolvimento dos exercícios de cada aluno, **EM OUTRO DIA**.

##Caso entregue atrasado não será aceita a prova. **O Classroom/Collab NÃO DEIXA ENTREGAR FORA DO PRAZO**.

##Depois de terminada a prova, você NÃO PODE MAIS ALTERAR O ARQUIVO DELA, essa ação fica registrada e assim a prova será anulada.

##Na próxima aula (sábado) será realizada a correção da prova.

##**Não é permitido o acesso a qualquer outro site/aplicativo para o desenvolvimento da prova, ou seja, apenas poderão estar abertas e visíveis as guias (no navegador de internet) do Classroom e Colab.**

#Não é permitido o uso do celular no dia da prova.

#CASO VERIFIQUE QUE O COLLAB TENHA ALGUM PROBLEMA, VÁ NO MENU, NA OPÇÃO DE AMBIENTE DE EXECUÇÃO, ESCOLHA A OPÇÃO REINICIAR AMBIENTE DE EXECUÇÃO, CLIQUE EM SIM E TENTE EXECUTAR NOVAMENTE O SEU PROGRAMA.
______________________________________________________

##**1.** [1,5 pontos - **Entrada, processamento e saída**] Uma empresa de pavimentação foi contratada para asfaltar uma rua, para custear este trabalho é necessário saber a distância entre dois pontos marcados na rua.

##Você foi contratado para desenvolver um programa utilizando a linguagem Python, que calcule e apresente a distância, para isso deve ser lido as coordenadas x e y do ponto A, x e y do ponto B. Utilize a fórmula a seguir:

##distancia = (( xB – xA)<sup>2</sup> + ( yB – yA)<sup>2</sup>)  <sup>0.5</sup>
"""

print('.'*100)
print("Programa para calcular a distância entre A e B")
print('.'*100)
xA = float(input("Digite aqui o valor de X referente à A: "))
yA = float(input("Digite aqui o valor de Y referente à A: "))
xB = float(input("Digite aqui o valor de X refererente à B: "))
yB = float(input("Digite aqui o valor de Y referente à B: "))
potencia1 = (xB - xA) ** 2
potencia2 = (yB - yA) ** 2
resultado = (potencia1 + potencia2) ** 0.5
print(f"O valor da distância entre A e B é de {resultado:.2f}")

"""##**2.** [2,5 pontos - **Estrutura de decisão**] Desenvolva um programa, utilizando a linguagem Python, que receba três valores (obrigatoriamente maiores que zero) representando: a medida da hipotenusa, do cateto adjacente e do cateto oposto.
##Faça o calculo para verificar o Teorema de Pitágoras se "a soma do quadrado dos catetos é **igual** ao quadrado da hipotenusa".
##Se for verdadeira a resposta, apresente a frase/str 'É verdade', senão 'É Falso'.

##hiponetusa<sup>2</sup> = medida_cateto_adjacente<sup>2</sup> + medida_cateto_Oposto<sup>2</sup>

##Observação: não utilize estrutura de repetição.
"""

print('.'*100)
print("Programa para verificar o Teorema de Pitágoras")
print('.'*100)
hipotenusa = float(input("Digite aqui o valor da hipotenusa: "))
cateto_adjacente = float(input("Digite aqui o valor do cateto_adjacente: "))
cateto_oposto = float(input("Digite aqui o valor do cateto_oposto: "))
medida_cateto_adjacente = cateto_adjacente ** 2
medida_cateto_oposto = cateto_oposto ** 2
medida_hipotenusa = hipotenusa ** 2
soma_catetos = medida_cateto_adjacente + medida_cateto_oposto
if medida_hipotenusa == soma_catetos:
    print("É verdade!")
else:
    print("É falso!")

"""##**3.**  [3,0 pontos - **Estrutura de repetição**] O Instituto de Radiologia é uma empresa que oferece aos seus médicos e pacientes a possibilidade de realizar diversos exames, entre eles Raio x, tomografia, ressonância.
##A empresa fará uma troca de camas, onde o paciente deita para realizar um destes exames, mas precisam saber quantas pessoas possuem altura maior que 2 metros dentre 500 pacientes atendidos.

##Observação: apresenta a quantidade.

##Pode implementar com o comando while ou for.
"""

print('.'*100)
print("Programa para a quantidade de pessoas com altura maior que 2 metros - Instituto de Radiologia")
print('.'*100)
contador = 0
for cont in range(5):
    altura = int(input("Digite aqui a sua altura (em centímetros): "))
    if altura > 200:
        contador = contador + 1
print("A quantidade de pessoas com altura acima de 2 metros é de", contador)

print('.'*100)
print("Programa para a quantidade de pessoas com altura maior que 2 metros - Instituto de Radiologia")
print('.'*100)
pessoas = 1
contador = 0
while pessoas <= 5:
    altura = float(input("Digite aqui a sua altura (em centímetros): "))
    if altura > 200:
        contador = contador + 1
    pessoas = pessoas + 1
print("A quantidade de pessoas com altura acima de 2 metros é de", contador)