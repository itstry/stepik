# 2 день; +56 задача; всего: 56
operator_list = ['-', '+', '*', '/']


def calc(x: int, y: int, operator: str) -> any:
    if y == 0 and operator == '/':
        return 'На ноль делить нельзя!'
    elif operator == operator_list[0]:
        return x - y
    elif operator == operator_list[1]:
        return x + y
    elif operator == operator_list[2]:
        return x * y
    elif operator == operator_list[3]:
        return x / y
    elif operator != any(operator_list):
        return 'Неверная операция'


if __name__ == '__main__':
    print(calc(int(input()), int(input()), str(input())))
