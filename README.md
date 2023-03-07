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
# Configure --version 1.2
Было использовано всего 2 библиотеки
```python
from customtkinter import *  # main interface
from tkinter import messagebox as ms
```
Был написан простой и понятный интерфейс
Сохранение файлов работает по простому принципу:

```python
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
        photo.write(f"{e4.get()}{e2.get()}")
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

```

## У Юрок есть сайт: 
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Сайт+Юрок)](https://sites.google.com/view/iurok/)
#### Примечание: код в ветке master
