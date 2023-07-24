def timso(a,b,c,d):
    for i in range(a,b+1,1):
        if i % 7 ==0 and i % 5 ==0:
            return i
        h=timso(a,b,c,d)
        print('so chia het 5 va 7',h)
a,b,c,d =int(input('nhap a , b ,c ,d:'))