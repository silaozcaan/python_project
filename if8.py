"""
Şehir Seçme Programı

Kullanıcıdan bir şehir seçmesini isteyelim. 
Eğer şehir İstanbul, Ankara veya İzmir ise "Büyükşehir" yazsın, 
değilse "Büyükşehir değil" yazsın.

"""


sehir=input("bir şehir giriniz: ").lower()

if sehir=="istanbul" or sehir=="ankara" or sehir=="izmir":
    print("Büyükşehir")
else:
    print("Büyükşehir değil")

    