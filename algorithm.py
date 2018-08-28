# def fizzbuzz(n):
#     for i in range(1, n+1):
#         if (i % 15 == 0):
#             print("FizzBuzz");
#         elif (i % 5 == 0):
#             print("Buzz");
#         elif (i % 3 == 0):
#             print("Fizz");
#         else :
#             print(i);

# a = int(input("angkanya : "))
# fizzbuzz(a);

# def fibo(urut):
#     listData = [1,1];
#     for i in range(2, urut):
#         listData.append(listData[i-2] + listData[i-1]);       
#     return listData[-0];

# a = int(input("angkanya : "))
# print(fibo(a));

# import math;
# x = [1,2,3,4,5,6,7,8]

# print(x[::-1]);

# def reverseList(x):
#     for i in range(0, math.floor(len(x)/2)):
#         tempList = x[i];
#         x[i] = x[len(x) - 1 - i];
#         x[len(x) -1 -i] = tempList;
#     return x;

# print(reverseList(x));

x = [1,2,3,2,5,2,7,2]

def mean(x):
    sum = 0;
    for item in x:
        sum += item;
    mean = sum/len(x);

    # mean = sum(x)/len(x);

    return mean;
    # return sum(x)/len(x);

def median(x):
    x.sort();
    median = 0;
    if(len(x)%2 != 0):
        median = list[floor(len(x) /2)];
    else :
        mid1 = list[(int(len(x) /2)) -1];
        mid2 = list[int(len(x) /2)];
        median = (mid1 + mid2)/2;
    return median;

def mode():
    return

print(mean(x));