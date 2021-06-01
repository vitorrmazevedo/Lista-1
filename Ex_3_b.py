class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    def subtrai(self):
        return self.a - self.b
    def multiplica(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
    def __init__(self, param1, param2) :
        self.a = param1
        self.b = param2

result = Calculadora(10,5)
print("Soma: ", result.soma())
print("subtração: ", result.subtrai())
print("multiplicação: ", result.multiplica())
print("divisão: ", result.divide())
