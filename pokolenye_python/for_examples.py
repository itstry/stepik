num = int(input())
end = int(((1 + num) / 2) * num)
for i in range(1, num + 1):
    i_end = int(((1 + i) / 2) * i)
    for j in range((i_end - i) + 1, i_end + 1):
        print(j, end=' ')
    print()
