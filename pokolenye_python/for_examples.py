list_word, counter_article = input().lower().split(), 0

for i in ('a', 'an', 'the'):
    for k in list_word:
        if i == k:
            counter_article += 1
print(f'Общее количество артиклей: {counter_article}')
