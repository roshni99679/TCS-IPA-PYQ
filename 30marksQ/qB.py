'''
Create a class Laptop with the below attributes:

laptopId - int
brand - String
osType - String
price - double
rating - int

The above attributes should be private, write getters, setters and parameterized constructor as required.

Create class Solution with main method.

Implement two static methods - countOfLaptopsByBrand and searchLaptopByOsType in Solution class.

countOfLaptopsByBrand method:
This method will take two input parameters - array of Laptop objects and a String parameter.
The method will return the count of laptops from array of Laptop object for the given brand(String parameter passed) whose rating is more than 3.
If no Laptop with the above condition is present in the array of Laptop objects, then the method should return 0.

searchLaptopByOsType method:
This method will take two input parameters - array of Laptop objects and a String parameter.
The method will return Laptop object array in an descending order of their laptopId, from the array of Laptop objects whose os attribute matches with the given OS(String parameter passed).
If no Laptop with the given OS is present in the array of Laptop objects, then the method should return null.

Note : No two Laptop object would have the same laptopId.
All the searches should be case insensitive.

The above mentioned static methods should be called from the main method.

For countOfLaptopsByBrand method - The main method should print the count of laptops as it is, if the returned value is greater than 0, or it
should print "The given brand is not available".

For searchLaptopByOsType method - The main method should print the laptopId and rating from the returned Laptop object array if the returned value is not null.
If the returned value is null then it should print "The given os is not available".

Before calling these static methods in main, use Scanner object to read the values of Four Laptop objects referring attributes in the above mentioned attribute sequence. 
Next, read two String values for capturing brand and os.


Consider below sample input and output:
TestCase1:
Input:
123
HP
Windows
35000
5
124
Apple
Mac OS
70000
5
125
Dell
Ubuntu
30000
4
126
HP
windows
40000
4
HP
windows

Output:
2
126
4
123
5


TestCase2:
Input:
123
HP
Windows
35000
5
124
Apple
Mac OS
70000
5
125
Dell
Ubuntu
30000
4
126
Asus
windows
40000
3
HP1
Ubuntu1

Output:
The given brand is not available
The given os is not available

'''


'''
class Laptop:
    def __init__(self, laptopId, brand, osType, price, rating):
        self.__laptopId = laptopId
        self.__brand = brand
        self.__osType = osType
        self.__price = price
        self.__rating = rating

    def getLaptopId(self):
        return self.__laptopId

    def getBrand(self):
        return self.__brand

    def getOsType(self):
        return self.__osType

    def getPrice(self):
        return self.__price

    def getRating(self):
        return self.__rating


class Solution:
    @staticmethod
    def countOfLaptopsByBrand(laptops, brand):
        count = 0
        for laptop in laptops:
            if laptop.getBrand().lower() == brand.lower() and laptop.getRating() > 3:
                count += 1
        return count

    @staticmethod
    def searchLaptopByOsType(laptops, osType):
        matching_laptops = []
        for laptop in laptops:
            if laptop.getOsType().lower() == osType.lower():
                matching_laptops.append(laptop)
        if len(matching_laptops) > 0:
            matching_laptops.sort(key=lambda x: x.getLaptopId(), reverse=True)
            return matching_laptops
        else:
            return None


def main():
    laptops = []
    for _ in range(4):
        laptopId = int(input())
        brand = input()
        osType = input()
        price = float(input())
        rating = int(input())

        laptop = Laptop(laptopId, brand, osType, price, rating)
        laptops.append(laptop)

    brand = input()
    osType = input()
    count = Solution.countOfLaptopsByBrand(laptops, brand)
    if count > 0:
        print(count)
    else:
        print("The given brand is not available")

    
    search_results = Solution.searchLaptopByOsType(laptops, osType)
    if search_results is not None:
        for laptop in search_results:
            print(laptop.getLaptopId())
            print(laptop.getRating())
    else:
        print("The given os is not available")


if __name__ == "__main__":
    main()
'''


class Laptop:
    def __init__(self,laptopId,brand,osType,price,rating):
        self.laptopId=laptopId
        self.brand=brand
        self.osType=osType
        self.price=price
        self.rating=rating

