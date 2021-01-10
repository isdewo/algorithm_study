# 요세푸스 문제/요세푸스 순열

# n = 인원 수, k = 제거 번호
from sys import stdin
n, k = map(int, stdin.readline().split(" "))

circle = list([i for i in range(1, n+1)])

i = 0
cnt = 0
result = []
l = len(circle)
while l != 0:
  cnt += 1
  if cnt == k:
    result.append(circle[i])
    del circle[i]
    l -= 1
    i -= 1
    cnt = 0
  i += 1
  if i == l:
    i = 0

print("<", end="")
for i in range(n):
  if i == n-1:
    print(result[i], end=">")
  else:
    print(result[i], end=", ")