print("Öğrencinin notuna göre hangi harf notunu alacağını belirleyen bir program")

a = int(input("notunuzu giriniz: "))

if a>=90:
    print("Harf Notu AA")
elif a>=80:
    print("Harf Notu BB")
elif a>=70:
    print("Harf Notu CB")
elif a>=60:
    print("Harf Notu CC")
elif a>=50:
    print("Harf Notu DC")
elif a>=40:
    print("Harf Notu DD")
else:
    print("Harf Notu FF")
