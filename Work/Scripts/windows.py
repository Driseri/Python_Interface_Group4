import tkinter as tki
import pandas as pd
import numpy as np
import os.path
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
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
    global mpf
    global fpf
    global spf
    def delete_elemets():
        global mass
        for object_name in mass:
            object_name.grid_remove()

    def deleting_db():
        global mass

        def sort_by_id():
            st_list.delete(*st_list.get_children())
            select_db = mpf
            if (stud_id.get() == "" or stud_id.get().isdigit()):
                if (stud_id.get().isdigit()):
                    select_db = mpf.loc[mpf["id"] == int(stud_id.get())]
                sort_by_name(select_db)
            else:
                error_label.config(text = "ID введен некорректно!")

        def sort_by_name(select_db):
            if (stud_name.get()!= ""):
                select_db = select_db.loc[select_db["name"] == stud_name.get()]
                sort_by_grade(select_db)
            else:
                sort_by_grade(select_db)

        def sort_by_grade(select_db):
            if (stud_grade.get().isdigit() or  stud_grade.get() == ""):
                if (stud_grade.get() != ""):
                    select_db = select_db.loc[select_db["grade"] == int(stud_grade.get())]
                for idx,row in select_db.iterrows():
                    fs_name = fpf[fpf['id_fs'] == row['id_fs']].iloc[0]['name_fs']
                    sh_name = spf[spf['id_sh'] == row['id_sh']].iloc[0]['shsh']
                    st_list.insert("",tki.END, values=[row["id"],row["name"],row["grade"],fs_name,sh_name])
            else:
                error_label.config(text = "Год обучения введен некорректно!")

        def del_el():
            global mpf
            if not st_list.selection():
                return
            selected_item = st_list.selection()[0]
            values = st_list.item(selected_item, option="values")
            mpf = mpf.loc[mpf["id"] != int(values[0])]
            st_list.delete(*st_list.get_children())
            error_label.config(text = "%s успешно удален\на"%(values[1]))

        select_db = 0
        delete_elemets()
        title_label = tki.Label(root, text="Выберите параметры:")
        title_label.grid(column=0, row=2)

        id_label = tki.Label(root, text="Id студента:")
        id_label.grid(column=0, row=3)
        stud_id = tki.Entry(justify = "left")
        stud_id.grid(column=0, row=4)

        name_label = tki.Label(root, text="ФИО студента:")
        name_label.grid(column=0, row=5)
        stud_name = tki.Entry(justify = "left")
        stud_name.grid(column=0, row=6)

        grade_label = tki.Label(root, text="Выберите год обучения:")
        grade_label.grid(column=0, row=7)
        stud_grade = tki.Entry(justify = "left")
        stud_grade.grid(column=0, row=8)


        columns = ("#1", "#2", "#3", "#4", "#5")
        st_list = tki.ttk.Treeview(root,show="headings", columns=columns, selectmode='browse')
        st_list.heading("#1", text="ID")
        st_list.heading("#2", text="ФИО")
        st_list.heading("#3", text="Год обучения")
        st_list.heading("#4", text="Любимый предмет")
        st_list.heading("#5", text="Стипендия")
        st_list.grid(column=1, row=2)
        ysb = tki.ttk.Scrollbar(root, orient=tki.VERTICAL, command=st_list.yview)
        st_list.configure(yscroll=ysb.set)
        ysb.grid(row=2, column=2, sticky=tki.N + tki.S)

        delete_btn = tki.Button(root, text='Удалить', command = del_el)
        delete_btn.grid(column=1, row=5)
        error_label  = tki.Label(root, text="Оставьте поля пустыми, чтобы пройтись по всем")
        error_label.grid(column=1, row=6)
        btn1 = tki.Button(root, text='Поиск', command = sort_by_id)
        btn1.grid(column=0, row=9)

        #ppt = mpf.loc[mpf['name'] == "Darina Yaschenko"]
    #    print(ppt)
    #    print("-"*15)
    #    ppt = ppt.loc[ppt['grade'] == 1]
    #    print(ppt)

        mass = [title_label,id_label,stud_id,name_label,stud_name,grade_label,stud_grade,st_list,ysb,error_label,btn1,delete_btn]

    def to_main():
        global mass_all
        global mass
        for object_name in mass:
            object_name.grid_remove()
        for object_name in mass_all:
            object_name.grid_remove()
        Main_window(root)

    def save_db():
        global mass
        global mpf

        def saving():
            mpf.to_csv(path_1.get(),index=False)
            error_label.config(text="База записана успешно")

        def common_saving():
            mpf.to_csv(r'../Data/main_db.csv',index=False)
            error_label.config(text="База записана успешно")

        delete_elemets()
        label_path = tki.Label(root, text="Введите путь для сохранения базы студентов")
        label_path.grid(column=0, row=2)
        path_1 = tki.Entry()
        path_1.grid(column=0, row=3)
        btn_save = tki.Button(root, text='Нажмите чтобы внести', command = saving)
        btn_save.grid(column=0, row=4)
        btn_save_common = tki.Button(root, text='Сохранить в базовое место', command = common_saving)
        btn_save_common.grid(column=0, row=5)
        error_label = tki.Label(root, text="")
        error_label.grid(column=0, row=6)

        mass = [label_path,path_1,btn_save,btn_save_common]


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

    btn1 = tki.Button(root, text='Удаление из базы', command=deleting_db)
    btn1.grid(column=1, row=0)
    btn2 = tki.Button(root, text='Добавление', command=add_db)
    btn2.grid(column=2, row=0)
    btn4 = tki.Button(root, text='Назад', command=to_main)
    btn4.grid(column=4, row=0)
    btn5 = tki.Button(root, text='Сохранить базу', command=save_db)
    btn5.grid(column=5, row=0)
    mass = []
    mass_all = [btn1,btn2,btn4,btn5]











