import numpy as np
import random

def crear_matriz():
    matriz = np.random.randint(1,5, size=(5,5))
    return matriz
    
def buscar_consecutivos(matriz):
    """
    Comienzo a recorrer la matriz en busca de consecutivos horizonal o verticalmente. Defino el resultado final como defecto
    """
    resultado = "No hay consecutivos"
    for i in range(5):       
        for j in range(5):
            if j < 2:
                 inicial = matriz[i][j]
                 if matriz[i][j+1]-1 == inicial and matriz[i][j+2]-2 == inicial and matriz[i][j+3]-3 == inicial:
                     resultado = (f'(Horizontal)Numeros consecutivos entre [{i}][{j}] y [{i}][{j+3}] : {matriz[i][j]}, {matriz[i][j+3]}')
        if i < 2:
            inicial1 = matriz[i][j]
            if matriz[i+1][j]-1 == inicial1 and matriz[i+2][j]-2 == inicial1 and matriz[i+3][j]-3 == inicial1:
                resultado = (f'(Vertical)Numeros consecutivos entre [{i}][{j}] y [{i+3}][{j}] : {matriz[i][j]}, {matriz[i+3][j]}')
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    matriz = crear_matriz()
    print("La matriz generada es: \n" ,matriz)
    print(buscar_consecutivos(matriz))