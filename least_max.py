size=int(input())
array=input()
list_=[]
sum_=0
list_=array.split()
for i in list_:
    i=int(i)
    sum_+=i
list_.sort()

least_max=sum_
x=int(len(list_)/2)

while True:
    if len(list_)*int(list_[int(x)])<=sum_:
        if len(list_)*int(list_[int(x+len(list_)/2)])>=sum_:
            x=int((x+len(list_))/2)
        else:
            x=int(x+(int(x+len(list_))/2))/2
    elif len(list_)*int(list_[x])>sum_:
        if least_max<len(list_)*int(list_[x]):
            print(list_[x])
            break
        else:
            if least_max<len(list_)*int(list_[x-1]) and least_max>len(list_)*int(list_[x-2]):
                print(list_[x-1])
            else:
                x=(len(list_)+1)/2
    else:
        pass

        
    
