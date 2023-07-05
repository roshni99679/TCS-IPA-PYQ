
'''
input:
hello
hello1234
12345
kgf2345123

output:
hello
Alphabet: 5
hello1234
Alphabet: 5
Number: 4
12345
Number: 5
kgf2345123
Number: 7
Alphabet: 3
'''

def count(str):
    alpha_count=0
    num_count=0
    for char in str:
        if char.isalpha():
            alpha_count+=1
        elif char.isdigit():
            num_count+=1
    if num_count==0:
        print("Alphabet:",alpha_count)
    if alpha_count==0:
        print("Number:",num_count)
    if alpha_count>0 and num_count>0 and alpha_count>num_count:
        print("Alphabet:",alpha_count)
        print("Number:",num_count)
    if alpha_count>0 and num_count>0 and num_count>alpha_count:
        print("Number:",num_count)
        print("Alphabet:",alpha_count)
for i in range(4):
    inp=input()
    count(inp)
 
