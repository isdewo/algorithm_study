# 덱

def push_front(deque, num):
  # 정수를 덱의 앞에 삽입
  deque.insert(0, num)

def push_back(deque, num):
  # 정수를 덱의 뒤에 삽입
  deque.append(num)

def pop_front(deque):
  # 덱의 가장 앞에 있는 수를 빼고 출력
  # 덱이 비어있으면 -1
  if empty(deque) == 0:
    print(deque[0])
    del deque[0]
  else:
    print("-1")

def pop_back(deque):
  # 덱의 가장 뒤에 있는 수를 빼고 출력
  # 덱이 비어있으면 -1
  if empty(deque) == 0:
    print(deque.pop())
  else:
    print("-1")
    
def size(deque):
  # 덱에 들어있는 정수의 개수를 출력
  print(len(deque))

def empty(deque):
  if len(deque) == 0:
    return 1
  else:
    return 0
    
def front(deque):
  # 덱에 가장 앞에 있는 정수 출력
  # 비어있으면 -1
  if empty(deque) == 0:
    print(deque[0])
  else:
    print("-1")

def back(deque):
  # 덱에 가장 뒤에 있는 정수 출력
  # 비어있으면 -1
  if empty(deque) == 0:
    print(deque[len(deque)-1])
  else:
    print("-1")


from sys import stdin
n = int(stdin.readline())
call = [0]*n
for i in range(n):
  call[i] = stdin.readline().split(" ")

deque = []
for i in range(n):
  if call[i][0] == "push_front":
    push_front(deque, int(call[i][1]))
  elif call[i][0] == "push_back":
    push_back(deque, int(call[i][1]))
  elif call[i][0] == "front\n":
    front(deque)
  elif call[i][0] == "back\n":
    back(deque)
  elif call[i][0] == "size\n":
    size(deque)
  elif call[i][0] == "empty\n":
    print(empty(deque))
  elif call[i][0] == "pop_front\n":
    pop_front(deque)
  elif call[i][0] == "pop_back\n":
    pop_back(deque)
  