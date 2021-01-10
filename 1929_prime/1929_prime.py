import sys
# M 이상 N 이하 소수를 모두 출력하기
# 에라토스테네스의 체
m, n = map(int, sys.stdin.readline().split(" "))

nList = [True] * (n+1)
nList[1] = False
end = int(n ** 0.5)
for i in range(2, end + 1):
  if nList[i] == True:
    for j in range(i+i, n+1, i):
      nList[j] = False

for i in range(m, n+1):
  if nList[i] == True:
    print(i)