# Funções de criptografia básica em Pyhton

class Encrypt1(object):
    def function(self, x: float):
        return (2 * x) - 6
    def inverse(self, y: float):
        return (y /2) + 3
    
class Encrypt2(object):
    def function(self, x: float):
        return 1 / (x + 1)
    def inverse(self, y: float):
        return y**-1 -1

F1 = Encrypt1()
F2 = Encrypt2()
while (True):
    x = input('Digite um número: ')
    print('Número cifrado...')
    print(F1.function(float(x)))
    print('Número decifrado...')
    print(F1.inverse(F1.function(float(x))))
    
    x = input('Digite um número: ')
    print('Número cifrado...')
    print(F2.function(float(x)))
    print('Número decifrado...')
    print(F2.inverse(F2.function(float(x))))
    
