numero_secreto=42
total_de_tentativas=3


for rodada in range(1, total_de_tentativas + 1):
    print('tentativa {} de {}'. format(rodada, total_de_tentativas))

    chute=int(input('digite o seu numero: '))
    print('voce digitou: ', chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
      print('voce acertou!')
      break
    elif(maior):
      print('voce errou! o seu chute foi maior que o numero secreto')
    elif(menor):
      print('voce errou! o seu chute foi menor que o numero secreto')

print('fim do jogo!')


