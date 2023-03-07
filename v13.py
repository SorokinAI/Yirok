# import
import time
import turtle
import webbrowser
import random
from tkinter import *
from tkinter import messagebox

# global vars

ok = 0
global_roots = True
number_lession = 0
numbers_app = False


# info in console
# --version 13.2


class Lessions:  # работа с уроками
    global number_lession

    def __init__(self, number, difficulty):
        self.number = number
        self.difficulty = difficulty

    def start(self):
        global number_lession
        print("Задачка под номером:", self.number, "и сложностью", self.difficulty, "запущена")
        print("\n")
        number_lession = self.number


# уроки в документации/lesson's in documentation
lev1 = Lessions(1, 'Normal')
lev2 = Lessions(2, 'Hard')
lev3 = Lessions(3, 'Easy')
lev4 = Lessions(4, 'Easy')
lev5 = Lessions(5, 'Hard')
lev6 = Lessions(6, 'Hard')
lev7 = Lessions(7, 'Normal')
else_number_l = Lessions('else', '$?')
game_paint = Lessions("game", "game")


def destroy():
    global number_lession
    # final window in lessios (1-7)
    global root
    global root3
    global root5, root7
    global root8, root9
    global root12
    global root15, root16
    global root20
    global gui

    global code
    global coden3
    global win

    if number_lession == 1:
        root.destroy()
    elif number_lession == 2:
        root3.destroy()
    elif number_lession == 3:
        root5.destroy()
    elif number_lession == 4:
        if code:
            root9.destroy()
        else:
            root8.destroy()
    elif number_lession == 5:
        root12.destroy()
    elif number_lession == 6:
        if win:
            root15.destroy()
        else:
            root16.destroy()
    elif number_lession == 7:
        root20.destroy()
    elif number_lession == 'else':
        gui.destroy()
    else:
        pass


