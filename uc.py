print("Kullanıcıdan Alınan Sayının Pozitif, Negatif veya Sıfır Olup Olmadığını Kontrol Etme")

sayi=int(input("bir sayı giriniz: "))

if sayi>0:
    print("sayı pozitiftir")
elif sayi<0:
    print("sayı negatiftir")
else:
    print("sayı 0'dır")
    
print("program sonlandı.")