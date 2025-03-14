def hesap_makinesi():
    islem_sayisi = 0 

    while True:  
        print("\n Basit Hesap Makinesi ")

        sayi1 = int(input("Birinci sayıyı giriniz: "))
        sayi2 = int(input("İkinci sayıyı giriniz: "))

        print("\nİşlem Seçiniz:")
        print("1️⃣ Toplama (+)")
        print("2️⃣ Çıkarma (-)")
        print("3️⃣ Çarpma (*)")
        print("4️⃣ Bölme (/)")
        print("5️⃣ Çıkış (q)")

        islem = input("Seçiminizi yapınız (1/2/3/4/q): ")

        if islem.lower() == "q":
            print("Programdan çıkılıyor...")
            break

        if islem == "1":
            sonuc = sayi1 + sayi2
            print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
        elif islem == "2":
            sonuc = sayi1 - sayi2
            print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
        elif islem == "3":
            sonuc = sayi1 * sayi2
            print(f"Sonuç: {sayi1} * {sayi2} = {sonuc}")
        elif islem == "4":
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
                print(f"Sonuç: {sayi1} / {sayi2} = {sonuc}")
            else:
                print("Hata! Bir sayı sıfıra bölünemez.")
        else:
            print("Geçersiz işlem seçimi! Lütfen 1, 2, 3, 4 veya q giriniz.")

        islem_sayisi += 1  

        if islem_sayisi == 3:
            print(" 3 işlem yapıldı, program kapanıyor.")
            break 


hesap_makinesi()
