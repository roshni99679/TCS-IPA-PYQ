#count of prime numbers in a list

def isprime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def ans(ls):
    cp=0
    lst=[]
    for l in ls:
        if isprime(l):
            lst.append(l)
            cp+=1
    print(lst,cp)
ans([3,5,7,11,1,2,4,19,54])