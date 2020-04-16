numero = 42
rodadas = 0
pontuacao = 1000

print("*********************")
print("*JOGO DA ADIVINHAÇÃO*")
print("*********************\n")

dificuldade = int(input("Dificuldade: 1 - Nível 1 | 2 - Nível 2 | 3 - Nível 3: "))

if(dificuldade == 1):
    rodadas = 20
elif(dificuldade == 2):
    rodadas = 10
elif(dificuldade == 3):
    rodadas = 5
else:
    print("Dificuldade padrão em 1")
    rodadas = 20

print("Você tem {} chances".format(rodadas))

for rodada in range(1,rodadas+1):
    print("Rodada {}".format(rodada))
    chute = int(input("Digite um número: "))
    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if(acertou):
        print("Você acertou")
        break
    elif(maior):
        print("Chute maior que o número")
        pontuacao -= abs(chute-numero)
    elif(menor):
        print("Chute menor que o número")
        pontuacao -= abs(chute-numero)

print("Fim de jogo! Você fez {} pontos".format(pontuacao))