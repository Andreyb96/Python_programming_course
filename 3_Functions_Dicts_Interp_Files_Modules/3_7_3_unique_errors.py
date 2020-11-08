d = int(input())
slovar = []
text = []
for i in range(d):
    slovar.append(input())
    slovar[i] = slovar[i].lower()
l = int(input())
for i in range(l):
    text.append(input())
    text[i] = text[i].lower()
b=[]
for i in range(l):
    a = text[i].split(' ')
    for j in range(len(a)):
        b.append(a[j])
g = []
for i in range(len(b)):
    if (b[i] not in slovar) and (b[i] not in g):
        g.append(b[i])
        print(b[i])