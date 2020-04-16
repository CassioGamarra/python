import os

nome_jogo = "***************\n*JOGO DA FORCA*\n***************"

print(nome_jogo)

palavra = input("Digite a palavra: ")
dica = input("Insira a dica: ")
acertou = False
enforcou = False
erros = 0
letras_da_palavra = []

os.system('clear')

for letra in palavra:
    letras_da_palavra.append('_')

print(nome_jogo)
print(letras_da_palavra)
print("A dica é: {} , você tem 7 tentativas".format(dica))
while(not acertou and not enforcou):    
    chute = input("Tentativa {}, digite uma letra: ".format(erros+1))
    
    if(chute in palavra):
        posicao = 0
        for letra in palavra:
            if(chute.upper() == letra.upper()):
                letras_da_palavra[posicao] = letra
            posicao += 1
    else:
        erros += 1

    acertou = '_' not in letras_da_palavra
    enforcou = erros == 7
    print(letras_da_palavra)

if(acertou):
    print("Você ganhou!")
else:
    print("Você perdeu!")