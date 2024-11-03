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
    nums_separados = list(str(num))
    suma = 0
    lista_num_pares = []
    cantidad_de_pares = 0


    while num != -1:
        lista_nums.append(num)
        nums_separados = list(str(num))
        
        if (num % 2) == 0:
            cantidad_de_pares += 1
            lista_num_pares.append(num)

        for i in range (len(nums_separados)):
            suma += int(nums_separados[i])

        nums_separados = []

        print('\nPara terminar el script escriba (-1).\n')

        print(f'La suma es igual de los digitos de {num} es {suma}.\n')

        suma = 0
        num = pedir_num()

    print(f'\nHas introducido {cantidad_de_pares} numeros pares, los numeros pares son:\n{lista_num_pares}\nLista de todos los numeros introducidos:\n{lista_nums}')
    

if __name__ == '__main__':
    main()