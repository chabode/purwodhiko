import math

jamAwal = 9
jarak = int(input('jarak tempuhnya = '));
kecepatanA = int(input('kecepatan Mobil A = '));
kecepatanB = int(input('kecepatan Mobil B = '));
kecepatan = kecepatanA + kecepatanB;
kecepatanTotal = kecepatan/3600;
detikTotal = jarak / kecepatanTotal;
lamaJam = math.floor(detikTotal / 3600);
lamaMenit = math.floor((detikTotal%3600)/60);
lamaDetik = math.floor((detikTotal%3600)%60);

print('Lama Jam = ' + str(lamaJam) + ' Lama Menit = ' + str(lamaMenit));
print('Tabrak mobil pukul ' + str(jamAwal + lamaJam) + ' dan Menit ke ' + str(lamaMenit) + ' dan Detik ke ' + str(lamaDetik));