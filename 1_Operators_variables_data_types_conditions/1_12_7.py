# put your python code here
a = int(input())
sum_1 = a//1000//100 + (a//1000//10)%10 + a//1000%10
sum_2 = a%1000//100 + (a%1000//10)%10 + a%1000%10
if sum_1 == sum_2:
    print('Счастливый')
else:
    print('Обычный')