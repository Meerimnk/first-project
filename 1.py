# from concurrent.futures import thread
# import threading

# lock = threading.Lock()
# total = 0

# def f(amount):
#     global total 
#     with lock:
#         total += amount

# for i in range(10):
#     MyThread = threading.Thread(target=f, args=(i,))
#     MyThread.start()

# print(total)



# import threading
# import time

# from meerim import MyThread 

# locker = threading.Lock()

# def filosov(name):
#     with locker:
#         print(name + ' eating')
#         time.sleep(3)
#         print(name + ' filosofia')
#         time.sleep(3)
#         print(name + ' exit')
#         time.sleep(3)

# filosovs = ["Kant", "Platon", "Hegel", "Aristotel", "Konfucii"]
# for i in range(5):
#     MyThread = threading.Thread(target=filosov, args=(filosovs[i],))
#     MyThread.start()




# import threading
# import time

# locker = threading.Lock()


# def chislo(a, b):
#     with locker: 
#         time.sleep(1)
#         print(a + b)
# Chislo1 = [1, 3, 5, 9, 2]
# Chislo2 = [9, 1, 7, 8, 4]

# for i in range(10):
#     MyThread = threading.Thread(target=chislo, args=(Chislo1[i], Chislo2[i],))
#     MyThread.start() 



# from PIL import Image
# from multiprocessing import Pipe, Pool
# import multiprocessing 
# from multiprocessing import Process


#         filename = "2.jpg"
#         with Image.open(filename) as img:
#             img.load()

#kfdhg

from tkinter import *

def on_button_click():
    label.config(text="Привет, " + entry.get())

# Создание основного окна
root = Tk()
root.title("Пример интерфейса")

# Создание виджетов
label = Label(root, text="Введите ваше имя:")
entry = Entry(root)
button = Button(root, text="Привет", command=on_button_click)

# Размещение виджетов на окне
label.pack()
entry.pack()
button.pack()

# Запуск основного цикла обработки событий
root.mainloop()