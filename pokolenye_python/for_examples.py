line = input().lower()

vowel = 'ауоыиэяюёе'
consonant = 'бвгджзйклмнпрстфхцчшщ'
vowel_count = 0
consonant_count = 0

for i in vowel:
    vowel_count += line.count(i)
for i in consonant:
    consonant_count += line.count(i)

print(f'Количество гласных букв равно {vowel_count}')
print(f'Количество согласных букв равно {consonant_count}')
