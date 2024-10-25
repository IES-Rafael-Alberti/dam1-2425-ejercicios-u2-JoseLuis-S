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
    nums_separados = list(num)
    suma = 0
    num_de_pares = []
    cantidad_de_pares = 0


    while num != -1:
        lista_nums.append(num)
        
        if (num % 2) == 0:
            cantidad_de_pares += 1
            num_de_pares.

        for i in range (len(nums_separados)):
            suma += int(nums_separados[i])

        print('\nPara terminar el script escriba (-1).\n')


        num = pedir_num()

    print(f'\nEl numero mas alto introducido es .\n')
    

if __name__ == '__main__':
    main()