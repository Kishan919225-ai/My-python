# To add task
todo_list=[]
def add_task():
    task=input("Enter a task: ")
    todo_list.append(task)
    print("Task added")

# TO view task
def view():
    if not todo_list:
        print("Empty list")
    else:
        print("\n------------To do list-------------------")
        for i,task in enumerate(todo_list,start=1):
            print(f"{i}.{task}")

def delete_task():
    view()
    if todo_list:
        try:
            num_task=int(input("Enter the number of task: "))
            if 1<=num_task<=len(todo_list):
                removed=todo_list.pop(num_task-1)
                print(f"Removed:{removed}")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter valid number")

add_task()
view()
delete_task()
