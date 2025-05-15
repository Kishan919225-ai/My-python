# A programme to show student's result


# To take input 
def add_student():
    handle=open("stdr.txt","a")
    student_name=[]
    student_marks=[]
    num_std=int(input("Enter no, of students: "))
    sid=1
    while sid<=num_std:
        print(f"===============student ID:{sid}============================")
        name=input("Enter name of student: ")
        english=float(input("Enter marks in english: "))
        nepali=float(input("Enter marks nepali: "))
        science=float(input("Enter marks in science: "))
        math=float(input("Enter marks in math: "))
        computer=float(input("Enter marks in computer: "))
        total=english+nepali+science+math+computer
        student_name.append(name)
        student_marks.append(total)
        sid+=1


    student_id=1
    for total in student_marks:
        per=total/5
        grade=""
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
        handle.write(f"{student_id},{total},{per:.2f},{grade} \n")
        student_id+=1

def show_result():
    obj=open("stdr.txt","r")
    for data in obj.readlines():
        print(data)

# Main
print("\n Chose a option: ")
print("1.Add student")
print("2.show result")
choice=int(input("Enter your choice: "))

if choice==1:
    add_student()
elif choice==2:
    show_result()
else:
    print("Invalid choice")

