def prime(n):
    flag=0
    for j in range(2,int(n**(1/2))+1):
        if n%j==0:
            return False        
    return True        
        
l=[]       
n=int(input())
for i in range(2,n):
    if prime(i):
        l.append(i)
print(l)        
a=set()        
for i in range(len(l)):
    for j in range(i,len(l)):
        s=l[i]+l[j]
        if not prime(s) and s<=n:
            a.add(s)
print(a)            
        
    
    