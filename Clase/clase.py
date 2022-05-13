import math

class Circulo:
    def __init__(self, radio):
        self.radio= float(radio)

    def __repr__(self):
        return "Objeto círculo".upper().center(50, "=") 

    def calculo_area(self, radio):
        area= ((math.pi)*(radio**2))
        print("El area del circulo es: ", area)


    def calculo_perimetro(self, radio):
        perimetro= (2*(math.pi)*radio)
        print("El perimetro del circulo es de: ", perimetro)


class Xcirculo:
    def __init__(self, radio, factor):
        self.radio= float(radio)
        self.factor= float(factor)

    def multiplicar (self, radio, factor):
        operacion=radio*factor
        print("El resultado de la multiplicación es", operacion)

    def __repr__(self):
        return "Se ha creado el nuevo objeto".upper().center(50, "=") 
 
def error_check(in_value):
    if in_value <=0:
        print("El valor ingresado no puede ser menor o igual a cero.")
        exit()
   
    
def info_circulo():
    print(nuevocirculo)
    nuevocirculo.calculo_area(nuevoradio)
    nuevocirculo.calculo_perimetro(nuevoradio)

def nuevo_objeto():
    factor=float(input("Ingrese el factor que multiplicará el radio: "))
    error_check(factor)
    nuevo_objeto = Xcirculo(nuevoradio, factor)
    print(nuevo_objeto)
    nuevo_objeto.multiplicar(nuevoradio, factor)

    
nuevoradio=float(input("Ingrese el radio del circulo en cm: "))

error_check(nuevoradio)
"""
>>> error_check(7)

>>> error_check(-8)
print("El valor ingresado no puede ser menor o igual a cero.")
"""
nuevocirculo = Circulo(nuevoradio)
info_circulo()
nuevo_objeto()

if __name__=="__main__":
    import doctest
    doctest.testmod()
