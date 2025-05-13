# # A programe that makes result 

# # To take input 
# def marks():
#     student_name=[]
#     student_marks=[]
#     num_student=int(input('Enter number of student: '))
#     total = 0 
#     for sid in range(1,num_student+1):
#         print(f"========================Students ID:{sid}=================================")
#         name = input("Enter name of student: ")
#         nepali = float(input("Enter marks in Nepali: "))
#         English  = float(input("Enter marks in English: "))
#         Math = float(input("Enter marks in Math: "))
#         Computer = float(input("Enter marks in Computer: "))
#         Science = float(input("Enter marks in Science: "))
#         total=nepali+English+Math+Computer+Science
#         student_marks.append(total)
#         student_name.append(name)
#     return student_name,student_marks

# # To calculate per 
# def per(student_marks):
#     percentage=[]
#     for mark in student_marks:
#         percentage.append(mark/5)
#     return percentage

# # To calculate grade 
# def grade(percentage):
#     grade=""
#     for per in percentage:
#         if per>=90:
#             grade="A+"
#         elif per>=80:
#             grade = "A"
#         elif per>=70:
#             grade = "B+"
#         elif per>=60:
#             grade = "B"
#         elif per>=50:
#             grade = "C+"
#         elif per>=40:
#             grade = "C"
#         else:
#             grade="F"
#     return grade

# # print result
# def result(student_name,student_marks,percentage,grade):
#     print("-----------------------------Result--------------------------------------------")
#     print("SID \t Name \t Total \t Percent\tGrade")
#     for i in range(len(student_name)):
#         print(f"{i+1} \t {student_name[i]} \t {student_marks[i]} \t {percentage[i]} \t {grade}")
# #main
# student_name , student_marks = marks()
# percentage = per(student_marks)
# grades = grade(percentage)
# result(student_name, student_marks, percentage, grades)


# def rep():
#     num=int(input("Enter number:"))
#     return [num,num,num,num,num]


# print(rep())


def products():
    return[
        {'pid':1,'name':'dell','price':50000,'qty':10},
        {'pid':2,'name':'mac','price':90000,'qty':8},
        {'pid':3,'name':'mi','price':20000,'qty':60},
        {'pid':4,'name':'sony','price':15000,'qty':30},

        ]
# To search product
def search():
    global products
    products=products()
    num_items = int(input("Enter types of product: "))
    for pid in range(1,num_items+1):
        name = input("Enter name of product: ")
        namel=[]
        for product in products:
            if name == product["name"]:
                print(f"Name:{product["name"]},Price:{product["price"]},Stock:{product["qty"]}")
                namel.append(name)
    return namel

def total():
    choice = input("Do you want to buy product(Yes/No): ")
    global products
    for product in products:
        if choice=="Yes":
            quantity=int(input("Enter quantity: "))
            if product["qty"]>=quantity:
                total=product["price"]*quantity
                print(total)
            else:
                print("Stock not available.")

def add_product():
    pass

def update_product():
    pass

def delete_product():
    pass

def display():
    pass

search()
total()