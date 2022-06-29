import time

start_time = time.time()

num_ex = [i ** 5 for i in range(0, 151)]
print(num_ex)

for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                e = int((num_ex[a] + num_ex[b] + num_ex[c] + num_ex[d])**(1/5))
                if (num_ex[a] + num_ex[b] + num_ex[c] + num_ex[d]) == e**5:
                    print(f'{a} + {b} + {c} + {d} = {a + b + c + d + e}')
                    print("time elapsed: {:.2f}s".format(time.time() - start_time))
                    exit()
