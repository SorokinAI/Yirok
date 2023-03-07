from customtkinter import *  # main interface
from tkinter import messagebox as ms


def save():
    """"save lesion"""
    print(e1.get(), e2.get(), e3.get(), e4.get())
    print(e4.get())
    if e1.get() and e2.get() and e3.get() and e4.get() != '':
        e1.configure(border_color='silver')
        e2.configure(border_color='silver')
        e3.configure(border_color='silver')
        e4.configure(border_color='silver')

        # true
        true = open(f'{e4.get()}/true.txt', 'w')
        true.write(e1.get())
        true.close()
        # photo (bg)
        photo = open(f'{e4.get()}/bg.txt', 'w')
        photo.write(f"{e4.get()}/{e2.get()}")
        photo.close()
        # comment
        comment = open(f'{e4.get()}/comment.txt', 'w')
        comment.write(e3.get())
        comment.close()
        l_.configure(text='Успешно!', text_color='green')
    else:
        l_.configure(text='Вы что-то не ввели или ввели неверно!\nВводите пути без кавычек!', text_color='#f34336')
        if e1.get() == '':
            e1.configure(border_color='#f34336')
        else:
            e1.configure(border_color='silver')
        if e2.get() == '':
            e2.configure(border_color='#f34336')
        else:
            e2.configure(border_color='silver')
        if e3.get() == '':
            e3.configure(border_color='#f34336')
        else:
            e3.configure(border_color='silver')
        if e4.get() == '':
            e4.configure(border_color='#f34336')
        else:
            e4.configure(border_color='silver')


def on_closing():
    """Destroy app"""
    if ms.askokcancel('Выход', 'Вы точно хотите выйти?\nЕсли да, то не забудьте сохранить задачку!'):
        quit()


# theme
set_appearance_mode('light')
set_default_color_theme('green')

# window
app = CTk()
app.iconbitmap('icon_edit.ico')
app.geometry('1000x550+300+00')
app.title("Конструктор задачек")
app.protocol("WM_DELETE_WINDOW", on_closing)
all_text_font = CTkFont(family='Bahnschrift', size=24)
all_button_font = CTkFont(family='Bahnschrift', size=18)

main_label = CTkLabel(app, text='Конструктор задачек для Юрок', font=all_text_font)
l1 = CTkLabel(app, text='Верный ответ (str):', font=all_text_font)
l2 = CTkLabel(app, text='Путь к фону задания (folder/photo):', font=all_text_font)
l3 = CTkLabel(app, text='Комментарий к заданию:', font=all_text_font)
l4 = CTkLabel(app, text='Папка для сохранения:', font=all_text_font)
l_ = CTkLabel(app, text='', font=all_text_font)

e1 = CTkEntry(app, border_color='silver', width=300, font=all_text_font)
e2 = CTkEntry(app, border_color='silver', width=300, font=all_text_font)
e3 = CTkEntry(app, border_color='silver', width=300, font=all_text_font)
e4 = CTkEntry(app, border_color='silver', width=300, font=all_text_font)

save_button = CTkButton(app, text="Сохранить", font=all_button_font, command=save)

# Widgets on window
main_label.pack(side='top')
l1.place(x=20, y=40)
l2.place(x=20, y=80)
l3.place(x=20, y=120)
l4.place(x=20, y=160)
l_.place(x=20, y=200)
e1.place(x=450, y=40)
e2.place(x=450, y=80)
e3.place(x=450, y=120)
e4.place(x=450, y=160)
save_button.pack(side='bottom')

app.minsize(800, 350)
app.mainloop()
