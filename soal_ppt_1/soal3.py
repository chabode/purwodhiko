#soal 3
import math

# def test(angka1):

x = int(input("masukkan jumlah hari : "));

tahun = math.floor(x/360);
sisaHari = x % 360;
bulan = math.floor(sisaHari/30);
sisaHari2 = sisaHari % 30;
minggu = math.floor(sisaHari2/7);
hari = math.floor(sisaHari2%7);

print(str(x) + " Hari adalah ");
print(str(tahun) + " Tahun ");
print(str(bulan) + " Bulan ");
print(str(minggu) + " Minggu dan ");
print(str(hari) + " Hari ");
