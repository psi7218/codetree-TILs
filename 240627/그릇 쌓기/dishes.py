answer = 10
word = input()

for i in range(1, len(word)):
    if word[i] == word[i-1]:
        answer += 5
    else:
        answer += 10

print(answer)