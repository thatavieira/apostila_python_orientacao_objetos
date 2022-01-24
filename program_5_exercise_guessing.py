print('jogo_da_adivinhaçao')

numero_secreto=42

chute = input('digite o seu numero: ')
chute = int(chute)
print('voce digitou: ', chute)

if(numero_secreto == chute):
   print('voce acertou!')
else:
   print('voce errou!')

if(numero_secreto == chute):
  print('voce acertou! ')
elif(chute > numero_secreto):
    print('voce errou! o seu chute foi maior que o numero secreto')
elif(chute < numero_secreto):
    print('voce errou! o seu chute foi menor que o numero secreto')

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
   print('voce acertou!')
elif(maior):
   print('voce errou! o seu chute foi maior que o numero secreto')
elif(menor):
   print('voce errou! o seu chute foi menor que o numero secreto')