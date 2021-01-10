# 팰린드롬수 - 뒤에서부터 읽어도 똑같은 단어
num = []
rev_num = []
while(1):
  n = input()
  if n == "0":
    break
  num.append(n)
  rev_num.append(n[::-1])

for i in range(len(num)):
  for j in range(len(num[i]) // 2):
    if num[i][j] != rev_num[i][j]:
      print("no")
      break
    elif j == (len(num[i]) // 2) - 1:
      print("yes")
  if len(num[i]) == 1:
    print("yes")