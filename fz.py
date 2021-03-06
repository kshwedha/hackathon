list_={}
a=[]
max_=int(0)
test_case=int(input())
for i in range(test_case):
    size=int(input())
    array=input()
    a=array.split()
    for i in a:
        list_[i]=0
        #print(i,list_[i])
    for i in a:
        list_[i]=list_[i]+1
    for i in list_:
        if int(i)>int(max_):
            max_=i
    for i in range(len(list_)):
        if(list_[i]==max_):
            print(i)
    size=int(0)
    a.clear()
    max=0
    list_.clear()
