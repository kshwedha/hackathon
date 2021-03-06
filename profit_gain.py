#1 2 3 4 9 8
#n = int(input())
a=[]
[a.append(int(i)) for i in input("enter\n").split(' ')]
sum = 0
for i, j in enumerate(a):
    if i+1==len(a)-1:
        sum+=a[i+1]
        break
    if a[i] < a[i+1]:
        sum+= j
    else:
        pass
print(sum)


#for i in a:
#    if sum < i:
#        sum+=i
#print(sum)
