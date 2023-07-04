'''

Create a Class Inventory with below attributes:

inventoryId - String
maximumQuantity - int
currentQuantity - int
threshold - int

Write constructor as required.

Create class Solution with main method. 

Implement static method - replenish 
in Solution class.

This method will take an int parameter 
named limit along with the other 
parameter as array of Inventory objects. 
The method will return array of Inventory 
where the threshold attribute 
is less than or equal to the int parameter 
passed.

This method should be called from main 
method and display the id of 
returned objects along with Filling status.

if the threshold is greater than or equal 
to 75 then it should 
print "Critical Filling" as Filling Status. 
If the threshold is 
between 74 to 50 then Filling status 
should be "Moderate Filling", 
else should be "Non-Critical Filling" .

Before calling this method(replenish) in 
the main method, 
use Scanner object to read values for four 
Inventory objects 
referring the attributes in the 
above sequence. 
then, read the value for limit parameter. 
Next call the method replenish and 
display the result. 

Consider below sample input and output:

Input:

1
100
50
40
2
100
50
50
3
100
40
45
4
100
80
25
45

Output:
1 Non-Critical Filling
3 Non-Critical Filling
4 Non-Critical Filling


'''
"""class Inventory:
    def __init__(self, inventoryId, maximumQuantity, currentQuantity, threshold):
        self.inventoryId = inventoryId
        self.maximumQuantity = maximumQuantity
        self.currentQuantity = currentQuantity
        self.threshold = threshold

class Solution:
    @staticmethod
    def replenish(limit, inventoryList):
        replenishedInventory = []
        for inventory in inventoryList:
            if inventory.threshold <= limit:
                replenishedInventory.append(inventory)

        for inventory in replenishedInventory:
            if inventory.threshold >= 75:
                print(inventory.inventoryId, "Critical Filling")
            elif 50 <= inventory.threshold < 75:
                print(inventory.inventoryId, "Moderate Filling")
            else:
                print(inventory.inventoryId, "Non-Critical Filling")

# Main method
if __name__ == "__main__":
    inventoryList = []

    for _ in range(4):
        inventoryId = input()
        maximumQuantity = int(input())
        currentQuantity = int(input())
        threshold = int(input())
        inventory = Inventory(inventoryId, maximumQuantity, currentQuantity, threshold)
        inventoryList.append(inventory)

    limit = int(input())

    Solution.replenish(limit, inventoryList)
"""


class Inventory:
    def __init__(self,iid,mq,cq,t):
        self.iid=iid
        self.mq=mq
        self.cq=cq
        self.t=t
class Solution:
    @staticmethod
    def replenish(ilist,t):
        ans=[]
        for i in ilist:
            if i.t<=t:
                ans.append(i)
                if i.t>=75:
                    fs="Critical filling"
                elif 50<=i.t<=74:
                    fs="Moderate filling"
                else:
                    fs="Non-Critical Filling"
        if len(ans)>0:
            for a in ans:
                print(a.iid,fs)

# n=int(input())
ilist=[]
for i in range(4):
    iid=int(input())
    mq=int(input())
    cq=int(input())
    t=int(input())
    inv=Inventory(iid,mq,cq,t)
    ilist.append(inv)
t=int(input())
Solution.replenish(ilist,t)





