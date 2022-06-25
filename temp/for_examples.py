# хз какой день; +71 задача; всего: 71

sobaken = float(input())
if sobaken == 2:
    i = 2
    j = 0
elif sobaken == 1:
    i = 1
    j = 0
elif sobaken > 2:
    i = 2
    j = sobaken - 2
else:
    i = j = 0
print(10.5 * (i) + 4 * j)
