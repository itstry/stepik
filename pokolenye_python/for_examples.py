line = input()
counter_word_global = 0
word = ''
for i in line:
    if line.count(i) >= counter_word_global:
        counter_word_global = line.count(i)
        word = i
print(word)
