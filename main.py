import math

a, b, c = map(int, input().split())

d = b ** 2 - 4 * a * c
sd = d ** 0.5

if d > 0:
    x1 = (-b + sd) / (2 * a)
    x2 = (-b - sd) / (2 * a)
    print(x1, x2)
elif d == 0:
    x = (-b) / (2 * a)
    print(x)
else:
    print("No solutions")