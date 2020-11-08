lst = input().split()
x = int(input())
for i in range(len(lst)):
    if x==int(lst[i]):
        print(i, ' ', end ='')
if str(x) not in lst:
    print('Отсутствует')