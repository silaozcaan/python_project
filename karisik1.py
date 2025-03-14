"""
Bu program, bilgisayarın rastgele seçtiği bir sayıyı (1-100 arası) tahmin etmeni isteyecek.
Her tahmininde sana ipucu verecek: "Daha büyük bir sayı gir" veya "Daha küçük bir sayı gir".

"""

import random
rastgele_sayi= random.randint(1,100)

tahmin=0
while tahmin!=rastgele_sayi:
    tahmin=int(input("sayı gir: "))
    if tahmin<rastgele_sayi:
         print("daha büyük sayı gir.")
    else:
        print("daha küçük sayı gir.")

print(f"girdiğiniz sayı doğru: {tahmin}")