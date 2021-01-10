# 영화감독 숌 - 시즌 번호 매기기 - 6이 적어도 3개이상 연속으로 들어가는 수
n = int(input())
title = 666
cnt = 0

while cnt != n:
  temp = str(title)
  sixCnt = temp.count("6")
  temp = list(temp)
  if sixCnt >= 3:
    start = temp.index("6")
    for i in range(start, len(temp) - 2):
      if temp[i] == "6" and temp[i+1] == "6" and temp[i+2] == "6":
        cnt += 1
        break
  title += 1

print(title-1)