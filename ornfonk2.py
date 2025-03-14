"""girilen sayının karesini döndüren bir program"""


def karesi():
    sayi=int(input("sayı giriniz: "))
    return sayi*sayi

sonuc=karesi()
print(f"girdiginiz sayının karesi : {sonuc}")