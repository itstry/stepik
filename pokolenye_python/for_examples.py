# 9 day; 1 задача; total: 137
mx = -(10 ** 6)
negative_num = 0
for _ in range(10):
    in_num = int(input())
    if in_num < 0:
        negative_num += in_num
        if in_num > mx:
            mx = in_num

if mx == -(10 ** 6):
    print('NO')
else:
    print(negative_num)
    print(mx)
