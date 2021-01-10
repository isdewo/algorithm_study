# 피타고라스의 정리
import math
from sys import stdin
line = []
result = ""
while True:
  line = list(map(int, stdin.readline().split(" ")))
  
  if line[0] == 0 and line[1] == 0 and line[2] == 0:
    break
  
  if line[0] >= line[1] and line[0] >= line[2]:
    left = line[0] ** 2
    right = line[1]**2 + line[2]**2
  elif line[1] >= line[0] and line[1] >= line[2]:
    left = line[1] ** 2
    right = line[0]**2 + line[2]**2
  elif line[2] >= line[0] and line[2] >= line[1]:
    left = line[2] ** 2
    right = line[0]**2 + line[1]**2

  if left == right:
    result += "right\n"
  else:
    result += "wrong\n"

print(result)