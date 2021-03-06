#1 2 3 4 9 8
#input
#constraint ith value < i+1th val to traverse for profit

a=[]
[a.append(int(i)) for i in input("enter\n").split(' ')]
sum = 0
for i, j in enumerate(a):
    if i+1==len(a):
        sum+=a[i]
    else:
        var_ = -1
        for k in a[i+1:]:
            if var > a[k]:
                var_ = a[k]
        sum+= var_
        return sum


def type2():
    for i in a:
        if sum < i:
            sum+=i
    return sum

choice = ("which type 1 or 2")
if ch == 1:
    sum = type1()
elif ch == 2:
    sum = type2()
else:
    import os
    sys.exit()    
print(sum)
