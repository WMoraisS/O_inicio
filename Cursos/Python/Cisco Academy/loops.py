### LOOPS EM PYTHON
## WHILE - (Enquanto) O sistema repete a função "enquanto" a condição for verdadeira (True)

# Endless loop - (Loop infinito)
#while True:
#    print("I'm stuck inside a loop...")

#LEMBRETE -  'while counter != 0:' equivale a 'while counter:'

## FOR-IN - (Para-em) O sistema conta as voltas do loop
# for i in range(100):
#     pass

# RANGE() - Função para delimitar uma area/período, iniciando sua contagem padrão no 0
# RANGE(x, y) - O 'x' representa o valor inicial de controle, o 'y' representa o primeiro valor que não será atribuído.
# for i in range(2, 8):
#     print(i) #2, 3, ... 6, 7
# RANGE(x, y, z) - O 'z' representa o incremento; o valor acrescentado a variável de controle a cada loop.
# RANGE(START, STOP, INCREASE)

### EXTRA - Biblioteca TIME - time.sleep() - É utilizado para 'pausar' a execução por um tempo determinado.
# import time
# for i in range(1, 6):
#     print(i, "Mississippi") # CONTAR MISSISSIPPI
#     time.sleep(1)
# print("Ready or not, here I come!")

### DOCES SINTÁTICOS -> break, continue <- São comandos capazes de interferir diretamente no loop, pulando para o próximo ou finalizando.
## -> while-else, for-else <- O 'else' funciona como no condicional 'if', sendo executado somente uma vez quando o laço é falso.
