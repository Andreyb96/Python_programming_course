n = int(input())
x=[]
c={}
for i in range(n):
    z = int(input())
    x.append(z)
for i in range(n):
    if x[i] in c:
        print(c[x[i]])
    else:
        c[x[i]] = f(x[i])
        print(c[x[i]])