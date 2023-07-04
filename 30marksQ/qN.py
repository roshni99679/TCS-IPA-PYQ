'''
input:
5
1
10000
Electric
Available
2
20000
Diesel
Not available
3
30000
Electric
Available
4
40000
Petrol
Available
5
50000
Electric
Available




output:
electric : 3
diesel : 0
petrol : 1

'''

class Feul:
    def __init__(self,id,p,fn,status):
        self.id=id
        self.p=p
        self.fn=fn
        self.status=status
class Answer():
    def __init__(self,flist):
        self.flist=flist
    def fs(self):
        dic={}
        for f in self.flist:
            if f.status.lower()=="available":
                if f.fn not in dic:
                    dic[f.fn]=0
                dic[f.fn]+=1
            elif f.status.lower()=="not available":
                dic[f.fn]=0

        if len(dic)>0:
            for k,v in dic.items():
                print(k,":",v)
n=int(input())
flist=[]
for i in range(n):
    id=int(input())
    p=int(input())
    fn=input()
    status=input()
    fobj=Feul(id,p,fn,status)
    flist.append(fobj)
obj=Answer(flist)
print("Output----------------")
obj.fs()
