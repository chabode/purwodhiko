z=''

n = int(input("masukkan angka yang diinginkan = "))

for i in range(n):
    for j in range(n,i,-1):
        z += '* '
    z += '\n'
for i in range(n-1):
    for j in range (0, i+2):
        z += '* ';
    z += '\n'
# for i in range(n):
#     if (i>0):
#         for j in range(0,i+1):
#             z += '* '
#         z += '\n'

print(z);