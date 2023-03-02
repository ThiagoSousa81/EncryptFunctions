# Funções de criptografia básica em Pyhton

class Encrypt1(object):
    def function(self, x: float):
        return (2 * x) - 6
    def inverse(self, y: float):
        return (y /2) + 3

F = Encrypt1()
while (True):
    x = input('Digite um número: ')
    print('Número cifrado...')
    print(F.function(float(x)))
    print('Número decifrado...')
    print(F.inverse(F.function(float(x))))
