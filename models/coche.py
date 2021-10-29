# Definicion de objeto coche

class coche:
    """Atributos privados de clase"""
    __ruedas = 4

    """Contructor de clase"""
    def __init__(self, color, aceleracion):
        self.__color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Metodos proios de clase"""
    def acelera(self):
        for i in range(1, 10):
            self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0
        self.velocidad = v

    """getters y setters"""
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, newColor):
        print("Atributo color modificado")
        self.__color = newColor

    @color.deleter
    def color(self):
        print("Atributo color eliminado")
        # del self.__color
        self.__color = ""


    """metodo object to String"""
    def __str__(self) -> str:
        return "ruedas: " + str(self.__ruedas) + \
               ", color: " + self.__color + \
               ", aceleracion: " + str(self.aceleracion) + \
               ", velocidad: " + str(self.velocidad)






