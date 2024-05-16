word = input()
n = len(word)
record = dict()

start = 0
max_val = 0
for i in range(n):
    if word[i] in record:
        start = record[word[i]] + 1
        record[word[i]] = i

    else:
        record[word[i]] = i
        max_val = max(max_val, i - start + 1)

print(max_val)