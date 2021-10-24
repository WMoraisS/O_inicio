# 3.4.1.11 - Listas

# # step 1
# beatles = []
# print("Step 1:", beatles)

# # step 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)
    
# # step 3
# print("...Head noice... ~Stu Sutcliffe~|~Pete Best~")
# for i in range(2):
#     beatle = input("Digite o nome dos outros integrantes da banda: ")
#     beatles.append(beatle)

# print("Step 3:", beatles)

# # step 4
# i = 1
# while i != len(beatles):
#     if beatles[i] == "Stu Sutcliffe" or beatles[i] == "Pete Best": 
#         del(beatles[i])
#         i -= 1
#     i += 1

# print("Step 4:", beatles)

# # step 5
# beatles.insert(0, "Ringo Starr")
# print("Step 5:", beatles)


# # testing list legth
# print("The Fab", len(beatles))

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

#A VIDA INTERNA DAS LISTAS
# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)

# Ao declarar 'list_2 = list_1' será copiado somente o nome da lista, herdando suas informações e alterações.
# As listas (e muitas outras entidades complexas de Python) são armazenadas de formas diferentes das variáveis ordinárias (escalares).
# -O nome de uma variável ordinária é o nome do seu conteúdo;
# -O nome de uma lista é o nome de um local de memória onde a lista é armazenada.


# >>   SLICE   << - Copia o conteúdo da lista, não somente seu nome
# Uma slice é um elemento da sintaxe Python que lhe permite fazer uma cópia completamente nova de uma lista ou partes de uma lista.
# list_1 = [1]
# list_2 = list_1[:] # Cria uma cópia da lista inteira.
# list_1[0] = 2
# print(list_2)
#
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3] # Cria uma cópia parcial da lista. Sintaxe: my_list[start:end] (end - 1)
# print(new_list)
#
# start é o index do primeiro elemento incluído no slice;
# end é o index do primeiro elemento não incluído no slice.

# del my_list[:] # Elimina todos os elementos da lista
# del my_list[]  # Elimina a lista em si.


# Os loops 'in' e 'not in' operadores
# O Python oferece dois operadores muito poderosos, capazes de olhar através da lista a fim de verificar se um valor específico 
# está ou não armazenado dentro da lista. Retorna resultado booleano.
# elem in my_list
# elem not in my_list

###### 3.7.1.1