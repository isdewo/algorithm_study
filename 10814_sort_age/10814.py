# 나이순 정렬 - 나이순 -> 가입순으로 출력
class member:
  def __init__(self, age, name):
    self.age = age
    self.name = name
  
  def __repr__(self):
    return repr((self.age, self.name))

  def getAge(self):
    return self.age
  def getName(self):
    return self.name

import sys
n = int(sys.stdin.readline())

members = []
for i in range(n):
  age, name = sys.stdin.readline().split(" ")
  age = int(age)
  members.append(member(age, name))

members = sorted(members, key=lambda member: member.age)
for i in range(n):
  print(members[i].getAge(), members[i].getName(), end="")