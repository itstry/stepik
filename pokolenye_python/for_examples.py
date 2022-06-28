# 8 day; 7 задача; total: 135
count, multi = 0, 1
for _ in range(10):  # 4
    x = int(input())
    if x >= 0:  # 2
        multi *= x
        count += 1
[print(f'{count}\n{multi}') if count > 0 else print('NO')]
