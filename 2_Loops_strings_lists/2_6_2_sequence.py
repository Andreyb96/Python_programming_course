n = int(input())
a = [0]*n
i = 0
k = 1
while i<=n:
    for j in range(k):
        if i+j == n:
            break
        a[i+j] = k
    i += k
    k += 1
for i in range(n):
    print(a[i],' ', end = '')