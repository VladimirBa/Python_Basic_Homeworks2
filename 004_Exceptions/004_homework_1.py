def cont():
    c = input("Do you want to stop computing? Enter Y if yes: ")
    while True:
        if c == "Y" or c == 'y':
            return None
        else:
            return main()


def div(x, y):
    try:
        x / y
    except ZeroDivisionError as error:
        print(error)
    else:
        print(f"Result: {(x / y):.3f}")


def mul(x, y):
    print(f"Result: {(x * y):.3f}")


def add(x, y):
    print(f"Result: {(x + y):.3f}")


def sub(x, y):
    print(f"Result: {(x - y):.3f}")


def exp(x, y):
    try:
        x ** y
    except ZeroDivisionError as error:
        print(error)
    else:
        print(f"Result: {(x ** y):.3f}")


def main():
    while True:
        enter_x = input('Enter the first number: ')
        try:
            x = float(enter_x)
        except ValueError as error:
            print(error)
        else:
            break

    d = input('Enter the type of operation on numbers: ')
    try:
        if d not in ['+', '-', '*', '/', '**']:
            raise Exception
    except Exception:
        print('Enter valid operation sign.')
        main()

    while True:
        enter_y = input('Enter the second number: ')
        try:
            y = float(enter_y)
        except ValueError as error:
            print(error)
        else:
            break

    if d == '/':
        div(x, y)
    elif d == '*':
        mul(x, y)
    elif d == '+':
        add(x, y)
    elif d == '-':
        sub(x, y)
    elif d == '**':
        exp(x, y)
    cont()


if __name__ == "__main__":
    main()
