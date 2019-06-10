#pg 102

def spam():
    global ovos #ovos é uma variavel global, msm sendo dentro de um funcao
    ovos = 'spam'

ovos = 'global'
spam()
print(ovos) 