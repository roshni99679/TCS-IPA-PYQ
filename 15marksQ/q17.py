'''
input: hello worldaeiou 123
output: hll wrld 3
remove vowels from the given string and also print count of digits in given string
'''

str="hello worldaeiou 123"


def rem(str):
    res=''
    dig_count=0
    vowels=["a","e","i","o","u"]
    for char in str:
        if char.isdigit():
            dig_count+=1
        elif char.isalpha() or char.isspace():
            if char.lower() in vowels:
                continue
            else:
                res+=char
    print(res,end="")
    print(dig_count)
rem("hello worldaeiou 123")


