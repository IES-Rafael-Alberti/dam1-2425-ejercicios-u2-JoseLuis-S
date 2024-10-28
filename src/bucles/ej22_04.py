def generar_cuenta_regresiva(num):
    lista = []

    for i in reversed(range (num + 1)):
        lista.append(i)

    return lista        

        
def pedir_numero():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero para la cuenta regresiva (mayor que 0): '))
            while num < 0:
                num = int(input('Introduce un numero para la cuenta regresiva (mayor que 0): '))

            comprobacion = True

        except ValueError:
            print('\n**ERROR**\n Numero no valido.')
        
        except:
            print('Error desconocido.')
    
    return num


def main():
    num = pedir_numero()
    lista = generar_cuenta_regresiva(num)
    
    print(f'La cuenta regresiva, desde {num} hasta 0, seria {lista}.')


if __name__ == '__main__':
    main()