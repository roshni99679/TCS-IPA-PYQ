n=int(input("Enter number of strings"))
ls=[]
for i in range(n):
    x=input("str: ")
    ls.append(x)
def fun(lst,key):
    for i,x in enumerate(lst):
        if x==key:
            return i
key=input("key: ")
ans=fun(ls,key)
if ans:
    print(ans)
else:
    print("String not found")

