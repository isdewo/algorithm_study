# 블랙잭 - 합이 m을 넘지 않으면서 m에 최대한 가까운 카드 3장의 합을 출력
import sys
n, m = map(int, sys.stdin.readline().split(" "))
card = []
card = list(map(int, sys.stdin.readline().split(" ")))

card.sort()
cur_max = 0
for i in range(n):
  if card[i] > m:
    break
  for j in range(i+1, n):
    if card[i] + card[j] > m:
      break
    for k in range(j+1, n):
      sum = card[i] + card[j] + card[k]
      if sum > m:
        break
      cur_max = max(sum, cur_max)

print(cur_max)