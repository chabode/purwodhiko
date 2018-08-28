print('Selamat datang di HaciHaciBen')

cart = [];
cart.append([]);
cart.append([]);

namaMenu = ["","Paket A Rp. 30000","Paket B Rp. 25000","Paket C Rp. 20000"]
hargaMenu = [0, 30000, 40000, 50000]
def program():
    print('Main Menu \n 1. Lihat Menu \n 2. Lihat Cart \n 3. Checkout \n 4. Keluar')
    print('\r')
    pick = int(input("Masukkan pilihan : "))
    if (pick == 1):
        lihatMenu() 
    elif (pick == 2):
        lihatCart() # print("sehat")
    elif (pick == 3):
        Checkout() # print("idih")
    elif (pick == 4):
        menuKeluar() # print("huehuehue")
    else :
        print("Anda salah memasukkan data")
        program();
    return

def lihatMenu():
    for i in range(len(namaMenu)):
        if (i > 0):
            print(f"{i}. {namaMenu[i]}")
    print('\r')
    pilih = int(input("pilih menu : "))
    if ((pilih > 0 and pilih < len(namaMenu) )and (pilih > 0 and pilih < len(hargaMenu)) ):
        print(f"{namaMenu[pilih]}");
        cart[0].append(namaMenu[pilih]);
        cart[1].append(hargaMenu[pilih]);
        program();
    else :
        print("Menu yang anda masukkan tidak ada")
        lihatMenu();
    
    print('\r');
    return

def lihatCart():
    for i in range(0, len(cart)):
        print(str[i+1] + '.' + cart[0][0]);
    print('\r')
    # print("Cart 2")
    # print("Cart 3")

    program();
    return

def Checkout():
    print("menu A")
    print("menu B")
    print("menu C")

    program();
    return

def menuKeluar():
    print("terimakasih atas kedatangannya")

    return

program();


