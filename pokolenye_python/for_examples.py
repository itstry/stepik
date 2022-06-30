num_1 = int(input())
num_2 = int(input())

counter_now = 0

if num_1 == 1:
    num_1 += 1

for i in range(num_1, num_2 + 1):
    counter_now = 0
    for k in range(1, i + 1):
        if i % k == 0:
            counter_now += 1
    if counter_now == 2:
        print(i)
