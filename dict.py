def con(a,d):
    for i in a:
        count=0
        for j in a:
            if(i==j):  
                count+=1
            d[i]=count
    if x not in d:
        print(0)
    else:
        print(d[x])
            
n=int(input())
a=list(map(int,input().split()))
q=int(input())
d=dict()
for i in range(q):
    x=int(input())
    con(a,d)
   
   