'''
Ej 21_06 

Este algoritmo determina a que grupo perteneces en funcion de tu nombre y sexo

Funciones disponibles:
    * determinar_grupo - determina a que grupo pertenece el usuario
    * pedir_genero - pide el genero
    * pedir_nombre - pide el nombre
    * main - funcion principal
'''
GRUPOS = ['A', 'B']
LETRA_HOMBRE = 'N'
LETRA_MUJER = 'M'

def determinar_grupo(genero: str, nombre: str, GRUPOS: list, LETRA_HOMBRE: str, LETRA_MUJER: str) -> str:
    '''
    Determina en funcion del genero y el grupo a que grupo pertenece el usuario

    Args:
        genero (str): Genero del usuario
        nombre (str): Nombre del usuario
        GRUPOS (list): Grupos posibles
        LETRA_HOMBRE (str): Letra que determina en que grupo vas para hombres
        LETRA_MUJER (str): Letra que determina en que grupo vas para mujeres

    Returns:
        str: Grupo al que pertenece 
    
    '''
    if genero == 'masculino':
        if ord(nombre[0]) > ord(LETRA_HOMBRE):
            return GRUPOS[0]
        else: 
            return GRUPOS[1]
    else:
        if ord(nombre[0]) < ord(LETRA_MUJER):
            return GRUPOS[0]
        else:
            return GRUPOS[1]


def pedir_genero() -> str:
    '''
    Pide el genero al usuario y comprueba que no tenga numeros
    
    Returns:
        str: Retorna el genero escrito en minusculas 
    '''
    genero = input('Introduce tu genero (masculino o femenino): ').lower()
    while genero not in ('masculino', 'femenino'):
        genero = input('ERROR, introduce tu genero (masculino o femenino): ').lower()
    return genero.lower()

def pedir_nombre() -> str:
    '''
    Pide el nombre al usuario y comprueba que no contenga numeros
    
    Returns:
        str: Retorna el nombre escrito en minusculas
    '''
    nombre = input('Introduce tu nombre: ').strip()
    while True:
        contiene_numeros = False  
        
        for i in nombre:
            contiene_numeros = contiene_numeros or (i in '0123456789')
        
        if contiene_numeros:
            nombre = input('ERROR, introduce un nombre valido: ').strip()
        else:
            return nombre.title()

def main():
    ''' Funcion main '''
    nombre = pedir_nombre()
    genero = pedir_genero()
    resultado = determinar_grupo(genero, nombre, GRUPOS, LETRA_HOMBRE, LETRA_MUJER)

    print(f'Hola {nombre}, tu genero es {genero} y perteneces al grupo {resultado}.')

if __name__ == '__main__':
    main()