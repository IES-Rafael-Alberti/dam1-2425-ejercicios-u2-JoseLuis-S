'''
Ej21_08

Este algoritmo calcula el salario del usuario en funcion de la puntuacion que 
le hayan asignado

Funciones disponibles:
    * calcular_salario - calcula el salario en funcion de la puntuacion
    * pedir_puntuacion - pide la puntuacion al usuario
    * main - funcion principal

'''
PUNTUACIONES = (0, 0.4, 0.6)
SALARIO_BASE = 2400

def calcular_salario(puntuacion: float, salario: int) -> float:
    '''
    Esta funcion calcula el salario del usuario en funcion de su
    puntuacion

    Args:
        puntuacion (float): La puntuacion del usuario
        salario (int): El salario base

    Returns: 
        float: Retorna el salario final del usuario
    '''
    return salario * puntuacion


def pedir_puntuacion() -> float:
    '''
    Esta funcion pide la puntuacion al usuario

    Returns: 
        float: Retorna la puntuacion del usuario
    '''
    not_true = False

    while not not_true:
        try:
            puntuacion = float(input('Introduce tu puntuacion (0.0, 0.4, 0.6 o superior): '))

            if puntuacion > 0.6:
                return puntuacion
            
            else:
                while puntuacion not in (PUNTUACIONES):
                    puntuacion = float(input('ERROR, introduce puntuacion valida (0.0, 0.4, 0.6 o superior): '))

            not_true = True
            
        except ValueError:
            puntuacion = float(input('ERROR, introduce puntuacion valida (0.0, 0.4, 0.6 o superior): '))
    
    return float(puntuacion)
            

def main():
    ''' Funcion main  '''
    puntuacion = pedir_puntuacion()
    salario = calcular_salario(puntuacion, SALARIO_BASE)
    
    print(f'Este mes has tenido una puntuacion de {puntuacion} y vas a ganar {salario} euros.')

if __name__ == '__main__':
    main()