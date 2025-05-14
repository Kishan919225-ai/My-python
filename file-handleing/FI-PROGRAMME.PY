# A programme to show student's result


# To take input 
def input_detail():
    handle=open("data.txt",)
    student_name=[]
    student_marks=[]
    total_marks=[]
    percent=[]
    num_std=int(input("Enter no, of students: "))
    sid=1
    while sid<=num_std:
        name=input("Enter name of student: ")
        english=float(input("Enter marks in english: "))
        nepali=float(input("Enter marks nepali: "))
        science=float(input("Enter marks in science: "))
        math=float(input("Enter marks in math: "))
        computer=float(input("Enter marks in computer: "))
        total=english+nepali+science+math+computer
        per=total/5
        percent.append(per)
        total_marks.append(total)
        student_name.append(name)
        student_marks.append(total)
        if per>=90:
            grade="A+"
        elif per>=80:
            grade="A"
        elif per>=70:
            grade="B+"
        elif per>=60:
            grade="B"
        elif per>=50:
            grade="C+"
        elif per>=40:
            grade="C"
        else:
            grade="F"
            grades.append(grade)
        sid+=1
    return grades


student_marks,student_name,student_percent=input_detail()
grades=grade_cal()

def add_student():
     obj=open("")

def show_result():
    obj=("data.txt","r")
    obj.write()
    obj.write
    obj.write
    obj.write
    obj.write





print("\n Chose a option: ")
print("1.Add student")
print("2.show result")
choice=int(input("Enter your choice: "))

if choice==1:
     input_detail()

else:
     