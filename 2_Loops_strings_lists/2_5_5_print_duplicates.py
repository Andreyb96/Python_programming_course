s = input().split()
d = []
for i in s:
    if (s.count(i)>1) and (i not in d):
        d.append(i)
        print(i,' ', end='')