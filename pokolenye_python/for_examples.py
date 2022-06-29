total = 0
for n in range(1, 11):
    for k in range(1, 21):
        for m in range(1, 201):
            if 10 * n + 5 * k + 0.5 * m == 100:
                total += 1
                if (n + k + m) == 100:
                    print('n =', n, 'k =', k, 'm =', m)
