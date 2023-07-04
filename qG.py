'''
Create a class Sim with below attributes:

simId - int
customerName - String
balance - double
ratePerSecond - double
circle - String

Write constructor as required. 

Create class Solution .

Implement static method - 
transferCustomerCircle in Solution class.

This method will take first 
parameter as array of Sim class objects, 
second parameter as circle 
to be transferred (which is 
String parameter circle1) 
and third parameter as new 
circle (which is String parameter circle2).

Method will transfer the customer to 
new circle (circle2), where the circle 
attribute would match second parameter 
(circle1). Method will return array of 
Sim objects for which circle is 
transferred. Return array should be sorted in 
descending order of ratePerSecond 
(assuming ratePerSecond is not same 
for any of the Sim objects).


This method should be called from 
main method and display the simId,
customerName,circle 
and ratePerSecond of returned 
objects (as per sample output).

Main method mentioned above already 
has Scanner code to read values, 
create objects 
and test above methods. 
Hence do not modify it.

Consider below sample input and output:

Input:

5
1
raj
100
1.5
KOL
2
chetan
200
1.6
AHD
3
asha
150
1.7
MUM
4
kiran
50
2.2
AHD
5
vijay
130
1.8
AHD
AHD
KOL

Output:
4 kiran KOL 2.2
5 vijay KOL 1.8
2 chetan KOL 1.6



'''


'''class Sim:
    def __init__(self, simId, customerName, balance, ratePerSecond, circle):
        self.simId = simId
        self.customerName = customerName
        self.balance = balance
        self.ratePerSecond = ratePerSecond
        self.circle = circle

class Solution:
    @staticmethod
    def transferCustomerCircle(simList, circle1, circle2):
        transferredSims = []
        for sim in simList:
            if sim.circle == circle1:
                sim.circle = circle2
                transferredSims.append(sim)
        transferredSims.sort(key=lambda x: x.ratePerSecond, reverse=True)
        return transferredSims

# Main method
if __name__ == "__main__":
    numSims = int(input())
    simList = []

    for _ in range(numSims):
        simId = int(input())
        customerName = input()
        balance = float(input())
        ratePerSecond = float(input())
        circle = input()
        sim = Sim(simId, customerName, balance, ratePerSecond, circle)
        simList.append(sim)

    circle1 = input()
    circle2 = input()

    transferredSims = Solution.transferCustomerCircle(simList, circle1, circle2)

    if transferredSims:
        for sim in transferredSims:
            print(sim.simId, sim.customerName, sim.circle, sim.ratePerSecond)
    else:
        print("No sims transferred.")
'''

class Sim:
    def __init__(self,sid,cn,b,rps,c):
        self.sid=sid
        self.cn=cn
        self.b=b
        self.rps=rps
        self.c=c
class Solution:
    @staticmethod
    def transferCustomerCircle(slist,c1,c2):
        ans=[]
        for s in slist:
            if s.c.lower()==c1.lower():
                s.c=c2
                ans.append(s)
        
        if len(ans)>0:
            ans=sorted(ans,key=lambda x:x.rps,reverse=True)
            for a in ans:
                print(a.sid,a.cn,a.c,a.rps)

        else:
            print("No customer with given circle")
# n=int(input())
slist=[]
for i in range(5):
    sid=int(input())
    cn=input()
    b=float(input())
    rps=float(input())
    c=input()
    simobj=Sim(sid,cn,b,rps,c)
    slist.append(simobj)
c1=input()
c2=input()
Solution.transferCustomerCircle(slist,c1,c2)
