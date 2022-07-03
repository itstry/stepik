list_sentence = ([input() for i in range(int(input()))])
list_keyword = ([input() for k in range(int(input()))])

for m in range(len(list_sentence)):
    counter_in = 0
    for z in range(len(list_keyword)):
        if list_keyword[z].lower() in (list_sentence[m].lower()):
            counter_in += 1
    if counter_in == (len(list_keyword)):
        print(list_sentence[m])
