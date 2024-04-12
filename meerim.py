# class drob:
#     chist = 0
#     znam = 0
#     def _init_(self, chist, znam):
    
#     self.chist = chist
#     self.znam = znam
#     def multiple(self, d):
#         print(self.chist * d.chist)
#         print(self.znam * d.znam)

# Drob1 = drob(6, 7)
# Drob2 = drob(9, 2)
# Drob1.multiple(Drob2)

# class animal:
#     def getRoar(self):
#         print('abstract roar')

# class Cat(animal):
#     def getRoar(self):
#         print('Meaw')

# class Bear(animal):
#     def getRoar(self):
#         print('RRR')

# kat = Cat()
# kat.getRoar()
# Medved = Bear()
# Medved.getRoar()
 
#  animals = [kat, Medved, Nemo]

#  for a in animals:
#     a.getRoar()



# class s:
#     def __init_(self, a, b):
#         self.a = a
#         self.b = b 

# S = s(4, 7)
# print(S.a)







# from time import time
# from turtle import color

# class Games:
#     def __init__(self, name):
#         self.name = name
#     def getName(self):
#       print (self.name)


# class PCGames(Games):
#     def __init__(self, name, time):
#         self.name = name
#         self.time = time


# class PS4Games(Games):
#     def __init__(self, name, data):
#         self.name = name
#         self.data = data
        
        
# class XboxGames(Games):
#     def __init__(self, name, xbox):
#         self.name = name
#         self.xbox = xbox
    
 
# class MobileGames(Games):
#     def __init__(self, name, mobile):
#         self.name = name
#         self.mobile = mobile
        

# pCGames = PCGames("Shoro", 80)
# pS4Games= PS4Games("UY", 2012)
# xboxGames = XboxGames("Meerim", 45)
# mobileGames = MobileGames("Shag", 67)

# games = [pCGames, pS4Games, xboxGames, mobileGames]

# for a in games:
#     a.getName()







# from math import sqrt
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def rast(self):
#         return sqrt(self.x**2 + self.y**2)
#     def getPoint(self):
#         return [self.x, self.y]

# class PointColor(Point):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y




# class Pet:
#     def getRoar(self):
#         print('abstract roar')

# class dog (Pet):
#     def getRoar(self):
#         print('gav')

# class cat(Pet):
#     def getRoar(self):
#         print('meow')

# class parrot(Pet):
#     def getRoar(self):
#         print('rrr')

# class hamster(Pet):
#     def getRoar(self):
#         print('RRR')


# Dog = dog()
# Kat = cat()
# Popugay = parrot()
# Hamster= hamster()

 
# Pet = [Dog, Kat, Popugay, Hamster]

# for a in Pet:
#     a.getRoar()




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

# from PIL import Image
# from multiprocessing import Pipe, Pool
# import multiprocessing 
# from multiprocessing import Process
# import time

# from matplotlib import pyplot as plt 


# def g(x):
#     print(multiprocessing.current_process().name)
#     print(x * x)

# def f(x):
#     print(x)

# def r(conn):
#     conn.send('Hello!')

# if __name__ == "__main__":
    # with Pool (multiprocessing.cpu_count()) as P:
    #         P.map(g, [2, 3, 5])

    # p = Process(target=f, args=(5,))
    # p.start()
    # p.join()
    # father_con, child_con = Pipe()
    # p = Process(target=r, args=(child_con, ))
    # p.start()
    # print(father_con.recv())

#     ima = Image.open("2.jpg")
# for i in range(3):
#     time.sleep(1)
#     plt.imshow(ima)
#     plt.show()

#     father_con, child_con = Pipe()
#     p = Process(target=r, args=(child_con, ))
#     p.start()
#     print(father_con.recv())



# import asyncio

# async def foo():
#     print("Hello ot foo")
#     await asyncio.sleep(3)
#     print("Bye ot foo!")

# async def yoo():
#     print("Hello ot yoo")
#     await foo()
#     print("Bye ot yoo!")

