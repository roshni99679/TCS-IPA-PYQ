str=input("Enter a string: ")
vowels=["a","e","i","o","u"]
def fun(str):
    str=str.lower()
    c_v=0
    c_c=0
    for x in str:
        if x.isdigit() or x==" ":
            continue
        if x in vowels:
            c_v+=1
        if x not in vowels:
            c_c+=1

    return c_v,c_c
a,b=fun(str)
print("count of vowels:",a,"count of consonants:",b)