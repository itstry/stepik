# import


def main():
    input_list = []
    operator_list = ['+', '-', '/', '*']

    print('Первое число', end=' ')
    num_1 = input()
    if not num_1.isnumeric():
        print('Error, it\'s not number')
        exit()

    print('Оператор ', end=' ')
    operator_in = input()
    if operator_in not in operator_list:
        print('Error, it\'s not only the following operators are supported', operator_list)
        exit()

    print('Второе число', end=' ')
    num_2 = input()
    if not num_2.isnumeric():
        print('Error, it\'s not number')
        exit()

    if operator_in == '+':
        print(f'{num_1} + {num_2} =', end=' ')
        print(sum(((int(num_1)), int(num_2))))



if __name__ == '__main__':
    main()
