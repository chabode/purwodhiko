# soal 1

def hasil(angka1, angka2, angka3) :
    eq1 = angka1 + angka2 * angka3; 
    eq2 = angka1 * angka2; 
    eq3 = eq1 / eq2; 
    eq4 = eq3 ** angka3;
    return eq4;

x = int(input("nilai x = "));
y = int(input("nilai y = "));
z = int(input("nilai z = "));

print(hasil(x,y,z));
