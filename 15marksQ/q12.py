#program to reverse remaining char of a str if first three characters if given str is CHM
#ex:
#ip:CHMRIA
#op:CHMAIR

def rev(str):
    str=str.lower()
    c=str[:3]
    if c=="chm":
        print(c+str[3:][::-1])
    else:
        print(str)
rev("CHMRAI")



