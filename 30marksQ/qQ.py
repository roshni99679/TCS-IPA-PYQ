'''


Create class Medicine with below attributes:
MedicineName - String 
batch - String
disease - String
price - int
Create class Solution and
implement static method "getPriceByDisease" in the Solution class.
This method will take array of Medicine objects and a disease String as parameters. And will return another array of Integer objects
where the disease String matches with the original array of Medicine object's disease attribute (case insensitive search).
Write necessary getters and setters.
Insight
Before calling "getPriceByDisease" method in the main method,
read values for four Medicine objects referring the attributes in above sequence along with a String disease.
Then call the "getPriceByDisease" method and print the result.


input:
4
dolo650
FAC124W
fever
100
paracetamol
PAC545B
bodypain
150
almox
ALM747S
fever
200
aspirin 
ASP849Q
flu
250
fever

Output :
100
200




'''


class Medicine:
    def __init__(self,mn,b,d,p):
        self.mn=mn
        self.b=b
        self.d=d
        self.p=p
class Solution:
    @staticmethod
    def getPriceByDisease(mlist,d):
        ans=[]
        for m in mlist:
            if m.d.lower()==d.lower():
                ans.append(m.p)
        if len(ans)>0:
            
            for a in ans:
                print(a)
n=int(input())
mlist=[]
for i in range(n):
    mn=input()
    b=input()
    d=input()
    p=input()
    med=Medicine(mn,b,d,p)
    mlist.append(med)
d=input()
Solution.getPriceByDisease(mlist,d)
        