# import


def get(value):
    if value > 0:
        return "Positive"
    if value < 0:
        return "Negative"
        pass
    return 'Zero'


if __name__ == '__main__':
    x = int(input())
    print(get(x).upper())

