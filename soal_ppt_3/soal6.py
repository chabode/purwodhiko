n = int (input("berapa ukurannya = "));
z=''

for i in range(n):
    for j in range(i,n):
        z += ' * ';
    for k in range(0, (i*2)-1):
        z += '   ';
    for l in range(n, i, -1):
        if (l==1):
            break;
        z += ' * ';
    z += '\n';
for i in range(n-1):
    for j in range(0,i+2):
        z += ' * ';
    for k in range(n*2-5, i*2, -1):
        z += '   ';
    for l in range(0, i+2):
        if (l==1):
            break;
        z += ' * ';
    z += '\n';

print(z)