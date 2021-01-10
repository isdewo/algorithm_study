# 괄호 - 주어진 문자열이 괄호문자열(VPS)인지 아닌지 판단하기
def isVPS(line):
  if line.count("(") != line.count(")"):
    print("NO")
    return
  elif line[0] != "(" or line[len(line)-1] != ")":
    print("NO")
    return

  cnt = line.count(")")
  pos = -1
  for i in range(cnt):
    pos = line.index(")", pos+1)
    if line[:pos].count("(") <= i:
      print("NO")
      return
  
  print("YES")


n = int(input())
line = []
for i in range(n):
  line.append(input())

for i in range(n):
  isVPS(line[i])
