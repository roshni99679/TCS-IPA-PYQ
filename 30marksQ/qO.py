'''

Create a class Scholar with attributes:
ScholarId Number (representing a unique id for each student)
ScholarName - String (represents the name of the student)
State String (representing the state of the student)
Marks List (storing the marks of 3 subjects, obtained marks from each subject is out of 100)
Define the_init_ method which takes parameters in the above sequence and sets the
values for attributes.
Create another class Scholar Result with following attribute and methods
ScholarGrade list of dictionaries (It will contain the record for each student which will have Scholar Id, ScholarName, Total Marks, Grade and State)
Define the init_ method which sets the values for above mentioned attribute.
Define the methods in the ScholarResult class as below
1. First method will take the list of Scholar objects and Grade as an input parameters. Firstly, you need to calculate the percentage for each student (based on the marks obtained in 3 subjects).
To calculate the percentage use the following formula:
Percentage (Subject1Marks + Subject2Marks + Subject3Marks) / 3)
Note: Percentage must be an integer value and rounds the value. That means, if
Percentage >=40.0% or <40>=40.5% or <=41.0% then it will be considered as a 41%.
After calculating the percentage, you need to assign the grades as per the following given conditions:
If student's percentage >=80, then If student's percentage >= 60 and If student's percentage >= 50 and
assign Grade "A"
80 then assign Grade "B" 60 then assign Grade "C"
If student's percentage <50 then assign Grade "D"
After calculating the grades, make a dictionary which contains ScholarId, ScholarName, Total Marks, Grade and state and append it to the Scholar Grade (list of dictionaries) which is an attribute of ScholarResult_class.
Secondly, your method will return the list of dictionaries according to the Grade passed as parameter. This list of dictionaries will be sorted based on their Total Marks in descending order.
For Example:
[{'ScholarId: 106, 'ScholarName': 'palak', 'Total Marks': 282, Grade: 'A', 'State': 'gujarat'}, {'ScholarId: 104, 'ScholarName': 'ramesh', 'TotalMarks': 275, 'Grade': 'A', 'state': 'rajasthan'},
{'ScholarId: 102, 'ScholarName': 'ram', 'TotalMarks': 285, 'Grade': 'A', 'state': 'rajasthan'}]
If student's percentage >=80, then assign Grade "A"
If student's percentage >= 60 and < 80>= 50 and < 60 xss=removed xss=removed>=40.0% or <40>=40.5% or <=41.0% then it will be considered as a 41%.
For ExampleYour returning list must follow the format as per the below sample example: [['delhi', '60:40'], ['gujarat', '100:0'], ['rajasthan', '70:30']]
Instructions to write main section of the code:
1. You would require to write the main section completely, hence please follow the below instructions for the same.
2. You would be required to write the main program which is inline to the "sample input description section" mentioned below and to read the data in the same sequence.
3. Create the respective objects (Scholar and ScholarResult) with the given sequence

Sample Input1:
5
101
Tanmay
delhi
90
88
93
102
Sunil
delhi
90
95
90
103
Karvi
maharashtra
70
45
50
154
monika
tamilnadu
20
35
40
105
Ram
tamilnadu
90
65
50
a
Sample Output1:
102 sunil 275 A delhi
101 tanmay 271 A delhi
delhi 100:0
maharashtra 100:0
tamilnadu 50:50

'''



'''class Scholar:
    def __init__(self, scholar_id, scholar_name, state, marks):
        self.scholar_id = scholar_id
        self.scholar_name = scholar_name
        self.state = state
        self.marks = marks


class ScholarResult:
    def __init__(self):
        self.scholar_grade = []

    def calculate_percentage(self, scholar):
        percentage = sum(scholar.marks) / len(scholar.marks)
        percentage = round(percentage)
        return percentage

    def assign_grade(self, percentage):
        if percentage >= 80:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        else:
            return 'D'

    def calculate_result(self, scholars, grade):
        result = []
        for scholar in scholars:
            percentage = self.calculate_percentage(scholar)
            scholar_grade = self.assign_grade(percentage)
            if scholar_grade == grade:
                result.append({
                    'ScholarId': scholar.scholar_id,
                    'ScholarName': scholar.scholar_name,
                    'Total Marks': sum(scholar.marks),
                    'Grade': scholar_grade,
                    'State': scholar.state
                })
        result.sort(key=lambda x: x['Total Marks'], reverse=True)
        return result


# Main method
if __name__ == "__main__":
    n = int(input("Enter the number of scholars: "))
    scholars = []
    for _ in range(n):
        scholar_id = int(input("Enter ScholarId: "))
        scholar_name = input("Enter ScholarName: ")
        state = input("Enter State: ")
        marks = []
        for i in range(3):
            marks.append(int(input(f"Enter marks for Subject {i+1}: ")))
        scholar = Scholar(scholar_id, scholar_name, state, marks)
        scholars.append(scholar)

    grade = input("Enter the Grade: ")

    result = ScholarResult()
    scholar_grade_list = result.calculate_result(scholars, grade)

    for scholar_grade in scholar_grade_list:
        print(scholar_grade)
'''




class Scholar:
    def __init__(self,sid,sn,st,mlst):
        self.sid=sid
        self.sn=sn
        self.st=st
        self.mlst=mlst
class Sresult:
    def __init__(self):
        self.LofD=[]
    def fn1(self,slist,inp_grade):
        dic={}
        tm=[]
        percentage=[]
        for s in slist:

            tmo=sum(s.mlst)
            per=sum(s.mlst)/len(s.mlst)
            tm.append(tmo)
            percentage.append(per)
            glst=[]

            for p in percentage:
                if p>=80:
                    glst.append('A')
                elif p>=60 and p<80:
                    glst.append('B')
                elif p>=50 and p<60:
                    glst.append('C')
                else:
                    glst.append('D')


            k=0
            dic["sid"]=s.sid
            dic["sn"]=s.sn
            dic["tm"]=tm[k]
            dic["G"]=glst[k]
            dic["st"]=s.st
            k+=1
            
            if dic["G"]==inp_grade.upper():
                self.LofD.append(dic)

        return self.LofD
            
        
n=int(input())
slist=[]
for i in range(n):
    sid=int(input())
    sn=input()
    st=input()
    mlst=[]
    for i in range(3):
        m=int(input())
        mlst.append(m)
    sobj=Scholar(sid,sn,st,mlst)
    slist.append(sobj)
inp_grade=input()
obj=Sresult()
ls=obj.fn1(slist,inp_grade)
print(ls)
    

