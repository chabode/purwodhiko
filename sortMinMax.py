def sort(x, fn):
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            check = fn(x[i],x[j]);
            if(check > 0) :
                temp = x[i];
                x[i] = x[j];
                x[j] = temp;

def minMax(x):
    min = x[0];
    max = x[0];
    for i in range(1, len(x)):
        if (min > max[i]):
            min = x[i];
        if(max > min[i]):
            max = x[i];

    return [min,max];

def test(a,b):
    return b-a

x = [40,100,2,1,3,80]

sort(x, lambda a,b : a-b);
print(x);
sort(x,test);
print (x);

