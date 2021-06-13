import tkinter as tki
import pandas as pd
import numpy as np
import os.path
import sys
sys.path.append(r'../')
import Library as lib

global mpf
global fpf
global spf

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
    def delete_elemets():
        for object_name in mass:
            object_name.grid_remove()

    def to_graf():
        delete_elemets()
        Select_graf(root)

    def to_select():
        delete_elemets()
        Select_db(root)

    def to_editing():
        delete_elemets()
        select_editing_db(root)


    btn1 = tki.Button(root, text='Внести базу данных', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command=to_select)
    btn1.grid(column=2, row=0)
    btn2 = tki.Button(root, text='Редактирование базы', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command=to_editing)
    btn2.grid(column=2, row=1)
    btn3 = tki.Button(root, text='Справочник', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn3.grid(column=2, row=2)
    btn4 = tki.Button(root, text='Отчеты', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command=to_graf)
    btn4.grid(column=2, row=3)
    mass = [btn1,btn2,btn3,btn4]


def select_editing_db(root):

    def delete_elemets():
        for object_name in mass:
            object_name.grid_remove()

    def deleting_db():
        pass

    def add_db():
        lbl1 = tki.Label(root, text="Введите данные нового студента", font=('Times', 20, 'italic'))
        lbl1.grid(column = 1, row=)
        mass = [lbl1]

    btn1 = tki.Button(root, text='Удаление из базы', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command=to_select)
    btn1.grid(column=1, row=0)
    btn2 = tki.Button(root, text='Добавление изменение', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command=to_editing)
    btn2.grid(column=2, row=0)
    mass = []



"""Сделать ссылки на функции """
def Select_graf(root):
    btn1 = tki.Button(root, text='Отчет 1')
    btn1.grid(column=1, row=0)
    btn2 = tki.Button(root, text='Отчет 2')
    btn2.grid(column=2, row=1)
    btn3 = tki.Button(root, text='Отчет 3')
    btn3.grid(column=3, row=2)
    btn4 = tki.Button(root, text='Отчет 4')
    btn4.grid(column=4, row=3)
    btn5 = tki.Button(root, text='Отчет 5')
    btn5.grid(column=5, row=4)
    btn6 = tki.Button(root, text='Отчет 6')
    btn6.grid(column=6, row=5)

"""Надо добавить проверку существования
добавить флаг для перехода на новое окно"""
def Select_db(root):
    def delete_elemets():
        for object_name in mass:
            object_name.grid_remove()

    def get_db_main():
        mpf = pd.read_csv(path_1.get())

    def get_db_fs():
        fpf = pd.read_csv(path_2.get())

    def get_db_sh():
        spf = pd.read_csv(path_3.get())

    def com_db():
        mpf = lib.db.base_main()
        fpf = lib.db.base_fs()
        spf = lib.db.base_sh()
        delete_elemets()
        Main_window(root)

    def next_to_main():
        delete_elemets()
        #Сюда вставить проверку наличия всех баз
        Main_window(root)

    lbl1 = tki.Label(root, text="Введите путь к базе студентов", font=('Times', 20, 'italic'))
    lbl1.grid(column=1, row=0, pady = 10, padx = 25)
    path_1 = tki.Entry()
    path_1.grid(column=1, row=1, pady = 10, padx = 25)
    btn1 = tki.Button(root, text='Нажмите чтобы внести', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command = get_db_main)
    btn1.grid(column=1, row=2)

    lbl2 = tki.Label(root, text="Введите путь к базе предметов", font=('Times', 20, 'italic'))
    lbl2.grid(column=1, row=3, pady = 10, padx = 25)
    path_2 = tki.Entry()
    path_2.grid(column=1, row=4, pady = 10, padx = 25)
    btn2 = tki.Button(root, text='Нажмите чтобы внести', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command = get_db_fs)
    btn2.grid(column=1, row=5)

    lbl3 = tki.Label(root, text="Введите путь к базе стипендий", font=('Times', 20, 'italic'))
    lbl3.grid(column=1, row=6, pady = 10, padx = 25)
    path_3 = tki.Entry()
    path_3.grid(column=1, row=7, pady = 10, padx = 25)
    btn3 = tki.Button(root, text='Нажмите чтобы внести', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command = get_db_sh)
    btn3.grid(column=1, row=8)

    common_db = tki.Button(root, text='Ипользовать готовую БД', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command = com_db)
    common_db.grid(column=2, row=2)

    btn4 = tki.Button(root, text='Далее', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command = next_to_main)
    btn4.grid(column=2, row=3)

    mass = [lbl1,path_1,btn1,lbl2,path_2,btn2,lbl3,path_3,btn3,btn4,common_db]
