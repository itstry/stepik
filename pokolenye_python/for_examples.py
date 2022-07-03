list_num = [int(input()) for i in range(int(input()))]
print([(list_num[k] + list_num[k + 1]) for k in range(len(list_num)) if k != (list_num.index(list_num[-1]))])
