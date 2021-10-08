# Caracter de ESCAPE >>    \    << (Barra invertida) Informa que o próximo caracter é um caracter especial.

# NewLine >>    \n    <<

from typing import Type


print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain\nand washed the spider out.")

# Multiplos argumentos dentro da função.

print("The itsy bitsy spider" , "climbed up" , "the waterspout.")


# Argumentos de Keyword
# >>    END    << Esse argumento de keyword cancela a NewLine padrão da função Print, substituindo-o por "ESPAÇO" como no caso abaixo...

print("My name is", "Python.", end=" ")
print("Monty Python.")

# >>    SEP    << Esse argumento de keyword substitui o espaçamento padrão entre os argumentos da função...

print("My", "name", "is", "Monty", "Python.", sep="-")

# Diversos keywords na mesma invocação

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*")

# Áspas dentro das strings
# 1- Caracter de ESCAPE \"\"
print("I like \"Monty Python\"")

# 2- Apóstrofe
print('I like "Monty Python"')
print("I like 'Monty Python'")
print('I like \'Monty Python\'')
print('I\'m Monty Python')

# VALORESNUMÉRICOS
# NOTAÇÃO CIENTÍFICA >>    E    << Ex: 3e8 = 300000000

print(3e8)
print(.000000003)

# Constante de Planck ( 6.62607 x 10(e-34) )

print(6.62607e-34)

# VALORES BOOLEANOS >>    True | False    <<

print(True > False)
print(True < False)

# EXERCÍCIOS
# 1- "Hello", "007"
print(type("Hello"), type("007"))
# STRINGS

# 2- "1.5", 2.0, 528, False
print(type("1.5"), type(2.0), type(528), type(False))
print(" STRING, FLOAT, INT, BOOL")

print("3- Binário 1011 em decimal?")
print("        1      0       1       1")
print((2**3) + (0) + (2**1) + (2**0)) # = 11
print()

print("OPERADORES BÁSICOS +, -, *, /, //, %, **")
print(">>  **  << EXPONENCIAÇÃO(POTÊNCIA) É EXECUTADA DA DIREITA PARA ESQUERDA EM UMA EQUAÇÃO")
print(2 ** 3) # = 8
print()

print(">>  /  << DIVISÃO ou FLOOR DIVISION (RETORNA UM VALOR FLOAT)")
print( 4 / 2) # = 2
print( 3 / 2) # = 1.5
print(">>  //  << (RETORNA UM VALOR INT TRUNCADO, IGNORANDO AS CASAS DECIMAIS)")
print( 4 // 2) # = 2
print( 3 // 2) # = 1
print()

print(">>  %  << REMAINDER, MÓDULO ou RESTO (RETORNA O QUE SOBROU DA DIVISÃO INTEIRA)")
print(14 / 4) # = 3.5
print(14 // 4) # = 3
print(14 % 4) # = 2
print()

print("OPERADOR UNÁRIO É UM OPERADOR COM APENAS UM OPERANDO, Ex: -1 ou +3")
print("OPERADOR BINÁRIO É UM OPERADOR COM DOIS OPERANDOS, Ex: 4 + 6 ou 12 % 5")
