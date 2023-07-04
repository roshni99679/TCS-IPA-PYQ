'''
Create a class Bill with below attributes:

billNo- int
name - String
typeOfConnection - String
billAmount - double
status - boolean

where billNo is the bill number, name 
is the name of the customer, 
typeOfConnection is the type of the 
connection (prepaid, postpaid), 
billAmount is the bill amount and 
status is whether the bill is paid 
or not (if paid then value is TRUE 
else value is FALSE). 

The above attributes should be private, 
write getters, setters and 
parameterized constructor as required. 

Create class Solution with main method.
Implement two static methods - 
findBillWithMaxBillAmountBasedOnStatus 
and getCountWithTypeOfConnection 
in Solution class.

findBillWithMaxBillAmountBasedOnStatus method:
This method will take an array of 
Bill objects and a boolean parameter 
as parameters. 

The method will return bill object 
array in ascending order of 
their bill number from the array of 
Bill objects whose bill 
Amount is maximum in the array with 
the status attribute that 
matches with the input parameter.

If no Bill with the given status is 
present in the array 
of Bill objects, then the method should 
return null.

getCountWithTypeOfConnection method:
This method will take two input 
parameters - array of Bill
objects and string parameter ( for type 
of connection).
The method will return the count of bills 
from array of bill 
objects for the given type of connection.
If no bill with the given type of 
connection is present in 
the array of bill objects, then 
the method should return 0.


Note :

Two bill object can have the same 
bill amount.
All the searches should be case insensitive. 

The above mentioned static methods 
should be called from the main method.

For findBillWithMaxBillAmountBasedOnStatus 
method - The main method 
should print the billNo followed by # and 
name from the returned 
Bill object array if the returned 
value is not null.

If the returned value is null then 
it should print 
"There are no bill with the given status".


For getCountWithTypeOfConnection method - 
The main method should 
print the count of bills as it is, if the 
returned value is greater than 0,  
otherwise it should print 
"There are no bills with given type of connection".


Before calling these static methods in 
main, use Scanner to read the 
number of object and objects to read 
the values of Bill objects 
referring attributes in the above 
mentioned attribute sequence. 

Next, read the value for status and 
typeOfConnection.


Consider below sample input and output:
Input:

4
111
Aman Mittal
Prepaid
914.25
true
222
Rekha Kumar
Prepaid
1425.75
false
333
Samyra Gupta
Prepaid
1305.00
true
444
Mohit Saxena
Postpaid
1300.50
false
false
Prepaid

Output:

222#Rekha Kumar
3
'''

# class Bill:
#     def __init__(self, billNo, name, typeOfConnection, billAmount, status):
#         self.__billNo = billNo
#         self.__name = name
#         self.__typeOfConnection = typeOfConnection
#         self.__billAmount = billAmount
#         self.__status = status

#     def getBillNo(self):
#         return self.__billNo

#     def getName(self):
#         return self.__name

#     def getTypeOfConnection(self):
#         return self.__typeOfConnection

#     def getBillAmount(self):
#         return self.__billAmount

#     def getStatus(self):
#         return self.__status

# class Solution:
#     @staticmethod
#     def findBillWithMaxBillAmountBasedOnStatus(billList, status):
#         filteredBills = [bill for bill in billList if bill.getStatus() == status]
#         if len(filteredBills) == 0:
#             return None
#         else:
#             sortedBills = sorted(filteredBills, key=lambda bill: bill.getBillAmount(), reverse=True)
#             return sortedBills

#     @staticmethod
#     def getCountWithTypeOfConnection(billList, typeOfConnection):
#         filteredBills = [bill for bill in billList if bill.getTypeOfConnection().lower() == typeOfConnection.lower()]
#         return len(filteredBills)

# # Main method
# if __name__ == "__main__":
#     billList = []
#     numBills = int(input())

#     for _ in range(numBills):
#         billNo = int(input())
#         name = input()
#         typeOfConnection = input()
#         billAmount = float(input())
#         status = input().lower() == "true"
#         bill = Bill(billNo, name, typeOfConnection, billAmount, status)
#         billList.append(bill)

#     status = input().lower()
#     typeOfConnection = input().lower()

#     result1 = Solution.findBillWithMaxBillAmountBasedOnStatus(billList, status)
#     if result1 is not None:
#         for bill in result1:
#             print(str(bill.getBillNo()) + "#" + bill.getName())
#     else:
#         print("There are no bills with the given status")

#     result2 = Solution.getCountWithTypeOfConnection(billList, typeOfConnection)
#     if result2 > 0:
#         print(result2)
#     else:
#         print("There are no bills with the given type of connection")

''
class Bill:
    def __init__(self,bn,n,tc,ba,s):
        self.bn=bn
        self.n=n
        self.tc=tc
        self.ba=ba
        self.s=s

class Solution:
    @staticmethod
    def findBillWithMaxBillAmountBasedOnStatus(blist,s):
        # ans=[b for b in blist if b.s==s]
        # if len(ans)>0:
        #     ans.sort(key=lambda x:x.ba,reverse=True)
        #     for a in ans:
        #         print(str(a.bn)+"#"+str(a.n))
        #         break
        # else:
        #     print("No bill")
        ans=[]
        for b in blist:
            if b.s.lower()==s.lower():
                ans.append(b)
        if len(ans)>0:
            ans=sorted(ans,key=lambda x:x.ba,reverse=True)
            for a in ans:
               print(str(a.bn)+"#"+str(a.n))
               break
        else:
            print("None")

    @staticmethod    
    def getCountWithTypeOfConnection(blist,tc):
        count=0
        for b in blist:
            if b.tc.lower()==tc.lower():
                count+=1
        if count==0:
            print("2.No bill")
        else:
            print(count)


n=int(input())
blist=[]
for i in range(n):
    bn=int(input())
    n=input()
    tc=input()
    ba=float(input())
    s=input()
    billobj=Bill(bn,n,tc,ba,s)
    blist.append(billobj)
s=input()
tc=input()
Solution.findBillWithMaxBillAmountBasedOnStatus(blist,s)
Solution.getCountWithTypeOfConnection(blist,tc)