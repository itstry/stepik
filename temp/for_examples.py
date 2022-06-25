# 2 день; +55 задача; всего: 55
def func(x):
    if (i := x) < 60:
        print('Легкий вес')
    elif i < 64:
        print('Первый полусредний вес')
    elif i < 69:
        print('Полусредний вес')


if __name__ == '__main__':
    func(int(input()))
