# Funções de criptografia em Pyhton

class Encrypt1(object):
    def function(self, x: float):
        return (2 * x) - 6
    def inverse(self, y: float):
        return (y /2) + 3

F = Encrypt1()
print(F.function(9))
print(F.inverse(F.function(9)))
