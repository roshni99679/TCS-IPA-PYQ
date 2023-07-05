'''
input:
hello hi loli hello hi lola hello

output:
{hello:3,
hi:2,
loli:1,
lola:1}
'''


def fn(str):
    ls=str.split()
    dic={}
    for l in ls:
        if l not in dic:
            dic[l]=0
        dic[l]+=1
    print(dic)
fn("hello hi loli hello hi lola hello")