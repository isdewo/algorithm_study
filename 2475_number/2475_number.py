# 검증수 - 고유번호의 검증수 구하기
# 방법
# 처음 5자리에 들어가는 5개의 숫자를 각각 제곱하여 합한다
# 구해진 값을 10으로 나눈 나머지가 검증수가 된다

line = input().split(" ")
n = []
sum = 0
for i in range(len(line)):
  n.append(int(line[i]))
  sum += int(line[i])*int(line[i])

result = sum % 10
print(result)