class circulo:
    def __init__(self):
        self.__raio = 0
    def set_base(self, v):
        if v > 0: self.__raio = v
        else: raise ValueError()
    def get_base(self, v):
        return self.__raio