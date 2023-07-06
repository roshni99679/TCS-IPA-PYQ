'''
Consider one string as input. You have to check whether the strings obtained from the input string with single backward and single forward shift are the same or not. If they are the same, then print 1: otherwise, print 0.
Backward Shift: A single circular rotation of the string in which the first character becomes the last character and all the other characters are shifted one index to the left. For example, "abcde" becomes "bcdea" after one backward shift.
the one bed sight
Forward Shift: A single circular rotation of the string in which the last character becomes the first character and all the other characters are shifted to the right. For example, "abcde" becomes "eabcd" after one forward shift.
'''

def bshift(str):
    ans=str[1:]+str[0]
    return ans
        
def fshift(str):
    ans=str[-1]+str[:-1]
    return ans

def fn(s):

        if bshift(s)==fshift(s):
            print(1) 
        else:
            print(0) 

# s="mama"
s="gfhpwarujwehg"
fn(s)

'''
input:
mama
gfhpwarujwehg

output:
1
0
'''