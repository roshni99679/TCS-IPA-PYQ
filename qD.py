'''
Create a class Vegetable with the below attributes:

name of type String name of the vegetable 
price of type float //price 
( in Rupees ) of the Fx: 
Kilogram quantity of type int ,/ quantity — number of units / Number of Kilograms

​Create the init method which takes all parameters in the above sequence.
 The method should set the value of attributes with the parameter values 
 received from main function.

Create another class Store with the below attribute: 
storeName of type String /specifies the vegList of type List L ist of Vegetable
 which takes all sequence. The method should set the value of attributes with
  the parameter values received from main.

​Create method inside the Store class with name categorizeVegetablesAlphabetically

This method use and traverse the list of Vegetables(vegList) and returns a
dictionary of alphabetically categorized and sorted vegetable names(name),
where in key represent an alphabet character(e.g. ‘a’, ‘b’, se etc) and value 
represents a tuple, containing vegetable names that starts with that specific 
character as per key. Both the keys and values are sorted in alphabetically.
respective tuple of vegetable names), then the list of vegitable names also 
needs to be sorted.
e.g. Ex on fruits, resultant dictionary data looks like 
: fas:(‘ananas’, ‘apple), ’13: (‘banana’), ‘p’:(‘pineapple)) 
Here ‘a’ ,’b’ and ‘p’ (excluding the single quote ) represents the 
keys of dictionary and (‘ananass, ‘apple), (‘banana’), (pineapple’) 
,excluding the ‘single quote and brackets’ represents the tuple for 
respective and corresponding keys(a , b, p ).

​For more details refer the sample test case input and respective output

Create another method inside Store class with the name
filterVegetablesForPriceRange This method takes minimum price 
and maximum price in Rupees as input parameters and return a list of 
alphabetically sorted vegetable names(name), where in the Vegetable unit 
price falls in the given range(minimum price and maximum price). This method 
use and traverse the list of Vegetables(vegList) for comparing the price of 
vegetable per Unit with the given range

If there is no vegetable in given price range, the method 
returns an empty list and based on the value main function should 
print “No Vegetable(s) in the given price range” (Excluding the double quotes) .

​For more details refer the sample test case input and respective output

You can use/refer the below given sample input and output to verify your 
solution using ‘ Custom Input ‘ option ,down the coding editor
Instructions to write main and to call the methods of the classes defined above:

a. You would required to write the main function completely, please follow
 the below instructions for the same.

b. You would required to write the main program which is inlign to the 
“sample input description section” mentioned below and to read the data 
in the same sequence.

c. Create the respective objects(Vegetable and Store) with the given sequence 
of arguments to fulfill the constructor requirement defined in the respective class.

    i.Create a Vegetable object after reading the data related to Vegetable and 
    add the Vegetable object to list of Vegetable objects, This point repeats for 
    the number of Vegetable objects you want to create and add to Vegetable list or 
    as mentioned in the first line of input in the input data

    ii. Create Store object by passing the Store name and list of Vegetable objects
    ( created and as mentioned in above point# c.i ) as the arguments to the constructor .

d. Call the methods ( categorizeVegetablesAlphabetically and
filterVegetablesForPriceRange) mentioned above from the main function in the 
same order , they appear in the question text. e. Display the data returned by 
the functions , in the main program as per the order of calling the functions
and as per the format mentioned in the sample output. f. If None/empty list
is returned.

y 1 terVegeta function then display “No Vegetable found for given prince range” 
(excluding the double quotes) in the main function.

Sample Input (below) description:

• The first input line represents the count of 
vegetable objects to create and add to the vegetable list.

• Second set of inputs lines(2nd to 4th ) represents 
vegetable name, vegetable price and quantity of first vegetable object and this set(Name,Price and Quantity for each different vegetable object ) of input is repeated for the number of vegetable objects mentioned in the first line of input .

• Next inputs represents store name(third line of input from last).

• Last two lines represents the minimum price and maximum
 price to be supplied to the filterVegetablesForPriceRange to find the vegitables, whose price falls in the range


Input:

5
corn
20.0
30
onion
10.0
15
potato
30.0
10
cucumber
5.0
10
brocolli
24.5
8
big bazaar
5.0
25.0

Output:

b
brocolli
c
corn
cucumber
o
onion
P
potato
5.0-25.0
brocolli
corn
cucumber
onion

'''

