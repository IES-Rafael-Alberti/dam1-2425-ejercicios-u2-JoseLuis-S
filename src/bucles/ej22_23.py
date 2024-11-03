def sumar_linea(comando):
    lineas = ''
    lineas += comando + ','
    return lineas


def contar_nums(lineas):
    cantidad_nums = 0

    for i in lineas:
        if i in '1234567890':
            cantidad_nums += 1
    
    return cantidad_nums


def pedir_comando():
    comando = input('Libro: ').strip()
    return comando


def main():
    asterisco = False
    lineas = ''
    cantidad_nums = 0
    num_lineas = 0

    while not asterisco:
        comando = pedir_comando()

        if comando == '/' and len(comando) == 1:
            print(f'Linea completa. Aparecen {cantidad_nums} digitos numericos.')
            num_lineas += 1
            cantidad_nums = 0
        elif comando == '*' and len(comando) == 1:
            print(f'Fin. Se leyeron {num_lineas} lineas completas.')
            asterisco = True
        else:
            lineas = sumar_linea(comando)
            nums = contar_nums(lineas)
            cantidad_nums += nums


if __name__ == '__main__':
    main()