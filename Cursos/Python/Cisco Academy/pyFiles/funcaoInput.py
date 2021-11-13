# CTRL + / ou CTRL + ; para adicionar comentários em um bloco de linhas
## FUNÇÃO INPUT - Como falar com um computador
# 2.6.1.1

# print("Digite qualquer coisa: ")
# anything = input()
# print("Hmmm... ", anything, " ......really???")
# #--------------------------------------------------------------------
# anything = input("Digite qualquer coisa: ")
# print("Hmmm... ", anything, " ......really???")

# 2.6.1.2
# anything = input("Enter a number: ")
# something = float(anything) ** 2.0
# print(anything, "to the power of 2 is", something)
# #----------------------------------------------------------------------
# anything = float(input("Enter a number: "))
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# Operadores de String
## 2.6.1.6 - Concatenar strings >>   +   <<
#x = "Hello"
#y = "World"
#print(x + ", " + y + "!!!")

## 2.6.1.7 - Replicar >>   *   <<
#print("+" + 10 * "-" + "+")
#print(("|" + " " * 10 + "|\n") * 5, end="")
#print("+" + 10 * "-" + "+")

## 2.6.1.10 - LAB: Operadores e expressões

#x = float(input("Enter value for x: "))
#y = 1 / (x+1/(x+1/(x+1/x)))
#print("y =", y)
# Input 1 deve resultar: y = 0.6000000000000001
# Input 10 deve resultar: y = 0.09901951266867294
# Input 100 deve resultar: y = 0.009999000199950014
# Input -5 deve resultar: y = -0.19258202567760344

## 2.6.1.11 - LAB: Operadores e expressões

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))

# min = (mins + dura) % 60
# hr = (hour + ((mins + dura) // 60)) % 24

# print(hr , ":", min)

# Input 12, 17, 59 deve resultar: 13:16
# Input 23, 58, 642 deve resultar: 10:40
# Input 0, 1, 2939 deve resultar: 1:0






