print("Not Hesaplama Programı")

ad = input("Öğrenci adını giriniz: ")
vize = float(input("Vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

ortalama = (vize * 0.40) + (final * 0.60)

print("\n--- Not Bilgileri ---")
print("Öğrenci:", ad)
print("Vize:", vize)
print("Final:", final)
print("Ortalama:", ortalama)

if ortalama >= 50:
    print("Durum: Geçti")
else:
    print("Durum: Kaldı")

input("\nÇıkmak için Enter tuşuna basın...")
