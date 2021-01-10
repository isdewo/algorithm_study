# 분해합 - 자연수 N의 가장 작은 생성자 구하기
from sys import stdin
n = int(stdin.readline())

result = 0
for i in range(1, n):
  if n < 10:
      break
  
  m = str(i)
  ans = 0
  if i >= 10 and i < 100:
    # 십의 자리
    ans = int(m[0]) + int(m[1]) + i
  elif i >= 100 and i < 1000:
    # 백의 자리
    ans = int(m[0]) + int(m[1]) + int(m[2]) + i
  elif i >= 1000 and i < 10000:
    # 천의 자리
    ans = int(m[0]) + int(m[1]) + int(m[2]) + int(m[3]) + i
  elif i >= 10000 and i < 100000:
    # 만의 자리
    ans = int(m[0]) + int(m[1]) + int(m[2]) + int(m[3]) + int(m[4]) + i
  elif i >= 100000 and i < 1000000:
    # 십만의 자리
    ans = int(m[0]) + int(m[1]) + int(m[2]) + int(m[3]) + int(m[4]) + int(m[5]) + i

  if ans == n:
    result = i
    break

print(result)