# class animal:
#     def getRoar(self):
#         print('abstract roar')

# class Cat(animal):
#     def getRoar(self):
#         print('Meaw')

# class Bear(animal):
#     def getRoar(self):
#         print('RRR')

# class Fish(animal):
#     def getRoar(self):
#         super().getRoar()

# kat = Cat()
# Medved = Bear()
# Nemo = Fish()

# Medved.getRoar()
 
# animals = [kat, Medved, Nemo]

# for a in animals:
#      a.getRoar()




# class book:
#     def getsoderj(self):
#         print('abstract')

# class history(book):
#     def getsoderj(self):
#         print('Book of history')

# class philosophy(book):
#     def getsoderj(self):
#         print('Book of philosophy')

# class philology(book):
#     def getsoderj(self):
#         print('Book of hilology')

# class fantasy(book):
#     def getsoderj(self):
#         print('Book of fantasy')

# WarAndMir = history()
# Stoicism = philosophy()
# Homer = philology()
# Marvel = fantasy()

# book = [WarAndMir, Stoicism, Homer, Marvel]

# for a in book:
#      a.getsoderj()


# class coffe_machine:
#     def active(self):
#         print('Coffemachine is cool!')
    
#     def __private(self):
#         print('Working...')


# CO = coffe_machine()
# CO.active()

# from unittest.mock import seal




# class human:
#      rost = 0
#      ves = 0
#      hair = ''
#      nogi = 0
#      def __init__(self, rost, ves, hair):
#          self.rost = rost
#          self.ves = ves
#          self.hair = hair
#          self.nogi = 2


#      def setNogi(self, noga):
#         if noga > 2:
#             print('Error')
#         else:
#             self.nogi = noga
#         def get(self):
#          def get_nogi():

# H = human()
# H.set(180, 60, 'black')
# H.setNogi(3)


import requests
import tkinter as tk
from tkinter import ttk

def load_json_data():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        show_json_data(json_data)
    else:
        result_label.config(text="Ошибка при загрузке данных: {}".format(response.status_code))

def show_json_data(json_data):
    for key, value in json_data.items():
        tree.insert("", "end", values=(key, value))

# Создание главного окна
root = tk.Tk()
root.title("")

# Создание таблицы
tree = ttk.Treeview(root, columns=("Key", "Value"), show="headings")
tree.heading("Key", text="Key")
tree.heading("Value", text="Value")
tree.pack(fill="both", expand=True)

# Создание кнопки для загрузки данных
load_button = tk.Button(root, text="Загрузить JSON", command=load_json_data)
load_button.pack(pady=10)

# Создание метки для вывода результатов
result_label = tk.Label(root, text="")
result_label.pack()

# Запуск главного цикла обработки событий
root.mainloop()