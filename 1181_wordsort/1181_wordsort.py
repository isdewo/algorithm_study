# 팰린드롬 수 - 어떤 단어를 앞뒤 어디서 읽어도 똑같은 수
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