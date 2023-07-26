def cau9():
    data = input("nhap day so tu ban phim").split(' ')
    demsochan = 0
    demsole = 0
    for i in data:
        if eval(i)%2 == 0:
            demsochan += 1
        else:
            demsole += 1
    print("tong phan tu la so chan la: ",demsochan)
    print("tong phan tu la so le la: ",demsole)

cau9()
    