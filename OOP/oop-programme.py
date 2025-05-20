# class calculator:

#     def add(x,y):
#         print(x+y)

#     def subtract(x,y):
#         print(x-y)

#     def multilply(x,y):
#         print(x*y)

#     def divide(x,y):
#         print(x/y)

# result = calculator
# result.add(8,9)
# result.subtract(8,9)
# result.multilply(8,9)
# result.divide(8,9)


class collage:

    def __init__(self):
        self.students=['ram','gita','sita']

    def show(self):
        print(f"Students list: {self.students}")

    def add_student(self,name):
        self.students.append(name)

    def update(self,index,name):
        oldname = self.students[index]
        self.students[index] = name
        print(f"{oldname} updated to{name}")

    def delete(self,index):
        index=int(input("Enter index:"))
        self.students.remove(index)

Collage=collage()
print(dir(Collage))
print("\n OPTIONS")
print("1.Show list")
print("2.Add student")
print("3.update list")
print("4.remove")

choice=int(input("Enter a choiice(1/2/3/4):"))

if choice==1:
    Collage.show()
elif choice==2:
    name=input("Enter name:")
    Collage.add_student(name)
    print(f"{name} added to students")
elif choice==3:
    index=int(input("Enter index to update:"))
    name=input("Enter new name:")
    Collage.update(name,index)


# class College:
#     def __init__(self):
#         self.students = ['ram', 'gita', 'sita']

#     def show(self):
#         print("Student list:", self.students)

#     def add_student(self, name):
#         self.students.append(name)
#         print(f"{name} added successfully!")

#     def update(self, index, name):
#         if 0 <= index < len(self.students):
#             old_name = self.students[index]
#             self.students[index] = name
#             print(f"{old_name} updated to {name}")
#         else:
#             print("Invalid index")

#     def delete(self, index):
#         if 0 <= index < len(self.students):
#             removed = self.students.pop(index)
#             print(f"{removed} removed from list")
#         else:
#             print("Invalid index")


# college = College()

# while True:
#     print("\nOPTIONS")
#     print("1. Show list")
#     print("2. Add student")
#     print("3. Update student")
#     print("4. Remove student")
#     print("5. Exit")

#     choice = int(input("Enter your choice (1-5): "))

#     if choice == 1:
#         college.show()
#     elif choice == 2:
#         name = input("Enter name to add: ")
#         college.add_student(name)
#     elif choice == 3:
#         index = int(input("Enter index to update: "))
#         name = input("Enter new name: ")
#         college.update(index, name)
#     elif choice == 4:
#         index = int(input("Enter index to remove: "))
#         college.delete(index)
#     elif choice == 5:
#         print("Exiting program.")
#         break
#     else:
#         print("Invalid choice. Please enter 1-5.")



