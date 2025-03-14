"""


bu bir not defteri uygulamasıdır.
Adımlar:
Kullanıcı not yazıp kaydedebilecek.
Bu notları görüntüleyebilecek.
Ve isterse silebilecek.


"""

import os

def ana_menu():
    while True:
        print("\n--- Ana Menü ---")
        print("1. Yeni Not Ekle")
        print("2. Notları Görüntüle")
        print("3. Not Sil")
        print("4. Çıkış")

        secim = input("Bir işlem seçin (1/2/3/4): ")

        if secim == "1":
            not_ekle()
        elif secim == "2":
            notlari_goruntule()
        elif secim == "3":
            not_sil()
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

def not_ekle():
    
    not_icerigi = input("Yeni notunuzu girin: ")

    
    with open("notlar/notlar.txt", "a") as file:
        file.write(not_icerigi + "\n")

    print("Not başarıyla eklendi!")

def notlari_goruntule():
    
    if not os.path.exists("notlar/notlar.txt"):
        print("Henüz not eklenmemiş!")
        return

    with open("notlar/notlar.txt", "r") as file:
        notlar = file.readlines()

    if not notlar:
        print("Henüz not eklenmemiş!")
        return

    
    print("\nKaydedilen Notlar:")
    for index, not_icerigi in enumerate(notlar, 1):
        print(f"{index}. {not_icerigi.strip()}")

def not_sil():
    
    if not os.path.exists("notlar/notlar.txt"):
        print("Henüz not eklenmemiş!")
        return

    with open("notlar/notlar.txt", "r") as file:
        notlar = file.readlines()

    
    if not notlar:
        print("Silinecek hiçbir not yok!")
        return

    
    print("\nKaydedilen Notlar:")
    for index, not_icerigi in enumerate(notlar, 1):
        print(f"{index}. {not_icerigi.strip()}")

    try:
        secim = int(input("\nSilmek istediğiniz notun numarasını girin: ")) - 1

        if secim < 0 or secim >= len(notlar):
            print("Geçersiz numara, silme işlemi yapılamaz.")
            return

        del notlar[secim]

        with open("notlar/notlar.txt", "w") as file:
            file.writelines(notlar)

        print("Not başarıyla silindi!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if not os.path.exists("notlar"):
    os.mkdir("notlar")

ana_menu()