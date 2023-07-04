'''
1. Python_SBQ_Icecream

Create a class Icecream with below attributes:
int - id
int - price
String - name
int - quantityInGms
String - category

Create the __init__ method which takes 
all parameters in the above sequence.
The method should set the value 
of attributes to parameter values inside 
the method.


Create a class IcecreamStore 
with below attributes:

String - IcecreamStoreName
List - IcecreamList

Create the __init__ method which takes 
all parameters in the above sequence.
The method should set the value of 
attributes to parameter values inside the method.

 

Implement two  methods - 
findMinimumIcecreamByPrice and 
sortIcecreamByid in IcecreamStore class.

 

findMinimumIcecreamByPrice-----
Create a method findMinimumIcecreamByPrice 
in the IcecreamStore class. This method 
will return the Icecream having the 
minimum value for price of all the 
Icecream in the Icecream List of the 
IcecreamStore class. If there is no 
Icecream found in the Icecream List 
or list is empty then return None to main program.

 
sortIcecreamByid-------
Create a method sortIcecreamByid in 
the IcecreamStore class. This method 
will return the sorted list of ids in 
ascending order of all the Icecreams in 
the IcecreamList of the IcecreamStore class. 
If there is no Icecream found in the 
Icecream List or list is empty, then 
return None to main program.

 

These methods should be called from 
the main method.

 

Instructions to write main section of the code:

a. You would require to write the main 
section completely, hence please follow 
the below instructions for the same.

b. You would require to write the main 
program which is inline to the sample 
input description section  mentioned 
below and to read the data in the same sequence.

c.  To create IcecreamStore and Icecream 
objects , take the inputs in below sequence.

    To create a List of n Icecream 
    objects read the value of n.

    To create a List of n Icecream 
    objects read values for id, price, 
    name, quantityInGms, category 
    (in this order) and create the 
    Icecream object and add to the 
    List. Repeat this step n times.

    Create the IcecreamStore object 
    passing the IcecreamStoreName and the 
    List of Icecreams created in previous 
    step.

d. Call the method findMinimumIcecreamByPrice 
using the IcecreamStore object created in 
point  #c. 

e. Call the method sortIcecreamByid using 
the IcecreamStore object created in point #c.

f. Print the output of both methods as per 
given sample output.

g. If there is NONE returned from any method 
print-"No Data Found."(without quotes)

 

Don't use any static text or formatting 
for printing the result. Just invoke 
the method and print the result.

Sequence for specific object will 
follow same attribute sequence as 
mentioned in the question. You may 
refer to the sample Input/output for 
the display format.

 

Sample Input:

5
47
247
Vanilla
50
Mochi Icecream
61
877
Cookies n Cream
55
Gelato
90
310
Strawberry
45
Sorbet
24
620
Chocolate
30
Frozen Yogurt
54
163
Butterscotch
97
Rolled Icecream

 
Sample Output:

54
163
Butterscotch
97
Rolled Icecream
24
47
54
61
90

'''

'''
class Icecream:
    def init(self, id, price, name, quantityInGms, category):
        self.id = id
        self.price = price
        self.name = name
        self.quantityInGms = quantityInGms
        self.category = category

class IcecreamStore:
    def init(self, IcecreamStoreName, IcecreamList):
        self.IcecreamStoreName = IcecreamStoreName
        self.IcecreamList = IcecreamList
    def findMinimumIcecreamByPrice(self):
        if not self.IcecreamList:
            return None
        min_icecream = min(self.IcecreamList, key=lambda x: x.price)
        return min_icecream

    def sortIcecreamByid(self):
        if not self.IcecreamList:
            return None
        sorted_ids = sorted(icecream.id for icecream in self.IcecreamList)
        return sorted_ids

# Read the number of Icecream objects
n = int(input())
# Create a list of Icecream objects
IcecreamList = []
for _ in range(n):
    # Read the Icecream details
    id = int(input())
    price = int(input())
    name = input()
    quantityInGms = int(input())
    category = input()
    icecream = Icecream(id, price, name, quantityInGms, category)
    IcecreamList.append(icecream)

# Read the IcecreamStore name
IcecreamStoreName = input()

# Create an IcecreamStore object
icecreamStore = IcecreamStore(IcecreamStoreName, IcecreamList)

# Call the findMinimumIcecreamByPrice method
minimumIcecream = icecreamStore.findMinimumIcecreamByPrice()

# Print the minimum Icecream
if minimumIcecream:
    print(minimumIcecream.id)
    print(minimumIcecream.price)
    print(minimumIcecream.name)
else:
    print("No Data Found.")

# Call the sortIcecreamByid method
sortedIds = icecreamStore.sortIcecreamByid()

# Print the sorted Icecream ids
if sortedIds:
    for id in sortedIds:
        print(id)
else:
    print("No Data Found.")
'''

class Icecream:
    def __init__(self,iid,p,n,q,c):
        self.iid=iid
        self.p=p
        self.n=n
        self.q=q
        self.c=c
class IcecreamStore:
    def __init__(self,stn,ilist):
        self.stn=stn
        self.ilist=ilist
    def findMinimumIcecreamByPrice(self):
        # minicecream=min(self.ilist, key= lambda x:x.p)
        # return minicecream
        prices=[]
        for i in self.ilist:
            prices.append(i.p)

        if prices==[]:
            return None
        else:
            for l in self.ilist:
                if l.p==min(prices):
                    print(l.iid)  
                    print(l.p)
                    print(l.n)
                    print(l.q)
                    print(l.c)         
    def sortIcecreamByid(self):
        li=[]
        for v in self.ilist:
            li.append(v.iid)
        if li==[]:
            return None
        else:
            li=sorted(li)
            for x in li:
                print(x)
n=int(input())
ilist=[]
for i in range(n):
    iid=int(input())
    p=int(input())
    n=input()
    q=int(input())
    c=input()
    ice=Icecream(iid,p,n,q,c)
    ilist.append(ice)
st=input()
ist=IcecreamStore(st,ilist)
ist.findMinimumIcecreamByPrice()

# ans=ist.findMinimumIcecreamByPrice()
# if ans:
#     print(ans.iid)
#     print(ans.p)
#     print(ans.n)
#     print(ans.q)
#     print(ans.c)
# else:
#     print("No icecream found!")

ist.sortIcecreamByid()
