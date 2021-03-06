
def loop(i, s, d):
    c = 0
    while True:
        if i == len(s):
            break
        if 3 in [d[i] for i in d]:
            break
        else:
            if d[s[i]]==1:
                d[s[i]] = 0
                if 1 not in [d[i] for i in d]:
                    d[s[i]]+=1
                    c+=1
                else:
                    d[s[i]]+=1
                d[s[i]]+=1
            else:
                d[s[i]]+=1
            al = 0
            al2 = 0
            for k in d:
                if d[k] == 2:
                    al = 1
                else:
                    al2 = 1
            if al == 1 and al2 == 0:
                break
            else:
                i+=1
    return c

def fun(strn):
    dic = {}
    count = 0
    i = 0
    for j in range(0,len(strn)):
        for i in range(len(strn)-1):
            dic[strn[i]] = 0
        print("count {}".format(count))
        count += loop(j, strn,  dic)
    return count

print("this program prints the no of sub strings possible with each letter atmost 2 times.\n")
string = 'aabccbbcaa'
ct = fun(string)
print(ct)
