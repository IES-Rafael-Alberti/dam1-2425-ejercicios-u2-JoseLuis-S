def pedir_nombre():
    nombre = input('Introduce tu nombre: ')
    return nombre

def main():
    nombre = pedir_nombre()

    for i in range (10):
        print(nombre)   

if __name__ == '__main__':
    main() 