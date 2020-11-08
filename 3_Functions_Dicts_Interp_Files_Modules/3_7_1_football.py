n = int(input())
s = []
for i in range(n):
    s.append(input().split(';'))
slovar = {}
for i in range(len(s)):
    if (s[i][0] not in slovar):
        slovar[s[i][0]] = [1]
    else:
        slovar[s[i][0]][0] += 1
    if (s[i][2] not in slovar):
        slovar[s[i][2]] = [1]
    else:
        slovar[s[i][2]][0] += 1
for i in slovar:
    for j in range(4):
        slovar[i].append(0)
for i in range(len(s)):
    if s[i][1] > s[i][3]:
        slovar[s[i][0]][1] += 1
        slovar[s[i][2]][3] += 1
        slovar[s[i][0]][4] += 3
    elif s[i][1] < s[i][3]:
        slovar[s[i][2]][1] += 1
        slovar[s[i][0]][3] += 1
        slovar[s[i][2]][4] += 3
    else:
        slovar[s[i][2]][2] += 1
        slovar[s[i][0]][2] += 1
        slovar[s[i][0]][4] += 1
        slovar[s[i][2]][4] += 1
for i in slovar:
    print(i + ':', end = '')
    for j in range(len(slovar [i])):
        print(slovar[i][j], ' ', end = '')
    print('')