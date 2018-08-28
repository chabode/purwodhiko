
massa = int(input('Masukkan Massa (kg) : '));
tinggi = int (input('Masukkan Tinggi (cm) : '));

imt = massa/((tinggi/100)**2);

if (imt > 39.9):
    text = 'BB Obesitas!';
elif (30.0 <= imt <= 39.9):
    text = 'BB sangat berlebih';
elif (25.0 <= imt <= 29.9):
    text = 'BB berlebih';
elif (18.5 <= imt <= 24.5):
    text = 'BB ideal';
else :
    text = 'BB kurang';

print ('Massa ' + str(massa) + ' kg & tinggi ' + str(tinggi/100) + ' m ');
print ('IMT = ' + str(imt) +', ' + text);
