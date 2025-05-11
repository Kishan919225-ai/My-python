# A programe that makes result 

# To take input 
def marks():
    student_name=[]
    student_marks=[]
    num_student=int(input('Enter number of student: '))
    total = 0 
    for sid in range(1,num_student+1):
        print(f"========================Students ID:{sid}=================================")
        name = input("Enter name of student: ")
        nepali = float(input("Enter marks in Nepali: "))
        English  = float(input("Enter marks in English: "))
        Math = float(input("Enter marks in Math: "))
        Computer = float(input("Enter marks in Computer: "))
        Science = float(input("Enter marks in Science: "))
        total=nepali+English+Math+Computer+Science
        student_marks.append(total)
        student_name.append(name)
    return student_name,student_marks

# To calculate per 
def per(student_marks):
    percentage=[]
    for mark in student_marks:
        percentage.append(mark/5)
    return percentage

# To calculate grade 
def grade(percentage):
    grade=""
    for per in percentage:
        if per>=90:
            grade="A+"
        elif per>=80:
            grade = "A"
        elif per>=70:
            grade = "B+"
        elif per>=60:
            grade = "B"
        elif per>=50:
            grade = "C+"
        elif per>=40:
            grade = "C"
        else:
            grade="F"
    return grade

# print result
def result(student_name,student_marks,percentage,grade):
    print("-----------------------------Result--------------------------------------------")
    print("SID \t Name \t Total \t Percent\tGrade")
    for i in range(len(student_name)):
        print(f"{i+1} \t {student_name[i]} \t {student_marks[i]} \t {percentage[i]} \t {grade}")
#main
student_name , student_marks = marks()
percentage = per(student_marks)
grades = grade(percentage)
result(student_name, student_marks, percentage, grades)


