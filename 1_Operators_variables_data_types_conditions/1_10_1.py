# put your python code here
A = int(input())
B = int(input())
H = int(input())
if (H<A):
    print('Недосып')
elif (H>=A) and (H<=B):
    print('Это нормально')
else:
    print('Пересып')