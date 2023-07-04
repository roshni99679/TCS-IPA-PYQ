# num = int(input("Please enter a number"))
# lst = []
# for i in range(num):
#     x = int(input())
#     lst.append(x)
#     n= ''.join(map(str, lst))
# print(type(n))#<class 'str'>
# def factors(n):
#     s_f=0
#     factors = set()#using set because same factors are not added more than once
#     for i in range(1, n + 1):
#         if n % i == 0:  
#             factors.add(i)
#             s_f+=i
#     return factors,s_f
# a,b = factors(int(n))
# print("list of factors:", list(a))
# print("sum of factors:", b)

# ls=[1,3,5,7,89,90]
# a1=''.join(map(str,ls))
# ls2=["hello","good","morning"]
# a2=' '.join(ls2)
# print(a1+a2)#13578990hello good morning
# print(a1,a2)#13578990 hello good morning



lst=[]
n=int(input())
for i in range(n):
    x=input()
    lst.append(x)
    ans=''.join(lst)
print(ans)
ans=int(ans)
def fun(ans):
    myl=[]
    st=set()
    for i in range(1,ans+1):
        if ans%i==0:
            st.add(i)
            myl.append(i)
    return myl,st
a,b=fun(ans)
print(a,len(a),sum(a))
print(b,len(b),sum(b))
#[1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120] 16 360
#{1, 2, 3, 4, 5, 6, 8, 40, 10, 12, 120, 15, 20, 24, 60, 30} 16 360