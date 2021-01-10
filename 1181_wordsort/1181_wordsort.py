# 단어 정렬 - 길이가 짧은 것부터, 길이가 같으면 사전순으로
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