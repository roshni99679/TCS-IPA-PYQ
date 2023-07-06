'''

Create a class Traveler with below attributes
travelerName : (string type)
traveled Country: (list of string type represents the names of the country the traveler has travelled.) 
travelerAge: (int type)
countryFrom:(string type)
Create a constructor which takes all the above attributes in the same sequence.

Define another class TravelAgency with below attributes:
travelerList: (list of Traveler objects)
and having the below member functions:

countTravelersTraveled Country: Which takes a string representing the name of a country as input, and returns the count of travelers from the travelerList of Travel Agency who has travelled that country.

getTravelerTravelledMaxCountry: finds the traveler who has travelled highest number of countries and returns the name of that traveler. If more than one such travelers are there having the highest count of countries travelled method returns the name of the traveler whose name appears first in the list as taken as input.

input:
5
Sachin
4
A
B
C
D
40
India
Kamini
4
P
Q
R
S
20
China
Saurav
6
S
D
F
G
H
J
32
Nepal
Ricky
3
A
F
V
33
Hyd
Dravid
2
S
F
55
Kol
S

output:
3
Saurav

'''

class Traveller:
    def __init__(self,n,cls,a,c):
        self.n=n
        self.cls=cls
        self.a=a
        self.c=c
class TravelAgency:
    def __init__(self,tlist):
        self.tlist=tlist
    def countTravelersTraveledCountry(self,c):
        ans=[]
        for t in self.tlist:
            if c in t.cls:
                ans.append(t.n)
        count=len(ans)
        print(count)
    def getTravelerTravelledMaxCountry(self):
        ans_count=[]
        ans_name=[]
        for t in self.tlist:
            count=len(t.cls)
            ans_count.append(count)
        ans_count.sort(reverse=True)
        max_count=ans_count[0]
        for t in self.tlist:
            if len(t.cls)==max_count:
                ans_name.append(t.n)
        if len(ans_name)>0:
            print(ans_name[0])
nofT=int(input())
tlist=[]
for i in range(nofT):
    n=input()
    cls=[]
    num=int(input())
    for i in range(num):
        inp=input()
        cls.append(inp)
    a=int(input())
    c=input()
    trav=Traveller(n,cls,a,c)
    tlist.append(trav)
c=input()
travagency=TravelAgency(tlist)
travagency.countTravelersTraveledCountry(c)
travagency.getTravelerTravelledMaxCountry()


