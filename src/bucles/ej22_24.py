def comprobar_primo(num: int) -> str:
    '''Comprueba si el numero introducido es un numero primo o no

    Args: 
        num (int): Numero a comprobar si es primo o no

    Returns:
        str: Devuelve un mensaje en funcion de si el numero es
        primo o no
    
    '''
    numDivisores = 0

    # Con este bucle for se calcula el numero de divisores,
    # comienza desde el 1 hasta 1 numero menos que el numero
    # introducido
    for i in range (1, num):
            # Si el modulo de la division es 0 se le suma un
            # divisor
            divisores = num % i
            if divisores == 0:
                numDivisores += 1

    if numDivisores > 1:
        return False
    else:
        return True


def pedir_num():
    comprobacion = False

    while not comprobacion:
        try:
            num = int(input('Introduce un numero mayor que 1 (introduce 0 para terminar): '))
            
            if num != 0:
                if num < 1:
                    raise ValueError
                else:
                    comprobacion = True
            else:
                comprobacion = True

        except ValueError:
            print('Numero no valido')

        except:
            print('Error desconocido')

    return num

def main():
    comprobacion = False
    lista_nums = []
    lista_primos = []
    lista_no_primos = []

    while not comprobacion:
        num = pedir_num()
        if num == 0:
            comprobacion = True
        else:
            lista_nums.append(num)
            if comprobar_primo(num) is True:
                lista_primos.append(num)
            else:
                lista_no_primos.append(num)
    
    print(f'\nHas introducido {len(lista_nums)} numeros.\nSon:\n{lista_nums}\nDe ellos {len(lista_primos)} son primos, y son:\n{lista_primos}\nHay {len(lista_no_primos)} no primos, que son:\n{lista_no_primos}')

if __name__ == '__main__':
    main()