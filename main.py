def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def pow(a, b):
    return a ** b

def sqrt(a):
    return a ** 0.5


if __name__ == '__main__':
    a, b = 10, 5
    print(f"Сумма: {sum(a, b)}")
    print(f"Разность: {sub(a, b)}")
    print(f"Произведение: {mul(a, b)}")
    print(f"Частное: {div(a, b)}")