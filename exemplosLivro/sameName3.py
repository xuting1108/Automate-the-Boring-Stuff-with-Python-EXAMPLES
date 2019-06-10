#pg 102

def spam():
    global ovos
    ovos = 'spam' # essa variavel é global

def bacon():
    ovos = 'bacon' #essa variavel é local
    
def ham():
    print(ovos) #essa variavel é global



ovos = 42 #essa variavel é global
spam()
print(ovos) 