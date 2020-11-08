a = int(input())
b = int(input())
sum = 0
k = 0
for i in range(a,b+1):
    if i%3==0:
        sum += i
        k += 1
print(sum/k)