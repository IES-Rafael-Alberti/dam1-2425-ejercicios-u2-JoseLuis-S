def division(num1: float, num2: float) -> float:
    return num1/num2

def pedirNums() -> float:
    num1 = input('Introduce el dividendo de la division: ')
    num2 = input('Introduce el divisor de la division: ')

def main() -> None:
    num1, num2 = pedirNums()

if __name__ == '__main__':
    main() 