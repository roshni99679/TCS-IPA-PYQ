'''

Create a class pan .
Make attributes id , string
material , string
brand , string
price , int
capacity , int

Write constructor having argument in 
same order as above . 

Write the solution class
 and write main method
implement two static functions 
namely (costliest pan) and 
(discounted price) in it. 

Costliest pan function : 
It accepts 2 arguments , 
namely the array of pan class 
objects and material of a pan . 
It return the costliest pan 
of the given material.

Discounted price : 
It accepts 2 arguments , 
namely , array of pan objects and brand of pan . 
If capacity of given brand > 500 ml , 
update price to 20% discount . 
If capacity > 1000 ml , 
then update price to 26% discount . 


In the main function , 
take input of variable for 7 class objects . 
Take material as input , 
then take brand as input 
for passing to different functions. 
Call the costliest pan 
function , print the id of the 
object returned. 
Call the discounted price function , 
print the new value after updating . 



Input:

7
id23
brass
a
200
120
id24
cupper
b
300
1130
id25
chromium
c
400
640
id26
steel
d
500
950
id27
steel
e
800
950
id28
iron
f
500
950
id29
aluminum
g
500
950
steel
d


output:

id27
400


'''

'''
class Pan:
    def __init__(self, panId, material, brand, price, capacity):
        self.panId = panId
        self.material = material
        self.brand = brand
        self.price = price
        self.capacity = capacity

class Solution:
    @staticmethod
    def costliest_pan(pan_list, material):
        max_price = float('-inf')
        max_pan = None
        for pan in pan_list:
            if pan.material == material and pan.price > max_price:
                max_price = pan.price
                max_pan = pan
        return max_pan

    @staticmethod
    def discounted_price(pan_list, brand):
        for pan in pan_list:
            if pan.brand == brand:
                if pan.capacity > 1000:
                    pan.price *= 0.74  # 26% discount
                elif pan.capacity > 500:
                    pan.price *= 0.80  # 20% discount

# Main method
if __name__ == "__main__":
    pan_list = []
    for _ in range(7):
        panId = input("Enter Pan ID: ")
        material = input("Enter Material: ")
        brand = input("Enter Brand: ")
        price = int(input("Enter Price: "))
        capacity = int(input("Enter Capacity: "))
        pan = Pan(panId, material, brand, price, capacity)
        pan_list.append(pan)

    material = input("Enter Material to find costliest pan: ")
    costliest = Solution.costliest_pan(pan_list, material)
    if costliest is not None:
        print(costliest.panId)

    brand = input("Enter Brand to apply discount: ")
    Solution.discounted_price(pan_list, brand)
    for pan in pan_list:
        print(pan.price)
'''


class Pan:
    def __init__(self,pid,m,b,p,c):
        self.pid=pid
        self.m=m
        self.b=b
        self.p=p
        self.c=c
class Solution:
    @staticmethod
    def costliestPan(pList,m): 
        pans=[]
        for p in pList:
            if p.m.lower()==m.lower():
                pans.append(p)
        for pan in pans:
            max_cost=float('-inf')
            if pan.p>max_cost:
                max_cost=pan.p
        for pan in pans:
            if pan.p==max_cost:
                print(pan.pid)

    @staticmethod
    def discountedPrice(pList,b):
        for _ in pList:
            if _.b.lower()==b.lower():
                if _.c>1000:
                    _.p=0.74*_.p
                if _.c>500:
                    _.p=0.8*_.p
                print(int(_.p))
def main():
    pList=[]
    for i in range(7):
        pid=input()
        m=input()
        b=input()
        p=int(input())
        c=int(input())
        pan=Pan(pid,m,b,p,c)
        pList.append(pan)
    m=input()
    b=input()
    Solution.costliestPan(pList,m)
    Solution.discountedPrice(pList,b)

if __name__=="__main__":
    main()