alph = input()
shifr = input()
to_shifr = input()
un_shifr = input()
slovar_1 = {}
slovar_2 = {}
for i in range(len(alph)):
    slovar_1[alph[i]] = shifr[i]
    slovar_2[shifr[i]] = alph[i]
ts = []
for i in range(len(to_shifr)):
    ts.append(slovar_1[to_shifr[i]])
    print(ts[i], end ='')
us = []
print('')
for i in range(len(un_shifr)):
    us.append(slovar_2[un_shifr[i]])
    print(us[i], end ='')