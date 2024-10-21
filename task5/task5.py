t = int(input())
n = int(input())
a = []
b = []
for _ in range(n):
    a.append(int(input()))
    b.append(int(input()) + t)
m = int(input())
c = []
d = []
for _ in range(m):
    c.append(int(input()))
    d.append(int(input()) + t)
ans = 0
first = 0
second = 0
for t in sorted(list(set(a + b + c + d))):
    x = b.count(t)
    second += x
    for _ in range(x):
        b.remove(t)
    x = d.count(t)
    first += x
    for _ in range(x):
        d.remove(t)
    x = a.count(t)
    if first < x:
        ans += x - first
        first = 0
    else:
        first -= x
    x = c.count(t)
    if second < x:
        ans += x - second
        second = 0
    else:
        second -= x
print(ans)
