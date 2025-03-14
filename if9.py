""" 
Basit bir Taş-Kağıt-Makas oyunu yapalım. 
Kullanıcı seçim yapacak, bilgisayar da rastgele bir seçim yapacak ve sonucu belirleyeceğiz.

"""
import random

print("Taş-Kağıt-Makas Oyunu")

secenekler=["taş", "kağıt", "makas"]
kendi_secimim=input(" Taş-Kağıt-Makas seciniz: ")
bilgisayar_secimi=random.choice(secenekler)

print("Bilgisayarın Secimi: ", bilgisayar_secimi)

if bilgisayar_secimi==kendi_secimim:
    print("Berabere!")
elif bilgisayar_secimi== "taş" and kendi_secimim=="makas" or \
     bilgisayar_secimi== "kağıt" and kendi_secimim=="taş" or \
     bilgisayar_secimi== "makas" and kendi_secimim=="kağıt":
         print("Bilgisayar Önde!")
else:
    print("Ben Öndeyim.")
