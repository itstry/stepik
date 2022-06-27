# 7 day; 6 задача; total: 125
debt = int(input())
coin_1 = coin_5 = coin_10 = coin_25 = 0
while debt > 0:
    if debt >= 25:
        debt -= 25
        coin_25 += 1
        continue
    if debt >= 10:
        debt -= 10
        coin_10 += 1
        continue
    if debt >= 5:
        debt -= 5
        coin_5 += 1
        continue
    if debt >= 1:
        debt -= 1
        coin_5 += 1
        continue
print(coin_1 + coin_5 + coin_10 + coin_25)
