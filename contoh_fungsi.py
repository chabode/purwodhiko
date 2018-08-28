def hitung_luas_lingkaran():
    print("menghitung luas lingkaran")
    radius = float(input("jari-jari = "))
    luas = 3.14 * radius * radius
    print("luas = ", luas)

def hitung_luas_persegi():
    print("menghitung luas persegi")
    sisi = int(input("Sisi = "))
    luas = sisi*sisi
    print("luas = ", luas)

print ("menghitung luas")
print ("1. Luas Lingkaran")
print ("2. Luas persegi")

pilihan = int(input("Pilihan (1 atau 2) : "))
if pilihan == 1:
    hitung_luas_lingkaran()
elif pilihan == 2:
    hitung_luas_persegi()
else:
    print("input anda salah")
