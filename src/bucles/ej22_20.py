def comprobar_letra_en_frase(frase, letra):
    for i in frase:
        if letra not in i:
            print(f'En la posicion {i} no esta la letra {letra}')
        else:
            return f'En la posicion {i} esta la letra {letra}'

    return f'La letra {letra} no esta en la frase ({frase}).'


def pedir_frase_letra(index):
    comprobacion = False
    mensajes = ['Introduce una frase: ', 'Introduce una letra: ']

    while not comprobacion:
        try:
            frase_letra = input(mensajes[index])
            for i in frase_letra:
                if i.isdigit():
                    frase_letra = ''
                    raise ValueError
                else:
                    comprobacion = True

        except ValueError:
            print('Valor introducido no valido')
        
        except:
            print('Error desconocido')

    return frase_letra.strip()

def main():
    frase = pedir_frase_letra(0)
    letra = pedir_frase_letra(1)
    resultado = comprobar_letra_en_frase(frase, letra)

    print(resultado)


if __name__ == '__main__':
    main()