sum = int(input())
sum_squared = sum**2
a=[]
a.append(sum)
while sum!=0:
    a.append(input())
    sum += int(a[-1])
    sum_squared += int(a[-1])**2
print(sum_squared)