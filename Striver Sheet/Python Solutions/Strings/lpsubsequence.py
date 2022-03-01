from math import sqrt

def getpro(a,rc,st,cc):
    p=1
    for i in range(st,st+rc):
        for j in range(cc,cc+rc):
            p=p*a[i][j]
    return p

def isper(num):
    sq=int(sqrt(num))
    return sqrt(num)-sq==0

n=int(input())
a=[]
for i in range(n):
    a.append([int(i) for i in input().split(",")])
m=int(input())
pref=[]
rpref=[]
for i in range(n-m+1):
    for j in range(len(a[i])-m+1):
        p=getpro(a,m,i,j)
        if isper(p):
            pref.append(p)
        else:
            rpref.append(p)
pref.sort()
rpref.sort(reverse=True)
pref.extend(rpref)
print(*pref,sep=",")