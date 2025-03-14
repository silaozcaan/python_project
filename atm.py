bakiye = 5000

print("ATM'ye Hoşgeldiniz!")
print("\nLütfen bir işlem seçiniz")
print("1 - Para Çekme")
print("2 - Para Yatırma")
print("3 - Bakiye Görüntüleme")
print("Çıkış yapmak için 'b' tuşlayınız.")


while True:

    secim = input("Seçim: ")  # HER DÖNGÜDE TEKRAR SEÇİM ALIYORUZ

    if secim == "1":
        cekilecek = int(input("Çekilecek tutarı giriniz: "))
        if cekilecek > bakiye:
            print("Yetersiz bakiye!")
        else:
            bakiye -= cekilecek
            print(f"Yeni bakiyeniz: {bakiye} TL")
    
    elif secim == "2":
        yatirma = int(input("Yatırılacak tutarı giriniz: "))
        bakiye += yatirma
        print(f"Yeni bakiyeniz: {bakiye} TL")
    
    elif secim == "3":
        print(f"Toplam bakiyeniz: {bakiye} TL")
    
    elif secim.lower() == "b":
        print("Çıkış yapılıyor...")
        break  # Döngüden çık
    
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")
