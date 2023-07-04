# program to print char at odd positions/indexes including white spaces

def fn(str):
    for i in range(len(str)):
        if i%2!=0:
            print(str[i],end='')
fn("hey there!")
# e hr!


# def ofn(str):
#     res=''
#     for i,v in enumerate(str):
#         if i%2!=0:
#             res+=v
#     print(res)
# ofn("hey there!")
# e hr!