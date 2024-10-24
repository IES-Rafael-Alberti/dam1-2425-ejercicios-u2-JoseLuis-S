def pedir_contraseña():
    contraseña = input('\nIntroduce la contraseña: ')
    return contraseña

def main():
    password = 'contraseña'
    contraseña = pedir_contraseña()

    while contraseña != password:
        print('\nCONTRASEÑA INCORRECTA.')
        contraseña = pedir_contraseña()

    print('\nContraseña introducida con exito.\n')

if __name__ == '__main__':
    main()