'''
class Vegetable:
    def init(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def init(self, storeName, vegList):
        self.storeName = storeName
        self.vegList = vegList
        def categorizeVegetablesAlphabetically(self):
            categorizedVegetables = {}
            for vegetable in self.vegList:
                firstLetter = vegetable.name[0].lower()
                if firstLetter not in categorizedVegetables:
                    categorizedVegetables[firstLetter] = []
                categorizedVegetables[firstLetter].append(vegetable.name)
            for key in categorizedVegetables:
                categorizedVegetables[key] = tuple(sorted(categorizedVegetables[key]))
            categorizedVegetables = dict(sorted(categorizedVegetables.items()))
            return categorizedVegetables

        def filterVegetablesForPriceRange(self, minPrice, maxPrice):
            filteredVegetables = []
            for vegetable in self.vegList:
                if minPrice <= vegetable.price <= maxPrice:
                    filteredVegetables.append(vegetable.name)
            return sorted(filteredVegetables)
# Create a list of vegetable objects
vegetableList = []
n = int(input())
for _ in range(n):
    # Read the vegetable details
    name = input()
    price = float(input())
    quantity = int(input())
    vegetable = Vegetable(name, price, quantity)
    vegetableList.append(vegetable)

# Read the store name
storeName = input()

# Create a store object
store = Store(storeName, vegetableList)

# Call the categorizeVegetablesAlphabetically method
categorizedVegetables = store.categorizeVegetablesAlphabetically()

# Print the categorized vegetables
for key, value in categorizedVegetables.items():
    print(key)
    for vegetable in value:
        print(vegetable)

# Read the minimum and maximum prices
minPrice = float(input())
maxPrice = float(input())

# Call the filterVegetablesForPriceRange method
filteredVegetables = store.filterVegetablesForPriceRange(minPrice, maxPrice)

# Print the filtered vegetables
if filteredVegetables:
    print(f"{minPrice}-{maxPrice}")
    for vegetable in filteredVegetables:
        print(vegetable)
else:
    print("No Vegetable(s) in the given price range")


'''

'''
class Vegetable:
    def __init__(self,vn,p,q):
        self.vn=vn
        self.p=p
        self.q=q

class Store:
    def __init__(self,sn,vList):
        self.sn=sn
        self.vList=vList
    def categorizeVegetablesAlphabetically(self):
        dic={}
        self.vList = sorted(self.vList,key=lambda x:x.vn)
        key="abcdefghijklmnopqrstuvwxyz"
        for k in key:
            val=[]
            for v in self.vList:
                if v.vn[0].lower()==k:
                    val.append(v.vn)
                
                if len(val)>0:
                    dic[k]=tuple(val)

        return dic

    def filterVegetablesForPriceRange(self,minval,maxval):
        ls=[]
        for v in self.vList:
            if minval<=v.p<=maxval:
                ls.append(v.vn)
        ls.sort()
        if ls==[]:
            print("No Vegetable(s) in the given price range")
        else:
            for l in ls:
                print(l)

def main():
    vList=[]
    n=int(input())
    for i in range(n):
        vn=input()
        p=float(input())
        q=int(input())
        veg=Vegetable(vn,p,q)
        vList.append(veg)

    sn=input()
    st=Store(sn,vList)
    minval=float(input())
    maxval=float(input())
    
    dic=st.categorizeVegetablesAlphabetically()
    if dic=={}:
        print("No vegetables..")
    else:
        for k,v in dic.items():
            print(k)
            for j in v:
                print(j)
    print(minval,"-",maxval)
    st.filterVegetablesForPriceRange(minval,maxval)

if __name__=="__main__":
    main()
'''

class Vegetable:
    def __init__(self,vn,p,q):
        self.vn=vn
        self.p=p
        self.q=q

class Store:
    def __init__(self,vlist):
        self.vlist=vlist
    def anydic(self):
        dic={}
        key="abcdefghijklmnopqrstuvwxyz"
        self.vlist=sorted(self.vlist,key=lambda x:x.vn)
        for k in key:
            ls=[]
            for v in self.vlist:
                if v.vn[0].lower()==k:
                    ls.append(v.vn)
                if len(ls)>0:
                    dic[k]=tuple(ls)
        for k,v in dic.items():
            print(k)
            for x in v:
                print(x)
    def ranger(self,l,h):
        for v in self.vlist:
            if l<=v.p<=h:
                print(v.vn)
n=int(input())
vlist=[]
for i in range(n):
    vn=input()
    p=float(input())
    q=int(input())
    veg=Vegetable(vn,p,q)
    vlist.append(veg)
s=input()
l=float(input())
h=float(input())
st=Store(vlist)
st.anydic()
st.ranger(l,h)

