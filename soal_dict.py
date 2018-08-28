dictionari = {"test":20, "44":409, "buka":74};

def printMainMenu() :
    # inputUser = input("Main Menu : \n 1. Lihat Dictionary\n 2. Insert Dictionary\n 3. Filter Dictionary\n 4. Keluar\n\n Pilih Menu : ");
    # return inputUser;
    return input("Main Menu : \n 1. Lihat Dictionary\n 2. Insert Dictionary\n 3. Filter Dictionary\n 4. Keluar\n\n Pilih Menu : ");

def lihatDict(theDictionari):
    print("dictionari :")

    for key in theDictionari:
        if(str(type(theDictionari[key])) == "<class 'str'>"):
            print("| " + key + " | '" + theDictionari[key] + "' |");
        elif (str(type(theDictionari[key])) == "<lass 'int'>" ):
            print("| " + key + " | " + theDictionari[key] + " |");


def insertDict(theDictionari):
    inputKey = input("Isi Key : ")
    inputJenis = input("Value input 1 untuk string 2 untuk angka : ");
    if (inputJenis == "1"):
        inputValue = input("Value : ");
        theDictionari[inputKey] = inputValue;
    elif (inputJenis == "2"):
        inputValue = int(input("Value : "));
        theDictionari[inputKey] = inputValue;   
    else :
        print("ulangin lagi dul");

def searchDict(theDictionari):
    inputSearch = input("Key yang dicari : ");
    newDD = {};
    for key in theDictionari:
        if(inputSearch.lower() in key.lower()):
            newDD[key] = theDictionari[key];

    lihatFullDict(newDD);

newDictionari = {};
while True :
    pilihanUser = printMainMenu();
    if(pilihanUser == "1") :
        lihatDict(newDictionari);
    elif(pilihanUser == "2") :
        insertDict(newDictionari);
    elif(pilihanUser == "3") :
        searchDict(newDictionari);
    elif(pilihanUser == "4") :
        print("Bye bye!")
        break;