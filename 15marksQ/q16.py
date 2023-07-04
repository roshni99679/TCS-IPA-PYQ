'''
input: Rosh is happyil and satisfied very wellil
output: Rosh is happy and satisfied very well
remove unwanted string 'il' from given string
'''

def rem(str):
    ans=[]
    ls=str.split()
    for l in ls:
        if "il" not in l:
            ans.append(l)
        elif "il" in l:
            new=l.replace("il",'')
            ans.append(new)
    res=" ".join(ans)
    print(res)
rem("Rosh is happyil and satisfiedil with the current situationil")


inp=input()
ans=inp.replace("il",'')
print(ans)