# asyncio.run(yoo())



# import asyncio

# async def Kant():
#     print("Кант думает...")
#     await asyncio.sleep(4)
#     print("Начал кушать")

# async def Platon():
#     print("Платон думает...")
#     await asyncio.sleep(1) 
#     print("Начал кушать")

# async def Aristotel():
#     print("Аристотель думает...")
#     await asyncio.gather(Kant(), Platon())
#     print("Начал кушать")

# asyncio.run(Aristotel())



# import asyncio

# async def func():
#     print("Кант думает...")
#     await asyncio.sleep(4)
#     print("Начал кушать")

# async def Platon():
#     print("Платон думает...")
#     await asyncio.sleep(1) 
#     print("Начал кушать")

# async def Aristotel():
#     print("Аристотель думает...")
#     await asyncio.gather(Kant(), Platon())
#     print("Начал кушать")

# asyncio.run(Aristotel())


# import random
# r = random.randint(0, 100)
# myfile = open("hello.txt", "w")
# myfile.write(str(r))
# myfile.close()


# import asyncio
# from random import randint
# import time

# async def fail():
#     global i 
#     await asyncio.sleep(2)
#     my_file = open(f"file{i}.txt", "w+")
#     i += 1 
#     if i < 3:
#         await fail()
#         r = randint(0, 100)
#         my_file.write(str(r))
#         my_file.close()
# i = 0
# for i in range(3):
#     print(asyncio.run(fail()))








# def summa(a):
#     t = 0
#     try:
#         t = 5 / a 
#     except:
#         print("???")
#         return 4 
#     else:
#         return t + 2

# print(summa(2))


# class KletkaMnogoException(Exception):
    # def __init__(self, *args):
#         self.message = args[0] if args else ""
#     def __str__(self):
#         return f"Are you crazy? {self.message}"

# class shahmat:
#     def setKletki(self, a):
#         if a > 8:
#             raise KletkaMnogoException("Kletok mnogo")
#         else:
#             pass 

# s = shahmat()
# s.setKletki(9)




# a = input()
# b = input()
# try:
#     print(int(a) + int(b))
# except:
#     print(a + b)



# a = input()
# b = input()
# c = input()
# try:
#     print(int(a) + int(b) + int(c))
# except:
#     print(a + b + c)




# class DlinnoeImyaException(Exception):
#     def __init__(self, *args):
#         self.message = args[0] if args else ""
#     def __str__(self):
#         return f" oshibka {self.message}"

# class name:
#     def setName(self, a):
#         if len(a) > 4:
#             raise DlinnoeImyaException("Имя длиннее 4 символов")
#         else:
#             pass 

# s = name()
# s.setName("garry") 




# class DlinnoeImyaException(Exception):
#     def __init__(self, *args):
#         self.message = args[0] if args else ""
#     def __str__(self):
#         return f" oshibka {self.message}"

# class name:
#     def setName(self, a):
#         if len(a) > 4:
#             raise DlinnoeImyaException("Имя длиннее 4 символов")
#         else:
#             pass 

# s = name()
# s.setName("garry") 




# class VkladException(Exception):
#     def __init__(self, *args):
#         self.message = args[0] if args else ""
#     def __str__(self):
#         return f" oshibka {self.message}"

# class name:
#     def setName(self, a):
#         if a > 10000:
#             raise VkladException("Превышает лимит")
#         else:
#             pass 

# s = name()
# s.setName(100000) 




# class RomanException(Exception):
#     def __init__(self, *args):
#         self.message = args[0] if args else ""
#     def __str__(self):
#         return f" oshibka {self.message}"

# class name:
#     def setName(self, a):
#         if len (a) > 10000:
#             raise RomanException("")
#         else:
#             pass 

# s = name()
# s.setName(100000) 


# a = int(input())
# b = int(input())
# print(a + b)
 



# import numbers
# from tokenize import Name


