from tkinter import *
from PIL import ImageTk, Image

def init_cal():
    rt = Tk()
    rt.title("Basic Calculator")
    rt.iconbitmap('C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\Calc-icon.ico')
    rt.geometry("300x430")

    bg = ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\300x430_background.png")
    bg_label = Label(rt, image=bg)
    bg_label.place(x=0, y=0)

    e = Entry(rt, width=35, borderwidth=10, font=("Times", 10))
    e.grid(row=0 , column=0, pady=20, padx=30, columnspan=3)

    images = {
        "1": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\1.png"),
        "2": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\2.png"),
        "3": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\3.png"),
        "4": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\4.png"),
        "5": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\5.png"),
        "6": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\6.png"),
        "7": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\7.png"),
        "8": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\8.png"),
        "9": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\9.png"),
        "0": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\10.png"),
        "+": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\11.png"),
        "-": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\12.png"),
        "*": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\13.png"),
        "/": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\14.png"),
        "=": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\15.png"),
        "C": ImageTk.PhotoImage(file = "C:\\Users\\rd\\Downloads\\Calculator Photo-20250112T094619Z-001\\Calculator Photo\\16.png"),
    }

    def butt_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def butt_add():
        first_num = e.get()
        global f_num
        global maths
        maths = "addition"
        f_num = int(first_num)
        e.delete(0, END)

    def butt_sub():
        first_num = e.get()
        global f_num
        global maths
        maths = "subtraction"
        f_num = int(first_num)
        e.delete(0, END)

    def butt_div():
        first_num = e.get()
        global f_num
        global maths
        maths = "division"
        f_num = int(first_num)
        e.delete(0, END)

    def butt_mult():
        first_num = e.get()
        global f_num
        global maths
        maths = "multiplication"
        f_num = int(first_num)
        e.delete(0, END)

    def butt_equal():
        second_num = e.get()
        e.delete(0, END)

        if maths == "addition":
            e.insert(0, f_num + int(second_num))
        if maths == "subtration":
            e.insert(0, f_num - int(second_num))
        if maths == "multiplication":
            e.insert(0, f_num * int(second_num))
        if maths == "division":
            e.insert(0, f_num / int(second_num))

    def butt_clear():
        e.delete(0, END)

    butts = {
        "1": (1, 0, lambda: butt_click(1)),
        "2": (1, 1, lambda: butt_click(2)),
        "3": (1, 2, lambda: butt_click(3)),
        "4": (2, 0, lambda: butt_click(4)),
        "5": (2, 1, lambda: butt_click(5)),
        "6": (2, 2, lambda: butt_click(6)),
        "7": (3, 0, lambda: butt_click(7)),
        "8": (3, 1, lambda: butt_click(8)),
        "9": (3, 2, lambda: butt_click(9)),
        "0": (4, 1, lambda: butt_click(0)),
        "+": (4, 2, butt_add),
        "-": (4, 0, butt_sub),
        "*": (5, 1, butt_mult),
        "/": (5, 0, butt_div),
        "=": (5, 2, butt_equal),
        "C": (6, 1, butt_clear),
    }

    for btn, (row, col, cmd) in butts.items():
        Button(rt, border="3", image=images[btn], command=cmd).grid(row=row, column=col)
    rt.images = images
    rt.mainloop()

init_cal()




