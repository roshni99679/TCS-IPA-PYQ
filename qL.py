#https://youtube.com/playlist?list=PLu-8vKAl2tQFxb5QT7sPTTL6w2EpxVC0d


class Film:
    def __init__(self,fs,fn,p,l):
        self.fs=fs
        self.fn=fn
        self.p=p
        self.l=l
class Answer:
    def __init__(self,flist):
        self.flist=flist
    def fn(self):
        ls=[]
        for f in self.flist:
            if f.l.lower()=="english" and f.p>=500:
                ls.append(f)
        if len(ls)>0:
            ls.sort(key=lambda x:x.p,reverse=True)
            for l in ls:
                print(l.fs)
                print(l.fn)
        else:
            print("No such film")
n=int(input())
flist=[]
for i in range(n):
    fs=input()
    fn=input()
    p=int(input())
    l=input()
    filmobj=Film(fs,fn,p,l)
    flist.append(filmobj)
ans=Answer(flist)
print("Output-----------------")
ans.fn()




'''
5
abc
hahk
400
hindi
def
avengers
300
english
ghi
hellobaby
700
chinese
dbkcjdc
engmovie
501
english
hdcbowljc
engmovie2
799
english
'''


'''
hdcbowljc
engmovie2
dbkcjdc
engmovie
'''