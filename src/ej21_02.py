'''
Este algoritmo se encarga de pedir una contraseña y luego preguntar la contraseña para comprobar
si se ha introducido por segunda vez de manera correcta
'''

# Define la funcion comprobarContraseña que comprueba si la contraseña
# introducida es igual a la contraseña puesta
def comprobarContraseña(contraseña, contraseñaIntroducida):
    # Si la contraseña introducida no es igual a la anterior
    # muestra mensaje de error
    if contraseña != contraseñaIntroducida:
        return 'Has introducido la contraseña incorrecta.'
    # Si la contraseña introducida es igual a la anterior
    # muestra mensaje de exito
    if contraseña == contraseñaIntroducida:
        return 'Has introducido la contraseña con exito.'

# Define la funcion preguntarContraseña que pregunta la contraseña
# puesta anteriormente 
def preguntarContraseña():
    contreñaIntroducida = input('Dime la contraseña: ')
    # Devuelve la contraseña en minusculas
    return contreñaIntroducida.lower()

# Define la funcion pedir contraseña que lee una contraseña
def pedirContraseña():
    contraseña = input('Introduce la contraseña: ')
    # Devuelve la contraseña en minusculas
    return contraseña.lower()

# Define la funcion main
def main():
    contraseña = pedirContraseña()
    contraseñaIntroducida = preguntarContraseña()
    print(comprobarContraseña(contraseña, contraseñaIntroducida))

# Ejecuta la funcion main
if __name__ == "__main__":
    main()