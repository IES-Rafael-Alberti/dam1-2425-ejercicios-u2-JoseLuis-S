'''
Ej21_07

Este algoritmo determina en funcion de tu renta anual la cantidad que debes tributar
en funcion de tus ingresos anuales

Funciones disponibles:
    * calcular_impuestos - calcula la cantidad de impuestos que debe pagar el usuario
    * determinar_tramo - determina en que tramo se encuentra el usuario
    * pedir_renta_anual - pide la renta anual al usuario
    * main - funcion principal
'''

RENTAS = (
    (0, 10000, 5),
    (10000, 20000, 15),
    (20000, 35000, 20),
    (35000, 60000, 30),
    (60000, None, 45)
)

def calcular_impuestos(renta: float, porcentaje: int) -> float:
    '''
    Esta funcion calcula la cantidad de impuestos a pagar por el usuario

    Args:
        renta (float): Renta anual del usuario
        porcentaje (int): Porcentaje a pagar 

    Returns:
        float: Retorna cantidad a pagar por el usuario
    '''
    return renta*(porcentaje/100)


def determinar_tramo(renta: float, RENTAS: tuple) -> tuple:
    '''
    Esta funcion determina en que tramo se encuentra el usuario, en funcion
    del tramo en que este asigna un minimo, un maximo y un porcentaje

    Args:   
        renta (float): Renta anual del usuario
        RENTAS (tuple): Tupla con los tramos y porcentajes 

    Returns:
        tuple: Retorna los valores entre los que se encuentra la renta y el
        porcentaje que le toca pagar
    '''
    for tramos in RENTAS:
        minimo = tramos[0]
        maximo = tramos[1]
        porcentaje = tramos[2]

        if maximo is None or (minimo <= renta < maximo):
            return minimo, maximo, porcentaje
    
    return 0


def pedir_renta_anual() -> float:
    '''
    Este algoritmo pide la renta anual al usuario

    Returns:
        float: Retorna la renta anual del usuario
    '''
    while True:
        try:
            renta = float(input('Introduce tu renta anual: '))
            return renta
        except ValueError:
            print('ERROR, introduce un importe valido.')


def main():
    ''' Funcion main '''
    renta_anual = pedir_renta_anual()
    minimo, maximo, porcentaje = determinar_tramo(renta_anual, RENTAS)
    cantidad_impuestos = calcular_impuestos(renta_anual, porcentaje)

    if renta_anual < 0:
        print(f'No has ganado dinero, por lo que no tendras que tributar.')
    elif maximo is None:
        print(f'Has ganado {renta_anual} euros, estas en el tramo maximo y tienes que pagar {cantidad_impuestos} euros, que es un {porcentaje}%.')
    else:
        print(f'Has ganado {renta_anual} euros, estas en el tramo de {minimo} euros a {maximo} euros y tienes que pagar {cantidad_impuestos} euros, que es un {porcentaje}%.')
    

if __name__ == "__main__":
    main()