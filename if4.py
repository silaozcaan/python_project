print("Kullanıcıdan bir şifre isteyelim, eğer şifre doğruysa 'Giriş başarılı' yazsın, yanlışsa 'Şifre yanlış' desin.")

dogru_sifre="909090"
girilen_sifre=input("şifreyi giriniz: ")

if dogru_sifre == girilen_sifre:
    print("Girdiginiz sifre doğru!")
else:
    print("Girdiğiniz sifre yanlıs, tekrar deneyiniz.")