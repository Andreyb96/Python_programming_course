a = input()
a = a.lower()
b = a.split(' ')
c={}
for x in b:
    if x not in c:
        c[x] = 1
    else:
        c[x] += 1
for x in c:
    print(x,'',c[x])