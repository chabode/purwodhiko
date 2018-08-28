z=''
n = int(input("masukkan angka diinginkan = "));

for i in range(n):
    for j in range(n,i,-1):
        z += '* '
    z += '\n'

print(z)