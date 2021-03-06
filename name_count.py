def check_rep(strin):
    #print(strin)
    i=0
    count_suvo=0
    count_suvojit=0
    while i<len(strin)-1:
        if strin.find('SUVOJIT')!=-1:
            count_suvojit+=1
            i=i+7
        if strin.find('SUVO')!=-1:
            count_suvo+=1
            i=i+4
    print("SUVO = {0}, SUVOJIT = {1}".format(count_suvo,count_suvojit))
            
            
    

test_cases=int(input())
for i in range(test_cases):
    #srin=str(input())
    check_rep(str(input()))
