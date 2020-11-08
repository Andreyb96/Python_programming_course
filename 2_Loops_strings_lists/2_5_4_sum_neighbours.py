s = input().split()
s.append(s[0])
s.insert(0,s[-2])
for i in range(1,len(s)-1):
    if len(s)==3:
        print(s[1])
        break
    print(int(s[i-1])+int(s[i+1]),' ',end='')