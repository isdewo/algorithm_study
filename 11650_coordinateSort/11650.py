# 좌표 정렬하기
n = int(input())
x = []
for i in range(n):
  x.append(list(map(int, input().split(" "))))

x.sort()
for i in range(n):
  print(x[i][0], x[i][1])
  