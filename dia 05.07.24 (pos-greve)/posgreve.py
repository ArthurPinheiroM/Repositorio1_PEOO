import math
class circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        return self.raio**2 * math.pi
    def circu(self):
        return 2*self.raio * math.pi

ct = circulo()
ct.raio = float(input("Qual o raio do circulo?"))
print(f"A circuferencia é:{ct.circu()}")
print(f"A area é:{ct.area()}")
