def contador_pares_impares(digitos_num):
    num_impares = 0
    num_pares = 0
    lista_pares = []
    lista_impares = []

    for i in range (len(digitos_num)):
        if int(digitos_num[i])%2 != 0:
            num_impares += 1
            lista_impares.append(digitos_num[i])
        else:
            num_pares += 1
            lista_pares.append(digitos_num[i])
    
    return num_pares, num_impares, lista_pares, lista_impares

def dividir_num(num):
    return list(str(num))


def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero entero positivo (Introduce 0 para terminar): '))
            if num < 0:
                raise ValueError

            comprobacion = True

        except ValueError:
            print('Valor no valido')

        except:
            print('Error desconocido')
        
    return num


def main():
    num_total_pares = 0
    num_total_impares = 0
    nums_pares = []
    nums_impares = []
    confirmacion = False

    while not confirmacion:
        num = pedir_num()
        if num != 0:
            digitos_num = dividir_num(num)
            num_pares_impares = contador_pares_impares(digitos_num)
            num_total_pares += num_pares_impares[0]
            num_total_impares += num_pares_impares[1]

            if len(num_pares_impares[2]) > 0:
                nums_pares.append(num_pares_impares[2])

            if len(num_pares_impares[3]) > 0:
                nums_impares.append(num_pares_impares[3])

            print(f'El numero {num} tiene {num_pares_impares[0]} pares ({num_pares_impares[2]}) y {num_pares_impares[1]} impares ({num_pares_impares[3]}).')

        else:
            confirmacion = True
    
    print(f'\nSe han introducido {num_total_pares} numeros pares y {num_total_impares} numeros impares.\n**Numeros pares**:\n{nums_pares}\n**Numeros impares**:\n{nums_impares}\n')


if __name__ == '__main__':
    main()