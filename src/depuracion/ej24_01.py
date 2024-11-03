'''
Ej24_01 Algoritmo Burbuja

Este algoritmo ordena los numeros de una lista

Funciones disponibles
    * algoritmo_burbuja - funcion que ordena los valores de una lista de menor a mayor
    * main - funcion principal
'''


def algoritmo_burbuja (a: list, n: int) -> list:
    '''
    Esta funcion ordena los valores de una lista de menor a mayor

    Args:
        a: Lista
        n: Longitud lista

    Returns:
        list: Retorna la lista ordenada de menor a mayor
    '''
    for i in range (n): # Bucle padre
        cambio = False
        for j in range (n - i - 1): # Bucle hijo
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cambio = True

            if not cambio:
                break

    return a

def main():
    ''' Funcion principal '''
    a = [8, 3, 1, 19, 14]
    n = len(a)
    nueva_lista = algoritmo_burbuja(a, n)

    print(nueva_lista)


if __name__ == '__main__':
    main()
