# 큐

def push(queue, num):
  # 정수를 큐에 삽입
  queue.append(num)

def pop(queue):
  # 큐에서 가장 앞에 있는 정수 빼고 출력
  # 큐가 비어있으면 -1
  if empty(queue) == 0:
    print(queue[0])
    del queue[0]
  else:
    print("-1")

def front(queue):
  # 큐의 가장 앞에 있는 정수 출력
  # 큐가 비어있으면 -1
  if empty(queue) == 0:
    print(queue[0])
  else:
    print("-1")

def back(queue):
  # 큐의 가장 뒤에 있는 정수 출력
  # 큐가 비어있으면 -1
  if empty(queue) == 0:
    print(queue[len(queue)-1])
  else:
    print("-1")

def size(queue):
  # 큐에 들어있는 정수의 개수
  print(len(queue))

def empty(queue):
  # 큐가 비어있으면 1, 아니면 0
  if len(queue) == 0:
    return 1
  else:
    return 0

from sys import stdin
n = int(stdin.readline())

call = [0]*n
for i in range(n):
  call[i] = stdin.readline().split(" ")

queue = []
for i in range(n):
  if call[i][0] == "push":
    push(queue, int(call[i][1]))
  elif call[i][0] == "front\n":
    front(queue)
  elif call[i][0] == "back\n":
    back(queue)
  elif call[i][0] == "size\n":
    size(queue)
  elif call[i][0] == "empty\n":
    print(empty(queue))
  elif call[i][0] == "pop\n":
    pop(queue)
  