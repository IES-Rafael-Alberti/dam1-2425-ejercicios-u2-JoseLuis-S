# Define la funcion comprobar_mayoria_edad que comprueba si la edad introducida
# es mayor o menor a 18 años
def comprobar_mayoria_edad(edad):
    # Si la edad es mayor o igual a 18 es mayor de edad
    if edad >= 18:
        return print('Felicidades!! Puedes tomarte una cerveza e ir a la carcel.')
    # Si la edad introducida es menor a 18 es menor de edad
    if edad < 18:
        return print('Felicidades!! Aun puedes no tener responsabilidades.')

# Define la funcion pedirEdad que lee un numero y lo devuelve
def pedirEdad():
    # Lee el dato introducido
    edad = input('Introduce tu edad: ')

    # Mientras que la funcion comprobarEdad no devuelva que el dato
    # introducido es un entero pedira la edad
    while comprobarEdad(edad) is not True:
        edad = input('ERROR, introduce una edad valida: ')
        
    return int(edad)

# Define la funcion comprobarEdad que asegura que el numero introducido sea
# un entero natural
def comprobarEdad(edad: str):
    # Elimina los espacios tras convertir num en str
    edad = edad.strip()

    # Comprueba que la edad introducida unicamente contenga numeros enteros naturales
    for i in edad:
        if i not in '0123456789':
            return False 

    # Si todas las anteriores no se cumplen significa que es un entero natural,
    # por lo que devuelve True
    return True

# Define la funcion main
def main():
    edad = pedirEdad()
    comprobar_mayoria_edad(edad)
    
# Ejecuta la funcion main
if __name__ == "__main__":
    main()
