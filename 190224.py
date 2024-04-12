# from tkinter import *

# v = ''
# def knopa():
#     v = value.get()
    


# calculator = Tk() 
# calculator.title('Калькулятор')
# value = IntVar()
# calculator.resizable(width=False, height=False)
# calculator.title('Калькулятор')
# calculator.geometry('250x250')

# number = Label(text='Label')

# B1 =  Button(text='1')
# B2 = Button(text='2')
# B3 = Button(text='3')
# B4 = Button(text='4')
# B5 = Button(text='5')
# B6 = Button(text='6')
# B7 = Button(text='7')
# B8 = Button(text='8')
# B9 = Button(text='9')
# B10 = Button(text='+')
# B11 = Button(text='-')
# B12 = Button(text='*')
# B13 = Button(text='/')

# B = Button(text ='')


# number = Entry(textvariable=value)

# B1.grid(row = 2, column= 1)
# B2.grid(row = 2, column= 2)
# B3.grid(row = 2, column= 3)

# B4.grid(row = 3, column= 1)
# B5.grid(row = 3, column= 2)
# B6.grid(row = 3, column= 3)

# B7.grid(row = 4, column= 1)
# B8.grid(row = 4, column= 2)
# B9.grid(row = 4, column= 3)

# B10.grid(row = 5, column= 1)
# B11.grid(row = 5, column= 2)
# B12.grid(row = 5, column= 3)
# B13.grid(row = 5, column= 4)


# number.grid(row = 1, column= 5)

# calculator.mainloop()



# import tkinter as tk

# def on_button_click():
#     label.config(text="Привет, " + entry.get())

# # Создание основного окна
# root = tk.Tk()
# root.title("Пример интерфейса")

# # Создание виджетов
# label = tk.Label(root, text="Введите ваше имя:")
# entry = tk.Entry(root)
# button = tk.Button(root, text="Привет", command=on_button_click)

# # Размещение виджетов на окне
# label.pack()
# entry.pack()
# button.pack()

# # Запуск основного цикла обработки событий
# root.mainloop()












# import tkinter as tk
# from tkinter import messagebox

# def add_task():
#     task = entry.get()
#     if task:
#         listbox.insert(tk.END, task)
#         entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("Внимание", "Пожалуйста, введите задачу!")

# def delete_task():
#     try:
#         selected_task_index = listbox.curselection()[0]
#         listbox.delete(selected_task_index)
#     except IndexError:
#         messagebox.showwarning("Внимание", "Выберите задачу для удаления!")

# # Создаем основное окно
# root = tk.Tk()
# root.title("To-Do List")

# # Создаем и настраиваем элементы интерфейса
# frame = tk.Frame(root)
# frame.pack(pady=10)

# listbox = tk.Listbox(frame, selectbackground="lightblue")
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)

# entry = tk.Entry(root, font=("Italic", 18))
# entry.pack(pady=10)

# add_button = tk.Button(root, text="Добавить задачу", command=add_task)
# add_button.pack(pady=5)

# delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
# delete_button.pack(pady=5)

# # Запускаем главный цикл
# root.mainloop()





# import tkinter as tk
# from tkinter import messagebox

# def add_task():
#     task = entry.get()
#     if task:
#         listbox.insert(tk.END, task)
#         entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning("Внимание", "Пожалуйста, введите задачу!")

# def delete_task():
#     try:
#         selected_task_index = listbox.curselection()[0]
#         listbox.delete(selected_task_index)
#     except IndexError:
#         messagebox.showwarning("Внимание", "Выберите задачу для удаления!")

# # Создаем основное окно
# root = tk.Tk()
# root.title("To-Do List")

# # Создаем и настраиваем элементы интерфейса
# frame = tk.Frame(root)
# frame.pack(pady=10)

# listbox = tk.Listbox(frame, selectbackground="lightblue", width=30)
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# scrollbar = tk.Scrollbar(frame)
# scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# listbox.config(yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)

# entry = tk.Entry(root, font=("Helvetica", 14))
# entry.pack(pady=10)

# add_button = tk.Button(root, text="Добавить задачу", command=add_task)
# add_button.pack(pady=5)

# delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
# delete_button.pack(pady=5)

# # Запускаем главный цикл
# root.mainloop()



# from distutils import command
# from logging import root
# from tkinter import *


# class table:
#     def init(self, n, r, c):
#         self.n = n
#         self.r = r
#         self.c = c

# T = table("" , 1, 1)

# def addColumn():
#     T.c += 1
#     for i in range(T.r): 
#         for j in range(T.c): 
#             Entry(okoshko2).grid(row=i, column=j) 
 
# def addName(n):
#     Label(okoshko2, text=n).pack()
    

# def addRow():
#     T.r += 1
#     for i in range(T.r): 
#         for j in range(T.c): 
#             Entry(okoshko2).grid(row=i, column=j) 


# okoshko = Tk()
# okoshko.resizable(width=False, height=False)
# okoshko.title("To Do List")  
# okoshko.geometry("500x500+900+200")

# okoshko2 = Toplevel(okoshko)
# okoshko2.resizable(width=False, height=False)
# okoshko2.title("To Do List")        
# okoshko2.geometry("500x500+380+200")

# oko1 = Entry(okoshko)
# oko2 = Label(okoshko)

# e = Entry()
# b1 = Button(text="__название__", command= lambda: addName("Txt"))                             
# b2 = Button(text="добавить столбец", command=addColumn)
# b3 = Button(text="удалить столбец ")
# b4 = Button(text="добавить строку ", command=addRow)

# e.grid(row = 1, column=2)
# b1.grid(  row=2, column=2)
# b2.grid(  row=3, column=2)
# b3.grid(  row=4, column=2)
# b4.grid(  row=5, column=2)



# okoshko2.mainloop()
# okoshko.mainloop()



