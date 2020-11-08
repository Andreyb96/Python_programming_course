s = input()
k = 1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        k += 1
    else:
        print(s[i],k,sep='',end='')
        k = 1
print(s[-1],k, sep='')