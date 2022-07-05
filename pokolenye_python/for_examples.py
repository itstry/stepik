list_num = [int(i) for i in input().split()]

index_max = list_num.index(max(list_num))
index_min = list_num.index(min(list_num))

list_num[index_max], list_num[index_min] = list_num[index_min], list_num[index_max]

print(*list_num)
