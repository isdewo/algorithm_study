# 직사각형에서 탈출
x, y, w, h = map(int, input().split(" "))

a = abs(x-w)
b = abs(y-h)

c = min(a, b)
d = min(x, y)
print(min(c, d))