def comprobar_contraseña(password):
    comprobacion = False

    while not comprobacion:
        try:
            contraseña = input('Introduce la contraseña: ')
            if contraseña == password:
                comprobacion = True
            else:
                raise NameError

        except NameError:
            print('Incorrect Password!!')

        except:
            print('Error desconocido')

    print('Contraseña introducida con exito!!')

def main():
    password = 'contraseña'
    comprobacion = comprobar_contraseña(password)

if __name__ == '__main__':
    main()