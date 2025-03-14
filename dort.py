print("Girilen Sayının Tek mi, Çift mi Olduğunu Kontrol Etme")

sayi = int(input("Bir sayı giriniz: "))

if sayi == 0:
    print("Sayı 0'dır.")
elif sayi % 2 == 0:
    print("Sayı çifttir.")
else:
    print("Sayı tektir.")
