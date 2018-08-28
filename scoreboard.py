#### Main Menu
# 1. isi list
# 2. lihat List
# 3. Keluar

# isi angka list, balik ke main menu
# cetak list, print list yang udah diisi
# lihat list, cetak list dalam bentuk score board
#  _  _  _  _  _     _  _
# |_||_|  ||_ |_ |_| _| _| |
#  _||_|  ||_| _|  | _||_  |
# 

def inputlist(rep):
    while True:
        angka = input("masukkan angka : ")
        if angka.isdigit():
            rep += list(angka)
            return rep
        else :
            print("\nanda salah memasukkannya.")


def lihatlist(angka):
    upper   = {"0":" _ ", "1":"   ", "2":" _ ", "3":" _ ", "4":"   ", "5":" _ ", "6":" _ ", "7":" _ ", "8":" _ ", "9":" _ "}
    middle  = {"0":"| |", "1":"  |", "2":" _|", "3":" _|", "4":"|_|", "5":"|_ ", "6":"|_ ", "7":"  |", "8":"|_|", "9":"|_|"}
    lower   = {"0":"|_|", "1":"  |", "2":"|_ ", "3":" _|", "4":"  |", "5":" _|", "6":"|_|", "7":"  |", "8":"|_|", "9":" _|"}
    atas,tengah,bawah = "","","";
    for i in angka:
        atas += upper[i];
        tengah += middle[i];
        bawah += lower[i];
    print(f"{atas}\n{tengah}\n{bawah}");

def clearlist(rep):
    rep.clear();
    print("clear ");
    return rep

# def mainmenu(rep = []):
rep = rep.copy();
while True:
    inputuser = input("7Segments\n 1. Isi List angka\n 2. Lihat List angka\n 3. Hapus List angka\n 4. Keluar\n Input Menu : ")
    if (inputuser == "1"):
        rep = inputlist(rep);
    elif (inputuser == "2"):
        lihatlist(rep);
    elif (inputuser == "3"):
        clearlist(rep);
    elif (inputlist == "4"):
        print("Program selesai")
        break;

# mainmenu()