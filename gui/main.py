# # import tkinter as tk

# # root = tk.Tk()
# # # TO display label
# # message=tk.Label(root,text="Hello World!")
# # message.pack()

# # root.mainloop()


# import tkinter as tk
# from tkinter import messagebox

# def greet():
#     name=entry.get()
#     messagebox.showinfo("Greeting",f"Hello {name}!")

# window=tk.Tk()
# window.title("GUI")
# window.geometry("350x150")

# label=tk.Label(window,text="Enter your name: ")
# label.pack(pady=5)

# entry=tk.Entry()
# entry.pack(pady=5)

# button=tk.Button(window,text="Greet",command=greet)
# button.pack(pady=15)

# window.mainloop()

# import tkinter as tk

# window=tk.Tk()
# window.geometry("300x250")
# window.resizable(False,False)
# window.title("Demo")

# def hello():
#     name=entry.get()
#     print(f"Namaste {name}!")

# label=tk.Label(window,text="Enter your name: ")
# label.pack(pady=5)


# entry=tk.Entry()
# entry.pack(pady=5)
# btn=tk.Button(window,text="Greet",command=hello)
# btn.pack()

# window.mainloop()

# import tkinter as tk

# window=tk.Tk()
# window.title("Calculator")
# window.geometry("300x200")
# window.resizable(True,True)

# def calculate():
#     num1=float(entry1.get())
#     num2=float(entry2.get())
#     print(num1+num2)

# label1=tk.Label(window,text="Enter number")
# label1.pack()
# entry1=tk.Entry(window)
# entry1.pack(pady=5)

# label2=tk.Label(window,text="Enter number")
# label2.pack(pady=5)
# entry2=tk.Entry(window)
# entry2.pack(pady=5)

# btn=tk.Button(window,text="Calculate",command=calculate)
# btn.pack(pady=5)

# result_label=tk.Label(window,text="Result:")
# result_label.pack(pady=5)

# window.mainloop()

# import tkinter as tk

# window=tk.Tk()
# window.geometry("300x200")
# window.resizable(False,False)
# window.title("Calculator")

# btn1=tk.Button(window,text="9",command=)
# btn1.grid(row=0,column=0)


# import tkinter as tk

# root = tk.Tk()
# root.title="Empty calculatlor"


# display=tk.Entry(root,width=30)
# display.grid(row=0,column=0,columnspan=4,padx=5,pady=5)

# for i in range(4):
#     for j in  range(4):
#         btn=tk.Button(root,text="",width=5,height=2)
#         btn.grid(row=i+1,column=j,padx=5,pady=5)

# root.mainloop()

# import tkinter as tk

# root=tk.Tk()
# root.geometry("350x400")
# root.resizable(True,True)
# root.title("Calculator")

# expression=""
# entry_text=tk.StringVar()

# entry=tk.Entry(root,textvariable=entry_text,font=("Arial",24),width=18,justify="right")
# entry.grid(row=0,column=0,columnspan=5,padx=15,pady=30)


# def button_click(char):
#     global expression
#     expression+=str(char)
#     entry_text.set(expression)

# def clear():
#     global expression
#     expression=""
#     entry_text.set("")

# def delete():
#     global expression
#     expression=expression[:-1]

# def calculate():
#     global expression
#     try:
#         result=str(eval(expression))
#         entry_text.set(result)
#         expression=result
#     except Exception as e :
#         entry_text.set("Error")
#         expression=""

# buttons=[
#     ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
#     ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
#     ("3",3,0),("2",3,1),("1",3,2),("+",3,3),
#     (".",4,0),("0",4,1),("-",4,2),("=",4,3),
# ]

# for (text,row,col) in buttons:
#     if text== "=":
#         action=calculate
#     else:
#         action=lambda x=text:button_click(x)
#     tk.Button(root,text=text,font=("Arial",20),command=action).grid(row=row,column=col,padx=0,pady=0,sticky="nsew")

# tk.Button(root,text="C",font=("Arial",20),command=clear).grid(row=5,column=1,padx=0,pady=0,sticky="nsew")
# tk.Button(root,text="DEL",font=("Arial",20),command=delete).grid(row=5,column=2,padx=0,pady=0,sticky="nsew")

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk


# def return_pressed(event):
#     print('Return key pressed.')


# root = tk.Tk()

# btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed)


# btn.focus()
# btn.pack(expand=True)

# root.mainloop()