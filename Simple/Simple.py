import pprint
import random

'''
Genero un diccionario con edades aleatorias e ID predefinido
'''
def CrearDiccionario():
        diccionario = dict([('1', random.randint(0,100)),
                            ('2', random.randint(0,100)),
                            ('3', random.randint(0,100)),
                            ('4', random.randint(0,100)),
                            ('5', random.randint(0,100)),
                            ('6', random.randint(0,100)),
                            ('7', random.randint(0,100)),
                            ('8', random.randint(0,100)),
                            ('9', random.randint(0,100)),
                            ('10', random.randint(0,100))])
        return diccionario

'''
Busco a la persona de menor y mayor edad
'''
def SegundaFuncion(diccionario):
    persona = []
    persona2 = []
    maximo = 0
    minimo = 100
    
    for personaId, edad in diccionario.items():
        if edad > maximo:
            maximo = edad
            persona = [personaId, edad]
    print('La persona de mayor edad es la de ID', persona[0], "con", persona[1], "años")
    
    for personaId, edad in diccionario.items():
        if edad < minimo:
            minimo = edad
            persona2 = [personaId, edad]
    print('La persona de menor edad es la de ID', persona2[0], "con", persona2[1], "años")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    diccionario = CrearDiccionario()

    print("Diccionario generado:")
    pprint.pprint(diccionario)
    SegundaFuncion(diccionario)