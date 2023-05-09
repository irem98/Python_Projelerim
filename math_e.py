import math
import decimal

print(math.e)


toplam = decimal.Decimal("1")
sayac = 1
for i in range(1,20):
    sayac *=i
    toplam += decimal.Decimal(1) /decimal.Decimal(sayac)

print(toplam)

