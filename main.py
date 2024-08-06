from tkinter import *
from tkinter import font as ft
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import pandas as pd
import os

w_home = Tk()
w_home.geometry("1280x720")
w_home.title("Graph painter")
w_home.iconbitmap("D:/python projects/graph painter/images/icons8_stocks.ico")
w_home.config(bg="#1F0058")
w_home.resizable(False, False)


# def Buttones-------------------------------------------------------------------------------------------
def close_all():
    w_home.destroy()
    w_painter.destroy()
    w_excle.destroy()
    w_circle.destroy()
    w_comp.destroy()


def show_painter():
    w_home.withdraw()
    w_excle.withdraw()
    w_circle.withdraw()
    w_comp.withdraw()

    w_painter.deiconify()
    w_painter.mainloop()


def show_w_excle():
    w_home.withdraw()
    w_painter.withdraw()
    w_circle.withdraw()
    w_comp.withdraw()

    w_excle.deiconify()
    w_excle.mainloop()


def show_home():
    w_excle.withdraw()
    w_painter.withdraw()
    w_circle.withdraw()
    w_comp.withdraw()

    w_home.deiconify()


def show_circle():
    w_home.withdraw()
    w_painter.withdraw()
    w_excle.withdraw()
    w_comp.withdraw()

    w_circle.deiconify()
    w_circle.mainloop()


def show_comp():
    w_home.withdraw()
    w_painter.withdraw()
    w_excle.withdraw()
    w_circle.withdraw()

    w_comp.deiconify()


wh_frame = Frame(w_home, bg="white", width=640, height=720)
wh_frame.pack(side="right")

word1_lb = Label(wh_frame, text="Welcome to", bg="white", font=12, fg="black")
word1_lb.place(x=90, y=120)

title_size = ft.Font(size=30)

graph_lb = Label(wh_frame, text="Graph Painter!!", fg="#1F0058", bg="white", font=title_size)
graph_lb.place(x=190, y=100)

# image but1-----
image1 = Image.open("D:/python projects/graph painter/images/graph_painter.png")
image1_1 = image1.resize((250, 125))

photo1 = ImageTk.PhotoImage(image1_1)

# image but2-----
image2 = Image.open("D:/python projects/graph painter/images/excle_geaph.png")
image2_1 = image2.resize((250, 125))

photo2 = ImageTk.PhotoImage(image2_1)

painter_but = Button(wh_frame, text="print", bg="white", borderwidth=0)
painter_but.place(x=200, y=450)

# image but3------
image4 = Image.open("images/chart4.png")
image4_1 = image4.resize((250, 125))

photo8 = ImageTk.PhotoImage(image4_1)

w4_but = Button(w_home, image=photo8, bg="#1F0058", borderwidth=0, command=show_comp)
w4_but.place(x=210, y=450)

# close but-------
close_but1 = Button(w_home, text="X", bg="red", width=3, command=close_all)
close_but1.place(x=0, y=0)

# W_painterGraph------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
w_painter = Toplevel()
w_painter.geometry("1280x720")
w_painter.title("Painter Graph")
w_painter.state("withdrawn")
w_painter.iconbitmap("images/icons8_stocks.ico")
w_painter.config(bg="#1F0058")
w_painter.resizable(False, False)

# frame----------------------------------------------------------------------------------------------------------------------------------------------------------------
p_frame = Frame(w_painter, bg="white", width=320, height=720)
p_frame.pack(side="left")

x_frame = Frame(p_frame, bg="white", width=224, height=20)
x_frame.place(x=10, y=60)

x = []


def add():
    get_entry = enter_lb.get()
    x.append(get_entry)

    x_lb = Label(x_frame, text="x = " + str(x), bg="white", fg="black")
    x_lb.place(x=0, y=0)


def remove():
    x.pop()

    x_lb2 = Label(x_frame, bg="white", width=40)
    x_lb2.place(x=0, y=0)

    x_lb3 = Label(x_frame, text="x = " + str(x), bg="white", fg="dark gray")
    x_lb3.place(x=0, y=0)


