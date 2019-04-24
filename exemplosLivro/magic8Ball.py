#pg 94
import random #modulo random é importado

def resposta(numeroRespondido):# a funcao é definida
    #conteudo da funcao
    if numeroRespondido == 1:
        return 'é certo'
    elif numeroRespondido == 2:
        return 'será?'
    elif numeroRespondido == 3:
        return 'Simm?'
    elif numeroRespondido == 4:
        return 'Tente de novo'
    elif numeroRespondido == 5:
        return 'Responda daqui a pouco'
    elif numeroRespondido == 6:
        return 'responda novamente'
    elif numeroRespondido == 7:
        return 'Nãaaaao'
    elif numeroRespondido == 8:
        return 'Muito duvidoso'

r = random.randint(1,9)#inteiro aleatorio entr 1 e 9
a = resposta(r)
print(a)#será exibida alguma das mensagens na tela de acordo com o n sorteado

#pode ser feita em uma linha: print(resposta(random.randint(1,9)))