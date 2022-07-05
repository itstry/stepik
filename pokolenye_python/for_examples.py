list_num = [int(i) for i in input().split()]
list_num.sort()
print(*list_num)
list_num.sort(reverse=True)
print(*list_num)
