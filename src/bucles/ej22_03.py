def generar_serie(num):
    serie = []

    for i in range(1, num, 2):
        serie.append(i)

    return serie

def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero positivo: '))

            while num < 0:
                num = int(input('Introduce un numero positivo: '))
        
            comprobacion = True

        except ValueError:
            print('NUMERO NO VALIDO')

    return num


def main():
    num = pedir_num()
    serie = generar_serie(num)
    print(serie)

if __name__ == '__main__':
    main()