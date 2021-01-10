# 이항 계수
from sys import stdin
n, k = map(int, stdin.readline().split(" "))

a = 1
for i in range(n, 0, -1):
  a *= i

b = 1
for i in range(k, 0, -1):
  b *= i

c = 1
for i in range((n-k), 0, -1):
  c *= i

result = int(a/(b*c))
print(result)