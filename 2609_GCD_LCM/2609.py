# 최대공약수와 최소공배수
a, b = map(int, input().split(" "))

m = min(a, b)

while m > 0:
  if a % m == 0 and b % m == 0:
    n = m * (a//m) * (b//m)
    print(m)
    print(n)
    break
  m -= 1

