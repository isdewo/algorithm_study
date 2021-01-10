# 숫자카드2
# lower_bound와 upper_bound를 이용하여 구하기
def lower_bound(lst, target):
  # target이상인 값이 처음 나오는 위치 구하기
  start = 0
  end = len(lst) - 1
  while start <= end:
    if start == end:
      return start

    mid = (start+end) // 2
    if lst[mid] < target:
      start = mid + 1
    elif lst[mid] >= target:
      end = mid

def upper_bound(lst, target):
    # target을 초과한 값이 처음 나오는 위치 구하기
  start = 0
  end = len(lst) - 1
  while start <= end:
    if start == end:
      return end

    mid = (start+end) // 2
    if lst[mid] <= target:
      start = mid + 1
    elif lst[mid] > target:
      end = mid

from sys import stdin

n = int(stdin.readline())
card = [0] * 2
card[0] = list(map(int, stdin.readline().split(" ")))
m = int(stdin.readline())
card[1] = list(map(int, stdin.readline().split(" ")))

card[0].sort()
s = ""
for i in range(m):
  ub = upper_bound(card[0], card[1][i])
  lb = lower_bound(card[0], card[1][i])
  result = ub - lb
  if card[0][ub] == card[1][i]:
    result += 1

  s += (str(result) + " ")

s = s[:len(s)-1]
print(s)