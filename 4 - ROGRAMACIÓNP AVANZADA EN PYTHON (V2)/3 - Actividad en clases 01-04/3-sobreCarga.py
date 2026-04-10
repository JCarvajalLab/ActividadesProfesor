class Calculadora:
    # def suma(self, a, b):
    #     return a + b
    # def suma(self, a, b, c = 0):
    #     return a + b + c
    def suma(self, *args):
        return sum(args)
calc = Calculadora()

print(calc.suma(1,2))
print(calc.suma(1,2,3))
print(calc.suma(1,2,3,4,5,6,7,8,9,10,11,12,13))