num = int(input())
dict_en = 'abcdefghijklmnopqrstuvwxyz'

for ch in input():
    print(dict_en[dict_en.find(ch) - num], end='')