"""Сделать ссылки на функции """
def Select_graf(root):
    root.geometry("1200x800")
    global mass
    global mass_all
    global mpf
    global fpf
    global spf

    def delete_elemets():
        for object_name in mass:
            object_name.grid_remove()

    def delete_all_elemets():
        for object_name in mass_all:
            object_name.grid_remove()

    def to_main():
        delete_elemets()
        Main_window(root)


    def first_text():
        global mass
        global mass_all
        delete_elemets()

        def back_to_choose():
            delete_all_elemets()
            Select_graf(root)

        def choose_col():
            st_list.delete(*st_list.get_children())

            bool_mass = [bolcb1.get(),bolcb2.get(),bolcb3.get(),bolcb4.get(),
                         bolcb5.get(),bolcb6.get(),bolcb7.get()]

            columns = ["name","grade","id_fs","name_fs",
                       "id_sh","shsh","value_shsh"]

            columns_names = ["Имя","Год обучения","ID предмета",
            "Название предмета","ID степендии","Название степендии","сумма стипендии"]

            columns_table = ("#1", "#2", "#3", "#4", "#5","#6","#7")
            need_columns = ["id"]
            need_columns_names = ["ID"]
            for i in range(0,7):
                if (bool_mass[i]):
                    need_columns.append(columns[i])
                    need_columns_names.append(columns_names[i])

            need_columns_table = columns_table[:len(need_columns)]


            st_list.config(columns=need_columns_table)
            for i in range(len(need_columns)):
                st_list.heading(need_columns_table[i],text=need_columns_names[i])



            for idx,row in full_db.iterrows():
                row_list = [row["name"],row["grade"],row["id_fs"],
                            row["name_fs"],row["id_sh"],row["shsh"],row["value_shsh"]]
                need_rows = [row["id"]]
                for i in range(0,7):
                    if (bool_mass[i]):
                        need_rows.append(row_list[i])

                st_list.insert("",tki.END, values=need_rows)


        st_list = tki.ttk.Treeview(root,show="headings", selectmode='browse')
        ysb = tki.ttk.Scrollbar(root, orient=tki.VERTICAL, command=st_list.yview)
        st_list.configure(yscroll=ysb.set)
        ysb.grid(row=7, column=2, sticky=tki.N + tki.S)
        bolcb1 = tki.BooleanVar()
        cb1 = tki.Checkbutton(root,text="Имя", variable=bolcb1)
        bolcb2 = tki.BooleanVar()
        cb2 = tki.Checkbutton(root,text="Год обучения", variable=bolcb2)
        bolcb3 = tki.BooleanVar()
        cb3 = tki.Checkbutton(root,text="ID предмета", variable=bolcb3)
        bolcb4 = tki.BooleanVar()
        cb4 = tki.Checkbutton(root,text="Название предмета", variable=bolcb4)
        bolcb5 = tki.BooleanVar()
        cb5 = tki.Checkbutton(root,text="ID степендии", variable=bolcb5)
        bolcb6 = tki.BooleanVar()
        cb6 = tki.Checkbutton(root,text="Название степендии", variable=bolcb6)
        bolcb7 = tki.BooleanVar()
        cb7 = tki.Checkbutton(root,text="сумма стипендии", variable=bolcb7)
        cb1.grid(column=0, row=0)
        cb2.grid(column=0, row=1)
        cb3.grid(column=0, row=2)
        cb4.grid(column=0, row=3)
        cb5.grid(column=0, row=4)
        cb6.grid(column=0, row=5)
        cb7.grid(column=0, row=6)
        st_list.grid(column=1, row=7)
        btn_do = tki.Button(root,text="Поиск",command=choose_col)
        btn_do.grid(column=0, row=7)
        back_btn = tki.Button(root,text="Hазад",command=back_to_choose)
        back_btn.grid(column=0, row=8)
        mass_all = [st_list,cb1,cb2,cb3,cb4,cb5,cb6,cb7,btn_do,back_btn,ysb]

    def second_text():
        global mass
        delete_elemets()
        def back_to_choose():
            delete_all_elemets()
            Select_graf(root)


        nl = pd.pivot_table(full_db,index=["grade","shsh"],values=["id_sh"],aggfunc=[len])

        columns = ("#1", "#2", "#3")
        st_list1 = tki.ttk.Treeview(root,show="headings", columns=columns, selectmode='browse')
        st_list1.heading("#1", text="Год обучения")
        st_list1.heading("#2", text="Вид стипендии")
        st_list1.heading("#3", text="Количество имеющих")
        st_list1.grid(column=1, row=0)
        ysb1 = tki.ttk.Scrollbar(root, orient=tki.VERTICAL, command=st_list1.yview)
        st_list1.configure(yscroll=ysb1.set)
        ysb1.grid(row=0, column=2, sticky=tki.N + tki.S)

        for inx,row in nl.iterrows():
            st_list1.insert("",tki.END, values=[inx[0],inx[1],row["len"]["id_sh"]])

        ns = pd.pivot_table(full_db,index=["grade","name_fs"],values=["id_fs"],aggfunc=[len])

        st_list2 = tki.ttk.Treeview(root,show="headings", columns=columns, selectmode='browse')
        st_list2.heading("#1", text="Год обучения")
        st_list2.heading("#2", text="Любимый предмет")
        st_list2.heading("#3", text="Количество имеющих")
        st_list2.grid(column=1, row=1)
        ysb2 = tki.ttk.Scrollbar(root, orient=tki.VERTICAL, command=st_list2.yview)
        st_list2.configure(yscroll=ysb2.set)
        ysb2.grid(row=1, column=2, sticky=tki.N + tki.S)

        for inx,row in ns.iterrows():
            st_list2.insert("",tki.END, values=[inx[0],inx[1],row["len"]["id_fs"]])


        back_btn = tki.Button(root,text="Hазад",command=back_to_choose)
        back_btn.grid(column=0, row=0)
        mass = [st_list1,ysb1,st_list2,ysb2,back_btn]

    def third_text():
        global mass
        delete_elemets()

        def choose_index():
            attributes = np.array(["id", "name", "grade", "name_fs", "shsh"])
            values = [check_brand_state.get(), check_model_state.get(), check_price_state.get(),
            check_discount_state.get(), check_size_state.get()]
            return attributes[values]

        def choose_values():
            attributes = np.array(["grade", "value_shsh","id_fs","id_sh"])
            values = [check_price_values_state.get(), check_discount_values_state.get(),
                      check_fs_values_state.get(), check_sh_values_state.get()]
            return attributes[values]

        def show_text_message():
            tki.messagebox.showinfo("Готово", "Ваш отчет сохранен. Название файла — pivot table!")

        def back():
            delete_elemets()
            Select_graf(root)

        def ok():
            index_attributes = choose_index()
            values_attributes = choose_values()
            lib.reports.pivot_table(index_attributes, values_attributes, full_db)
            pivot_table_index_choose_label.destroy()
            pivot_table_values_choose_label.destroy()
            pivot_table_label.destroy()
            first_check_button.destroy()
            second_check_button.destroy()
            third_check_button.destroy()
            forth_check_button.destroy()
            fifth_check_button.destroy()
            third_check_values_button.destroy()
            forth_check_values_button.destroy()
            space_label.destroy()
            pivot_table_index_button.destroy()
            pivot_table_values_button.destroy()
            fifth_check_values_button.destroy()
            six_check_values_button.destroy()

            back_button.destroy()
            ok_button.destroy()
            show_text_message()
            Select_graf(root)

        pivot_table_index_choose_label = tki.Label(
        root,
        text='Выберите индекс атрибуты: '
        )

        pivot_table_values_choose_label = tki.Label(
        root,
        text='Выберите значимые атрибуты: '
        )

        pivot_table_label = tki.Label(
        root,
        text='Сводная таблица'
        )

        check_brand_state = tki.BooleanVar()
        check_brand_state.set(False)
        first_check_button = tki.Checkbutton(
        root,
        text="ID студента",
        padx=15,
        pady=5,
        var=check_brand_state
        )
        first_check_button.grid(column=1, row=2, sticky=tki.W)

        check_model_state = tki.BooleanVar()
        check_model_state.set(False)
        second_check_button = tki.Checkbutton(
        root,
        text="Имя студента",
        padx=15,
        pady=5,
        var=check_model_state
        )
        second_check_button.grid(column=1, row=3, sticky=tki.W)

        check_price_state = tki.BooleanVar()
        check_price_state.set(False)
        third_check_button = tki.Checkbutton(
        root,
        text="Год обучения",

        padx=15,
        pady=5,
        var=check_price_state
        )
        third_check_button.grid(column=1, row=4, sticky=tki.W)

        check_discount_state = tki.BooleanVar()
        check_discount_state.set(False)
        forth_check_button = tki.Checkbutton(
        root,
        text="Любимый предмет",
        padx=15,
        pady=5,
        var=check_discount_state
        )
        forth_check_button.grid(column=1, row=5, sticky=tki.W)

        check_size_state = tki.BooleanVar()
        check_size_state.set(False)
        fifth_check_button = tki.Checkbutton(
        root,
        text="Стипендия",
        padx=15,
        pady=5,
        var=check_size_state
        )
        fifth_check_button.grid(column=1, row=6, sticky=tki.W)

        check_price_values_state = tki.BooleanVar()
        check_price_values_state.set(False)
        third_check_values_button = tki.Checkbutton(
        root,
        text="Год обучения",
        padx=15,
        pady=5,
        var=check_price_values_state
        )
        third_check_values_button.grid(column=3, row=3, sticky=tki.W)

        check_discount_values_state = tki.BooleanVar()
        check_discount_values_state.set(False)
        forth_check_values_button = tki.Checkbutton(
        root,
        text="Сумма стипендии",
        padx=15,
        pady=5,
        var=check_discount_values_state
        )
        forth_check_values_button.grid(column=3, row=5, sticky=tki.W)


        check_fs_values_state = tki.BooleanVar()
        check_fs_values_state.set(False)
        six_check_values_button = tki.Checkbutton(
        root,
        text="Любимый предмет",
        padx=15,
        pady=5,
        var=check_fs_values_state
        )
        six_check_values_button.grid(column=3, row=7, sticky=tki.W)


        check_sh_values_state = tki.BooleanVar()
        check_sh_values_state.set(False)
        fifth_check_values_button = tki.Checkbutton(
        root,
        text="Стипендия",
        padx=15,
        pady=5,
        var=check_sh_values_state
        )
        fifth_check_values_button.grid(column=3, row=8, sticky=tki.W)

        space_label = tki.Label(
        root,
        text=' ',
        width=30
        )

        pivot_table_index_button = tki.Button(
        root,
        text='Выбрать',
        command=choose_index()
        )

        pivot_table_values_button = tki.Button(
        root,
        text='Выбрать',
        command=choose_values()
        )

        back_button = tki.Button(
        root,
        text='Назад',
        width=5,
        command=back
        )

        ok_button = tki.Button(
        root,
        text='Ок',
        width=5,
        command=ok
        )

        back_button.place(relx=.75, rely=.8)
        ok_button.place(relx=.85, rely=.8)

        pivot_table_label.grid(column=1, columnspan=3, row=0)
        pivot_table_index_choose_label.grid(column=1, row=1)
        pivot_table_values_choose_label.grid(column=3, row=1)
        space_label.grid(column=2, rowspan=7, row=1)

        pivot_table_index_button.grid(column=1, row=7)
        pivot_table_values_button.grid(column=3, row=9)


    def second_graf():
        global mass

        def back_to_choose():
            delete_all_elemets()
            Select_graf(root)

        def make_graf():
            plt.clf()
            kind = choose_box.curselection()[0]

            if (kind == 0):
                nl = full_db["grade"]
                plt.xticks([1,2,3,4], ["1 курс","2 курс","3 курс","4 курс"],
                           rotation=10, fontsize=8)
                plt.xlabel('Курс')
                plt.ylabel('Количесвто студентов')
                plt.hist(nl,bins = 16)

            else:
                nl = full_db["value_shsh"]
                plt.xticks([0,3500,13000],
                           ["Без стипендии","Повышенная","Президентская"],
                           rotation=10, fontsize=8)
                plt.xlabel('Курс')
                plt.ylabel('Стипендия')
                plt.hist(nl,bins = 16)
            plt.savefig(r"../Graphics/second_hist.png")
            fig.canvas.draw()


        delete_elemets()
        matplotlib.use('TkAgg')
        fig = plt.figure(figsize = (9,6))
        canvas = FigureCanvasTkAgg(fig, master=root)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row=1, column=1)


        choose_parm = ["График курс\кол_студентов","График курс\средняя стипендия"]
        choose_box = tki.Listbox(exportselection=False, width=25)
        choose_box.grid(row=1, column=0)
        for row in choose_parm:
            choose_box.insert(tki.END,row)

        btn_make = tki.Button(root,text="Построить график",command=make_graf)
        btn_make.grid(row=2, column=0)

        back_btn = tki.Button(root,text="Hазад",command=back_to_choose)
        back_btn.grid(column=0, row=0)
        mass = [plot_widget,back_btn,choose_box,btn_make]


    def first_graf():
        global mass

        def back_to_choose():
            delete_all_elemets()
            Select_graf(root)

        def update_graf():

            def draw(lists):
                plt.clf()
                plt.bar(x, height=hght)
                plt.xticks(x, name_col,rotation=10, fontsize=8)
                fig.canvas.draw()
                plt.savefig(r"../Graphics/first_bar.png")



            kind = choose_box.curselection()[0]
            choose_parm = ["График по стипендиям","График по предметам" ]
            if (kind == 0):
                nl = pd.pivot_table(full_db,index=["shsh"],values=["id_sh"],aggfunc=[len])
                hght=[]
                name_col = []
                for idx,row in nl.iterrows():
                    name_col.append(idx)
                    hght.append(int(row["len"]["id_sh"]))
                x = [(x+10)  for x in range(len(name_col))]
                draw(nl)
                plt.xlabel('Вид стипендий')
                plt.ylabel('Количесвто студентов')

            else:
                nl = pd.pivot_table(full_db,index=["name_fs"],values=["id_fs"],aggfunc=[len])
                hght=[]
                name_col = []
                for idx,row in nl.iterrows():
                    name_col.append(idx)
                    hght.append(int(row["len"]["id_fs"]))

                x = [(x+10)  for x in range(len(name_col))]
                draw(nl)

                plt.xlabel('Предметы')
                plt.ylabel('Количесвто студентов')



        delete_elemets()
        matplotlib.use('TkAgg')
        fig = plt.figure(figsize = (9,6))
        canvas = FigureCanvasTkAgg(fig, master=root)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row=1, column=1)

        choose_parm = ["График по стипендиям","График по предметам" ]
        choose_box = tki.Listbox(exportselection=False, width=25)
        for row in choose_parm:
            choose_box.insert(tki.END,row)

        btn_make = tki.Button(root,text="Построить график",command=update_graf)
        btn_make.grid(row=1, column=0)
        choose_box.grid(row=1, column=2)
        back_btn = tki.Button(root,text="Hазад",command=back_to_choose)
        back_btn.grid(column=0, row=0)
        mass=[back_btn,plot_widget,choose_box,btn_make]


    def fourth_graf():
        global mass

        def back_to_choose():
            delete_elemets()
            Select_graf(root)

        def update_graf():
            kind = choose_box.curselection()[0]
            if (kind == 0):
                plt.scatter(full_db["id"].tolist(),full_db["value_shsh"].tolist())
                plt.xlabel('Студенты')
                plt.ylabel('Стиппендия')
            else:
                nl = pd.pivot_table(full_db,index=["grade","id_fs"],values=["name_fs"],aggfunc=[len])
                x = []
                y = []
                vals = []
                for idx,row in nl.iterrows():
                    x.append(int(idx[0]))
                    y.append(int(idx[1]))
                    vals.append(25 * row["len"]["name_fs"])
                y_names = ["Calculus","Physics","Algorithmization","Physical Education",
                     "Chemistry", "Projects seminar"]
                plt.xlabel('Курс')
                plt.ylabel('Дисциплина')
                plt.yticks([11,12,13,14,15,16],
                           y_names,fontsize=8)
                plt.scatter(x,y,s = vals)



            fig.canvas.draw()
            plt.savefig(r"../Graphics/forth_scatter.png")
        delete_elemets()
        matplotlib.use('TkAgg')
        fig = plt.figure(figsize = (9,6))
        canvas = FigureCanvasTkAgg(fig, master=root)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row=1, column=1)

        choose_parm = ["студенты/стипендия","курс\предметы" ]
        choose_box = tki.Listbox(exportselection=False, width=25)
        for row in choose_parm:
            choose_box.insert(tki.END,row)
        choose_box.grid(row = 1, column=0)

        btn_make = tki.Button(root,text="Построить график",command=update_graf)
        btn_make.grid(row=0, column=1)
        back_btn = tki.Button(root,text="Hазад",command=back_to_choose)
        back_btn.grid(column=0, row=0)
        mass = [plot_widget]

    delete_elemets()
    full_db = lib.reports.make_full_db(mpf, fpf, spf)
    btn1 = tki.Button(root, text='Простой текстовый отчет',command=first_text)
    btn1.grid(column=1, row=0)
    btn2 = tki.Button(root, text='Общий ',command=second_text)
    btn2.grid(column=1, row=1)
    btn3 = tki.Button(root, text='Сводная таблица',command=third_text)
    btn3.grid(column=1, row=2)
    btn4 = tki.Button(root, text='Кластеризованная столбчатая диаграмма',command=first_graf)
    btn4.grid(column=1, row=3)
    btn5 = tki.Button(root, text='Категоризированная гистограмма',command=second_graf)
    btn5.grid(column=1, row=4)
    btn7 = tki.Button(root, text='Kатегоризированная диаграмма рассеивания',command=fourth_graf)
    btn7.grid(column=1, row=5)


    exit = tki.Button(root, text='В главное меню', command=to_main)
    exit.grid(column=0, row=6)
    mass = [btn1,btn2,btn3,btn4,btn5,btn7,exit]
















"""Надо добавить проверку существования
добавить флаг для перехода на новое окно"""
def Select_db(root):
    root.geometry("800x650")
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
        if ((mpf != 0) and (fpf != 0) and (spf != 0)):
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
