import tkinter as tki
import pandas as pd
import numpy as np

def Start_window(root):
    def delete_elemets():
        for object_name in mass:
            if object_name.winfo_viewable():
                object_name.grid_remove()
            else:
                object_name.grid()
        Select_db(root)
    lbl1 = tki.Label(root, text="Добро пожаловать в говно епта!!!", font=('Times', 20, 'italic'))
    lbl1.grid(column=1, row=0, pady = 10, padx = 25)
    btn = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'),bg='blue',fg='red',command=delete_elemets)
    btn.grid(column=1, row=1)
    mass = [lbl1,btn]

"""Надо вставить command во все кнопки"""
def Main_window(root):
    btn1 = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn1.grid(column=1, row=0)
    btn2 = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn2.grid(column=1, row=1)
    btn3 = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn3.grid(column=1, row=2)



def Select_db(root):
    def get_db():
            pf = pd.read_csv(path_1.get())
            print(pf)
    lbl1 = tki.Label(root, text="Введите путь к базе студентов", font=('Times', 20, 'italic'))
    lbl1.grid(column=1, row=0, pady = 10, padx = 25)
    path_1 = tki.Entry()
    path_1.grid(column=1, row=1, pady = 10, padx = 25)
    btn1 = tki.Button(root, text='Нажмите чтобы внести', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command = get_db)
    btn1.grid(column=1, row=2)

    lbl2 = tki.Label(root, text="Введите путь к базе предметов", font=('Times', 20, 'italic'))
    lbl2.grid(column=1, row=3, pady = 10, padx = 25)
    path_2 = tki.Entry()
    path_2.grid(column=1, row=4, pady = 10, padx = 25)
    btn2 = tki.Button(root, text='Нажмите чтобы внести', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn2.grid(column=1, row=5)

    lbl3 = tki.Label(root, text="Введите путь к базе стипендий", font=('Times', 20, 'italic'))
    lbl3.grid(column=1, row=6, pady = 10, padx = 25)
    path_3 = tki.Entry()
    path_3.grid(column=1, row=7, pady = 10, padx = 25)
    btn3 = tki.Button(root, text='Нажмите чтобы внести', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn3.grid(column=1, row=8)
