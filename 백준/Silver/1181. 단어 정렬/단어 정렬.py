n = int(input())

word = []
for i in range(n):
    word.append(input())
    
set_word = list(set(word))
sort_w = []
for j in set_word:
    sort_w.append((len(j),j))
    
result = sorted(sort_w)

for len_w, word in result:
    print(word)