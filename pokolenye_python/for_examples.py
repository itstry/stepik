# 5 day; 21 задача; total: 118
# ^-^ в профиле ссылка гитхаб

n = int(input())
n_l = [0, 1, 1]
for i in range(1, n+1):
    n_l.append(n_l[i]+n_l[-1])
    print(n_l[i], end=' ')
