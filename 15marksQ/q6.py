n=int(input("Enter a number:"))
ls=[]
for i in range(n):
    x=input("str: ")
    ls.append(x)
def fun(ls,key):
    key=key.lower()
    s_key=0
    for str in ls:
        str=str.lower()
        s_key+=str.count(key)
    return s_key
print("sum of occurence of key is:",end=" ")
print(fun(ls,"hello"))
