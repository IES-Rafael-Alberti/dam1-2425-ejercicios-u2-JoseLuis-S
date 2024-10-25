def invertir_palabra(palabra):
    return palabra[::-1]


def comprobar_palabra(palabra):
    for i in palabra:
        if i not in 'asdfghjklqwertyuiopzxcvbnm':
            return False
        
    return True

def pedir_palabra():
    palabra = input('Introduce una palabra: ')
    comprobacion = comprobar_palabra(palabra)

    while not comprobacion:
        palabra = input('Introduce una palabra: ')
        comprobacion = comprobar_palabra(palabra)

    return palabra


def main():
    palabra = pedir_palabra()
    palabra_invertida = invertir_palabra(palabra)

    for i in range (len(palabra)):
        letras = list(palabra_invertida)
        print(letras[i])

if __name__ == '__main__':
    main()