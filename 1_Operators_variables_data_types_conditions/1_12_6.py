# put your python code here
a = int(input())
if (a%10==0) or (a%100==11) or (a%100==12) or (a%100==13) or (a%100==14) or (a%10==5) or (a%10==6) or (a%10==7) or (a%10==8) or (a%10==9):
    print(a, ' программистов')
elif (a%10==1) and (a%100!=11):
    print(a, ' программист')
elif (a%10==2) and (a%100!=12) or (a%10==3) and (a%100!=13) or (a%10==4) and (a%100!=14):
    print(a, ' программиста')