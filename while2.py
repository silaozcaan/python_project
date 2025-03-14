print("Bu program, kullanıcıdan sürekli bir şeyler girmesini isteyecek ve 'çık' komutunu girene kadar devam edecek.")

komut= " "
while komut != "çık":
    komut=input("bir şeyler yaz, eğer programı sonlandırmak istiyorsan 'çık' yaz: ")
    if komut=="çık":
        print("program sonlandı.")
    else:
        print(komut)
    