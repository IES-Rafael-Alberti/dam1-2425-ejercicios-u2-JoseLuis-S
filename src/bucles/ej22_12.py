def comprobar_letra(letra):
    for i in letra:
        if i not in 'asdfghjklqwertyuiopzxcvbnm':
            return False
        
    return True


def pedir_letra():
    letra = input('Introduce una letra: ')
    comprobacion = comprobar_letra(letra)

    while not comprobacion:
        letra = input('Introduce una palabra: ')
        comprobacion = comprobar_letra(letra)

    return letra

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
    letra = pedir_letra()
    numero_veces = 0

    for i in range (len(palabra)):
        letras_palabra = list(palabra)

        if letra == letras_palabra[i]:
            numero_veces += 1
        

    print(f'La letra ({letra}) aparece {numero_veces} veces en la palabra {palabra}.')

    '''
    Tambien puede hacerse asi y es mas sencillo
    
    numero_de_veces = palabra.count(letra)
    '''

if __name__ == '__main__':
    main()