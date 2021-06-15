import tkinter as tki
import pandas as pd
import numpy as np
import os.path
import sys
sys.path.append(r'../')
import Library as lib

mpf = 0
fpf = 0
spf = 0
max_id_stud = -1
max_id_fs = -1
max_id_sh = -1
mass = []
mass_all = []





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
    root.geometry("1300x550")
    global mpf
    global fpf
    global spf
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
    btn1.grid(column=0, row=0)
    btn2 = tki.Button(root, text='Редактирование базы', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command=to_editing)
    btn2.grid(column=0, row=1)
    btn3 = tki.Button(root, text='Справочник', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn3.grid(column=0, row=2)
    btn4 = tki.Button(root, text='Отчеты', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2, command=to_graf)
    btn4.grid(column=0, row=3)

    columns = ("#1", "#2", "#3", "#4", "#5")
    tree = tki.ttk.Treeview(root,show="headings", columns=columns)
    tree.heading("#1", text="ID")
    tree.heading("#2", text="ФИО")
    tree.heading("#3", text="Год обучения")
    tree.heading("#4", text="Любимый предмет")
    tree.heading("#5", text="Стипендия")
    tree.grid(column=1, row=0)
    ysb = tki.ttk.Scrollbar(root, orient=tki.VERTICAL, command=tree.yview)
    tree.configure(yscroll=ysb.set)
    ysb.grid(row=0, column=2, sticky=tki.N + tki.S)
    for idx,row in mpf.iterrows():
        fs_name = fpf[fpf['id_fs'] == row['id_fs']].iloc[0]['name_fs']
        sh_name = spf[spf['id_sh'] == row['id_sh']].iloc[0]['shsh']
        tree.insert("",tki.END, values=[row.id,row["name"],row.grade,fs_name,sh_name])

    mass = [btn1,btn2,btn3,btn4,tree,ysb]












def select_editing_db(root):
    global mass_all

    def delete_elemets():
        global mass
        for object_name in mass:
            object_name.grid_remove()

    def deleting_db():
        delete_elemets()

    def to_main():
        global mass_all
        global mass
        print(mass)
        print(mass_all)
        for object_name in mass:
            object_name.grid_remove()
        for object_name in mass_all:
            object_name.grid_remove()
        Main_window(root)


    """Добавить проверку на пустые поля
    Добавить messagebox"""
    def add_db():

        def save():
            global mpf
            global fpf
            global spf
            global max_id_stud
            his_id = max_id_stud + 1
            max_id_stud += 1
            name = stud_name.get()
            grade = stud_grade.get()
            fs = fs_list.curselection()[0]
            fs = fs_list.get(fs)
            id_fs = 0
            for idx,row in fpf.iterrows():
                if (row.name_fs == fs):
                    id_fs = row.id_fs
            sh = sh_list.curselection()[0]
            sh = sh_list.get(sh)
            id_sh = 0
            for idx,row in spf.iterrows():
                if (row.shsh == sh):
                    id_sh = row.id_sh

            ns = pd.DataFrame([[his_id,name,grade,id_fs,id_sh]],columns=['id','name','grade','id_fs','id_sh'])
            mpf = mpf.append(ns,ignore_index=True)


        global fpf
        global spf
        global mass
        delete_elemets()
        name_label = tki.Label(root, text="ФИО студента:")
        name_label.grid(column=0, row=3)
        stud_name = tki.Entry(justify = "left")
        stud_name.grid(column=1, row=3)

        grade_label = tki.Label(root, text="Выберите год обучения:")
        grade_label.grid(column=0, row=4)
        stud_grade = tki.Spinbox(root, from_=1, to=4)
        stud_grade.grid(column=1, row=4)

        fs_label = tki.Label(root, text="Выберите любимый предмет:")
        fs_label.grid(column=2, row=3)
        fs_list = tki.Listbox(height=8,width=40,exportselection=False)
        scroll = tki.Scrollbar(command=fs_list.yview)
        scroll.grid(column=3, row=4)
        fs_list.grid(column=2, row=4)
        for idx,row in fpf.iterrows():
            fs_list.insert(0,row.name_fs)

        sh_label = tki.Label(root, text="Выберите тип стипендии:")
        sh_label.grid(column=2, row=5)
        sh_list = tki.Listbox(height=8,width=40,exportselection=False)
        sh_list.grid(column=2,row=6)
        sh_scroll = tki.Scrollbar(command=sh_list.yview)
        sh_scroll.grid(column=3, row=6)

        for idx,row in spf.iterrows():
            sh_list.insert(0,row.shsh)

        add_student = tki.Button(root, text='Добавить студента', command = save)
        add_student.grid(column=3, row=7)
        mass = [name_label,stud_name,grade_label,stud_grade,fs_label,
        fs_list,scroll,sh_label,sh_list,sh_scroll,add_student]

    def repl_db():
        delete_elemets()

    btn1 = tki.Button(root, text='Удаление из базы', font=('Colibry', 12, 'bold'), command=deleting_db)
    btn1.grid(column=1, row=0)
    btn2 = tki.Button(root, text='Добавление', font=('Colibry', 12, 'bold'), command=add_db)
    btn2.grid(column=2, row=0)
    btn3 = tki.Button(root, text='Изменение', font=('Colibry', 12, 'bold'), command=repl_db)
    btn3.grid(column=3, row=0)
    btn4 = tki.Button(root, text='Назад', font=('Colibry', 12, 'bold'), command=to_main)
    btn4.grid(column=4, row=0)
    mass = []
    mass_all = [btn1,btn2,btn3,btn4]














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

    def max_id(db,name_col,id_max):
        for id in db[name_col]:
            if (id > id_max):
                id_max = id
        return id_max

    def delete_elemets():
        for object_name in mass:
            object_name.grid_remove()

    def get_db_main():
        global mpf
        global max_id_stud
        mpf = pd.read_csv(path_1.get())
        max_id_stud = max_id(mpf,'id',max_id_stud)

    def get_db_fs():
        global fpf
        global max_id_fs
        fpf = pd.read_csv(path_2.get())
        max_id_fs = max_id(fpf,'id_fs',max_id_fs)

    def get_db_sh():
        global spf
        global max_id_sh
        spf = pd.read_csv(path_3.get())
        max_id_sh = max_id(spf,'id_sh',max_id_sh)

    def com_db():
        global mpf
        global fpf
        global spf
        global max_id_stud
        global max_id_fs
        global max_id_sh
        mpf = lib.db.base_main()
        fpf = lib.db.base_fs()
        spf = lib.db.base_sh()
        max_id_stud = max_id(mpf,'id',max_id_stud)
        max_id_fs = max_id(fpf,'id_fs',max_id_fs)
        max_id_sh = max_id(spf,'id_sh',max_id_sh)
        delete_elemets()
        Main_window(root)

    def next_to_main():
        global mpf
        global fpf
        global spf
        if ((mpf !=0) and (fpf != 0) and (spf != 0)):
            delete_elemets()
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
