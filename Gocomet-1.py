n,m=map(int,input().split(','))
c1,c2=0,0
a1,a2=0,0
while n>0:
    if n&1==1:
        c1+=1
    else:
        a1+=1
    n=n>>1
while m>0:
    if m&1==1:
        c2+=1
    else:
        a2+=1
    m=m>>1
if c1==c2 and a1==a2:
    print(True)
else:
    print(False)
   
        