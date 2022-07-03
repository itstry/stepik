list_num = [int(input()) for i in range(int(input()))]
for i in range(len(list_num) // 2):
    del list_num[i + 1]
print(list_num)
