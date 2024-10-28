def contador_palabras(frase):
    


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

if __name__ == '__main__':
    main()