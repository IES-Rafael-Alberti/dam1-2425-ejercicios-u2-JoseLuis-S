def division(num1: float, num2: float) -> float:
    return num1/num2

def pedirNum() -> float:
    num = input('pinga')
    return num

def main() -> None:
    num1 = pedirNum()
    num2 = pedirNum()
    division(num1, num2)

if __name__ == '__main__':
    main() 