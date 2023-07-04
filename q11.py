#print smallest vowel in given str
#ex: 
#inp:handu
#op:a

def sv(str):
    ls=[]
    vowels='aeiou'
    str=str.lower()
    for s in str:
        if s in vowels:
            ls.append(s)
    ls.sort()
    print(ls[0])
str=input()
sv(str)

