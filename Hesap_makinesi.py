menu = """
1)Topla
2)Çıkar
3)Çarp
4)Böl
5)Karesini Hesapla
6)Karekök Hesapla
q)Çıkış
"""

print(menu)
kontrol = True
while kontrol:
    secim = input("Yapmak istediğiniz işlemi seçiniz:")

    if secim == "q":
        print("Program sonu")
        kontrol = False
    elif secim == "1":
        print("Toplama İşlemi")
        print("-" * 30)
        topla1 = int(input("İlk sayıyı giriniz:"))
        topla2 = int(input("İkinci sayıyı giriniz:"))
        print(f"{topla1} + {topla2} = {topla1 + topla2}")
    elif secim == "2":
        print("Çıkarma İşlemi")
        print("-" * 30)
        cıkar1 = int(input("İlk sayıyı giriniz:"))
        cıkar2 = int(input("İkinci sayıyı giriniz:"))
        print(f"{cıkar1}  {cıkar2} = {cıkar1 - cıkar2}")
    elif secim == "3":
        print("Çarpma İşlemi")
        print("-" * 30)
        carp1 = int(input("İlk sayıyı giriniz:"))
        carp2 = int(input("İkinci sayıyı giriniz:"))
        print(f"{carp1} * {carp2} = {carp1 * carp2}")
    elif secim == "4":
        print("Bölme İşlemi")
        print("-" * 30)
        bol1 = int(input("İlk sayıyı giriniz:"))
        bol2 = int(input("İkinci sayıyı giriniz:"))
        print(f"{bol1} /{bol2} = {bol1 / bol2}")
    elif secim == "5":
        print("Karesini Hesapla")
        print("-" * 30)
        kare = int(input("sayıyı giriniz:"))
        print(f"{kare} sayısının karesi {kare ** 2}")
    elif secim == "6":
        print("Karekökü Hesapla")
        print("-" * 30)
        kok = int(input("sayıyı giriniz:"))
        print(f"{kok} sayısının kare kökü {kok ** 0.5}")
    else:
        print("Yanlış Seçim")
