"""" 
Başlangıç bakiyemiz 5000 TL olsun.
Kullanıcıdan çekmek istediği miktarı al.
Eğer bakiye yeterliyse, parayı çeksin ve yeni bakiyeyi ekrana yazdırsın.
Eğer bakiye yetersizse, "Bakiye yetersiz!" desin. """

bakiye= 5000
a=float(input("çekmek istediğiniz tutarı giriniz: "))

if a<=5000:
    bakiye-=a
    print(f"Para çekme işlemi Başarılı \nYeni Bakiyeniz: {bakiye}")
else:
    print("Bakiyeniz yetersizdir. Lütfen tekrar deneyiniz.")
