def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero entero: '))

            comprobacion = True

        except ValueError:
            print('Numero no valido.')
        
        except:
            print('Error desconocido.')
        
    return num


def main():
    num = pedir_num()
    lista_nums = []

    while num != 0:
        lista_nums.append(num)
        print('\nPara terminar el script escriba (0).\n')
        num = pedir_num()

    num_max = max(lista_nums)

    print(f'\nEl numero mas alto introducido es {num_max}.\n')
    

if __name__ == '__main__':
    main()