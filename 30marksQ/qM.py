"""
input:
5
104
india
forest
101
america
mountain
108
japan
zoo
110
china 
mountain
105
canada 
mountain
MOUNTAIN


op:
110
china 
mountain
105
canada 
mountain
101
america
mountain

"""


class Adventure:
    def __init__(self,id,c,adv_spot):
        self.id=id
        self.c=c
        self.adv_spot=adv_spot
class Answer:
    def __init__(self,alist):
        self.alist=alist
    def aspot(self,adv_spot):
        ans=[]
        for a in self.alist:
            if a.adv_spot.lower()==adv_spot.lower():
                ans.append(a)
        if len(ans)>0:
            ans.sort(key=lambda x:x.id,reverse=True)
            for a in ans:
                print(a.id)
                print(a.c)
                print(a.adv_spot)
        else:
            print("Not found")
n=int(input())
alist=[]
for i in range(n):
    id=int(input())
    c=input()
    adv_spot=input()
    adv=Adventure(id,c,adv_spot)
    alist.append(adv)
adv_spot=input()
obj=Answer(alist)
print("Output-------------")
obj.aspot(adv_spot)