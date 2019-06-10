#pg 101

def spam():
    ovos = 'spam local'
    print(ovos) #exibe "spam local"

def bacon():
    ovos = 'bacon local'
    print(ovos) #exibe "bacon local"
    spam()
    print(ovos) #exibe "bacon local"

ovos = 'global'
bacon()
print(ovos) #exibe "global"