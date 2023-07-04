str=input("Enter string : ")
def fun(str):
    c_a=0
    c_s=0
    for s in str:
        if s.isdigit():
            continue
        elif s.isalpha():
            c_a+=1
        elif s.isspace():
            c_s+=1
    return c_a,c_s
a,b=fun(str)
print("alphabet count: ",a,"space count: ",b)
