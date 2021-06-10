import tkinter as tki

def Start_window(root):
    def delete_elemets():
        for object_name in mass:
            if object_name.winfo_viewable():
                object_name.grid_remove()
            else:
                object_name.grid()
        Main_window(root)

    lbl1 = tki.Label(root, text="Добро пожаловать в говно епта!!!", font=('Times', 20, 'italic'))
    lbl1.grid(column=1, row=0, pady = 10, padx = 25)
    btn = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'),bg='blue',fg='red',command=delete_elemets)
    btn.grid(column=1, row=1)
    mass = [lbl1,btn]


def Main_window(root):
    btn1 = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn1.grid(column=1, row=0)    #Вставить command
    btn2 = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn2.grid(column=1, row=1)
    btn3 = tki.Button(root, text='Нажмите чтобы продолжить', font=('Colibry', 12, 'bold'), pady = 20,width = 25, height = 2)
    btn3.grid(column=1, row=2)
