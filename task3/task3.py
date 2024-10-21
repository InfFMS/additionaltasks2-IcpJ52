n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst = sorted(lst)
ans = [n, lst[0]]
max_sum = n * lst[0]
for i in range(1, n):
    sm = (n - i) * lst[i]
    if sm > max_sum:
        ans = [n - i, lst[i]]
        max_sum = sm
print(*ans)
