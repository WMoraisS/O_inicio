### LOOPS EM PYTHON
## WHILE - (Enquanto) O sistema repete a função "enquanto" a condição for verdadeira (True)

# Endless loop - (Loop infinito)
#while True:
#    print("I'm stuck inside a loop...")

#LEMBRETE -  'while counter != 0:' equivale a 'while counter:'

#----------------------------------------------------------------------------------------------------------------

## FOR-IN - (Para-em) O sistema conta as voltas do loop
# for i in range(100):
#     pass

# word = "Python"
# for letter in word:
#     print(letter, end="*")

#----------------------------------------------------------------------------------------------------------------

# RANGE() - Função para delimitar uma area/período, iniciando sua contagem padrão no 0
# RANGE(x, y) - O 'x' representa o valor inicial de controle, o 'y' representa o primeiro valor que não será atribuído.
# for i in range(2, 8):
#     print(i) #2, 3, ... 6, 7
# RANGE(x, y, z) - O 'z' representa o incremento; o valor acrescentado a variável de controle a cada loop.
# RANGE(START, STOP, STEP)

#----------------------------------------------------------------------------------------------------------------

### EXTRA - Biblioteca TIME - time.sleep() - É utilizado para 'pausar' a execução por um tempo determinado.
# import time
# for i in range(1, 6):
#     print(i, "Mississippi") # CONTAR MISSISSIPPI
#     time.sleep(1)
# print("Ready or not, here I come!")

#----------------------------------------------------------------------------------------------------------------

### DOCES SINTÁTICOS -> break, continue <- São comandos capazes de interferir diretamente no loop, pulando para o próximo ou finalizando.
## -> while-else, for-else <- O 'else' funciona como no condicional 'if', sendo executado somente uma vez quando o laço é falso.

#----------------------------------------------------------------------------------------------------------------

### 3.2.1.14 LAB - Pirâmide
# Cenário
# Leia esta história: um rapaz e o seu pai, um programador de computador, estão a brincar com blocos de madeira. Eles estão a construir uma pirâmide.

# A sua pirâmide é um pouco estranha, pois na realidade é uma parede em forma de pirâmide - é plana. A pirâmide é empilhada de acordo com um princípio simples: cada camada inferior contém mais um bloco do que a camada superior.

# A figura ilustra a regra utilizada pelos construtores:

# A sua tarefa é escrever um programa que leia o número de blocos que os construtores têm, e que produza a altura da pirâmide que pode ser construída utilizando estes blocos.

# Nota: a altura é medida pelo número de camadas completamente preenchidas - se os construtores não tiverem um número suficiente de blocos e não conseguirem completar a camada seguinte, terminam o seu trabalho imediatamente.

# blocks = int(input("Enter the number of blocks: "))
# height = 0 # Camada
# in_layer = 1 # Na camada

# while in_layer <= blocks:
#     height += 1 # Soma 1 camada a cada loop
#     blocks -= in_layer # Subtrai a quantidade de blocos da camada no total de blocos
#     in_layer += 1 # Soma 1 bloco a camada em cada loop

# print("The height of the pyramid:", height)

#----------------------------------------------------------------------------------------------------------------

### 3.2.1.15 LAB - A hipótese de Collatz
# Cenário
# Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese intrigante (ainda não provada) que pode ser descrita da seguinte forma:

# tomar qualquer número inteiro não-negativo e não-nulo e nomeá-lo c0;
# se for par, avalie um novo c0 como c0 ÷ 2;
# caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# Se c0 ≠ 1, saltar para o ponto 2.
# A hipótese diz que, independentemente do valor inicial de c0, irá sempre para 1.

# É claro que é uma tarefa extremamente complexa utilizar um computador para provar a hipótese de qualquer número natural (pode até requerer inteligência artificial), mas pode usar o Python para verificar alguns números individuais. Talvez até encontre o que possa refutar a hipótese.


# Escreva um programa que leia um número natural e execute os passos acima indicados, desde que c0 permaneça diferente de 1. Também queremos que conte os passos necessários para alcançar o objetivo. O seu código deve fazer output de todos os valores intermédios de c0, também.

# Dica: a parte mais importante do problema é como transformar a ideia de Collatz num loop while - esta é a chave para o sucesso.

# c0 = 0

# while c0 != -1:
#     c0 = int(input("Digite um número inteiro (-1 para sair): "))
#     i = 0
#     while c0 !=1:

#         if c0 % 2 == 0:
#             c0 = c0 / 2
            
#         elif c0 % 2 != 0:
#             c0 = 3 * c0 + 1

#         print(int(c0))
#         i += 1

#     print("steps", int(i))

#------------------------------------------------------------------------------------------

### EXERCÍCIOS
# 1 - Crie um loop for que conta de 0 a 10, e imprime os números ímpares no ecrã.
# for i in range(1, 11):
#     if i % 2 != 0:
#         print(i)

# 2 - Crie um loop while que conta de 0 a 10, e imprime os números ímpares no ecrã. 
# i = 0
# while i <= 10:
#     if i % 2 != 0:
#         print(i)
#     i += 1

# 3 - Crie um programa com um loop for e uma declaração break . O programa deve iterar sobre os caracteres de um endereço de 
# e-mail, sair do loop quando chegar ao símbolo @ , e imprimir a parte antes de @ numa linha.
# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

# 4 - Crie um programa com um loop for e uma declaração continue . O programa deve iterar sobre 
# uma string de dígitos, substituir cada '0' com 'x' e imprimir a string modificada no ecrã.

# for digit in "0165031806510":
#     if digit == '0':
#         digit = 'X'
#     print(digit, end='')
