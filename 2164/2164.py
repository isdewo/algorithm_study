# 카드2 - 카드 버리기, 제일 위를 제일 아래로 옮기기를 반복하여
# 제일 마지막에 남는 카드 구하기
n = int(input())
card = []

if n % 2 == 0:
  for i in range(n//2):
    card.append((i+1)*2)
else:
  for i in range(n):
    card.append(i+1)

cnt = 1
l = len(card)
i = 0
while(l != 1):
  if cnt == 1:
    i += 1
    cnt += 1
    l -= 1
  elif cnt == 2:
    temp = card[i]
    i += 1
    card.append(temp)
    cnt = 1

print(card[i])