class Solution:
    @staticmethod
    def countOfLaptopsByBrand(lap_list,brand):
        count=0
        for lap in lap_list:
            if lap.brand.lower()==brand.lower() and lap.rating>3:
                count+=1
        if count==0:
            print("The given brand is not available")
        else:
            print(count)
            

    @staticmethod
    def searchLaptopByOsType(lap_list,osType):
        ls=[]
        for lap in lap_list:
            if lap.osType.lower()==osType:
                ls.append(lap)
        ls.sort(key=lambda x: x.laptopId,reverse=True)
        if ls==[]:
            print("The given os is not available")    
        else :
            for l in ls:
                print(l.laptopId)
                print(l.rating)
            
        
def main():
    lap_list=[]
    for i in range(4):
        laptopId=int(input())
        brand=input()
        osType=input()
        price=float(input())
        rating=int(input())
        lap=Laptop(laptopId,brand,osType,price,rating)
        lap_list.append(lap)

    brand=input()
    osType=input()
    Solution.countOfLaptopsByBrand(lap_list,brand) 
    Solution.searchLaptopByOsType(lap_list,osType)

if __name__=="__main__":
    main()












'''
sort()
sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original sequence. Moreover, sort() is a method of list class and can only be used with lists. 

Syntax: List_name.sort(key, reverse=False)
Parameters: 
key: A function that serves as a key for the sort comparison. 
reverse: If true, the list is sorted in descending order.
Return type: None 


# Python program to demonstrate
# sort()
 
 
# List of Integers
numbers = [1, 3, 4, 2]
 
# Sorting list of Integers
numbers.sort()
 
print(numbers)
 
# List of Floating point numbers
decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68]
 
# Sorting list of Floating point numbers
decimalnumber.sort()
 
print(decimalnumber)
 
# List of strings
words = ["Geeks", "For", "Geeks"]
 
# Sorting list of strings
words.sort()
 
print(words)
Output
[1, 2, 3, 4]
[1.68, 2.0, 2.01, 3.28, 3.67]
['For', 'Geeks', 'Geeks']

# function to return the second element of the
# two elements passed as the parameter
 
 
def sortSecond(val):
    return val[1]
 
 
# list1 to demonstrate the use of sorting
# using  second key
list1 = [(1, 2), (3, 3), (1, 1)]
 
# sorts the array in ascending according to
# second element
list1.sort(key=sortSecond)
print(list1)
 
# sorts the array in descending according to
# second element
list1.sort(key=sortSecond, reverse=True)
print(list1)

-----------------------------------------------------------------------

sorted()
sorted() method sorts the given sequence as well as set and dictionary(which is not a sequence) either in ascending order or in descending order(does unicode comparison for string char by char) and always returns the a sorted list. This method doesn’t effect the original sequence.
Syntax: sorted(iterable, key, reverse=False)affect
Parameters: 
Iterable: sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted. 
Key(optional): A function that would serve as a key or a basis of sort comparison. 
Reverse(optional): If set True, then the iterable would be sorted in reverse (descending) order, by default it is set as False.
Return Type: Returns a sorted list. 

# List
x = ['q', 'w', 'r', 'e', 't', 'y']
print(sorted(x))
 
# Tuple
x = ('q', 'w', 'e', 'r', 't', 'y')
print(sorted(x))
 
# String-sorted based on ASCII translations
x = "python"
print(sorted(x))
 
# Dictionary
x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
print(sorted(x))
 
# Set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))
Output
['e', 'q', 'r', 't', 'w', 'y']
['e', 'q', 'r', 't', 'w', 'y']
['h', 'n', 'o', 'p', 't', 'y']
['e', 'q', 'r', 't', 'w', 'y']
['e', 'q', 'r', 't', 'w', 'y']

python program to demonstrate
# sorted()
 
 
L = ['aaaa', 'bbb', 'cc', 'd']
 
# sorted without key parameter
print(sorted(L))
print()
 
# sorted with key parameter
print(sorted(L, key=len))
Output
['aaaa', 'bbb', 'cc', 'd']

['d', 'cc', 'bbb', 'aaaa']
'''