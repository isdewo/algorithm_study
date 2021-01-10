# 수 찾기 - N개의 정수 중 X라는 정수가 존재하는지 알아내기

def binary_search(lst, target):
  start = 0
  end = len(a) - 1
  while start <= end:
    mid = (start + end) // 2
    if target == lst[mid]:
      return 1
    elif target > lst[mid]:
      start = mid + 1
    else:
      end = mid - 1
  return 0

from sys import stdin
n = int(stdin.readline())
a = list(map(int, stdin.readline().split(" ")))

m = int(stdin.readline())
b = list(map(int, stdin.readline().split(" ")))

a.sort()

result = ""
for i in range(m):
  result += str(binary_search(a, b[i])) + "\n"

print(result)
