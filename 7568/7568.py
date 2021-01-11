# 키와 몸무게를 입력받아 덩치 등수 매기기
# 등수는 자신보다 큰 덩치의 사람 수 + 1이 되어
# 나보다 큰 덩치가 한명이면 2등, 두명이면 3등 이렇게 된다.
from sys import stdin
n = int(stdin.readline())

info = [0] * n
for i in range(n):
  info[i] = list(map(int, stdin.readline().split(" ")))


rank = ""
cnt = 1
for i in range(n):
  for j in range(n):
    if i != j and info[i][0] < info[j][0] and info[i][1] < info[j][1]:
      cnt += 1
  
  rank += str(cnt) + " "
  cnt = 1

print(rank)