list_words = [input() for i in range(int(input()))]
k = int(input())
for words in list_words:
    if len(words) >= k:
        print(words[k - 1], end='')
