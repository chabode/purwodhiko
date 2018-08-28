#Right triangle star

# n = int(input("masukkan baris yang diinginkan : "))

# for i in range(n+1):
#     for j in range(i):
#         print("*", end=" ");
#     print("\r");

# Hollow Triangle

# n = int(input("masukkan baris yang diinginkan : "))

# for i in range(n+1):
#     for j in range(i+1):
#         if(j==0 or j==i or j==n+1):
#             print("*");
#         else :
#             print(" ", end=" ");
#     print("\r");

#zip range diatas 4

for i,j,k,l in zip(range(4), range(3,-1,-1), range(10,5,-1), range(2,20,2)):
    print(f'{i} diatas {j} dibawah {k} diantara {l}');