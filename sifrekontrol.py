"""
Bu program, kullanıcıdan bir şifre oluşturmasını ister ve şifreyi kontrol eder.
Şifre şu kurallara uymalıdır:
✅ En az 8 karakter uzunluğunda olmalı
✅ İçinde en az 1 rakam olmalı
✅ En az 1 büyük harf içermeli

"""


def sifre_kontrol(sifre):
    uzunluk=len(sifre)>=8
    buyuk_harf=any(char.isupper()for char in sifre) 
    rakam= any(char.isdigit() for char in sifre)
    
    if uzunluk and buyuk_harf and rakam:
        return True
    else:
        return False


sifre=input("Şifre oluşturun: ")

if sifre_kontrol(sifre):
    print("Şifreniz Başarıyla Oluşturuldu!")
else:
    print("Şifreniz geçersiz! En az 8 karakter, 1 büyük harf ve 1 rakam içermeli.")