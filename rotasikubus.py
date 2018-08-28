
def mainMenu(theList):
    while True:



kubus = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

if ((kali == 0 and arah == 'Kanan') or (kali == 0 and arah == 'Kiri')):
    for i in range(4):
        for j,k in zip(range(4), range(4):
            newArr[i][j] = arr[i][k]

elif ((kali == 1 and arah == 'Kanan') or (kali == 3 and arah == 'Kiri')):
    for i,k in zip(range(4), range(3,-1,-1)):
        for j in range(4):
            newArr[j][k] = arr[i][j];

elif (kali == 2):
    for i,k in zip(range(4), range(3,-1,-1)):
        for j,l in zip(range(4), range(3,-1,-1)):
            newArr[k][l] = arr[i][j];

elif ((kali == 3 and arah == 'Kanan') or (kali == 1 and arah == 'Kiri')):
    for i in range(4):
        for j,k in zip(range(4), range(3,-1,-1):
            newArr[k][i] = arr[i][j];


rotated =  list(zip(*kubus[::-1]));
rotated2 = list(zip(*rotated[::-1]));
rotated3 = list(zip(*rotated2[::-1]));
print(kubus);
# print(rotated);
# print(rotated2);
# print(rotated3);