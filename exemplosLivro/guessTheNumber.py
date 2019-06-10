#pg 107

#Este é um jogo de advinhar o numero

import random

numero_secreto = random.randint(1, 20)
print('Estou pensando em um numero de 1 a 20')

# peça para o jogador adivinhar 6 vezes

for advinhacoes in range(1, 7):
    print('advinhe: ')
    advinha = int(input())

    if advinha < numero_secreto:
        print('seu numero é muito baixo')
    elif advinha > numero_secreto:
        print('seu numero é muito alto')
    else:
        break #essa condicao corresponde ao palpitr correto

if advinha == numero_secreto:
    print('Bom trabalho, vc acertou meu numero em ' + str(advinhacoes) + ' tentativas')
else:
    print('Não, o numero que eu tinha pensado era ' + str(numero_secreto))