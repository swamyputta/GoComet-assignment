s=list(map(int,input().split()))
target=int(input())
l,h=0,len(s)-1
while l<h:
    mid=(l+h)//2
    if s[mid]>s[h]:
        l=mid+1
    else:
        h=mid
p=l
p1,p2=0,len(s)-1
a=s[p:]+s[:p]
f=False
while p1<p2:
    if a[p1]+a[p2]==target:
        f=True
        break
    elif a[p1]+a[p2]>target:
        p2-=1
    else:
        p1+=1
if f:
    print(True)
else:
    print(False)
    