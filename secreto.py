'''
implementar o sistema de níveis de dificuldade:

Fácil: O jogador tem 30 tentativas para adivinhar o número secreto.                          CHECK
Médio: O jogador tem 15 tentativas para adivinhar o número secreto.                          CHECK
Difícil: O jogador tem 5 tentativas para adivinhar o número secreto.                         CHECK

Implementar o sistema de pontuação:
O jogador começa com uma pontuação inicial de 100 pontos.                                    CHECK
A cada tentativa errada, o jogador perde pontos.                                             CHECK

O cálculo da pontuação perdida pode ser adaptado ao nível de dificuldade. Por exemplo:
Fácil: Perde 10 pontos por erro.                                                             CHECK
Médio: Perde 20 pontos por erro.                                                             CHECK
Difícil: Perde 50 pontos por erro.                                                           CHECK
'''



import random
pontos = 100
secreto = None #DEIXEI ESSA VARIÁVEL SEM VALOR PORQUE É A VARIÁVEL DO USUÁRIO
tentativas = None #DEIXEI ESSA VARIÁVEL SEM VALOR PRA RECEBER DE ACORDO COM O NÍVEL
randomNumber = random.randint(1,100)
nivel = int(input('Selecione o nível de difículdade desejado fácil, médio ou difícil (1,2 ou 3): '))


'''NÍVEL FÁCIL'''

if nivel == 1:
    print("\nVocê escolheu o nível fácil!\n\nPerderá 10 pontos por erro e terá 30 tentativas.\n")

    tentativas = 30

    while secreto != randomNumber and tentativas > 0:
        print("------------------------------------") #PRINT FEITO PURAMENTE PARA FINS ESTÉTICOS
        print(f"Você tem {tentativas} tentativas restantes\n")
        

        secreto = int(input("Escolha o seu número de 1 a 100: "))
        
        
        if randomNumber == secreto:
            if pontos < 0: #COLOQUEI UM IF PARA SEMPRE QUE O NÚMERO FOR NEGATIVO ELE IGUALAR A ZERO
                pontos = 0
            pontos += 100 #COLOQUEI UMA PONTUAÇÃO PARA QUANDO O USUÁRIO ACERTAR
            print(f"\nParabéns, você acertou o número secreto!\nA sua pontuação é: {pontos} ponto(s)\n")
            break

        elif secreto > 200:
            print("Só números de 1 a 100! Tente Novamente.\n")
            tentativas += 1 #ISSO AQUI É PRA CASO A PESSOA DIGITE ALGO MAIOR QUE 100 ELA NÃO PERCA TENTATIVAS

        elif randomNumber > secreto < 100:
            print('\nO número secreto é maior que esse!')
            pontos -= 10


        elif randomNumber < secreto > 0:
            print('O número secreto é menor que esse!\n')
            pontos -= 10

        tentativas -= 1

'''NIVEL MÉDIO'''

if nivel == 2:
    print("Você escolheu o nível Médio!\n\nPerderá 20 pontos por erro e terá 15 tentativas.\n")

    tentativas = 15

    while secreto != randomNumber and tentativas > 0:
        print("------------------------------------") #PRINT FEITO PURAMENTE PARA FINS ESTÉTICOS
        print(f"Você tem {tentativas} tentativas restantes\n")
        secreto = int(input("Escolha o seu número de 1 a 100: "))

        if randomNumber == secreto:
            if pontos < 0: #COLOQUEI UM IF PARA SEMPRE QUE O NÚMERO FOR NEGATIVO ELE IGUALAR A ZERO
                pontos = 0
            pontos += 300 #COLOQUEI UMA PONTUAÇÃO PARA QUANDO O USUÁRIO ACERTAR
            print(f"\nParabéns, você acertou o número secreto!\nA sua pontuação é: {pontos} ponto(s)\n")
            break


        elif randomNumber > secreto:
            print('O número secreto é maior que esse!\n')
            pontos -= 20


        elif randomNumber < secreto:
            print('O número secreto é menor que esse!\n')
            pontos -= 20


        elif secreto > 100:
            print("Só números de 1 a 100! Tente Novamente.\n")
            tentativas += 1


        tentativas -= 1

'''NÍVEL DIFÍCIL'''

if nivel == 3:
    print("Você escolheu o nível Difícil!\n\nPerderá 50 pontos por erro e terá 5 tentativas.\n")

    tentativas = 5

    while secreto != randomNumber and tentativas > 0:
        print("------------------------------------") #PRINT FEITO PURAMENTE PARA FINS ESTÉTICOS
        print(f"Você tem {tentativas} tentativas restantes\n")
        secreto = int(input("Escolha o seu número de 1 a 100: "))

        if randomNumber == secreto:
            if pontos < 0: #COLOQUEI UM IF PARA SEMPRE QUE O NÚMERO FOR NEGATIVO ELE IGUALAR A ZERO
                pontos = 0
            pontos += 400 #COLOQUEI UMA PONTUAÇÃO PARA QUANDO O USUÁRIO ACERTAR
            print(f"\nParabéns, você acertou o número secreto!\nA sua pontuação é: {pontos} ponto(s)\n")
            break


        elif randomNumber > secreto:
            print('O número secreto é maior que esse!\n')
            pontos -= 50


        elif randomNumber < secreto:
            print('O número secreto é menor que esse!\n')
            pontos -= 50


        elif secreto > 100:
            print("Só números de 1 a 100! Tente Novamente.\n")
            tentativas += 1


        tentativas -= 1

   
if tentativas == 0:
    if pontos < 0:
        pontos = 0
        print(f"\nVocê Perdeu!\nA sua pontuação é: {pontos} ponto(s)\n")
