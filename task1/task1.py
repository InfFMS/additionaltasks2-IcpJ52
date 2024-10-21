a = int(input())
b = int(input())
n = int(input())
m = int(input())
s = n - m + (n - 1) * a - (m - 1) * b
if -2 * a <= s <= 2 * b:
    print(max(n + (n - 1) * a, m + (m - 1) * b) ,min(n + (n - 1) * a + 2 * a, m + (m - 1) * b + 2 * b))
else:
    print(-1)
