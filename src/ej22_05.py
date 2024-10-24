def calcular_intereses_x_anio(anios, cantidad, interes):
    dinero_x_anios = []
    cantidad_temp = cantidad

    for i in range (anios):
        cantidad_final = cantidad_temp * (1 + interes/100)
        cantidad_temp = cantidad_final

        dinero_x_anios.append(round(cantidad_final, 2))

    return dinero_x_anios
    

def pedir_interes():
    comprobacion = False

    while not comprobacion:
        try:
            interes = float(input('Introduce el interes: '))

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\n Numero no valido.')
        
        except:
            print('Error desconocido.')
    
    return interes

def pedir_anios():
    comprobacion = False

    while not comprobacion:
        try:
            anios = int(input('Introduce la cantidad de años para invertir: '))

            while anios < 0:
                anios = int(input('Introduce la cantidad de años para invertir: '))

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\n Numero no valido.')
        
        except:
            print('Error desconocido.')
    
    return anios


def pedir_cantidad():
    comprobacion = False

    while not comprobacion:
        try:
            cantidad = float(input('Introduce la cantidad para invertir: '))
            while cantidad < 0:
                cantidad = float(input('Introduce un numero para la cuenta regresiva (mayor que 0): '))

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\n Numero no valido.')
        
        except:
            print('Error desconocido.')
    
    return cantidad


def main():
    cantidad = pedir_cantidad()
    anios = pedir_anios()
    interes = pedir_interes()
    dinero_x_anios = calcular_intereses_x_anio(anios, cantidad, interes)

    print('La cuenta ha generado en cada año: ')

    for i in range (len(dinero_x_anios)):
        print(f'Año {i + 1}: {dinero_x_anios[i]} euros.')

if __name__ == '__main__':
    main()