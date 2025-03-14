"""
Mükemmel sayı, kendisi hariç pozitif bölenlerinin toplamı kendisine eşit olan sayıdır.
"""

def mukemmel_sayi_mi(sayi):
    toplam=0

    for i in range(1, sayi):
        if sayi%i==0:
            toplam+=i
        
    return toplam==sayi

sayi = int(input("Bir sayı girin: "))

if mukemmel_sayi_mi(sayi):
    print(f"{sayi} bir mükemmel sayıdır!")
else:
    print(f"{sayi} bir mükemmel sayı değildir.")