a=[]
c=[]
b=''
while 'end' not in b:
    b = input().split()
    if 'end' not in b:
        a.append(b)
for i in range(len(a)):
    for j in range(len(a[0][:])):
        c.append(int(a[i-1][j]) + int(a[i][j-1]) + int(a[(i+1)%len(a)][j]) + int(a[i][(j+1)%len(a[0][:])]))
        print(c[-1],' ', end='')
    print('')