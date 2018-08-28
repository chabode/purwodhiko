# def times(num):
#     return num*2;

# listNum = [1,2,3,4,5]
# listNum = [times(item) for item in listNum];
# print (listNum);

# listnum = [{"test1":[5,2]}, {"test1": [7,3]}, {"test1":[5,7]}];

# def test(a,b):
#     b = 5;
#     return {"test1" : [(a+b,5,9)]};

# listnum = [test(item["test1"][1] , item["test1"][0]) for item in listnum];
# print(listnum);
# print (listnum[1]["test1"][0][2:]);

# d = {"key1" : "kucing1", "key2" : "kucing2", "key3" : [4,"reeee"] };

# print(d["key1"]);
# print(d["key2"]);
# print(d["key3"][1]);

# t = (1, [0,"test"], {"a1" : True});

# print(t[2]["a1"]);
# print(t[1][1]);
# print(t[1][1]);
# print(t[0]);

# a = [1,2,1,3,"test1","hahaha", "test2", "hahaha"];
# s = set(a);
# print(s);
# print(list(s)[2])

##### MAPPING ########

# def times2(num , test =2):
#     return num[1] * test;

# listNum = [[1,9],[2,3],[4,3],[4,5],[4,5]];
# listNum = list(map(times2, listNum));
# print(listNum);

#############

##### FILTERING #####

# def genap(num):
#     return num % 2 == 0;

# listnum = [1,3,4,5,6,7,2,4,3,6,8,9];
# listnum = list(filter(genap, listnum));
# s = set(listnum);
# print(listnum);
# print(s);

##################################

###### SEARCHING #####

# numList = [1,2,3];
# # input = 'x';
# abc = input("Search : ");

# check1 = input in numList;
# # check2 = 'x' in ['x','y','z'];
# check3 = abc in 'kurakas';

# print(type(check1))
# # print(check2)
# print(check3)

######## SOAL PPT ########

# words = ['Merdeka','Sohib','Hellos','Hello','Kari Ayam']
# print(words);

# kata = input("Search : ");
# words = list(filter(lambda isi : kata in isi.lower(), words));
# print(words);

###########################

a = "test1";
b = 20;
d = { "" + a + "": 5, "" + str(b) + "": 9, "maruk": [7,8]};

for k,v in d.items():
    print("| %s | %s | " %(k, v));
# for item in d:
#     print(d[item]);

# d["keren"] = 70;
# d.update({"sito":"gendheng"});
# a = input("masukkan key : ");
# b = input("masukkan value : ");
# d.update({a : b});

kata = input("Search : ");
print(d.items());
b = dict(filter(lambda item : kata.lower() in item[0] , d.items()));

print(b);

################################

# d = {1:11, 2:22, 3:33}

# d2 = {k:v for k,v in filter(lambda t: t[0] in [1], d.items())}

# d3 = {k:v for k,v in d.items() if k in [2,3]}

# print(d2);
# print(d3);
