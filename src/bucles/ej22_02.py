
def contar_anios(edad):
    anios_cumplidos = []

    for i in range(edad + 1):
        anios_cumplidos.append(i)  

    return anios_cumplidos

def pedir_edad():
    comprobacion = False

    while not comprobacion:
        try:
            edad = int(input('Introduce tu edad: '))

            if 0 < edad > 120:
                edad = int(input('\n**ERROR**\nIntroduce tu edad: '))

            comprobacion = True

        except ValueError:
            print('EDAD NO VALIDA')

    return edad


def main():
    edad = pedir_edad()
    anios_cumplidos = contar_anios(edad)

    print(f'Tienes {edad} y has cumplido {anios_cumplidos} hasta ahora.')

if __name__ == '__main__':
    main()