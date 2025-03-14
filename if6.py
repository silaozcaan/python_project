print("Bir kullanıcı adı ve şifre belirleyelim. Kullanıcıdan giriş yapmasını isteyelim.")

kullanici_adi= "sila_ozcan"
sifre= "123456"

a=input("kullanıcı adını giriniz: ")
b=input("şifreyi giriniz: ")


if a==kullanici_adi and b==sifre:
    print("giriş yaptınız.")
else:
    print("kullanıcı adı veya şifre hatalı")