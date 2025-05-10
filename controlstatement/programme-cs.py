# age  = int(input(" Enter your age: "))
# if age >= 18:
#     print("Yes,eligible")
# else:
#     print("not,eligible")

# number = 10
# if number%2==0:
#     print("even")
# else:
#     print("odd")
         

# a=5
# b=6
# c=10
# if a>c and a>c:
#     print("a is greater")
# elif b>c and b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# a=2
# b=4
# c=5
# d=10
# if a>b and a>c and a>d:
#     print("a")
# elif b>a and b>c and b>d:
#     print("b")
# elif c>a and c>b and c>d:
#     print("c")
# else:
#     print("d")

# alphabet = input("Enter your alphabet: ")
# vowel = ("a,e,i,o,u")
# if alphabet==vowel:
#    print("vowel")
# else:
#    print("consonant")

# A=maths = int(input("Enter ypur marks: "))
# B=english = int(input("Enter your marks: "))
# C=nepali = int(input("Enter your marks: "))
# D=science = int(input("Enter your marks: "))
# E=social = int(input("Enter your number: "))
# total = A+B+C+D+E
# per = total/5
# print("your total marks is: ",total)
# print("Your percent is: ",per)
# if per<=40:
#     print("Your grade is:D")
# elif per<=60:
#     print("Your grade is:C")
# elif per<=80: 
#     print("Your grade is:B")
##     print("Your grade is:A")


# name = input("Enter your name: ")
# if name=='admin':
#     age=input("Enter your age: ")
#     print(name)
#     print(age)
# else:
#     print("Enter your name: ")

# print("==========WELCOME TO ATM============")
# PIN = int(input("Enter your PIN: "))
# BALANCE = int(10000)
# if PIN==1234:
#     task = {
#        1:("Check Balance: "),
#        2:("Withdraw Money: "),
#     }
#     choice = int(input("Enter your task: "))
#     if choice==1:
#         print(f"Your balance is {BALANCE}")
#     else:
#         amount = int(input('Enter your amount:'))
#         if amount<=10000:
#             print("TASK COMPLETED")
#         else:
#             print("Insufficient Balance")
# else:
#     print("Invalid PIN")

# username = input("Enter your username: ")
# password = input("Enter your password: ")
# if username=='admin':
#     if password=='admin002':
#        age = int(input('Enter your age: '))
#        if age<=25:
#            print("You can only drink soft drinks")
#        elif age<=40:
#            print("You can  drink soft drinks and wine")
#        else:
#            print("You can drink all soft drink,wine and alcohol")
#     else:
#         print("Invalid password")
# else:
#     print('Ínvalid username')

a =first_number = int(input("Enter your first_number: "))
b=second_number = int(input('Enter your second_number: '))
c=third_number = int(input('Enter your third_number: '))
if a>b and b>c:
    list = [a,b,c]
    print(list)
elif b>a and a>c:
    list=[b,a,c]
    print(list)
elif b>c and c>a:
    list =[b,c,a]
    print(list)
elif a>c and c>b:
    list = [a,c,b]
    print(list)
else:
    list =[c,b,a]
    print(list)
