# m 이상 n 이하의 자연수 중 소수인 것을 모두 골라
# 소수의 합과 최솟값 찾기

def isPrime(num):
  if num < 2:
    return False
  elif num == 2:
    return True

  for i in range(2, num):
    if num % i == 0:
      return False
  
  return True

m = int(input())
n = int(input())

prime = []
pSum = 0

for i in range(m, n+1):
  if isPrime(i) == True:
    prime.append(i)
    pSum += i

if len(prime) == 0:
  print(-1)
else:
  print(pSum)  
  print(prime[0])