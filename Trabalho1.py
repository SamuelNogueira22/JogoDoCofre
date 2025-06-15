#Jogo do Cofre, usuário tem 4 opções de digitos numéricos (0-9) e 4 chances no total, a cada tentativa há dicas, após a quarta
#Jogo acaba e usuário perde;
#Estrutura com Listas, Condicionais e Loops.

import random


#Defino no começo a senha e transformo ela numa lista, o que futuramente será útil
i = 0
senha = []

for i in range(0, 4):
    x = random.randint(0,9)
    senha.append(x)

#Apresentando conceitos do jogo
print("\033[1m----------------------------------------------------------------------JOGO DO COFRE------------------------------------------------------------------------\033[0m")
print("\033[1m                                        Esse é o jogo do Cofre! Você tem 4 chances para acertar a senha\n                                        Ao longo de suas tentativas te fornceremos dicas para te ajudar\033[0m")

#Para fonecer alguma ajuda ao usuário, informo se os dígitos são maiores ou menores que 5, dobrando suas chances iniciais de acertar por chute:
for i in range(0,4):
    if senha[i] >= 5:
        print("A posição", i + 1, "da senha é Maior OU Igual a 5")
    else:
        print("A posição", i + 1, "da senha é Menor que 5")


tentativa = 0
i = 0

while tentativa < 4:
    # Coletando os 4 números da tentativa
    lista = []
    for i in range(4):
        numero = int(input("Digite o número " + str(i + 1) + " da senha: "))
        lista.append(numero)

    print("Você selecionou os números:", lista)
    print("Comparando sua tentativa com a senha:")

    if lista == senha:
        print("\033[1m----------------------------------------------------------------------Correto, Parabéns!----------------------------------------------------------------------\033[0m")
        break

    for i in range(4):
        if lista[i] == senha[i]:
            print("Posição", i + 1, "correta!")
        elif lista[i] in senha:
            print("Número", lista[i], "está na senha, mas em posição errada")
        else:
            print("Número", lista[i], "não faz parte da senha")

    print("PARECE QUE NÃO FOI NESSA, MAS TENTE MAIS UMA VEZ")

    tentativa = tentativa + 1

if tentativa >= 4:
    print("IT'S OVER, NÃO FOI DESSA VEZ")
    print("A senha correta era", senha)
