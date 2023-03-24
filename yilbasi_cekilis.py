from random import choice
kisiSayisi = int(input("Kişi Sayısı girin:"))

sonuc = dict()
kisiler =[]

for i in range(kisiSayisi):
    kisi = input("İsim Giriniz:")
    kisiler.append(kisi)


for i in range(kisiSayisi):
     while True:
        kime = choice(kisiler)
        if kime != kisiler[i] and kime not in sonuc.values():
            sonuc[kisiler[i]] = kime
            break


for key in sonuc:
    print(key,sonuc[key])