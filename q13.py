def ans(ls,n):
    res=[]
    for l in ls:
        if l%n==0:
            res.append(l)
    if len(res)>0:
        print(max(res))
    else:
        print("no number found")
        
num=int(input())
ls=[]
for i in range(num):
    l=int(input())
    ls.append(l)
n=int(input())
ans(ls,n)

