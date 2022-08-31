#Faktoriyel Hesaplama

sayi = input("Faktoriyelini hesaplamak istediginiz sayiyi giriniz: ")
faktoriyel = 1

while not sayi.isdigit():
    print("Gecersiz deger girdiniz.")
    sayi = input("Lutfen faktoriyelini hesaplamak istediginiz sayiyi giriniz: ")
else:
    if int(sayi) == 0:
        print("0! = 1")
    else:
        for i in range(1,int(sayi)+1):
            faktoriyel*=i   
        print("{0}! = {1}".format(sayi,faktoriyel))

