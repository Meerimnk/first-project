# from tkinter import * 
 
# class table: 
#     def __init__(self, n, r, c): 
#         self.n = n 
#         self.r = r 
#         self.c = c 
#         self.labels = [] 
#         self.p = [] 
# T = table("" , 1, 0) 
 
# def addName(n): 
#     T.c += 1 
#     T.labels.append(n) 
 
#     for i in range(len(T.p)): 
#         T.p[i].grid_remove() 
#     T.p = [] 
 
#     for i in range(T.r + 1): 
#         for j in range(T.c): 
#             if i == 0: 
#                 Label(okoshko2, text=T.labels[j]).grid(row=i, column=j) 
#             else: 
#                 e = Entry(okoshko2) 
#                 e.grid(row=i, column=j) 
#                 T.p.append(e) 
#     n["text"] = v 
 
 
# def addRow(): 
#     if T.r == 1: 
#         T.r += 2 
#     else: 
#         T.r += 1 
#     for i in range(len(T.p)): 
#         T.p[i].grid_remove() 
#     T.p = [] 
 
#     for i in range(T.r): 
#         for j in range(T.c): 
#             if i == 0: 
#                 Label(okoshko2, text=T.labels[j]).grid(row=i, column=j) 
#             else: 
#                 e = Entry(okoshko2) 
#                 e.grid(row=i, column=j) 
#                 T.p.append(e) 
 
# def reneme(): 
#     for i in range(len(T.p)): 
#         T.p[i].grid_remove() 
 
#     T.r -= 1 
#     for i in range(T.r): 
#         for j in range(T.c): 
#             if i == 0: 
#                 Label(okoshko2, text=T.labels[j]).grid(row=i, column=j) 
#             else: 
#                 e = Entry(okoshko2) 
#                 e.grid(row=i, column=j) 
#                 T.p.append(e) 
                                                                                                                 
# okoshko = Tk() 
# okoshko.resizable(width=False, height=False) 
# okoshko.title("To Do List")   
# okoshko.geometry("500x500+900+200") 
 
# okoshko2 = Toplevel(okoshko) 
# okoshko2.resizable(width=False, height=False) 
# okoshko2.title("To Do List") 
# okoshko2.geometry("500x500+380+200") 
 
# v = StringVar() 
# f = Entry(textvariable=v) 
# b1 = Button(text="Название", command= lambda: addName(v.get())) 
# b3 = Button(text="удалить строку ", command=reneme) 
# b4 = Button(text="добавить строку ", command=addRow) 
 
# f.grid(row = 1, column=2) 
# b1.grid(row=2, column=2) 
# b3.grid(row=4, column=2) 
# b4.grid(row=5, column=2) 
 
# okoshko2.mainloop() 
# okoshko.mainloop()



from ast import Param
from asyncore import write
import re
from urllib import response
import requests
import pprint
import tkinter as tk
from tkinter import ttk
# response1 = requests.get('https://api.github.com/')
# # response2 = requests.get('https://api.github.com/')
# print('')
# json_responces = response1.json()
# print(json_responces)
# pprint.pprint(json_responces)
# pprint.pprint(json_responces['user_search_url'])

# # print(response1.content)


# params = {"q": "python"}
# response = requests.get('https://api.github.com/search/repositories', params= params)

# print(pprint.pprint(response.json()))

# print('')


# img_url = 'https://img.freepik.com/free-photo/bright-petals-gift-love-in-a-bouquet-generated-by-ai_188544-13370.jpg?w=1380&t=st=1710511990~exp=1710512590~hmac=83762fd562c2a09307616704319cd07a5eeea6d82d8ebcd39447c88934e9175b'
# response = requests.get(img_url)

# with open('image.png', 'wb') as file:
#     file.write(response.content)





# response = requests.get('https://api.github.com/')
# response2 = response.json()
# # pprint.pprint(response2)

# print(len(response2))


# def load_json_data():
#     url = 'https://api.github.com/'
#     response = requests.get(url)
#     if response.status_code == 200:
#         json_data = response.json()
#         show_json_data(json_data)
#     else:
#         result_label.config(text="Ошибка при загрузке данных: {}".format(response.status_code))

# def show_json_data(json_data):
#     for key, value in json_data.items():
#         tree.insert("", "end", values=(key, value))

# # Создание главного окна
# root = tk.Tk()
# root.title("")

# # Создание таблицы
# tree = ttk.Treeview(root, columns=("Key", "Value"), show="headings")
# tree.heading("Key", text="Key")
# tree.heading("Value", text="Value")
# tree.pack(fill="both", expand=True)

# # Создание кнопки для загрузки данных
# load_button = tk.Button(root, text="JSON", command=load_json_data)
# load_button.pack(pady=10)

# # Создание метки для вывода результатов
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Запуск главного цикла обработки событий
# root.mainloop()


import pandas as pd 
import requests
from docx import Document 
# import json 

df = pd.read_excel(r'Meerim.xlsx', sheet_name='list')
print(df)

doc = Document('Meerim4.docx')
pars = doc.paragraphs

for i in pars:
    print(i.text)
