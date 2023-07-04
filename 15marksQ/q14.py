'''
You've got a  list, l=[10,20,30]. This list, whose values correspond to the mileage of a bike, vehicle, and bus, was provided. 
You should be aware that you'll need three inputs for the code: the distance to be traveled, the amount of gasoline required, and the budget for doing so. 
Since the mileage of the three vehicles varies, we can use a formula to calculate the actual amount of money we will need to spend while traveling by bike, car, or bus. 
We also input a fixed budget at the top, and when we compare all three to that budget, only those amounts that are less than the fixed budget are considered to be valid.
'''


def fn(ls,d,amt_of_feul,budget):
    ans=[]
    for l in ls:
        cost=(d*l)/amt_of_feul
        if cost<=budget:
            ans.append(round(cost,2))
    print(ans)
    if len(ans)==0:
        print("You cannot travel in any of those with your budget")
    elif len(ans)==1:
        print(ans[0])
    elif len(ans)>1:
        print(max(ans))
ls=[10,20,30]
d=int(input())
amt_of_feul=int(input())
budget=int(input())
fn(ls,d,amt_of_feul,budget)
    
