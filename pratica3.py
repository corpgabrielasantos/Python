# nome = input("Qual seu nome?")
# print("Prazer em te conhecer {:20}!".format(nome))
# print("Prazer em te conhecer {:>20}!".format(nome))
# print("Prazer em te conhecer {:<20}!".format(nome))
# print("Prazer em te conhecer {:^20}!".format(nome))
# print("Prazer em te conhecer {:=^20}!".format(nome))

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
# print(f"O total é {n1 + n2}")
s = n1 + n2
sub = n1 - n2
d = n1 / n2
mult = n1 * n2
DI = n1 // n2
exp = n1 ** n2
print(f"A soma é {s}, a subtração é {sub}, a divisão é {d}, a multiplicação é {mult}, a divisão é {DI} e a exponenciação é {exp}")