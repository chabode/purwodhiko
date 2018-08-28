z = ""
n = int(input("masukkan angka nya = "))

for i in range(n):
    for j in range(0, i):
        z += '  ';
    for k in range(0, (n*2)-(i*2)-1):
        z += "* ";
    z += '\n';

print(z);