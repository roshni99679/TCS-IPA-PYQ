# num=int(input("Enter a number"))
# def fun(num):
#     s_d=0
#     temp=num
#     while temp!=0:
#         ld=temp%10
#         s_d+=ld
#         temp=temp//10
#     if s_d%3==0:
#         print("Sum of digit of the number",num,"is",s_d," and it is div by 3")
#     else:
#         print("Sum of digit of the number",num,"is",s_d," and it is not div by 3")
# fun(num)



num2=int(input("Enter a number:"))
def fun2(num2):
    s=0
    num2=str(num2)
    for x in num2:
        s+=int(x)
    if s%3==0:
        print("True")
    else:
        print("False")
fun2(num2)