### AND   == 'Conjunção' ###
### OR    == 'Disjunção' ###
### 'OU EXCLUSIVO' - Quando somente um operador da disjunção é verdadeiro

### NOT   == 'Negação' ###
##Pode estar familiarizado com as leis de De Morgan. Dizem que:
#A negação de uma conjunção é a disjunção das negações.
#A negação de uma disjunção é a conjunção das negações.
#Vamos escrever a mesma coisa usando Python:
#not (p and q) == (not p) or (not q)
#not (p or q) == (not p) and (not q)
# i = 1
# j = not not i
# print(j)

### OPERADORES BITWISE
# No entanto, existem quatro operadores que lhe permitem manipular bits únicos de dados. São chamados operadores bitwise.

# Abrangem todas as operações que mencionámos anteriormente no contexto lógico, e um operador adicional. Este é o operador 
# 'xor' (como em exclusivo ou), e é denotado como ^ (acento circunflexo).
# Aqui estão todos eles:

# & (e comercial) - conjunção bitwise;
# | (barra) - disjunção bitwise;
# ~ (til) - negação bitwise;
# ^ (acento circunflexo) - bitwise exclusive ou (xor).

# Vamos facilitar as coisas:

# & requer exatamente dois 1 para fornecer 1 como resultado;
# | requer pelo menos um 1 para fornecer 1 como resultado;
# ^ requer exatamente um 1 para fornecer 1 como resultado.

#A diferença no funcionamento dos operadores lógicos e de bit é importante: 
# _Os operadores lógicos não penetram no nível de bits do seu argumento. Eles só estão interessados no valor inteiro final.
# _Os operadores bitwise são mais rigorosos: lidam com cada bit separadamente. Se assumirmos que a variável inteira ocupa 
# 64 bits (o que é comum nos sistemas informáticos modernos), podemos imaginar a operação bitwise como uma avaliação de 64 
# vezes do operador lógico para cada par de bits dos argumentos. Esta analogia é obviamente imperfeita, pois no mundo real 
# todas estas 64 operações são realizadas ao mesmo tempo (simultaneamente).

# OPERAÇÕES LÓGICAS vs BITWISE
# EXEMPLOS:
# Operações lógicas
# i = 15
# j = 22
# log = i and j
# print(bool(log))
# # Em Bitwise funciona diferente (Notação binária)
# i = 15 # 1111
# j = 22 # 10110
# log = i & j
# print(bin(log), "\n", log)
## OPERADORES DE NEGAÇÃO:
# i = 15
# logneg = not i
# bitneg = ~i
# print(logneg, "\n", bitneg, "\n", bin(bitneg))

### OPERADORES SHIFT / SHIFTING BINÁRIO [  <<  ] e [  >>  ] (DESLOCAMENTO) Aplicado somente a valores inteiros
# Você já aplica esta operação com alguma frequência, e bastante inconscientemente. De que forma multiplica qualquer número por dez? Dê uma vista de olhos:
# 12345 × 10 = 123450
# Como se pode ver, multiplicar por dez é, de facto, um shifting de todos os dígitos para a esquerda, preenchendo a lacuna resultante com zero.
# Divisão por dez? Dê uma vista de olhos:
# 12340 ÷ 10 = 1234
# Dividir por dez não é mais do que um shifting dos dígitos para a direita.
# O mesmo tipo de operação é realizado pelo computador, mas com uma diferença: como dois é a base para números binários (não 10), o shifting de um valor um bit para a esquerda corresponde assim a multiplicá-lo por dois; respetivamente, o shifting um bit para a direita é o mesmo que dividí-lo por dois (repare que o bit mais à direita é perdido).

# Os operadores shift em Python são um par de dígrafos: << e >>, sugerindo claramente em que direção a mudança irá ocorrer.
# value << bits
# value >> bits
#O argumento à esquerda destes operadores é um valor inteiro cujos bits são deslocados. O argumento à direita determina o tamanho do shifting.

# var = 17
# var_right = var >> 1
# var_left = var << 2
# print(var, var_left, var_right)
# print(bin(var),"\n",bin(var_left), "\n", bin(var_right))

# Nota:
# 17 >> 1 → 17 // 2 (17 divido por baixo por 2 à potência de 1) → 8 (shifting para a direita por um bit é o mesmo que a divisão inteira por dois)
# 17 << 2 → 17 * 4 17 multiplicado por 2 à potência de 2) → 68 (shifting para a esquerda por dois bits é o mesmo que a multiplicação de inteiros por quatro)

# E aqui está a tabela de prioridades atualizada, contendo todos os operadores introduzidos até agora:
# Prioridade	Operador	
# 1	~, +, -	unário
# 2	**	
# 3	*, /, //, %	
# 4	+, -	binário
# 5	<<, >>	
# 6	<, <=, >, >=	
# 7	==, !=	
# 8	&	
# 9	|	
# 10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=	