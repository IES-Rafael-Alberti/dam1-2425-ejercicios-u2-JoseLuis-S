def separador_palabras(frase):
    return frase.split(' ')


def contador_palabras(palabras):
    return len(palabras)


def pedir_frase():
    comprobacion = False

    while not comprobacion:
        try:
            frase = input('Introduce una frase: ').strip()
            
            if frase.isdigit():
                raise ValueError
            
            comprobacion = True
        
        except ValueError:
            print('Frase no valida')
        
        except:
            print('Error desconocido')

    return frase


def main():
    frase = pedir_frase()
    lista_palabras = separador_palabras(frase)
    num_palabras = contador_palabras(lista_palabras)
    palabras = list(lista_palabras)
    palabra_larga = max(palabras, key=len)

    print(f'La palabra mas larga es ({palabra_larga}) y tiene ({num_palabras}) palabras.\nFrase: {frase}')





if __name__ == '__main__':
    main()