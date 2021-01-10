# 스택

def push(stack, num):
  # 정수를 스택에 삽입
  stack.append(num)

def pop(stack):
  # 스택에서 가장 위에 있는 정수를 빼고 출력
  # 비어있으면 -1
  if empty(stack) == 0:
    print(stack.pop())
  else:
    print("-1")

def top(stack):
  # 스택의 가장 위에있는 정수 출력
  # 비어있으면 -1
  if empty(stack) == 0:
    n = stack.pop()
    stack.append(n)
    print(n)
  else:
    print("-1")

def size(stack):
  # 스택에 들어있는 정수의 개수 출력
  print(len(stack))

def empty(stack):
  # 스택이 비었으면 1, 아니면 0
  if len(stack) == 0:
    return 1
  else:
    return 0

from sys import stdin
n = int(stdin.readline())

call = [0]*n
for i in range(n):
  call[i] = stdin.readline().split(" ")

stack = []
for i in range(n):
  if call[i][0] == "push":
    push(stack, int(call[i][1]))
  elif call[i][0] == "top\n":
    top(stack)
  elif call[i][0] == "size\n":
    size(stack)
  elif call[i][0] == "empty\n":
    print(empty(stack))
  elif call[i][0] == "pop\n":
    pop(stack)
  