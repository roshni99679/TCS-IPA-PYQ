#program to print index of second occurence of given number in a list of numbers

def so(numlist,num):
    count=0
    for i,v in enumerate(numlist):
        
        if v==num:
            count+=1
            if count>=2:
                print(i)
                break


n=int(input())
numlist=[]
for i in range(n):
    inp=int(input())
    numlist.append(inp)
num=int(input())
print("output-----------------")
if num not in numlist:
    print("Number is not present in the list")
else:
    so(numlist,num)


