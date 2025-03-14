print("Sayı 3’e ve 5’e Bölünebiliyor mu?")

sayi= int(input("bir sayı giriniz: "))

if sayi%3==0 and sayi%5==0:
    print("sayı hem 3'e hem de 5'e bölünebiliyor.")
elif sayi%3==0:
    print("sayı sadece 3'e bölünebiliyor")
elif sayi%5==0:
    print("sayı sadece 5'e bölünebiliyor")
else:
    print("sayı 3'e de 5'e de bölünemiyor.")