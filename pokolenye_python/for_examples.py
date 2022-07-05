list_l = [int(i) for i in input().split()]
list_m = [int(k) for k in input().split()]
print(*(list_m[j] + list_l[j] for j in range(len(list_l))))
