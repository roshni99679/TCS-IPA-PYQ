def validstr(str):
    #return all[char.isalpha() or char.isspace for char in str]...returns true/false
    for char in str:
        if (char.isalpha() or char.isspace()):
            continue
        else:
            return False
    return True
n=int(input())
lst=[]
for i in range(n):
    str=input()
    lst.append(str)
def vcount(lst):
    count=0
    n=len(lst)
    for str in lst:
        if validstr(str):
            count+=1
    print("Count of valid string",count)
    print("Count of Invalid string",n-count)
vcount(lst)

    


