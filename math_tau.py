import math

print(math.tau)

r = float(input("Dairenin yarıçapını giriniz:"))

print("PI ile Hesapla")
print("Dairenin çevresi",2 * math.pi * r)
print("Dairenin alanı",math.pi * (r**2))


print("TAU ile Hesapla")
print("Dairenin çevresi",math.tau * r)
print("Dairenin alanı",(math.tau * (r**2))/2)