# put your python code here
a = float(input())
b = float(input())
c = input()
if c=='+':
    print(a+b)
elif b==0 and (c=='mod' or c=='div' or c=='/'):
    print('Деление на 0!')
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='pow':
    print(a**b)
elif c=='div':
    print(a//b)
elif c=='mod':
    print(a%b)
else: 
    print(a/b)