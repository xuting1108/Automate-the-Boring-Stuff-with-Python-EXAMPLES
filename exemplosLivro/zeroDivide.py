#pg 104
"""
def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(22))
print(spam(522))
print(spam(0)) #ERROR: ZeroDivisionError
"""
"Tratamento do erro"

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Erro: Argumento inválido')

print(spam(2))
print(spam(12))
print(spam(22))
print(spam(522))
print(spam(0)) #ERROR: ZeroDivisionError
