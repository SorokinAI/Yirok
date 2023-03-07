# Юрок 
## - как урок, только проще!

Юрок - электронная тетрадь, с весёлыми задачками. 
____
# Техническая часть
Юрок написан на языке программирования `Python 3.9`, были использованы библеотеки:
```python
  import time
  import turtle
  import webbrowser
  import random
  from tkinter import *
  from tkinter import messagebox
```

В 13-ой версии был добавлен конструктор задачек
Было использовано всего 2 библиотеки
```
from customtkinter import *  # main interface
from tkinter import messagebox as ms
```
Далее на основе CTK был создан  интерфейс программы
```
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
```
## У Юрок есть сайт: 
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Сайт+Юрок)](https://sites.google.com/view/iurok/)
#### Примечание: код в ветке master
