n = int(input())
word = []
for i in range(n):
  word.append(input())


word = set(word)
word = list(word)
word.sort()
word.sort(key=len)
for i in range(len(word)):
  print(word[i])