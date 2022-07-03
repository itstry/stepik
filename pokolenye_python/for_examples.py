list_sentence = ([input() for i in range(int(input()))])
key_word = input().lower()
print(*[list_sentence[k] for k in range(len(list_sentence)) if key_word in list_sentence[k].lower()], sep='\n')
