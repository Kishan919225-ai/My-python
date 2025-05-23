# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk()
# root.geometry("300x250")
# root.resizable(False,False)
# root.title("Weight conveter")


# def convert():
#     try:
#         weight=float(entry.get())
#         if unit_var=="kg to lb":
#             result=weight*0.4536
#             result_label.config(text=f"{result:.2f}kg")
#         else:
#             result=weight*2.20
#             result_label.config(text=f"{result:.2f}lb")

#     except Exception as e:
#         messagebox.showwarning("Please enter valid number")


# unit_var=tk.StringVar(value="Options") 
# dropdown=tk.OptionMenu(root,unit_var,"Kg to lb","lb to Kg")
# dropdown.pack(pady=10)
# entry=tk.Entry()
# entry.pack(pady=10)

# btn=tk.Button(root,text="Convert",font=("Arial",15),command=convert)
# btn.pack(pady=10)

# result_label=tk.Label(root,text="RESULT",width=20)
# result_label.pack(pady=10)

# root.mainloop()