word2_lb = Label(p_frame, text="Put the elements line x:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word2_lb.place(x=10, y=10)

enter_lb = Entry(w_painter, font=ft.Font(size=14), bg="#1F0058", fg="white")
enter_lb.place(x=10, y=30)

add_but = Button(p_frame, text="Add", bg="#8667BF", fg="white", width=4, command=add)
add_but.place(x=270, y=30)

remove_but = Button(p_frame, text="Del", bg="#8667BF", fg="white", width=4, command=remove)
remove_but.place(x=270, y=60)

# w_painter Button-------------------------------------------------------------------------------
painter_but = Button(wh_frame, image=photo1, bg="white", borderwidth=0, command=show_painter)
painter_but.place(x=200, y=300)
# -----------------------------------------------------------------------------------------------


y_frame = Frame(p_frame, bg="white", width=224, height=20)
y_frame.place(x=10, y=150)

y = []


def add2():
    get_entry = eval(entery_lb.get())
    y.append(get_entry)

    x2_lb = Label(y_frame, text="y = " + str(y), bg="white", fg="black")
    x2_lb.place(x=0, y=0)


def remove_y():
    y.pop()

    y_lb2 = Label(y_frame, bg="white", width=40)
    y_lb2.place(x=0, y=0)

    y_lb3 = Label(y_frame, text="y = " + str(y), bg="white", fg="dark gray")
    y_lb3.place(x=0, y=0)


word3_lb = Label(p_frame, text="Put the numbers line y:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word3_lb.place(x=10, y=100)

entery_lb = Entry(w_painter, font=ft.Font(size=14), bg="#1F0058", fg="white")
entery_lb.place(x=10, y=120)

add2_but = Button(p_frame, text="Add", bg="#8667BF", fg="white", width=4, command=add2)
add2_but.place(x=270, y=120)

removey_but = Button(p_frame, text="Del", bg="#8667BF", fg="white", width=4, command=remove_y)
removey_but.place(x=270, y=150)

# title entry ---------------------------------------
word4_lb = Label(p_frame, text="Enter the title:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word4_lb.place(x=10, y=190)

plot_en_title = Entry(p_frame, font=ft.Font(size=14), bg="#1F0058", fg="white")
plot_en_title.place(x=10, y=210)

# x label entry ---------------------------------------
word5_lb = Label(p_frame, text="Enter the x label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word5_lb.place(x=10, y=250)

x_en_lb = Entry(p_frame, font=ft.Font(size=14), bg="#1F0058", fg="white")
x_en_lb.place(x=10, y=270)

# y label entry ---------------------------------------
word6_lb = Label(p_frame, text="Enter the y label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word6_lb.place(x=10, y=310)

y_en_lb = Entry(p_frame, font=ft.Font(size=14), bg="#1F0058", fg="white")
y_en_lb.place(x=10, y=330)

# line label --- ---------------------------------------
word7_lb = Label(p_frame, text="Enter the line or bar label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word7_lb.place(x=10, y=370)

line_en_lb = Entry(p_frame, font=ft.Font(size=14), bg="#1F0058", fg="white")
line_en_lb.place(x=10, y=390)

# line label --- ---------------------------------------
word8_lb = Label(p_frame, text="do you want grid on the graph?", bg="white", fg="#1F0058", font=ft.Font(size=10))
word8_lb.place(x=10, y=430)

cmbol = ttk.Combobox(p_frame,
                     value=("Yes", "No"), width=33, state='readonly')
cmbol.place(x=10, y=450)

# plot color -------------------------------------------
word8_lb = Label(p_frame, text="line color", bg="white", fg="#1F0058", font=ft.Font(size=10))
word8_lb.place(x=10, y=490)

cmbol2 = ttk.Combobox(p_frame,
                      value=("red", "blue", "yellow", "green", "black", "orange"), width=33, state='readonly')
cmbol2.place(x=10, y=510)

# plot or bar --------------------------------------
word9_lb = Label(p_frame, text="type of the Graph:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word9_lb.place(x=10, y=550)

comb_bar_plot = ttk.Combobox(p_frame,
                             values=("bar", "plot"), width=33, state='readonly')
comb_bar_plot.place(x=10, y=570)


# draw the graph but -------------------------------------------------------------------------------------------------------------------------------------------------|

def draw():
    if len(x) == len(y):

        plt.title(plot_en_title.get())
        plt.xlabel(x_en_lb.get())
        plt.ylabel(y_en_lb.get())
        line_get = line_en_lb.get()

        line_color = cmbol2.get()

        if comb_bar_plot.get() == "plot":
            plt.plot(x, y, linewidth=5, marker="o", color=line_color, linestyle="--", label=line_get)

        elif comb_bar_plot.get() == "bar":
            plt.bar(x, y, color=line_color, label=line_get)

        else:
            error2_lb = Label(w_painter, text="Error: pleas chose one of the options in the graph type.", bg="#1F0058",
                              fg="white")
            error2_lb.place(x=700, y=400)

        if cmbol.get() == "Yes":
            plt.grid()
        elif cmbol.get() == "No":
            pass

        plt.legend()
        plt.show()
    else:
        error_lb = Label(w_painter,
                         text="Error: x elements must be equale y elements \n for example: x = [1,2,3]  and y = [A,B,C]",
                         bg="#1F0058", fg="white")
        error_lb.place(x=700, y=400)


back_but = Button(w_painter, text="Back to home", bg="white", fg="#1F0058", command=show_home)
back_but.place(x=1195, y=0)

image3 = Image.open("D:/python projects/program first/images/2graph-q.png")
image3_1 = image3.resize((250, 125))

photo3 = ImageTk.PhotoImage(image3_1)

draw_but = Button(w_painter, image=photo3, borderwidth=0, bg="#1F0058", command=draw)
draw_but.place(x=700, y=300)

# window excel--------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------
w_excle = Toplevel()
w_excle.geometry("1280x720")
w_excle.title("Excle Painter")
w_excle.state("withdrawn")
w_excle.iconbitmap("images/icons8_stocks.ico")
w_excle.config(bg="#1F0058")
w_excle.resizable(False, False)

w_excle.protocol("WM_DELET_WINDOW", close_all)
w_home.protocol("WM_DELET_WINDOW", close_all)
w_painter.protocol("WM_DELET_WINDOW", close_all)

data = None


# def commandes ---------
def open_excle():
    global data

    filepath = filedialog.askopenfilename(initialdir="/", title="Select Excel File",
                                          filetypes=(("Excel files", "*.xlsx;*.xls"), ("All files", "*.*")))

    if filepath:

        filename = os.path.basename(filepath)

        xl = pd.ExcelFile(filepath)
        sheet_names = xl.sheet_names

        lb_empty1 = Label(E_frame, bg="white", width=40, font=ft.Font(size=20))
        lb_empty1.place(x=200, y=2)

        lb_fileEn = Label(E_frame, text=filename, bg="white", fg="green", font=ft.Font(size=15))
        lb_fileEn.place(x=170, y=8)

        for i in sheet_names:
            lb_sheet_name = Label(sheet_frame, text=str(i), bg="light green", fg="dark green", font=ft.Font(size=13))
            lb_sheet_name.pack(side="bottom")

        data = pd.read_excel(filepath)


# button win excle --------------------------------------------------------------------------------------
painter_but = Button(wh_frame, image=photo2, bg="white", borderwidth=0, command=show_w_excle)
painter_but.place(x=200, y=450)
# -------------------------------------------------------------------------------------------------------

# back button ----------
back_but = Button(w_excle, text="Back to home", bg="white", fg="#1F0058", command=show_home)
back_but.place(x=1195, y=0)

# win excle frame ----------------
E_frame = Frame(w_excle, bg="white", width=1280, height=460)
E_frame.pack(side="bottom")

# excle information--------------
lb_filename = Label(E_frame, text="File   name  :", bg="white", font=ft.Font(size=20))
lb_filename.place(x=2, y=2)

sheet_frame = Frame(E_frame, bg="light green", width=100, height=200)
sheet_frame.place(x=0, y=130)

lb_sheet = Label(sheet_frame, text="Sheet names:", bg="light green", fg="black", font=ft.Font(size=18))
lb_sheet.pack(side="top")

# Entry sheet name =============
sheet_En = Entry(E_frame, bg="light green", font=ft.Font(size=20))
sheet_En.place(x=960, y=25)

sheet_word = Label(E_frame, text="Enter the sheet name:", bg="white", fg="black")
sheet_word.place(x=960, y=0)

# Entry x value ===============
x_valu_En = Entry(E_frame, bg="#1F0058", fg="white", font=ft.Font(size=20))
x_valu_En.place(x=960, y=100)

x_valu_lb = Label(E_frame, text="Enter X values from list in excle:", bg="white")
x_valu_lb.place(x=960, y=75)

# Entry y value =============
y_valu_En = Entry(E_frame, bg="#1F0058", fg="white", font=ft.Font(size=20))
y_valu_En.place(x=960, y=175)

y_valu_lb = Label(E_frame, text="Enter Y values from list in excle:", bg="white")
y_valu_lb.place(x=960, y=150)

# compobox bar plot =========
graph_kind = ttk.Combobox(E_frame, values=("plot", "bar"), font=ft.Font(size=19), state="readonly")
graph_kind.place(x=960, y=250)

kind_lb = Label(E_frame, text="Graph type:", bg="white")
kind_lb.place(x=960, y=225)

# combobox color ============
comb_color = ttk.Combobox(E_frame, values=("red", "blue", "Yellow", "black", "green", "pink"), font=ft.Font(size=19),
                          state="readonly")
comb_color.place(x=960, y=325)

lb_comb = Label(E_frame, text="Select the color", bg="white")
lb_comb.place(x=960, y=300)

# open excle folder button ---------
image4 = Image.open("images/EXL.png")
image4_1 = image4.resize((250, 125))

photo4 = ImageTk.PhotoImage(image4_1)

open_but = Button(E_frame, image=photo4, borderwidth=0, bg="white", command=open_excle)
open_but.place(x=525, y=100)


def print_Excle():
    x_values = list(data[x_valu_En.get()])
    y_values = list(data[y_valu_En.get()])

    if graph_kind.get() == "plot":
        plt.plot(x_values, y_values, color=comb_color.get(), marker="o", linestyle="--")

        plt.grid()

        plt.show()
    else:
        plt.bar(x_values, y_values, color=comb_color.get())

        plt.grid()

        plt.show()


# open excle folder button ---------
#image5 = Image.open("images/Draw_Graph2.png")=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/
#image5_1 = image5.resize((250, 125)) =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=

#photo5 = ImageTk.PhotoImage(image5_1)=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=

draw_but2 = Button(w_excle, text="Start Graph!!", borderwidth=0, command=print_Excle, bg="#1F0058", background="white",font=("", 30))
draw_but2.place(x=520, y=60)

# windo circle =================================================================================================================================================================================


image6 = Image.open("images/circle_i.png")
image6_1 = image6.resize((250, 125))

photo6 = ImageTk.PhotoImage(image6_1)

w_circle = Toplevel()
w_circle.geometry("1280x720")
w_circle.title("Circle Graph")
w_circle.state("withdrawn")
w_circle.config(bg="#1F0058")
w_circle.resizable(False, False)
w_circle.iconbitmap("images/icons8_stocks.ico")

# show windo circle but---------------------------------------------------------------------
circle_but = Button(w_home, image= photo6, borderwidth=0, bg="#1F0058", command=show_circle)
circle_but.place(x=210, y=300)
# ------------------------------------------------------------------------------------------

# frames -------------------------------
f_circle = Frame(w_circle, bg="white", height=720, width=640)
f_circle.pack(side="left")

f_circle2 = Frame(f_circle, bg="black", height=720, width=320)
f_circle2.place(x=0, y=0)

# back but ---------------------
back_but = Button(w_circle, text="Back to home", bg="white", fg="#1F0058", command=show_home)
back_but.place(x=1195, y=0)

lab = []


def add3():
    get_entry = labels_En.get()
    lab.append(get_entry)

    x_lb = Label(f_circle, text="labels = " + str(lab), bg="white", fg="black")
    x_lb.place(x=325, y=25)


def remove3():
    lab.pop()

    x_lb2 = Label(f_circle, bg="white", width=50)
    x_lb2.place(x=325, y=25)

    x_lb3 = Label(f_circle, text="labels = " + str(lab), bg="white", fg="dark gray")
    x_lb3.place(x=325, y=25)


# Labels Entery and buttons --------------------------------------------------------------------
# Entry
word_labels = Label(f_circle2, text="Enter the labels:", bg="black", fg="white")
word_labels.place(x=10, y=5)

labels_En = Entry(f_circle2, font=ft.Font(size=15))
labels_En.place(x=10, y=25)

# buttons --
add3_but = Button(f_circle2, text="Add", bg="#8667BF", fg="white", width=4, command=add3)
add3_but.place(x=270, y=10)

remove3_but = Button(f_circle2, text="Del", bg="#8667BF", fg="white", width=4, command=remove3)
remove3_but.place(x=270, y=40)

pr = []


def add4():
    get_entry = eval(pr_En.get())
    pr.append(get_entry)

    x_lb = Label(f_circle, text="percentage = " + str(pr), bg="white", fg="black")
    x_lb.place(x=325, y=85)


def remove4():
    pr.pop()

    x_lb2 = Label(f_circle, bg="white", width=50)
    x_lb2.place(x=325, y=85)

    x_lb3 = Label(f_circle, text="percentage = " + str(pr), bg="white", fg="dark gray")
    x_lb3.place(x=325, y=85)


# persent Entery and buttons --------------------------------------------------------------------
# Entry
word_pr = Label(f_circle2, text="Enter the percentage:", bg="black", fg="white")
word_pr.place(x=10, y=65)

pr_En = Entry(f_circle2, font=ft.Font(size=15))
pr_En.place(x=10, y=85)

# buttons --
add4_but = Button(f_circle2, text="Add", bg="#8667BF", fg="white", width=4, command=add4)
add4_but.place(x=270, y=80)

remove4_but = Button(f_circle2, text="Del", bg="#8667BF", fg="white", width=4, command=remove4)
remove4_but.place(x=270, y=110)

# title Entry-------------------
title_word = Label(f_circle2, text="Put the title:", bg="black", fg="white")
title_word.place(x=10, y=125)

title_En = Entry(f_circle2, font=ft.Font(size=15))
title_En.place(x=10, y=145)

# combobox chadow ------------
shadow_word = Label(f_circle2, text="Do you want shadwo?", bg="black", fg="white")
shadow_word.place(x=10, y=185)

comb_shadow = ttk.Combobox(f_circle, values=("Yes", "No"), state="readonly", font=ft.Font(size=14))
comb_shadow.place(x=10, y=205)

# combobox borders -----------
borders_word = Label(f_circle2, text="Do you want to draw borders?", bg="black", fg="white")
borders_word.place(x=10, y=245)

comb_borders = ttk.Combobox(f_circle, values=("Yes", "No"), state="readonly", font=ft.Font(size=14))
comb_borders.place(x=10, y=265)


def draw_pie():
    plt.title(title_En.get())

    if comb_shadow.get() == "Yes":
        tf = True
    else:
        tf = False

    if comb_borders.get() == "Yes":
        wedg = {'edgecolor': "black"}
    else:
        wedg = {'edgecolor': "white"}

    plt.pie(pr, labels=lab, shadow=tf, wedgeprops=wedg, autopct="%1.1f%%")

    plt.show()


# draw pie chart folder ---------
image7 = Image.open("images/pie_chart.png")
image7_1 = image7.resize((250, 125))

photo7 = ImageTk.PhotoImage(image7_1)

draw_but3 = Button(w_circle, image=photo7, borderwidth=0, command=draw_pie, bg="#1F0058")
draw_but3.place(x=850, y=260)

# windo comparison chart =================================================================================================================================================
w_comp = Toplevel()
w_comp.geometry("1280x720")
w_comp.title("Comparison Graph")
w_comp.state("withdrawn")
w_comp.iconbitmap("images/icons8_stocks.ico")
w_comp.config(bg="#1F0058")
w_comp.resizable(False, False)

back_but = Button(w_comp, text="Back to home", bg="white", fg="#1F0058", command=show_home)
back_but.place(x=1195, y=0)

# frame----------------------------------------------------------------------------------------------------------------------------------------------------------------
p_frame1 = Frame(w_comp, bg="white", width=320, height=720)
p_frame1.pack(side="left")

x_frame1 = Frame(p_frame1, bg="white", width=224, height=20)
x_frame1.place(x=10, y=60)

x01 = []


def addc():
    get_entryc = enter_lbc.get()
    x01.append(get_entryc)

    x_lbc = Label(x_frame1, text="x = " + str(x01), bg="white", fg="black")
    x_lbc.place(x=0, y=0)


def removec():
    x01.pop()

    x_lb2c = Label(x_frame1, bg="white", width=40)
    x_lb2c.place(x=0, y=0)

    x_lb3c = Label(x_frame1, text="x = " + str(x01), bg="white", fg="dark gray")
    x_lb3c.place(x=0, y=0)


word2_lbc = Label(p_frame1, text="Put the elements line x:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word2_lbc.place(x=10, y=10)

enter_lbc = Entry(p_frame1, font=ft.Font(size=14), bg="#1F0058", fg="white")
enter_lbc.place(x=10, y=30)

add_butc = Button(p_frame1, text="Add", bg="#8667BF", fg="white", width=4, command=addc)
add_butc.place(x=270, y=30)

remove_butc = Button(p_frame1, text="Del", bg="#8667BF", fg="white", width=4, command=removec)
remove_butc.place(x=270, y=60)

y_framec = Frame(p_frame1, bg="white", width=224, height=20)
y_framec.place(x=10, y=150)

y01 = []


def add2c():
    get_entryc = eval(entery_lbc.get())
    y01.append(get_entryc)

    x2_lbc = Label(y_framec, text="y = " + str(y01), bg="white", fg="black")
    x2_lbc.place(x=0, y=0)


def remove_yc():
    y01.pop()

    y_lb2c = Label(y_framec, bg="white", width=40)
    y_lb2c.place(x=0, y=0)

    y_lb3c = Label(y_framec, text="y = " + str(y01), bg="white", fg="dark gray")
    y_lb3c.place(x=0, y=0)


word3_lbc = Label(p_frame1, text="Put the numbers line y:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word3_lbc.place(x=10, y=100)

entery_lbc = Entry(w_comp, font=ft.Font(size=14), bg="#1F0058", fg="white")
entery_lbc.place(x=10, y=120)

add2_butc = Button(p_frame1, text="Add", bg="#8667BF", fg="white", width=4, command=add2c)
add2_butc.place(x=270, y=120)

removey_butc = Button(p_frame1, text="Del", bg="#8667BF", fg="white", width=4, command=remove_yc)
removey_butc.place(x=270, y=150)

# title entry ---------------------------------------
word4_lbc = Label(p_frame1, text="Enter the title:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word4_lbc.place(x=10, y=190)

plot_en_titlec = Entry(p_frame1, font=ft.Font(size=14), bg="#1F0058", fg="white")
plot_en_titlec.place(x=10, y=210)

# x label entry ---------------------------------------
word5_lbc = Label(p_frame1, text="Enter the x label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word5_lbc.place(x=10, y=250)

x_en_lbc = Entry(p_frame1, font=ft.Font(size=14), bg="#1F0058", fg="white")
x_en_lbc.place(x=10, y=270)

# y label entry ---------------------------------------
word6_lbc = Label(p_frame1, text="Enter the y label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word6_lbc.place(x=10, y=310)

y_en_lbc = Entry(p_frame1, font=ft.Font(size=14), bg="#1F0058", fg="white")
y_en_lbc.place(x=10, y=330)

# line label --- ---------------------------------------
word7_lbc = Label(p_frame1, text="Enter the line or bar label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word7_lbc.place(x=10, y=370)

line_en_lbc = Entry(p_frame1, font=ft.Font(size=14), bg="#1F0058", fg="white")
line_en_lbc.place(x=10, y=390)

# line label --- ---------------------------------------
word8_lbc = Label(p_frame1, text="do you want grid on the graph?", bg="white", fg="#1F0058", font=ft.Font(size=10))
word8_lbc.place(x=10, y=430)

cmbolc = ttk.Combobox(p_frame1,
                      value=("Yes", "No"), width=33, state='readonly')
cmbolc.place(x=10, y=450)

# plot color -------------------------------------------
word8_lbc = Label(p_frame1, text="line color", bg="white", fg="#1F0058", font=ft.Font(size=10))
word8_lbc.place(x=10, y=490)

cmbol2c = ttk.Combobox(p_frame1,
                       value=("red", "blue", "yellow", "green", "black", "orange"), width=33, state='readonly')
cmbol2c.place(x=10, y=510)

# plot or bar --------------------------------------
word9_lbc = Label(p_frame1, text="type of the Graph:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word9_lbc.place(x=10, y=550)

comb_bar_plotc = ttk.Combobox(p_frame1,
                              values=("bar", "plot"), width=33, state='readonly')
comb_bar_plotc.place(x=10, y=570)


# draw the graph but -------------------------------------------------------------------------------------------------------------------------------------------------|

def drawc():
    if len(x01) == len(y01):

        plt.title(plot_en_titlec.get())
        plt.xlabel(x_en_lbc.get())
        plt.ylabel(y_en_lbc.get())
        line_getc = line_en_lbc.get()

        line_colorc = cmbol2c.get()

        if comb_bar_plotc.get() == "plot":
            plt.plot(x01, y01, linewidth=5, marker="o", color=line_colorc, linestyle="--", label=line_getc)

        elif comb_bar_plotc.get() == "bar":
            plt.bar(x01, y01, color=line_colorc, label=line_getc)

        else:
            error2_lbc = Label(w_painter, text="Error: pleas chose one of the options in the graph type.", bg="#1F0058",
                               fg="white")
            error2_lbc.place(x=700, y=400)

        if cmbolc.get() == "Yes":
            plt.grid()
        elif cmbolc.get() == "No":
            pass

        plt.legend()
        plt.show()
    else:
        error_lbc = Label(w_painter,
                          text="Error: x elements must be equale y elements \n for example: x = [1,2,3]  and y = [A,B,C]",
                          bg="#1F0058", fg="white")
        error_lbc.place(x=700, y=400)


back_butc = Button(w_comp, text="Back to home", bg="white", fg="#1F0058", command=show_home)
back_butc.place(x=1195, y=0)

#image3c = Image.open("images/2graph-q.png")=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=
#image3_1c = image3.resize((250, 125))=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=

#photo3 = ImageTk.PhotoImage(image3_1)=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=

draw_butc = Button(w_comp, text="Start Graphing!!", borderwidth=0, bg="#1F0058", command=drawc)
draw_butc.place(x=700, y=300)

# frame 2 ==================================================================================================

p_frame12 = Frame(w_comp, bg="white", width=320, height=720)
p_frame12.pack(side="right")

x_frame12 = Frame(p_frame1, bg="white", width=224, height=20)
x_frame12.place(x=10, y=60)

x012 = []


def addc2():
    get_entryc2 = enter_lbc2.get()
    x012.append(get_entryc2)

    x_lbc2 = Label(x_frame12, text="x = " + str(x01), bg="white", fg="black")
    x_lbc2.place(x=0, y=0)


def removec2():
    x012.pop()

    x_lb2c2 = Label(x_frame12, bg="white", width=40)
    x_lb2c2.place(x=0, y=0)

    x_lb3c2 = Label(x_frame12, text="x = " + str(x01), bg="white", fg="dark gray")
    x_lb3c2.place(x=0, y=0)


word2_lbc2 = Label(p_frame12, text="Put the elements line x:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word2_lbc2.place(x=10, y=10)

enter_lbc2 = Entry(p_frame12, font=ft.Font(size=14), bg="#1F0058", fg="white")
enter_lbc2.place(x=10, y=30)

add_butc2 = Button(p_frame12, text="Add", bg="#8667BF", fg="white", width=4, command=addc2)
add_butc2.place(x=270, y=30)

remove_butc2 = Button(p_frame12, text="Del", bg="#8667BF", fg="white", width=4, command=removec2)
remove_butc2.place(x=270, y=60)

y_framec2 = Frame(p_frame12, bg="white", width=224, height=20)
y_framec2.place(x=10, y=150)

y012 = []


def add2c2():
    get_entryc2 = eval(entery_lbc2.get())
    y012.append(get_entryc2)

    x2_lbc2 = Label(y_framec2, text="y = " + str(y01), bg="white", fg="black")
    x2_lbc2.place(x=0, y=0)


def remove_yc2():
    y012.pop()

    y_lb2c2 = Label(y_framec2, bg="white", width=40)
    y_lb2c2.place(x=0, y=0)

    y_lb3c2 = Label(y_framec2, text="y = " + str(y01), bg="white", fg="dark gray")
    y_lb3c2.place(x=0, y=0)


word3_lbc2 = Label(p_frame12, text="Put the numbers line y:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word3_lbc2.place(x=10, y=100)

entery_lbc2 = Entry(w_comp, font=ft.Font(size=14), bg="#1F0058", fg="white")
entery_lbc2.place(x=10, y=120)

add2_butc2 = Button(p_frame12, text="Add", bg="#8667BF", fg="white", width=4, command=add2c2)
add2_butc2.place(x=270, y=120)

removey_butc2 = Button(p_frame12, text="Del", bg="#8667BF", fg="white", width=4, command=remove_yc2)
removey_butc2.place(x=270, y=150)

# title entry ---------------------------------------
word4_lbc2 = Label(p_frame12, text="Enter the title:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word4_lbc2.place(x=10, y=190)

plot_en_titlec2 = Entry(p_frame12, font=ft.Font(size=14), bg="#1F0058", fg="white")
plot_en_titlec2.place(x=10, y=210)

# x label entry ---------------------------------------
word5_lbc2 = Label(p_frame12, text="Enter the x label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word5_lbc2.place(x=10, y=250)

x_en_lbc2 = Entry(p_frame12, font=ft.Font(size=14), bg="#1F0058", fg="white")
x_en_lbc2.place(x=10, y=270)

# y label entry ---------------------------------------
word6_lbc2 = Label(p_frame12, text="Enter the y label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word6_lbc2.place(x=10, y=310)

y_en_lbc2 = Entry(p_frame12, font=ft.Font(size=14), bg="#1F0058", fg="white")
y_en_lbc2.place(x=10, y=330)

# line label --- ---------------------------------------
word7_lbc2 = Label(p_frame12, text="Enter the line or bar label:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word7_lbc2.place(x=10, y=370)

line_en_lbc2 = Entry(p_frame12, font=ft.Font(size=14), bg="#1F0058", fg="white")
line_en_lbc2.place(x=10, y=390)

# line label --- ---------------------------------------
word8_lbc2 = Label(p_frame12, text="do you want grid on the graph?", bg="white", fg="#1F0058", font=ft.Font(size=10))
word8_lbc2.place(x=10, y=430)

cmbolc2 = ttk.Combobox(p_frame12,
                       value=("Yes", "No"), width=33, state='readonly')
cmbolc2.place(x=10, y=450)

# plot color -------------------------------------------
word8_lbc2 = Label(p_frame12, text="line color", bg="white", fg="#1F0058", font=ft.Font(size=10))
word8_lbc2.place(x=10, y=490)

cmbol2c2 = ttk.Combobox(p_frame12,
                        value=("red", "blue", "yellow", "green", "black", "orange"), width=33, state='readonly')
cmbol2c2.place(x=10, y=510)

# plot or bar --------------------------------------
word9_lbc = Label(p_frame1, text="type of the Graph:", bg="white", fg="#1F0058", font=ft.Font(size=10))
word9_lbc.place(x=10, y=550)

comb_bar_plotc = ttk.Combobox(p_frame1,
                              values=("bar", "plot"), width=33, state='readonly')
comb_bar_plotc.place(x=10, y=570)


# draw the graph but -------------------------------------------------------------------------------------------------------------------------------------------------|

def drawc():
    if len(x01) == len(y01):

        plt.title(plot_en_titlec.get())
        plt.xlabel(x_en_lbc.get())
        plt.ylabel(y_en_lbc.get())
        line_getc = line_en_lbc.get()

        line_colorc = cmbol2c.get()

        if comb_bar_plotc.get() == "plot":
            plt.plot(x01, y01, linewidth=5, marker="o", color=line_colorc, linestyle="--", label=line_getc)

        elif comb_bar_plotc.get() == "bar":
            plt.bar(x01, y01, color=line_colorc, label=line_getc)

        else:
            error2_lbc = Label(w_painter, text="Error: pleas chose one of the options in the graph type.", bg="#1F0058",
                               fg="white")
            error2_lbc.place(x=700, y=400)

        if cmbolc.get() == "Yes":
            plt.grid()
        elif cmbolc.get() == "No":
            pass

        plt.legend()
        plt.show()
    else:
        error_lbc = Label(w_painter,
                          text="Error: x elements must be equale y elements \n for example: x = [1,2,3]  and y = [A,B,C]",
                          bg="#1F0058", fg="white")
        error_lbc.place(x=700, y=400)


back_butc = Button(w_comp, text="Back to home", bg="white", fg="#1F0058", command=show_home)
back_butc.place(x=1195, y=0)

#image3c = Image.open("D:/python projects/program first/images/2graph-q.png")=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=
#image3_1c = image3.resize((250, 125))=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=

#photo3 = ImageTk.PhotoImage(image3_1)=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=//=/=/=/=//=

draw_butc = Button(w_comp, text="draw", borderwidth=0, bg="#1F0058", command=drawc)
draw_butc.place(x=00, y=300)

w_home.mainloop()