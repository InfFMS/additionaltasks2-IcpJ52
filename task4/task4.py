x = int(input())
y = int(input())
x0, y0 = 0, 0
if x > 0:
    for _ in range(x // 4):
        print(x0 + 2, y0 + 1)
        print(x0 + 4, y0)
        x0 += 4
    x %= 4
    if x == 1:
        print(x0 + 2, y0 + 1)
        print(x0, y0 + 2)
        print(x0 + 1, y0)
        x0 += 1
    elif x == 2:
        print(x0 + 1, y0 + 2)
        print(x0 + 2, y0)
        x0 += 2
    elif x == 3:
        print(x0 + 2, y0 + 1)
        print(x0, y0 + 2)
        print(x0 + 1, y0)
        print(x0 + 2, y0 + 2)
        print(x0 + 3, y0)
        x0 += 3
else:
    x = abs(x)
    for _ in range(x // 4):
        print(x0 - 2, y0 + 1)
        print(x0 - 4, y0)
        x0 -= 4
    x %= 4
    if x == 1:
        print(x0 - 2, y0 + 1)
        print(x0, y0 + 2)
        print(x0 - 1, y0)
        x0 -= 1
    elif x == 2:
        print(x0 - 1, y0 + 2)
        print(x0 - 2, y0)
        x0 -= 2
    elif x == 3:
        print(x0 - 2, y0 + 1)
        print(x0, y0 + 2)
        print(x0 - 1, y0)
        print(x0 - 2, y0 + 2)
        print(x0 - 3, y0)
        x0 -= 3
if y > 0:
    for _ in range(y // 4):
        print(x0 + 1, y0 + 2)
        print(x0, y0 + 4)
        y0 += 4
    y %= 4
    if y == 1:
        print(x0 + 1, y0 + 2)
        print(x0 + 2, y0)
        print(x0, y0 + 1)
        y0 += 1
    elif y == 2:
        print(x0 + 2, y0 + 1)
        print(x0, y0 + 2)
        y0 += 2
    elif y == 3:
        print(x0 + 1, y0 + 2)
        print(x0 + 2, y0)
        print(x0, y0 + 1)
        print(x0 + 2, y0 + 2)
        print(x0, y0 + 3)
        y0 += 3
else:
    y = abs(y)
    for _ in range(y // 4):
        print(x0 + 1, y0 - 2)
        print(x0, y0 - 4)
        y0 -= 4
    y %= 4
    if y == 1:
        print(x0 + 1, y0 - 2)
        print(x0 + 2, y0)
        print(x0, y0 - 1)
        y0 -= 1
    elif y == 2:
        print(x0 + 2, y0 - 1)
        print(x0, y0 - 2)
        y0 -= 2
    elif y == 3:
        print(x0 + 1, y0 - 2)
        print(x0 + 2, y0)
        print(x0, y0 - 1)
        print(x0 + 2, y0 - 2)
        print(x0, y0 - 3)
        y0 -= 3
