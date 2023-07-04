''' 
Create a class Book with below attributes:

int - pages

int - price

String - author

int - id

String - title


Create the __init__ method which takes all 
parameters in the above sequence.
The method should set the value of attributes to 
parameter values inside the method.

 

Create a class BookStore with below attributes:

 

String - bookStoreName

List - BookList

 

Create the __init__ method which takes all parameters 
in the above sequence.
The method should set the value of attributes to 
parameter values inside the method.

 

Implement two  methods - 
findMinimumBookByid and 
sortBookByid in BookStore class.

 

findMinimumBookByid
Create a method findMinimumBookByid in the 
BookStore class. This method will return the
 Book having the minimum value for id of 
all the Books in the Book List of the BookStore 
 class. If there is no Book found in the 
Book List or list is empty then return None to main program.

 

sortBookByid
Create a method sortBookByid in the BookStore 
class. This method will return the sorted list 
of ids in ascending order of all the Books 
in the BookList of the BookStore class. If there is 
no Book found in the Book List, then return 
None to main program.

 

These methods should be called from the main method.

 

Instructions to write main section of the code:

a. You would require to write the main section 
completely, hence please follow the below 
instructions for the same.

b. You would require to write the main program 
which is inline to the sample input description 
section  mentioned below and to read the data in the same sequence.

c.  To create BookStore and Book objects , 
take the inputs in below sequence.

    To create a List of n Book objects read the value of n.

    To create a List of n Book objects read 
values for pages, price, author, id, title 
    (in this order) and create the Book object 
and add to the List. Repeat this step n times.

    Create the BookStore object passing the 
bookStoreName and the List of Books created 
    in previous step.

d. Call the method findMinimumBookByid 
using the BookStore object created in point  #c. 

e. Call the method sortBookByid using 
the BookStore object created in point #c.

f. Print the output of both methods as 
per given sample output.

g. If there is NONE returned from any 
method print-No Data Found.

 

Don't use any static text or formatting for 
printing the result. Just invoke the method
 and print the result.

Sequence for specific object will follow same 
attribute sequence as mentioned 
in the question. You may refer to the sample 
Input/output for the display format.

 

Sample Input:

5
47
247
MJ Demarco
19
The Millionaire Fastlane
61
877
James Clear
81
Atomic Habits
90
31
David Goggins
45
Can't Hurt Me
24
620
Yuval Noah Harari
8
Sapiens
54
163
Stephen Pressfield
97
The War of Art

 
Sample Output:

24
620
Yuval Noah Harari
8
Sapiens
8
19
45
81
97


 '''
''' 
class Book:
    def __init__(self, pages, price, author, id, title):
        self.pages = pages
        self.price = price
        self.author = author
        self.id = id
        self.title = title

class BookStore:
    def __init__(self, bookStoreName, bookList):
        self.bookStoreName = bookStoreName
        self.bookList = bookList

    def findMinimumBookByid(self):
        if len(self.bookList) == 0:
            return None
        minBook = min(self.bookList, key=lambda book: book.id)
        return minBook

    def sortBookByid(self):
        if len(self.bookList) == 0:
            return None
        sortedIds = sorted(book.id for book in self.bookList)
        return sortedIds

# Main method
if __name__ == "__main__":
    n = int(input())
    bookList = []

    for _ in range(n):
        pages = int(input())
        price = int(input())
        author = input()
        id = int(input())
        title = input()
        book = Book(pages, price, author, id, title)
        bookList.append(book)

    bookStoreName = input()
    bookstore = BookStore(bookStoreName, bookList)

    minBook = bookstore.findMinimumBookByid()
    if minBook is not None:
        print(minBook.id)
        print(minBook.pages)
        print(minBook.price)
        print(minBook.author)
        print(minBook.title)
    else:
        print("No Data Found")

    sortedIds = bookstore.sortBookByid()
    if sortedIds is not None:
        for id in sortedIds:
            print(id)
    else:
        print("No Data Found")'''



class Book:
    def __init__(self,pg,p,a,id,t):
        self.pg=pg
        self.p=p
        self.a=a
        self.id=id
        self.t=t
class BookStore:
    def __init__(self,st,blist):
        self.st=st
        self.blist=blist
    def fmbid(self):
        ans=[]
        for b in self.blist:
            ans.append(b)
        ans.sort(key=lambda x:x.id)
        if len(ans)>0:
            for a in ans:
                print(a.pg)
                print(a.p)
                print(a.a)
                print(a.id)
                print(a.t)
                return
        else:
            print("No book")

    def smbid(self):
        ans=[b for b in self.blist]
        ans=sorted(ans,key=lambda x:x.id)
        if len(ans)>0:
            for a in ans:
                print(a.id)
        else:
            print("No books")
n=int(input())
blist=[]
for i in range(n):
    pg=int(input())
    p=int(input())
    a=input()
    id=int(input())
    t=input()
    bookobj=Book(pg,p,a,id,t)
    blist.append(bookobj)
st=input()
stobj=BookStore(st,blist)
print("Output---------------")
stobj.fmbid()
stobj.smbid()