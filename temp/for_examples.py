# 2 день; +57 задача; всего: 57
basis_color_list = ['красный', 'синий', 'желтый']
extra_color_list = ['фиолетовый', 'оранжевый', 'зеленый']


def color_mix(color_1: str, color_2: str) -> str:
    if (color_1 == color_2) and (color_1 in basis_color_list):
        return color_1
    elif (color_1 == basis_color_list[0] and color_2 == basis_color_list[1]) or (
            color_1 == basis_color_list[1] and color_2 == basis_color_list[0]):
        return extra_color_list[0]
    elif (color_1 == basis_color_list[0] and color_2 == basis_color_list[2]) or (
            color_1 == basis_color_list[2] and color_2 == basis_color_list[0]):
        return extra_color_list[1]
    elif (color_1 == basis_color_list[1] and color_2 == basis_color_list[2]) or (
            color_1 == basis_color_list[2] and color_2 == basis_color_list[1]):
        return extra_color_list[2]
    elif color_1 != any(basis_color_list) or color_2 in basis_color_list:
        return 'ошибка цвета'


if __name__ == '__main__':
    print(color_mix(input(), input()))

if __name__ == '__main__':
    print(calc(int(input()), int(input()), str(input())))
