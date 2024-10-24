RANGOS_EDADES = (0, 4, 18)
PRECIOS = (0, 5, 10)

def determinar_precio(edad, edades, precios):
    if edad < edades[1]:
        return f'Tienes {edad} años y tienes que pagar {precios[0]} euros.'
    if edades[1] < edad < edades[2]:
        return f'Tienes {edad} años y tienes que pagar {precios[1]} euros.'
    if edad > edades[2]:
        return f'Tienes {edad} años y tienes que pagar {precios[2]} euros.'


def pedir_edad():
    confirmacion = False

    while not confirmacion:
        try:
            edad = int(input('Introduce tu edad: '))
            if edad < 0 or edad > 120:
                edad = int(input('\n**ERROR**\nIntroduce edad valida: '))
            confirmacion = True
            
        except ValueError:
            print('\n**ERROR**\nEdad no valida.')
    
    return edad


def main():
    edad = pedir_edad()
    resultado = determinar_precio(edad, RANGOS_EDADES, PRECIOS)
    print(resultado)

if __name__ == '__main__':
    main()