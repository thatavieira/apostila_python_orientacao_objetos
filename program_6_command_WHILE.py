numero_secreto=42
total_de_tentativas=3
rodada=1


while(total_de_tentativas > 0):
    print('tentativa {} de {}'. format(rodada, total_de_tentativas))
    chute=int(input('digite o seu numero: '))
    print('voce digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('voce acertou')
        break
    elif(maior):
        print('voce errou! o seu chute foi maior que o numero secreto')
    elif(menor):
        print('voce errou! o seu chute fi menor que o numero secreto')

    total_de_tentativas = total_de_tentativas - 1
    rodada = rodada + 1
    print('fim do jogo')


