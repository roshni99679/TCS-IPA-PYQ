'''
input:

5
1
rosh
56
4000
8
2
khush
57
5000
4
3
deep
26
400
5
4
geet
40
899
5.9
5
san
59
8000
8.9


op:
virat
virat1
virat4

'''

class Player:
    def __init__(self,pid,pn,wic,runs,run_rate):
        self.pid=pid
        self.pn=pn
        self.wic=wic
        self.runs=runs
        self.run_rate=run_rate
class Answer:
    def __init__(self,plist):
        self.plist=plist
    def sol(self):
        ans=[]
        for p in self.plist:
            if p.wic>50 and p.runs>1000 and p.run_rate>7.5:
                ans.append(p)
        ans.sort(key=lambda x:x.run_rate,reverse=True)
        if len(ans)>0:
            for a in ans:
                print(a.run_rate)
                print(a.pn)
                
                
n=int(input())
plist=[]
for i in range(n):
    pid=int(input())
    pn=input()
    wic=int(input())
    runs=int(input())
    run_rate=float(input())
    obj=Player(pid,pn,wic,runs,run_rate)
    plist.append(obj)
aobj=Answer(plist)
aobj.sol()