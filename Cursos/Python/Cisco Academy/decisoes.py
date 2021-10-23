### OPERADORES DE COMPARAÇÃO

## IGUALDADE <<   ==   >> - EQ[Equal] (igual a) Questiona o sistema se um valor é igual ao outro e retorna em booleano(True ou False)
# print(2 == 3)
# print(2 == 2)

## DESIGUALDADE <<   !=   >> - NE[Not Equal] (não igual a) Questiona o sistema se um valor é diferente ao outro e retorna em booleano(True ou False)
# print(2!=3)
# print(2!=2)

## MAIOR QUE            <<    >    >> - GT(Greater than)
## MAIOR OU IGUAL A     <<    >=    >> - GE(Greater than or Equal to)
## MENOR QUE            <<    <    >> - LT(Less than)
## MENOR OU IGUAL A     <<    <=    >> - LE(Less than or Equal to)

# Prioridade	Operador	
# 1	            +, -	        unário
# 2	            **	
# 3	            *, /, //, %	
# 4	            +, -	        binário
# 5	            <, <=, >, >=	
# 6	            ==, !=

### INSTRUÇÕES CONDICIONAIS
## IF - (Se)
# if python_is_easy:
#     be_happy

## IF-ELSE - (Se-Senão)
# if python_is_easy:
#     be_happy
# else:
#     sorry

## IF-ELSE *Nested* (Aninhado)
# if python_is_easy:
#     if man:
#         be_happy
#     else:
#         be_happy_too
# else:
#     sorry_u_need_study

## ELIF *Else if* (Senão-Se) (Cascata)
# if python_is_easy:
#     be_happy
# elif python_is_hard:
#     u_need_study
# else:
#     sorry

### EXTRA
## Função max() - Retorna o maior valor entre os argumentos. Exemplo de sintaxe: max(arg1, arg2, arg3)
## Função min() - Retorna o menor valor entre os argumentos. Exemplo de sintaxe: min(arg1, arg2, arg3)
# my_old_list = [8,10,6,2,4]
# my_list = [8,10,6,2,4]
# count = True
# while count == True:
#     count = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             my_list[i], my_list[i + 1] = my_list[i +1], my_list[i]
#             print(my_list)
#             count = True
    
# print(my_list)

# my_old_list.sort() # Ordena a lista em ordem Crescente
# print("Usando o .sort", my_old_list)
# my_old_list.reverse() # Ordena a lista em ordem Decrescente
# print("Usando o .reverse", my_old_list)

#3.6.1.1