numero_secreto=20
chute=20
numero_secreto=int(numero_secreto)
chute=int(chute)

chute=input('digite um numero: ')
numero_secreto=input('digite um numero: ')

if(numero_secreto == chute):
  print('voce acertou!')
elif(chute > numero_secreto):
    print('voce errou! o seu chute foi maior que o numero secreto')
elif(chute < numero_secreto):
    print('voce errou! o seu chute foi menor que o numero secreto')
