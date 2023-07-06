'''

Create class Associate with below attributes:
id - int
name - String
technology - String
experienceln Years - int
Create class Solution and implement
static method "associatesForGiven Technology" in the Solution class. This method will take array of Associate objects and a search Technology String as parameters. And will return another array of Associate objects where the search Technology String matches with the original array of Associate object's technology attribute (case insensitive search) and experienceln Years attribute should be multiples of 5.
Write necessary getters and setters.
Insight
Before calling "associatesForGiven Technology" method in the main method, read values for five associate objects referring the attributes in above sequence along with a String search Technology. Then call the
"associatesForGivenTechnology" method and write the logic to
print the id's in the main method.

input:
5
101
Alex
Java
15
102
Albert
Unix
20
103
Alferd
Testing
13
104 
Alfa
Java
15
105 
Almas
Java
29
Java

output:
101
104
105

'''


class Associate:
    def __init__(self,id,n,t,e):
        self.id=id
        self.n=n
        self.t=t
        self.e=e
n=int(input())
alist=[]
for i in range(n):
    id=int(input())
    n=input()
    t=input()
    e=int(input())
    assobj=Associate(id,n,t,e)
    alist.append(assobj)
class Solution:
    @staticmethod
    def associatesForGivenTechnology(t):
        ans=[]
        for a in alist:
            if a.t.lower()==t.lower():
                ans.append(a.id)
        if len(ans)>0:
            for a in ans:
                print(a)

t=input()
Solution.associatesForGivenTechnology(t)


