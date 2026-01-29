# from random import randint
# computador = randint(0, 5)
# print("-=-" * 20)
# print("Vou pensar em um número entre o e 5. Tente adivinhar...")
# print("-=-" * 20)
# jogador = int(input("Em que número eu pendei? "))
# if jogador == computador:
#     print("PARABÉNS, você conseguiu vencer!")
# else:
#     print(f"GANHEI, Eu pensei no número {computador} e não {jogador}")

# n = float(input("Qual foi a velocidade do carro? "))
# if n >= 80:
#     print("Você recebeu uma multa!")
# print("A multa vai custar R$ 7,00 por cada km acima do limite")
# else:
#     print("Você não possui multas")

# n = int(input("Qual número você quer saber? "))
# if n % 2 == 0:
#     print("Ele é PAR")
# else:
#     print("Ele é ÍMPAR")

# distancia = float(input("Qual a distância em km da viagem? "))
# if distancia <= 200:
#     preco = distancia * 0.50
#     print(f"O preço da sua passagem saira a {preco}")
# else:
#     preco = distancia * 0.45
#     print(f"Sua passagem saira a {preco}")

# ano = int(input("Me diga o ano, por favor: "))
# if ano % 4 == 0 and ano % 400 == 0:
#     print("O ano é bissexto!")
# else:
#     print("O ano não é bissexto!")

# n1 = int(input("Me diga um número, por favor: "))
# n2 = int(input("Me diga o 2º número, por favor: "))
# n3 = int(input("Me diga o 3º número, por favor: "))

# if n1 > n2 and n1 > n3:
#     print(f"O número maior é {n1}")
# else:
#     if n2 > n3:
#         print(f"O número maior é {n2}")
#     else:
#         print(f"O número maior é {n3}")

# salario = float(input("Qual o salãrio do funcionário? "))
# if salario <= 1250:
#     novo = salario + (salario * 15 / 100)
# else:
#     novo = salario + (salario * 10/ 100)
# print(f"Quem ganhava {salario} passo a ganhar {novo} agora ")

# print('-='*20)
# print("Analisador de triângulo")
# print('-='*20)
# r1 = float(input("Primeiro segmento: "))
# r2 = float(input("Segundo segmento: "))
# r3 = float(input("Terceiro segmento: "))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print("Os segmentos acima podem formar um triangulo!")
# else:
#     print("Os segmentos acima não podem formar triângulo")