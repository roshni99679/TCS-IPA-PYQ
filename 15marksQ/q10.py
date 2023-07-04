#program to append all the str char in given str(containg numbers and alphabets) and int char in given string separately in a list
#ex:
#ip:"Hello123baby001"
#op: ['Hellobaby',123001]
#ip:"hellobaby"
#op:['hellobaby']
#ip:"123456"
#op:[123456]

def createList(str):
    ls=[]
    st=''
    num=''
    for s in str:
        if s.isalpha():
            st+=s
        elif s.isdigit():
            num+=s
    if len(st)>0 and len(num)>0:
        ls.insert(0,st)
        ls.insert(1,int(num))
        # ls.append(st)
        # ls.append(int(num))
        print(ls)
    elif len(st)>0 and len(num)==0:
        ls.insert(0,st)
        # ls.append(st)
        print(ls)
    elif len(st)==0 and len(num)>0:
        ls.insert(1,int(num))
        # ls.append(int(num))
        print(ls)
inp=input()
createList(inp)