def numbers():
    destroy()
    global app
    global numbers_app
    global ok
    ok = 0  # обнуление баллов
    numbers_app = True
    app = Tk()
    app.title('Выбор след. задачки')
    app.geometry('750x600')
    app.resizable(False, False)
    app.iconbitmap('icon2.ico')
    app['bg'] = 'white'

    label = Label(app, text="Выбери следующую задачку!", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20")
    num1 = Button(app, text="Задачка №1 - Интересные треугольники", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20", cursor="hand2", command=number1)
    num2 = Button(app, text="Задачка №2 - Помоги Генералу Гавсу отгадать загадки", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20", cursor="hand2", command=number2)
    num3 = Button(app, text="Задачка №3 - Turtle", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20", cursor="hand2", command=number3)
    num4 = Button(app, text="Задачка №4 - Снова треугольники", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20", cursor="hand2", command=number4)
    num5 = Button(app, text="Задачка №5 - Тест на знание turtle", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20", cursor="hand2", command=number5)
    num6 = Button(app, text="Задачка №6 - Биты, байты и т.п.", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20", cursor="hand2", command=number6)
    num7 = Button(app, text="Задачка №7 - Задачка для мамкиных хацкеров", fg="Black", bg="white",
                  border=0, font="Bahnschrift 20", cursor="hand2", command=number7)
    n_else = Button(app, text="Выбрать другую", fg="Black", bg="white",
                    border=0, font="Bahnschrift 20", cursor="hand2", command=else_number)

    label.place(x=20, y=20)
    num1.place(x=20, y=50)
    num2.place(x=20, y=90)
    num3.place(x=20, y=130)
    num4.place(x=20, y=170)
    num5.place(x=20, y=210)
    num6.place(x=20, y=250)
    num7.place(x=20, y=290)
    n_else.place(x=20, y=350)
    app.mainloop()


# мини-игра/mini-game
# игровые настройки/game settings


size = 5


def game():  # код игры/game code
    if messagebox.askokcancel("Юрок Paint", "Хотите запустить мини-игру?"):
        messagebox.showinfo('Управление', 'Управление стрелочками!')
        destroy()

        game_paint.start()

        wind = turtle.Screen()
        wind.title("Рисовалка")
        wind.setup(1280, 780)

        turt1 = turtle.Turtle()

        # цвета/color's

        def color1():
            color = 'black'
            turt1.color(color)

        def color2():
            color = 'red2'
            turt1.color(color)

        def color3():
            color = 'gold'
            turt1.color(color)

        def color4():
            color = 'violet'
            turt1.color(color)

        def color5():
            color = 'lime green'
            turt1.color(color)

        def color6():
            color = 'dark green'
            turt1.color(color)

        def color7():
            color = 'cyan'
            turt1.color(color)

        def color8():
            color = 'RoyalBlue3'
            turt1.color(color)

        # размер ручки turtle/size pen turtle

        def siz1():
            turt1.pensize(1)

        def siz2():
            turt1.pensize(2)

        def siz3():
            turt1.pensize(3)

        def siz4():
            turt1.pensize(4)

        def siz5():
            turt1.pensize(5)

        def siz6():
            turt1.pensize(6)

        def siz7():
            turt1.pensize(7)

        def siz8():
            turt1.pensize(8)

        def siz9():
            turt1.pensize(9)

        def siz10():
            turt1.pensize(10)

        # джостик/gamepad

        def right():
            turt1.right(10)

        def left():
            turt1.left(10)

        def up():
            turt1.forward(10)

        def down():
            turt1.back(10)

        def cleargame():  # очистка окна для рисования/clear window for paint
            wind.reset()
            turt1.pensize(size)

        # окно настройки черепашки/window setting's turtle
        gui_game = Tk()
        gui_game.geometry("550x500")
        gui_game.title("Параметры")
        gui_game["bg"] = "white"
        gui_game.resizable(width=False, height=False)

        col0 = Label(gui_game, bg='white', text="Выбери цвет кисти:", font="Bahnschrift 21")
        col1 = Button(gui_game, text="Чёрный", fg='snow', bg='black', border=0, width=11, cursor="hand2",
                      command=color1)
        col2 = Button(gui_game, text="Красный", fg='black', bg='red2', border=0, width=11, cursor="hand2",
                      command=color2)
        col3 = Button(gui_game, text="Жёлтый", fg='black', bg='gold', border=0, width=11, cursor="hand2",
                      command=color3)
        col4 = Button(gui_game, text="Пурпурный", fg='black', bg='violet', border=0, width=11, cursor="hand2",
                      command=color4)
        col5 = Button(gui_game, text="Светло-зел", fg='black', bg='lime green', border=0, width=11, cursor="hand2",
                      command=color5)
        col6 = Button(gui_game, text="Тёмно-зел.", fg='black', bg='dark green', border=0, width=11, cursor="hand2",
                      command=color6)
        col7 = Button(gui_game, text="Голубой", fg='black', bg='cyan', border=0, width=11, cursor="hand2",
                      command=color7)
        col8 = Button(gui_game, text="Синий", fg='black', bg='RoyalBlue3', width=11, border=0, cursor="hand2",
                      command=color8)
        clear = Button(gui_game, bg='white', text="Очисчить экран🧹", border=0, cursor="hand2", command=cleargame)
        s0 = Label(gui_game, bg='white', text="Выбери размер кисти:", font="Bahnschrift 21")
        s1 = Button(gui_game, bg='silver', text="1(маленький)", border=0, width=11, cursor="hand2", command=siz1)
        s2 = Button(gui_game, bg='silver', text="2", border=0, width=11, cursor="hand2", command=siz2)
        s3 = Button(gui_game, bg='silver', text="3", border=0, width=11, cursor="hand2", command=siz3)
        s4 = Button(gui_game, bg='silver', text="4", border=0, width=11, cursor="hand2", command=siz4)
        s5 = Button(gui_game, bg='silver', text="5", border=0, width=11, cursor="hand2", command=siz5)
        s6 = Button(gui_game, bg='silver', text="6", border=0, width=11, cursor="hand2", command=siz6)
        s7 = Button(gui_game, bg='silver', text="7", border=0, width=11, cursor="hand2", command=siz7)
        s8 = Button(gui_game, bg='silver', text="8", border=0, width=11, cursor="hand2", command=siz8)
        s9 = Button(gui_game, bg='silver', text="9", border=0, width=11, cursor="hand2", command=siz9)
        s10 = Button(gui_game, bg='silver', text="10(большой)", width=11, border=0, cursor="hand2", command=siz10)

        clear.grid(column=4, row=2)
        col0.grid(column=2, row=1)
        col1.grid(column=2, row=2)
        col2.grid(column=2, row=3)
        col3.grid(column=2, row=4)
        col4.grid(column=2, row=5)
        col5.grid(column=3, row=2)
        col6.grid(column=3, row=3)
        col7.grid(column=3, row=4)
        col8.grid(column=3, row=5)
        s0.grid(column=2, row=6)
        s1.grid(column=2, row=7)
        s2.grid(column=2, row=8)
        s3.grid(column=2, row=9)
        s4.grid(column=2, row=10)
        s5.grid(column=2, row=11)
        s6.grid(column=3, row=7)
        s7.grid(column=3, row=8)
        s8.grid(column=3, row=9)
        s9.grid(column=3, row=10)
        s10.grid(column=3, row=11)

        # окно рисования/window for paint
        wind.reset()
        wind.bgpic("")
        wind.title("Paint Юрок")
        wind.setup(1280, 700)
        turt1.penup()
        turt1.speed(1000)
        turt1.hideturtle()
        turt1.goto(-600, 300)
        turt1.home()
        turt1.pensize(5)
        turt1.pendown()
        turt1.pensize(size)
        turt1.showturtle()

        # джостики2/gamepad2

        # WASD
        turtle.onkeypress(right, 'd')
        turtle.onkeypress(left, 'a')
        turtle.onkeypress(up, 'w')
        turtle.onkeypress(down, 's')

        # стрелочки/arrow's
        turtle.onkeypress(right, 'Right')
        turtle.onkeypress(left, 'Left')
        turtle.onkeypress(up, 'Up')
        turtle.onkeypress(down, 'Down')

        turtle.listen()

        gui_game.mainloop()
    else:
        numbers()


# главное окно/main window

global_root = Tk()
global_root.iconbitmap('icon2.ico')
global_root.state('zoomed')
global_root.title("Юрок")
global_root["bg"] = "white"

global_root.image = PhotoImage(file="bg/GL1 BG.png")
back = Label(global_root, image=global_root.image, border=0)
back.place(x=100, y=250)

yir = Label(global_root, text="Юрок", fg="red", bg="white", font="Impact 42")
yir2 = Label(global_root, text="-как урок, только проще!", fg="red", bg="white", font="Impact 20")


def site_school102():
    print("System: open 'http://школа102.рф/'")
    webbrowser.open("http://школа102.рф/")


def stop():
    global global_roots
    global numbers_app
    global app
    if global_roots:
        global_roots = False
        global_root.destroy()
    else:
        pass

    if numbers_app:
        app.destroy()
        numbers_app = False
    else:
        pass


# инструкция/instruction
def instruction():
    def open_yirok():
        webbrowser.open('https://sites.google.com/view/iurok/')

    app = Tk()
    app.title('Инструкция')
    app.iconbitmap('icon2.ico')
    app.geometry('1000x800')
    app['bg'] = 'White'

    instruction1 = Label(app, text='Инструкция для начала использования «Юрок»', bg='White', font='Bahnschrift 24')
    v1 = Label(app, text='Как пользоваться электронной тетрадью «Юрок»?', bg='White', font='Bahnschrift 20')
    otv1 = Label(app, text='1. Выберите нужную задачку из списка.\n'
                           '2. Напишите ответ в поле и нажмите кнопку\n'
                           '«Проверить ответы» или выберите ответ из списка.',
                 bg='white', justify='left', font='Bahnschrift 18')
    v2 = Label(app, text='Как играть в мини-игру?', bg='White', font='Bahnschrift 20')
    otv2 = Label(app, text='1. Решите задачку на оценку «4» или выше.\n'
                           '2. Игра откроется автоматически.\n'
                           '3. Выберите нужный цвет и размер кисти.\n'
                           '4. Играйте с помощью стрелочек и творите\n',
                 bg='White', justify='left', font='Bahnschrift 18')
    site_yirok = Button(app, text='Подробнее о проекте на сайте', bg='White', fg='Silver', font='Bahnschrift 20',
                        cursor='hand2', border=0, activeforeground='orange', command=open_yirok)

    instruction1.pack(side=TOP)
    v1.place(x=20, y=150)
    otv1.place(x=20, y=220)
    v2.place(x=20, y=320)
    otv2.place(x=20, y=410)
    site_yirok.pack(side=BOTTOM)
    app.mainloop()


# задачки/leseons
def number1():
    lev1.start()
    stop()
    global root
    global ok

    def on_closing_number1():
        if messagebox.askokcancel("Выход из приложения",
                                  "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
            root.destroy()

    root = Tk()
    root.state('zoomed')
    root.title("Юрок №1")
    root.iconbitmap("icon2.ico")
    root.protocol("WM_DELETE_WINDOW", on_closing_number1)
    root["bg"] = "white"

    root.image = PhotoImage(file="bg/BG.png")
    back1 = Label(root, image=root.image, border=0)
    back1.place(x=200, y=0)

    def prover_num1():  # проверка номера 1/examination number 1
        global ok

        otv1_ = otv1.get()
        otv2_ = otv2.get()
        print("System (норма 11 35 (True)):", otv1_, otv2_)

        if otv1_ == '13' and otv2_ == '35':
            y_or_n_num1["fg"] = "Green"
            y_or_n_num1["text"] = "Всё верно! Молодец!"
            root.update()
            time.sleep(3)
            ok = ok + 2

            if ok >= 2:
                y_or_n_num1['fg'] = 'Green'
                y_or_n_num1['text'] = "Я тебя поздравляю, ты отлично выполнил задачку\n- на все 5 баллов!"
                root.update()
                time.sleep(3)
                game()
            elif ok >= 0 and ok < 2:
                y_or_n_num1['fg'] = 'Green'
                y_or_n_num1['text'] = "Молодец, ты хорошо выполнил задание - 4."
                root.update()
                time.sleep(3)
                game()
            elif ok < 0 and ok > -5:
                y_or_n_num1['fg'] = 'DarkOrange2'
                y_or_n_num1['text'] = "Ты выполнил задание с потерями - 3."
                root.update()
                time.sleep(3)
                numbers()
            elif ok <= -4:
                y_or_n_num1['fg'] = 'Red2'
                y_or_n_num1['text'] = "Ты провалил задание - 2!"
                root.update()
                time.sleep(3)
                numbers()
            else:
                print("System: error grade")

        else:
            y_or_n_num1["fg"] = "Red2"
            y_or_n_num1["text"] = "Неверно, попробуй снова!"
            ok = ok - 2
            print("system ok==", ok)

    z1 = Label(root, text="Сколько треугольников на фигуре №1? ", fg="Black", bg="white",
               font="Bahnschrift 20")
    z2 = Label(root, text="Сколько треугольников на фигуре №2? ", fg="Black", bg="white",
               font="Bahnschrift 20")
    otv1 = Entry(root, fg="Black", bg="white", font="Bahnschrift 20")
    otv2 = Entry(root, fg="Black", bg="white", font="Bahnschrift 20")

    provbutt = Button(root, text="Проверить ответы", fg="Black", bg="white", border=1,
                      font="Bahnschrift 20", cursor="hand2", command=prover_num1)
    y_or_n_num1 = Label(root, text="  ", fg="Black", bg="white", font="Bahnschrift 20")

    z1.place(x=100, y=350)
    z2.place(x=100, y=450)
    otv1.place(x=630, y=350)
    otv2.place(x=630, y=450)
    provbutt.place(x=100, y=550)
    y_or_n_num1.place(x=400, y=550)


def number2():
    def num2_3():
        global root3
        global ok

        def on_closing_number23():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root3.destroy()

        root3 = Tk()
        root3.state('zoomed')
        root3.title("Юрок №2")
        root3.iconbitmap("icon2.ico")
        root3.protocol("WM_DELETE_WINDOW", on_closing_number23)
        root3["bg"] = "white"

        # w1 = Label(root3, text="Все шли в Москву*", fg="Black", bg="white", font="Bahnschrift 20")

        root3.image = PhotoImage(file="bg/BG2v3.png")
        back = Label(root3, image=root3.image, border=0)
        back.place(x=150, y=20)

        def prover_num2():

            global ok

            otv2_ = otv2.get()
            print("System (норма 7 (True)):", otv2_)

            if otv2_ == '7':
                y_or_n_num1["fg"] = "Green"
                y_or_n_num1["text"] = "Всё верно! Молодец!"
                ok = ok + 1
                root3.update()

                if ok == 3 or ok > 3:
                    y_or_n_num1["fg"] = 'Green'
                    y_or_n_num1["text"] = "Я тебя поздравляю, ты отлично выполнил задачку\n- на все 5 баллов!"
                    root3.update()
                    time.sleep(3)
                    game()
                elif ok < 3 and ok > 0:
                    y_or_n_num1["fg"] = 'Green'
                    y_or_n_num1["text"] = "Молодец, ты хорошо выполнил задание - 4."
                    root3.update()
                    time.sleep(3)
                    game()
                elif ok == 0:
                    y_or_n_num1["fg"] = 'orange'
                    y_or_n_num1["text"] = "Ты выполнил задание с потерями - 3."
                    root3.update()
                    time.sleep(3)
                    numbers()
                elif ok == -1 or -2 or -3 or -4 or -5 or -6 or -7 or -8 or -9 or -10 or ok < -10:
                    y_or_n_num1["fg"] = 'red'
                    y_or_n_num1["text"] = "Ты провалил задание - 2!"
                    root3.update()
                    time.sleep(3)
                    numbers()
                else:
                    print("System: error grade")

            else:
                y_or_n_num1["fg"] = "Red2"
                y_or_n_num1["text"] = "Неверно, попробуй снова!"
                ok = ok - 1

                print("system ok ==", ok)

        z2 = Label(root3, text="Ответ:", fg="Black", bg="white",
                   font="Bahnschrift 20")
        otv2 = Entry(root3, fg="Black", bg="white", font="Bahnschrift 20")
        provbutt = Button(root3, text="Проверить ответы", fg="Black", bg="white", border=1,
                          font="Bahnschrift 20", cursor="hand2", command=prover_num2)
        y_or_n_num1 = Label(root3, text="  ", fg="Black", bg="white", font="Bahnschrift 20")

        z2.place(x=500, y=550)
        otv2.place(x=630, y=550)
        provbutt.place(x=100, y=550)
        y_or_n_num1.place(x=400, y=610)

    def num2_2():

        global ok

        def on_closing_number22():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root2.destroy()

        root2 = Tk()
        root2.state('zoomed')
        root2.title("Юрок №2")
        root2.iconbitmap("icon2.ico")
        root2.protocol("WM_DELETE_WINDOW", on_closing_number22)
        root2["bg"] = "white"

        root2.image = PhotoImage(file="bg/BG4.png")
        back = Label(root2, image=root2.image, border=0)
        back.place(x=150, y=20)

        def prover_num2():

            global ok

            otv2_ = otv2.get()
            print("System (норма 4 (True)):", otv2_)

            if otv2_ == '4':
                y_or_n_num1["fg"] = "Green"
                y_or_n_num1["text"] = "Всё верно! Молодец!"
                ok = ok + 1
                root2.update()
                time.sleep(3)
                root2.destroy()
                num2_3()

            else:
                y_or_n_num1["fg"] = "Red2"
                y_or_n_num1["text"] = "Неверно, попробуй снова!"
                ok = ok - 1

        z2 = Label(root2, text="Ответ:", fg="Black", bg="white",
                   font="Bahnschrift 20")
        otv2 = Entry(root2, fg="Black", bg="white", font="Bahnschrift 20")
        provbutt = Button(root2, text="Проверить ответы", fg="Black", bg="white", border=1,
                          font="Bahnschrift 20", cursor="hand2", command=prover_num2)
        y_or_n_num1 = Label(root2, text="  ", fg="Black", bg="white", font="Bahnschrift 20")

        z2.place(x=500, y=500)
        otv2.place(x=630, y=500)
        provbutt.place(x=100, y=550)
        y_or_n_num1.place(x=400, y=550)

    global ok

    lev2.start()
    stop()

    def on_closing_number2():
        if messagebox.askokcancel("Выход из приложения",
                                  "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
            root1.destroy()

    root1 = Tk()
    root1.state('zoomed')
    root1.title("Юрок №2")
    root1.iconbitmap("icon2.ico")
    root1.protocol("WM_DELETE_WINDOW", on_closing_number2)
    root1["bg"] = "white"

    root1.image = PhotoImage(file="bg/BG3V2.png")
    back = Label(root1, image=root1.image, border=0)
    back.place(x=20, y=-80)

    def prover_num2():

        global ok

        otv2_ = otv2.get()
        print("System (норма 0 (True)):", otv2_)

        if otv2_ == '0':
            y_or_n_num1["fg"] = "Green"
            y_or_n_num1["text"] = "Всё верно! Молодец!"
            ok = ok + 1
            root1.update()
            time.sleep(3)
            root1.destroy()
            num2_2()
        else:
            y_or_n_num1["fg"] = "Red2"
            y_or_n_num1["text"] = "Неверно, попробуй снова!"
            ok = ok - 1

    z2 = Label(root1, text="Ответ:", fg="Black", bg="white",
               font="Bahnschrift 20")
    otv2 = Entry(root1, fg="Black", bg="white", font="Bahnschrift 20")
    provbutt = Button(root1, text="Проверить ответы", fg="Black", bg="white", border=1,
                      font="Bahnschrift 20", cursor="hand2", command=prover_num2)
    y_or_n_num1 = Label(root1, text="  ", fg="Black", bg="white", font="Bahnschrift 20")

    z2.place(x=500, y=450)
    otv2.place(x=630, y=450)
    provbutt.place(x=100, y=450)
    y_or_n_num1.place(x=450, y=500)


def number3():
    global global_roots
    global coden3
    coden3 = None
    stop()

    if global_root == True:
        global_root.destroy()

    elif global_root == False:
        pass

    lev3.start()

    def num3_3():
        global root7
        global coden3
        coden3 = True
        root4.destroy()

        def reset_num3():
            root7.destroy()
            number3()

        def on_closing_num3_3():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root7.destroy()

        root7 = Tk()
        root7.geometry("350x600")
        root7.title("Юрок №3")
        root7.iconbitmap("icon2.ico")
        root7.protocol("WM_DELETE_WINDOW", on_closing_num3_3)
        root7["bg"] = "white"

        root7.image = PhotoImage(file="bg/BG6_win2.png")
        back = Label(root7, image=root7.image, border=0)
        back.place(x=20, y=20)

        go = Button(root7, text='Открыть окно...', fg="Blue", bg="White",
                    border=0, font="Bahnschrift 20", cursor="hand2", command=reset_num3)
        go.place(x=50, y=545)

    def num3_2():
        root4.destroy()
        global root5
        global coden3
        coden3 = False

        def on_closing_num3_2():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root5.destroy()

        root5 = Tk()
        root5.state('zoomed')
        root5.title("Юрок №3")
        root5.iconbitmap("icon2.ico")
        root5.protocol("WM_DELETE_WINDOW", on_closing_num3_2)
        root5["bg"] = "white"

        root5.image = PhotoImage(file="bg/BG7.png")
        back2 = Label(root5, image=root5.image, border=0)
        back2.place(x=20, y=20)

        text2 = Label(root5, text="Открой IDLE Python и на основе прошлого кода сделай квадрат в 2 раза больше!",
                      fg="Black", bg="White", font="Bahnschrift 20")
        next_lession = Button(root5, text='Я решил!', fg="Black", bg="White",
                              border=0, font="Bahnschrift 20", cursor="hand2", command=game)
        next_lession.place(x=30, y=610)
        text2.place(x=30, y=570)

    def on_closing_num3():
        if messagebox.askokcancel("Выход из приложения",
                                  "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
            root4.destroy()

    root4 = Tk()
    root4.state('zoomed')
    root4.title("Юрок №3")
    root4.iconbitmap("icon2.ico")
    root4.protocol("WM_DELETE_WINDOW", on_closing_num3)
    root4["bg"] = "white"

    root4.image = PhotoImage(file="bg/BG6.png")
    back = Label(root4, image=root4.image, border=0)
    back.place(x=20, y=20)

    go = Button(root4, text='Далее...', fg="Blue", bg="White",
                border=0, font="Bahnschrift 20", cursor="hand2", command=num3_2)
    go2 = Button(root4, text='Открыть код...', fg="Blue", bg="White",
                 border=0, font="Bahnschrift 20", cursor="hand2", command=num3_3)
    text1 = Label(root4, text="Открой IDLE Python, введи код и посмотри, что вышло!", fg="Black", bg="White",
                  font="Bahnschrift 20")

    go.place(x=850, y=545)
    go2.place(x=850, y=595)
    text1.place(x=30, y=550)


def number4():
    global global_roots
    global code
    global root8
    code = False

    stop()

    if global_root == True:
        global_root.destroy()

    elif global_root == False:
        pass

    lev4.start()

    def on_closing_num4():
        if messagebox.askokcancel("Выход из приложения",
                                  "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
            root8.destroy()

    def num4_2():
        global code
        global root9
        root8.destroy()

        def reset_num4():
            root9.destroy()
            number4()

        def on_closing_num4_2():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root9.destroy()

        root9 = Tk()
        root9.geometry('500x700')
        root9.title("Юрок №4")
        root9.iconbitmap("icon2.ico")
        root9.protocol("WM_DELETE_WINDOW", on_closing_num4_2)
        root9["bg"] = "white"

        root9.image = PhotoImage(file="bg/BG9.png")
        back = Label(root9, image=root9.image, border=0)
        back.place(x=20, y=20)

        go = Button(root9, text='Открыть окно...', fg="Blue", bg="White",
                    border=0, font="Bahnschrift 20", cursor="hand2", command=reset_num4)

        go.place(x=50, y=545)
        code = True

    root8 = Tk()
    root8.state('zoomed')
    root8.title("Юрок №4")
    root8.iconbitmap("icon2.ico")
    root8.protocol("WM_DELETE_WINDOW", on_closing_num4)
    root8["bg"] = "white"

    root8.image = PhotoImage(file="bg/BG8.png")
    back = Label(root8, image=root8.image, border=0)
    back.place(x=20, y=20)

    go = Button(root8, text='Открыть код...', fg="Blue", bg="White",
                border=0, font="Bahnschrift 20", cursor="hand2", command=num4_2)
    next_lession = Button(root8, text='Я решил!', fg="Black", bg="White",
                          border=0, font="Bahnschrift 20", cursor="hand2", command=game)

    text1 = Label(root8, text="Открой IDLE Python, сделай синий прямоугольник 70 на 50", fg="Black", bg="White",
                  font="Bahnschrift 20")

    go.place(x=850, y=545)
    next_lession.place(x=30, y=600)
    text1.place(x=30, y=550)


def number5():
    global global_roots
    global ok

    stop()

    if global_root == True:
        global_root.destroy()

    elif global_root == False:
        pass

    lev5.start()

    def on_closing_num5():
        if messagebox.askokcancel("Выход из приложения",
                                  "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
            root10.destroy()

    def num5_2():
        global ok

        def yes():
            global ok
            ok = ok + 1
            otv["fg"] = "green"
            otv["text"] = "Всё верно! Молодец!"
            go["fg"] = "red"
            go2["fg"] = "green"
            go3["fg"] = "red"
            root7.update()
            time.sleep(3)
            num5_3()

        def no():
            global ok
            ok = ok - 1
            otv['fg'] = "red"
            otv["text"] = "Неверно, попробуй снова!"

        root10.destroy()

        def num5_3():

            def num5_4():
                global root12
                root11.destroy()

                global ok

                def yes():
                    global ok
                    ok = ok + 1
                    otv["fg"] = "green"
                    otv["text"] = "Всё верно! Молодец!"
                    go["fg"] = "red"
                    go2["fg"] = "red"
                    go3["fg"] = "green"
                    root12.update()
                    time.sleep(3)
                    if ok == 3 or ok > 3:
                        otv["fg"] = 'green'
                        otv["text"] = "Я тебя поздравляю, ты отлично выполнил задачку\n- на все 5 баллов!"
                        root12.image = PhotoImage(file="bg/BG14.png")
                        back = Label(root12, image=root12.image, border=0)
                        back.place(x=20, y=20)
                        root12.update()
                        time.sleep(3)
                        game()
                    elif ok < 3 and ok > 0:
                        otv["fg"] = 'Green'
                        otv["text"] = "Молодец, ты хорошо выполнил задание - 4."
                        root12.image = PhotoImage(file="bg/BG14.png")
                        back = Label(root12, image=root12.image, border=0)
                        back.place(x=20, y=20)
                        root12.update()
                        time.sleep(3)
                        game()
                    elif ok == 0:
                        otv["fg"] = 'orange'
                        otv["text"] = "Ты выполнил задание с потерями - 3."
                        root12.image = PhotoImage(file="bg/BG15.png")
                        back = Label(root12, image=root12.image, border=0)
                        back.place(x=20, y=20)
                        root12.update()
                        time.sleep(3)
                        numbers()
                    elif ok == -1 or -2 or -3 or -4 or -5 or -6 or -7 or -8 or -9 or -10 or ok < -10:
                        otv["fg"] = 'red'
                        otv["text"] = "Ты провалил задание - 2!"
                        root12.image = PhotoImage(file="bg/BG15.png")
                        back = Label(root12, image=root12.image, border=0)
                        back.place(x=20, y=20)
                        root12.update()
                        time.sleep(3)
                        numbers()
                    else:
                        print("System: error grade")

                def no():
                    global ok
                    ok = ok - 1
                    otv['fg'] = "red"
                    otv["text"] = "Неверно, попробуй снова!"

                def on_closing_num5_4():
                    if messagebox.askokcancel("Выход из приложения",
                                              "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                        root12.destroy()

                root12 = Tk()
                root12.state('zoomed')
                root12.title("Юрок №5")
                root12.iconbitmap("icon2.ico")
                root12.protocol("WM_DELETE_WINDOW", on_closing_num5_4)
                root12["bg"] = "white"

                root12.image = PhotoImage(file="bg/BG13.png")
                back = Label(root12, image=root12.image, border=0)
                back.place(x=20, y=20)

                go = Button(root12, text='Текст для его вывода с помощью turtle', fg="Black", bg="White",
                            border=0, font="Bahnschrift 20", cursor="hand2", command=no)
                go2 = Button(root12, text='Кол-во пиксилей для перемещения черепашки вправо', fg="Black", bg="White",
                             border=0, font="Bahnschrift 20", cursor="hand2", command=no)
                go3 = Button(root12, text='Угол поворота черепашки', fg="Black", bg="White",
                             border=0, font="Bahnschrift 20", cursor="hand2", command=yes)

                otv = Label(root12, text=" ", fg="Black", bg="white", font="Bahnschrift 20")

                go.place(x=50, y=520)
                go2.place(x=50, y=570)
                go3.place(x=50, y=620)
                otv.place(x=700, y=520)

            root7.destroy()

            global ok

            def yes():
                global ok
                ok = ok + 1
                otv["fg"] = "green"
                otv["text"] = "Всё верно! Молодец!"
                go["fg"] = "red"
                go2["fg"] = "red"
                go3["fg"] = "green"
                root11.update()
                time.sleep(3)
                num5_4()

            def no():
                global ok
                ok = ok - 1
                otv['fg'] = "red"
                otv["text"] = "Неверно, попробуй снова!"

            def on_closing_num5_3():
                if messagebox.askokcancel("Выход из приложения",
                                          "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                    root11.destroy()

            root11 = Tk()
            root11.state('zoomed')
            root11.title("Юрок №5")
            root11.iconbitmap("icon2.ico")
            root11.protocol("WM_DELETE_WINDOW", on_closing_num5_3)
            root11["bg"] = "white"

            root11.image = PhotoImage(file="bg/BG12.png")
            back = Label(root11, image=root11.image, border=0)
            back.place(x=20, y=20)

            go = Button(root11, text='Для вывода картинки с помощью turtle', fg="Black", bg="White",
                        border=0, font="Bahnschrift 20", cursor="hand2", command=no)
            go2 = Button(root11, text='Для перемещения черепашки вправо', fg="Black", bg="White",
                         border=0, font="Bahnschrift 20", cursor="hand2", command=no)
            go3 = Button(root11, text='Для поворота черепашки', fg="Black", bg="White",
                         border=0, font="Bahnschrift 20", cursor="hand2", command=yes)

            otv = Label(root11, text=" ", fg="Black", bg="white", font="Bahnschrift 20")

            go.place(x=50, y=500)
            go2.place(x=50, y=550)
            go3.place(x=50, y=600)
            otv.place(x=700, y=500)

        def on_closing_num5_2():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root7.destroy()

        root7 = Tk()
        root7.state('zoomed')
        root7.title("Юрок №5")
        root7.iconbitmap("icon2.ico")
        root7.protocol("WM_DELETE_WINDOW", on_closing_num5_2)
        root7["bg"] = "white"

        root7.image = PhotoImage(file="bg/BG11.png")
        back = Label(root7, image=root7.image, border=0)
        back.place(x=20, y=20)

        go = Button(root7, text='Для вывода текста с помощью turtle', fg="Black", bg="White",
                    border=0, font="Bahnschrift 20", cursor="hand2", command=no)
        go2 = Button(root7, text='Для перемещения черепашки вперёд', fg="Black", bg="White",
                     border=0, font="Bahnschrift 20", cursor="hand2", command=yes)
        go3 = Button(root7, text='Для создания 2-й черепашки', fg="Black", bg="White",
                     border=0, font="Bahnschrift 20", cursor="hand2", command=no)

        otv = Label(root7, text=" ", fg="Black", bg="white", font="Bahnschrift 20")

        go.place(x=50, y=500)
        go2.place(x=50, y=550)
        go3.place(x=50, y=600)
        otv.place(x=700, y=500)

    root10 = Tk()
    root10.state('zoomed')
    root10.title("Юрок №5")
    root10.iconbitmap("icon2.ico")
    root10.protocol("WM_DELETE_WINDOW", on_closing_num5)
    root10["bg"] = "white"

    root10.image = PhotoImage(file="bg/BG10.png")
    back = Label(root10, image=root10.image, border=0)
    back.place(x=20, y=20)

    go = Button(root10, text='Начать тест...', fg="Blue", bg="White",
                border=0, font="Bahnschrift 20", cursor="hand2", command=num5_2)
    text1 = Label(root10, text="Реши тест по теме «turtle»", fg="Black", bg="White",
                  font="Bahnschrift 20")

    go.place(x=850, y=545)
    text1.place(x=30, y=550)


def number6():
    global global_roots
    win = None

    stop()

    lev6.start()

    def winner():
        global win
        global root15
        win = True

        def on_closing_num6_win():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root15.destroy()

        root15 = Tk()
        root15.state('zoomed')
        root15.title("Юрок №6")
        root15.iconbitmap("icon2.ico")
        root15.protocol("WM_DELETE_WINDOW", on_closing_num6_win)
        root15["bg"] = "White"
        root15.image = PhotoImage(file="bg/BG21.png")
        back = Label(root15, image=root15.image, border=0)
        back.place(x=20, y=20)
        game()

    def loser():
        global win
        global root16
        win = False

        def on_closing_num6_los():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root16.destroy()

        root16 = Tk()
        root16.state('zoomed')
        root16.title("Юрок №6")
        root16.iconbitmap("icon2.ico")
        root16.protocol("WM_DELETE_WINDOW", on_closing_num6_los)
        root16["bg"] = "Black"
        root16.image = PhotoImage(file="bg/BG20.png")
        back = Label(root16, image=root16.image, border=0)
        back.place(x=20, y=20)
        root16.update()
        time.sleep(3)
        numbers()

    def num6_4():

        global ok

        def on_closing_num6_3():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root13.destroy()

        root13 = Tk()
        root13.state('zoomed')
        root13.title("Юрок №6")
        root13.iconbitmap("icon2.ico")
        root13.protocol("WM_DELETE_WINDOW", on_closing_num6_3)
        root13["bg"] = "white"

        x = [1, 2, 4, 8]
        x1 = random.choice(x)
        x2 = x1 * 1024
        xl = f"{x1} петабайт = ? терабайт "

        root13.image = PhotoImage(file="bg/BG19.png")
        back = Label(root13, image=root13.image, border=0)
        back.place(x=20, y=20)

        text1 = Label(root13, text="Сколько это в терабайтах?", fg="Black", bg="white", font="Bahnschrift 20")
        xl_ = Label(root13, text=xl, fg="Black", bg="white", border=0, font="Bahnschrift 20")
        otv = Entry(root13, fg="Black", bg="white", font="Bahnschrift 20", width=5)
        gol = Label(root13, text="", fg="Black", bg="white", font="Bahnschrift 20")

        def prov_num6():
            global ok

            otv_ = int(otv.get())
            if isinstance(otv_, int):
                if otv_ == x2:
                    gol["fg"] = "green"
                    gol["text"] = "Молодец! Всё верно!"
                    ok = ok + 1
                    root13.update()
                    print("System: ok==", ok)
                    time.sleep(3)

                    if ok == 3 or ok > 3:
                        gol["fg"] = 'Green'
                        gol["text"] = "Я тебя поздравляю,\nты отлично выполнил задачку\n- на все 5 баллов!"
                        root13.update()
                        time.sleep(5)
                        root13.destroy()
                        winner()
                    elif ok < 3 and ok > 0:
                        gol["fg"] = 'Green'
                        gol["text"] = "Молодец, ты хорошо выполнил задание - 4."
                        root13.update()
                        time.sleep(5)
                        root13.destroy()
                        winner()
                    elif ok == 0:
                        gol["fg"] = 'orange'
                        gol["text"] = "Ты выполнил задание с потерями - 3."
                        time.sleep(5)
                        root13.destroy()
                        loser()
                    elif ok == -1 or -2 or -3 or -4 or -5 or -6 or -7 or -8 or -9 or -10 or ok < -10:
                        gol["fg"] = 'red'
                        gol["text"] = "Ты провалил задание - 2!"
                        time.sleep(5)
                        root13.destroy()
                        loser()
                    else:
                        print("System: error grade")
                else:
                    gol["fg"] = "red2"
                    gol["text"] = "Неверно! Error 404!"
                    ok = ok - 1
                    print("System: ok==", ok)

            elif isinstance(otv_, str):
                gol["fg"] = "red2"
                gol["text"] = "Неверно! Ты ввёл не число!"
                ok = ok - 1
                print("System: ok==", ok)
            else:
                pass

        prov = Button(root13, text="Проверить", fg="Black", bg="white", border=0, font="Bahnschrift 20", cursor="hand2",
                      command=prov_num6)

        text1.pack(side=TOP)
        prov.place(x=450, y=92)
        xl_.place(x=50, y=100)
        otv.place(x=373, y=100)
        gol.place(x=660, y=100)

    def num6_3():

        global ok

        def on_closing_num6_3():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root17.destroy()

        root17 = Tk()
        root17.geometry("1280x800")
        root17.title("Юрок №6")
        root17.iconbitmap("icon2.ico")
        root17.protocol("WM_DELETE_WINDOW", on_closing_num6_3)
        root17["bg"] = "white"

        x = [1024, 2048, 4096, 8192]
        x1 = random.choice(x)
        x2 = x1 // 1024
        xl = f"{x1} байт = ? килобайт "

        root17.image = PhotoImage(file="bg/BG17.png")
        back = Label(root17, image=root17.image, border=0)
        back.place(x=20, y=20)

        text1 = Label(root17, text="Сколько это в килобайтах?", fg="Black", bg="white", font="Bahnschrift 20")
        xl_ = Label(root17, text=xl, fg="Black", bg="white", border=0, font="Bahnschrift 20")
        otv = Entry(root17, fg="Black", bg="white", font="Bahnschrift 20", width=5)
        gol = Label(root17, text="", fg="Black", bg="white", font="Bahnschrift 20")

        def prov_num6():
            global ok

            otv_ = int(otv.get())
            if isinstance(otv_, int):
                if otv_ == x2:
                    gol["fg"] = "green"
                    gol["text"] = "Молодец! Всё верно!"
                    ok = ok + 1
                    root17.update()
                    print("System: ok==", ok)
                    time.sleep(3)
                    root17.destroy()
                    num6_4()
                else:
                    gol["fg"] = "red2"
                    gol["text"] = "Неверно! Error 404!"
                    ok = ok - 1
                    print("System: ok==", ok)
            elif isinstance(otv_, str):
                gol["fg"] = "red2"
                gol["text"] = "Неверно! Ты ввёл не число!"
                ok = ok - 1
            else:
                pass

        prov = Button(root17, text="Проверить", fg="Black", bg="white", border=0, font="Bahnschrift 20", cursor="hand2",
                      command=prov_num6)

        text1.pack(side=TOP)
        prov.place(x=420, y=92)
        xl_.place(x=50, y=100)
        otv.place(x=343, y=100)
        gol.place(x=630, y=100)

    def num6_2():

        root19.destroy()

        global ok

        def on_closing_num6_2():
            if messagebox.askokcancel("Выход из приложения",
                                      "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                root18.destroy()

        root18 = Tk()
        root18.state('zoomed')
        root18.title("Юрок №6")
        root18.iconbitmap("icon2.ico")
        root18.protocol("WM_DELETE_WINDOW", on_closing_num6_2)
        root18["bg"] = "white"

        x = [8, 16, 32, 64, 128, 256, 512, 1024, 2048]
        x1 = random.choice(x)
        x2 = x1 // 8
        xl = f"{x1} бит = ? байт "

        root18.image = PhotoImage(file="bg/BG18.png")
        back = Label(root18, image=root18.image, border=0)
        back.place(x=20, y=20)

        text1 = Label(root18, text="Сколько это в байтах?", fg="Black", bg="white", font="Bahnschrift 20")
        xl_ = Label(root18, text=xl, fg="Black", bg="white", border=0, font="Bahnschrift 20")
        otv = Entry(root18, fg="Black", bg="white", font="Bahnschrift 20", width=5)
        gol = Label(root18, text="", fg="Black", bg="white", font="Bahnschrift 20")

        def prov_num6():
            global ok
            otv_ = int(otv.get())
            if isinstance(otv_, int):
                if otv_ == x2:
                    gol["fg"] = "green"
                    gol["text"] = "Молодец! Всё верно!"
                    ok = ok + 1
                    root18.update()
                    print("System: ok==", ok)
                    time.sleep(3)
                    root18.destroy()
                    num6_3()
                else:
                    gol["fg"] = "red2"
                    gol["text"] = "Неверно! Error 404!"
                    ok = ok - 1
                    print("System: ok==", ok)
            elif isinstance(otv_, str):
                gol["fg"] = "red2"
                gol["text"] = "Неверно! Ты ввёл не число!"
                ok = ok - 1
            else:
                pass

        prov = Button(root18, text="Проверить", fg="Black", bg="white", border=0, font="Bahnschrift 20", cursor="hand2",
                      command=prov_num6)

        text1.pack(side=TOP)
        prov.place(x=360, y=142)
        xl_.place(x=50, y=150)
        otv.place(x=283, y=150)
        gol.place(x=520, y=150)

    def on_closing_num6():
        if messagebox.askokcancel("Выход из приложения",
                                  "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
            root19.destroy()

    root19 = Tk()
    root19.state('zoomed')
    root19.title("Юрок №6")
    root19.iconbitmap("icon2.ico")
    root19.protocol("WM_DELETE_WINDOW", on_closing_num6)
    root19["bg"] = "white"

    root19.image = PhotoImage(file="bg/BG16.png")
    back = Label(root19, image=root19.image, border=0)
    back.place(x=20, y=20)

    go = Button(root19, text='Начать...', fg="Blue", bg="White",
                border=0, font="Bahnschrift 24", cursor="hand2", command=num6_2)

    go.place(x=850, y=545)


def number7():
    lev7.start()
    stop()
    global root20

    def prover_num7():  # проверка номера 7/examination number 7
        global ok

        otv = otv2.get()
        print("System (норма ждавбег (True)):", otv.lower())

        if otv.lower() == 'ждавбег':
            y_or_n_num1["fg"] = "Green"
            y_or_n_num1["text"] = "Всё верно! Молодец!"
            root20.update()
            time.sleep(3)
            ok = ok + 2

            if ok >= 2:
                y_or_n_num1['fg'] = 'Green'
                y_or_n_num1['text'] = "Я тебя поздравляю, ты отлично выполнил задачку\n- на все 5 баллов!"
                root20.update()
                time.sleep(3)
                game()
            elif ok >= 0 and ok < 2:
                y_or_n_num1['fg'] = 'Green'
                y_or_n_num1['text'] = "Молодец, ты хорошо выполнил задание - 4."
                root20.update()
                time.sleep(3)
                game()
            elif ok < 0 and ok > -5:
                y_or_n_num1['fg'] = 'DarkOrange2'
                y_or_n_num1['text'] = "Ты выполнил задание с потерями - 3."
                root20.update()
                time.sleep(3)
                numbers()
            elif ok <= -4:
                y_or_n_num1['fg'] = 'Red2'
                y_or_n_num1['text'] = "Ты провалил задание - 2!"
                root20.update()
                time.sleep(3)
                numbers()
            else:
                print("system: error grade")

        else:
            y_or_n_num1["fg"] = "Red2"
            y_or_n_num1["text"] = "Неверно, попробуй снова!"
            ok = ok - 2
            print("system ok==", ok)

    global ok

    def on_closing_number7():
        if messagebox.askokcancel("Выход из приложения",
                                  "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
            root20.destroy()

    root20 = Tk()
    root20.state('zoomed')
    root20.title("Юрок №7")
    root20.iconbitmap("icon2.ico")
    root20.protocol("WM_DELETE_WINDOW", on_closing_number7)
    root20["bg"] = "white"

    root20.image = PhotoImage(file="bg/BG22.png")
    back = Label(root20, image=root20.image, border=0)
    back.place(x=150, y=20)

    z2 = Label(root20, text="Напиши верную кодировку (писать слитно): ", fg="Black", bg="white",
               font="Bahnschrift 20")
    otv2 = Entry(root20, fg="Black", bg="white", font="Bahnschrift 20")
    provbutt = Button(root20, text="Проверить ответы", fg="Black", bg="white", border=1,
                      font="Bahnschrift 20", cursor="hand2", command=prover_num7)
    y_or_n_num1 = Label(root20, text="  ", fg="Black", bg="white", font="Bahnschrift 20")

    z2.place(x=100, y=500)
    otv2.place(x=660, y=505)
    provbutt.place(x=100, y=550)
    y_or_n_num1.place(x=400, y=550)


def else_number():
    else_number_l.start()

    class Data:
        def __init__(self, true_otv, bg, comment):
            self.true_otv = true_otv
            self.bg = bg
            self.comment = comment
            print(f'Open: true: {self.true_otv}, bg: {self.bg}, comment: {self.comment}\n')

    def open_data():

        def number():
            """Запуск задачки по нашим данным"""
            global data
            global_root.destroy()
            app_settings_else.destroy()

            def proverka_():
                global ok
                otv = otv_entry.get()
                print(f"System норма {data.true_otv} (True):")

                if otv.lower() == data.true_otv:
                    l_ok["fg"] = "Green"
                    l_ok["text"] = "Всё верно! Молодец!"
                    gui.update()
                    time.sleep(3)
                    ok += 2

                    if ok >= 2:
                        l_ok['fg'] = 'Green'
                        l_ok['text'] = "Я тебя поздравляю, ты отлично выполнил задачку\n- на все 5 баллов!"
                        gui.update()
                        time.sleep(3)
                        game()
                    elif ok >= 0 and ok < 2:
                        l_ok['fg'] = 'Green'
                        l_ok['text'] = "Молодец, ты хорошо выполнил задание - 4."
                        gui.update()
                        time.sleep(3)
                        game()
                    elif ok < 0 and ok > -5:
                        l_ok['fg'] = 'DarkOrange2'
                        l_ok['text'] = "Ты выполнил задание с потерями - 3."
                        gui.update()
                        time.sleep(3)
                        numbers()
                    elif ok <= -4:
                        l_ok['fg'] = 'Red2'
                        l_ok['text'] = "Ты провалил задание - 2!"
                        gui.update()
                        time.sleep(3)
                        numbers()
                    else:
                        print("system: error grade")
                else:
                    l_ok["fg"] = "Red2"
                    l_ok["text"] = "Неверно, попробуй снова!"
                    ok = ok - 2
                    print("system ok==", ok)

            def on_closing_else_num():
                if messagebox.askokcancel("Выход из приложения",
                                          "Вы точно хотите выйти из приложения?\nВесь прогресс будет утерян!"):
                    gui.destroy()

            global gui
            gui = Tk()
            gui.geometry('1280x720')
            gui.title("Юрок")
            gui.iconbitmap("icon2.ico")
            gui.protocol("WM_DELETE_WINDOW", on_closing_else_num)
            gui["bg"] = "white"
            global data
            background = PhotoImage(file=data.bg)
            background_label = Label(gui, image=background, border=0)
            comment_label = Label(gui, text=data.comment, fg="Black", bg="white", font="Bahnschrift 20")
            l_ok = Label(gui, text='', fg="Black", bg="white", font="Bahnschrift 20")
            proverka = Button(gui, text='Проверить ответ', bg='white', font="Bahnschrift 20", command=proverka_)
            otv_entry = Entry(gui, font="Bahnschrift 20")

            background_label.pack(anchor='nw')
            comment_label.place(x=20, y=500)
            otv_entry.place(x=680, y=500)
            proverka.place(x=1000, y=500)
            l_ok.place(x=20, y=550)

            gui.mainloop()

        try:
            if e1.get().replace(" ", "") != '':
                # for true
                true_txt = open(f'{e1.get()}/true.txt', 'r')
                true = true_txt.read()
                true_txt.close()
                # background
                bg_photo_txt = open(f'{e1.get()}/bg.txt', 'r')
                bg_photo = bg_photo_txt.read()
                bg_photo_txt.close()
                # comment
                comment_txt = open(f'{e1.get()}/comment.txt', 'r')
                comment_ = comment_txt.read()
                comment_txt.close()
                global data
                data = Data(true_otv=true, bg=bg_photo, comment=comment_)
                print(data.true_otv, data.bg, data.comment, 'end')

                number()
            else:
                l_error['text'] = 'Введи путь в поле ввода!'

        except:
            l_error['text'] = 'Ты ввёл неверно!\nВводи без кавычек'

    app_settings_else = Tk()
    app_settings_else.geometry('1000x500')
    app_settings_else.title("Выбор задачки")
    app_settings_else.iconbitmap("icon2.ico")
    app_settings_else["bg"] = "white"

    l_main = Label(app_settings_else, text='Спроси у учителя данные\nдля задачки и впиши их\n'
                                           '(вставка работает только при анг. раскладке)',
                   bg='White', font='Bahnschrift 24')
    l1 = Label(app_settings_else, text='Путь к папке (Пример: C:/Desktop/...):', bg='White', font='Bahnschrift 20')
    l_error = Label(app_settings_else, text='', bg='White', fg='Red', font='Bahnschrift 20')
    e1 = Entry(app_settings_else, font='Bahnschrift 20')
    b1 = Button(app_settings_else, text='Открыть', border=0, fg='Blue', bg='White',
                font='Bahnschrift 20', command=open_data)
    l_main.pack()
    l1.place(x=20, y=150)
    e1.place(x=510, y=150)
    b1.pack(side='bottom')
    l_error.place(x=20, y=220)
    app_settings_else.minsize(width=800, height=320)
    app_settings_else.mainloop()


# кнопки в начальном окне(global_root)/buttoms to global_root
n1 = Button(global_root, text="Задачка №1 - Интересные треугольники", fg="Black", bg="white",
            border=0, font="Bahnschrift 20", cursor="hand2", command=number1)
n2 = Button(global_root, text="Задачка №2 - Помоги Генералу Гавсу отгадать загадки", fg="Black", bg="white",
            border=0, font="Bahnschrift 20", cursor="hand2", command=number2)
n3 = Button(global_root, text="Задачка №3 - Turtle", fg="Black", bg="white",
            border=0, font="Bahnschrift 20", cursor="hand2", command=number3)
n4 = Button(global_root, text="Задачка №4 - Снова треугольники", fg="Black", bg="white",
            border=0, font="Bahnschrift 20", cursor="hand2", command=number4)
n5 = Button(global_root, text="Задачка №5 - Тест на знание turtle", fg="Black", bg="white",
            border=0, font="Bahnschrift 20", cursor="hand2", command=number5)
n6 = Button(global_root, text="Задачка №6 - Биты, байты и т.п.", fg="Black", bg="white",
            border=0, font="Bahnschrift 20", cursor="hand2", command=number6)
n7 = Button(global_root, text="Задачка №7 - Задачка для мамкиных хацкеров", fg="Black", bg="white",
            border=0, font="Bahnschrift 20", cursor="hand2", command=number7)
n_else = Button(global_root, text="Выбрать другую", fg="Black", bg="white",
                border=0, font="Bahnschrift 20", cursor="hand2", command=else_number)
instruction_button = Button(global_root, text="Инструкция", fg="Black", bg="White",
                            border=0, font="Bahnschrift 24", cursor="hand2", command=instruction)

img_for_sch102 = PhotoImage(file='bg/sch102_logo.png')
# размещение картинки: compound= bottom, center, left, none, right, or top
sch102 = Button(global_root, text='Открыть сайт\nшколы', image=img_for_sch102, compound='left', fg="Black", bg="white",
                border=0, font="Bahnschrift 20", cursor="hand2", command=site_school102)

yir.place(x=20, y=20)
yir2.place(x=160, y=45)
n1.place(x=20, y=100)
n2.place(x=20, y=160)
n3.place(x=20, y=220)
n4.place(x=20, y=280)
n5.place(x=20, y=340)
n6.place(x=20, y=400)
n7.place(x=20, y=460)
n_else.place(x=20, y=520)
instruction_button.place(x=1020, y=200)
sch102.place(x=900, y=70)
global_root.mainloop()
