'''
def divisao(n1, n2):
    try:
        return n1/n2
    except:
        print('Deu merda mano')


'''

def divisao(n1, n2):
    try:
        return n1/n2
    except TypeError:
        print('Apenas operações com números!')
    except ZeroDivisionError:
        print('Forneça um número diferente de zero!')
    finally:
        print('Sempre estou aqui.')

print(divisao(10, 2))
print(divisao(10, 0))
print(divisao(10, '12'))