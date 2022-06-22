def main():
    return {letter: index for index, letter in enumerate('qwertyuiop', 1)}


if __name__ == '__main__':
    x = main()
    z = {b: a for a, b in x.items()}
    print(x)
    print(z)
