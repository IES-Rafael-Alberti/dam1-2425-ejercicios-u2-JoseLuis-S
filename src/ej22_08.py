def calcular_serie(num_max):
    serie = ''

    for i in reversed(range (1, num_max + 3, 2)):
        serie += str(i) + ' '
    
    return serie 


def pedir_altura():
    comprobacion = False

    while not comprobacion:
        try:
            altura = int(input('Introduce la altura del triangulo: '))

            while altura < 0:
                altura = int(input('Introduce la altura del triangulo: '))

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\n Numero no valido.')
        
        except:
            print('Error desconocido.')
    
    return altura


def main():
    altura = pedir_altura()
    num_max = altura * 2
    serie = calcular_serie(num_max)

    print(serie)    

        
if __name__ == '__main__':
    main()