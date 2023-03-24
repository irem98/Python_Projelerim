first_num =int(input("Birinci sayıyı giriniz"))
second_num =int(input("İkinci sayıyı giriniz"))
min_num = second_num if first_num > second_num else first_num

for i in range(min_num,0,-1):
    if first_num %i ==0 and second_num %i ==0:
        print(first_num,"ile" , second_num,"sayısını bölen en büyük sayı",i)
        break
    else:
        print("Bölen sayı yok")