# class Phone:
#      number = 0
#      model = ""
#      weight = 0
   
#      def __init__(self, number, model, weight):
#          self.number = number
#          self.model = model 
#          self.weight = weight
#          self.name = 2


#      def setNumber(self, name):
#         if name > 2:
#             print('receivelCall')
#         else:
#             self.name = name

#      def receive_call(self, p):
#         print(f"{self.number} звонит {p.number}")

# P = Phone("4364675", "BQ", 67)
# P.setNumber(3)

# M = Phone("546546567", "M", 90)
# P.receive_call(M)




# from tkinter import *
# v = ''
# def knopochka():
#     v = value.get()
#     # print(v)
#     L3['text'] = v


# okoshko = Tk()
# value = StringVar()
# okoshko.resizable(width=False, height=False)
# okoshko.title('Bishkek')
# okoshko.geometry('400x500+700+300')

# L = Label(text='Isanova')
# L2 = Label(text='Chui')
# L3 = Label(text='Ahunbaeva')
# # L.pack(side='top')
# # L2.pack()
# # L3.pack()

# B = Button(text = 'Knopka', command=knopochka)

# e = Entry(textvariable=value)

# L.grid(row = 1, column = 1)
# L2.grid(row = 2, column = 2)
# L3.grid(row = 3, column = 3)
# B.grid(row = 1, column= 2)
# e.grid(row = 2, column= 3)

# okoshko.mainloop()






# from tkinter import *


# class captha:
#     def __init__(self, title, w, h):

#         self.okno = Tk()
#         self.okno.resizable(width=False, height=False)
#         self.okno.title(title)
#         self.okno.geometry(f"{w}x{h}+600+200")
#         self.valuev = StringVar()
#         self.e = Entry(textvariable=self.valuev)
#         self.l = Label() 
#         self.b = Button(text="Knopka", command=self.get)


#     def get(self):
#         v = self.valuev.get()
#         self.name = v

#     def call(self):
#         self.e.pack()
#         self.l.pack()
#         self.b.pack()
    

#         self.okno.mainloop()
        

# C = captha("Proverka", 200, 300)
# C.call()
# C.get()
# print(C.name)






from tkinter import * 

class calculator:
    def __init__(self):
        self.a = -1
        self.b = -1

    def setA(self, a):
        if self.a == -1:
            self.a = a
        else:
            self.setB(a)

    def setB(self, b):
        self.b = b

Calc = calculator()

def click():
    nil = Label(text=1)
    Calc.setA(1)
    print(Calc.a, Calc.b)


def plus():
    print(Calc.a + Calc.b)


oko = Tk()
oko.resizable(width=False, height=False)
oko.title("Calculatyr")
oko.geometry("350x500+600+200")



nil = Label(text=0)

a1 = Button(text = "1", command=click)
a2 = Button(text = "2", command=click)
a3 = Button(text = "3", command=click)
a4 = Button(text = "4", command=click)
a5 = Button(text = "5", command=click)
a6 = Button(text = "6", command=click)
a7 = Button(text = "7", command=click)
a8 = Button(text = "8", command=click)
a9 = Button(text = "9", command=click)
b1 = Button(text = "+", command=click)
b2 = Button(text = "-", command=click)
b3 = Button(text = "*", command=click)
b4 = Button(text = "/", command=click)
c1 = Button(text = "Считай", command=plus)
nil.grid(row=1, column=5)
a1.grid(row=2, column=1)    
a2.grid(row=2, column=2)
a3.grid(row=2, column=3)
a4.grid(row=3, column=1)
a5.grid(row=3, column=2)
a6.grid(row=3, column=3)
a7.grid(row=4, column=1)
a8.grid(row=4, column=2)
a9.grid(row=4, column=3)
b1.grid(row=5, column=1)
b2.grid(row=5, column=2)
b3.grid(row=5, column=3)
b4.grid(row=5, column=4)
c1.grid(row=5, column=6)

oko.mainloop()


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