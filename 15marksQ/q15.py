'''
calculate iq of each student using formula (iq=health_number/age)*100

input:
3
1
rosh
181
24
2
khush
236
34
3
deep
160
20

output:
1 rosh 754.16
2 khush 694.11
3 deep 800.00
'''


'''def calculate_iq(health_number, age):
    return (health_number / age) * 100

# Input the number of students
num_students = int(input("Enter the number of students: "))

# Initialize a dictionary to store the student information
students = {}

# Input student information
for i in range(1, num_students + 1):
    print(f"Student {i}:")
    student_id = int(input("Enter student ID: "))
    student_name = input("Enter student name: ")
    health_number = float(input("Enter health number: "))
    age = int(input("Enter age: "))
    students[student_id] = {'name': student_name, 'health_number': health_number, 'age': age}

# Calculate IQ for each student and print the output
for student_id, student_info in students.items():
    iq = calculate_iq(student_info['health_number'], student_info['age'])
    print(f"{student_id} {student_info['name']} {iq:.2f}")'''



n=int(input())
dic={}
for i in range(n):
    id=int(input())
    name=input()
    health_no=int(input())
    age=int(input())
    dic[id]={"name":name,"health_no":health_no,"age":age}
def calc(h,a):
    ans=round((h/a)*100,3)
    ans=str(ans)
    n=len(ans)
    ans=ans[:n-1]
    return float(ans)
for k,v in dic.items():
    iq=calc(v['health_no'],v['age'])
    print(k,v['name'],iq)


