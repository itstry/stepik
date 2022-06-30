num = int(input())
num_in_bin = ''
while num > 0:
    integer = num // 2
    remainder = num % 2
    num_in_bin += str(remainder)
    num = integer
print(num_in_bin[::-1])
