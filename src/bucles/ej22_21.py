def cantidad_a_pagar(cantidad_total):
    if cantidad_total > 1000:
        return cantidad_total * 0.9
    else:
        return cantidad_total


def obtener_cantidad_total():
    pagos = []
    cantidad_total = 0
    comprobacion = False

    while not comprobacion:
        cantidad = pedir_cantidad()

        if cantidad == 0:
            comprobacion = True
        else:
            pagos.append(cantidad)
            cantidad_total += cantidad

    return cantidad_total, pagos


def pedir_cantidad():
    comprobacion = False

    while not comprobacion:
        try:
            cantidad = float(input('Introduce la cantidad de la compra: '))

            if cantidad < 0:
                raise ValueError
            else:
                comprobacion = True

        except ValueError:
            print('Valor no valido')

        except:
            print('Error desconocido')

    return cantidad


def main():
    cantidad_total, pagos = obtener_cantidad_total()
    resultado = cantidad_a_pagar(cantidad_total)

    print(f'\nSe han hecho los siguientes pagos:\n{pagos}\nEl total es de {cantidad_total}€.\nDebera pagar {resultado}€.')

if __name__ == '__main__':
    main() 