from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import requests
from tkinter import messagebox
import random
from datetime import datetime
from tkinter import filedialog

def total_bills():
    lassi_price = 50
    shakes_price = 50
    juice_price = 30
    milk_price = 20
    redbull_price = 150
    tea_price = 10
    coffee_price = 20

    roti_price = 5
    rice_price = 50
    paratha_price = 40
    paneer_price = 150
    makhni_price = 120
    mix_price = 70

    lassi_q = lassi_qty.get()
    shakes_q = shakes_qty.get()
    juice_q = juice_qty.get()
    milk_q = milk_qty.get()
    redbull_q = redbull_qty.get()
    tea_q = tea_qty.get()
    coffee_q = coffee_qty.get()

    roti_q = roti_qty.get()
    rice_q = rice_qty.get()
    paratha_q = paratha_qty.get()
    paneer_q = paneer_qty.get()
    makhni_q = makhni_qty.get()
    mix_q = mix_qty.get()

    if lassi_var.get() == 0:
        lassi_q = 0
    elif lassi_var.get() == 1 and lassi_qty.get() == "":
        messagebox.showerror("error", "please fill the lassi quantity")
        lassi_q = 0

    if coffee_var.get() == 0:
        coffee_q = 0
    elif coffee_var.get() == 1 and coffee_qty.get() == "":
        messagebox.showerror("error", "please fill the coffee quantity")
        coffee_q = 0

    if tea_var.get() == 0:
        tea_q = 0
    elif tea_var.get() == 1 and tea_qty.get() == "":
        messagebox.showerror("error", "please fill the tea quantity")
        tea_q = 0

    if juice_var.get() == 0:
        juice_q = 0
    elif juice_var.get() == 1 and juice_qty.get() == "":
        messagebox.showerror("error", "please fill the juice quantity")
        juice_q = 0

    if shakes_var.get() == 0:
        shakes_q = 0
    elif shakes_var.get() == 1 and shakes_qty.get() == "":
        messagebox.showerror("error", "please fill the shakes quantity")
        shakes_q = 0

    if milk_var.get() == 0:
        milk_q = 0
    elif milk_var.get() == 1 and milk_qty.get() == "":
        messagebox.showerror("error", "please fill the milk quantity")
        milk_q = 0

    if redbull_var.get() == 0:
        redbull_q = 0
    elif redbull_var.get() == 1 and redbull_qty.get() == '':
        messagebox.showerror("error", "please fill the redbull quantity")
        redbull_q = 0


    if roti_var.get() == 0:
        roti_q =0
    elif roti_var.get() == 1 and roti_qty.get() == "":
        messagebox.showerror("error", "please fill the Roti quantity")
        roti_q = 0

    if makhni_var.get() == 0:
        makhni_q = 0
    elif makhni_var.get() == 1 and makhni_qty.get() == "":
        messagebox.showerror("error", "please fill the Dal Makhni quantity")
        makhni_q = 0

    if paneer_var.get() == 0:
        paneer_q = 0
    elif paneer_var.get() == 1 and paneer_qty.get() == "":
        messagebox.showerror("error", "please fill the Mutter paneer quantity")
        paneer_q = 0

    if paratha_var.get() == 0:
        paratha_q =0
    elif paratha_var.get() == 1 and paratha_qty.get() == "":
        messagebox.showerror("error", "please fill the Paratha quantity")
        paratha_q = 0

    if mix_var.get() == 0:
        mix_q =0
    elif mix_var.get() == 1 and mix_qty.get() == "":
        messagebox.showerror("error", "please fill the mix quantity")
        mix_q = 0

    if rice_var.get() == 0:
        rice_q =0
    elif rice_var.get() == 1 and rice_qty.get() == "":
        messagebox.showerror("error", "please fill the rice quantity")
        rice_q = 0

    total_lassi_price = lassi_price * int(lassi_q)
    total_coffee_price = coffee_price * int(coffee_q)
    total_tea_price = tea_price * int(tea_q)
    total_redbull_price = redbull_price * int(redbull_q)
    total_milk_price = milk_price * int(milk_q)
    total_juice_price = juice_price * int(juice_q)
    total_shakes_price = shakes_price * int(shakes_q)

    total_drinks_cost = total_shakes_price + total_juice_price + total_tea_price + total_redbull_price + total_coffee_price + total_milk_price + total_lassi_price

    if drinks_cost.get() != "":
        drinks_cost.delete(0, "end")
        drinks_cost.insert("end", total_drinks_cost)
    else:
        drinks_cost.insert("end", total_drinks_cost)


    total_roti_price = roti_price * int(roti_q)
    total_rice_price = rice_price * int(rice_q)
    total_paneer_price = paneer_price * int(paneer_q)
    total_paratha_price = paratha_price * int(paratha_q)
    total_makhni_price = makhni_price * int(makhni_q)
    total_mix_price = mix_price * int(mix_q)

    total_food_cost = total_makhni_price + total_mix_price + total_paratha_price + total_paneer_price + total_rice_price + total_roti_price

    if food_cost.get() != "":
        food_cost.delete(0, "end")
        food_cost.insert("end", total_food_cost)
    else:
        food_cost.insert("end", total_food_cost)

    if service_charge_cost.get() != "":
        service_charge_cost.delete(0, "end")
        service_charge_cost.insert(0, 10)
    else:
        service_charge_cost.insert(0, 10)

    fc = int(food_cost.get())
    dc = int(drinks_cost.get())

    total_paid_tax = fc + dc
    total_paid_tax = total_paid_tax * 8/100

    if paid_tax_cost != "":
        paid_tax_cost.delete(0, "end")
        paid_tax_cost.insert(0, total_paid_tax)
    else:
        paid_tax_cost.insert(0, total_paid_tax)

    total_sub_cost = fc + dc + int(service_charge_cost.get())
    if sub_total_cost.get() != "":
        sub_total_cost.delete(0, "end")
        sub_total_cost.insert(0, total_sub_cost)
    else:
        sub_total_cost.insert(0, total_sub_cost)

    if total_cost_cost.get() != "":
        total_cost_cost.delete(0, "end")
        total_cost_cost.insert(0, float(total_sub_cost + total_paid_tax))
    else:
        total_cost_cost.insert(0, float(total_sub_cost + total_paid_tax))

    date = datetime.now().date()
    if bill_details.get(1.0, "end") != "":
        bill_details.delete(1.0, "end")
        bill_details.insert(1.0, f" Billion-{random.randint(100, 1000)}\t{date} ======================= Items(q) \t \tAmount =======================\n Roti(25) \t \t  125.0\n Dal Makhni(2)\t   240.0\n Mutter Paneer(2) 300.0\n Coffee(2)\t \t  40.0\n Tea(2)   \t \t  20.0\n Juice(1) \t \t  30.0\n Shakes(1)\t \t  50.0\n======================="
                                 f" Service charge   {service_charge_cost.get()}\n"
                                 f" Tax      \t \t  {total_paid_tax}\n"
                                 f"\n"
                                 f" Sub Total\t \t  {total_sub_cost}\n"                                 
                                 f"\n======================= "
                                 f"Total\t\t{total_cost_cost.get()}\n=======================")


def save():
    root.filename = filedialog.asksaveasfile(mode="w", defaultextension='.txt')
    if root.filename is None:
        return
    file_save = str(bill_details.get(1.0, 'end'))
    root.filename.write(file_save)
    root.filename.close()

def lassi_chk():
    if lassi_var.get() == 1:
        lassi_qty['state'] = "normal"
        lassi_qty['bg'] = '#248aa2'
        lassi_qty['fg'] = "white"
    else:
        lassi_qty['state'] = "disabled"

def coffee_chk():
    if coffee_var.get() == 1:
        coffee_qty['state'] = "normal"
        coffee_qty['bg'] = '#248aa2'
        coffee_qty['fg'] = "white"
    else:
        coffee_qty['state'] = "disabled"

def tea_chk():
    if tea_var.get() == 1:
        tea_qty['state'] = "normal"
        tea_qty['bg'] = '#248aa2'
        tea_qty['fg'] = "white"
    else:
        tea_qty['state'] = "disabled"

def juice_chk():
    if juice_var.get() == 1:
        juice_qty['state'] = "normal"
        juice_qty['bg'] = '#248aa2'
        juice_qty['fg'] = "white"
    else:
        juice_qty['state'] = "disabled"

def milk_chk():
    if milk_var.get() == 1:
        milk_qty['state'] = "normal"
        milk_qty['bg'] = '#248aa2'
        milk_qty['fg'] = "white"
    else:
        milk_qty['state'] = "disabled"

def redbull_chk():
    if redbull_var.get() == 1:
        redbull_qty['state'] = "normal"
        redbull_qty['bg'] = '#248aa2'
        redbull_qty['fg'] = "white"
    else:
        redbull_qty['state'] = "disabled"

def shakes_chk():
    if shakes_var.get() == 1:
        shakes_qty['state'] = "normal"
        shakes_qty['bg'] = '#248aa2'
        shakes_qty['fg'] = "white"
    else:
        shakes_qty['state'] = "disabled"




def roti_chk():
    if roti_var.get() == 1:
        roti_qty['state'] = "normal"
        roti_qty['bg'] = '#248aa2'
        roti_qty['fg'] = "white"
    else:
        roti_qty['state'] = "disabled"

def makhni_chk():
    if  makhni_var.get() == 1:
        makhni_qty['state'] = "normal"
        makhni_qty['bg'] = '#248aa2'
        makhni_qty['fg'] = "white"
    else:
        makhni_qty['state'] = "disabled"

def paneer_chk():
    if paneer_var.get() == 1:
        paneer_qty['state'] = "normal"
        paneer_qty['bg'] = '#248aa2'
        paneer_qty['fg'] = "white"
    else:
        paneer_qty['state'] = "disabled"

def paratha_chk():
    if paratha_var.get() == 1:
        paratha_qty['state'] = "normal"
        paratha_qty['bg'] = '#248aa2'
        paratha_qty['fg'] = "white"
    else:
        paratha_qty['state'] = "disabled"

def mix_chk():
    if mix_var.get() == 1:
        mix_qty['state'] = "normal"
        mix_qty['bg'] = '#248aa2'
        mix_qty['fg'] = "white"
    else:
        mix_qty['state'] = "disabled"

def rice_chk():
    if rice_var.get() == 1:
        rice_qty['state'] = "normal"
        rice_qty['bg'] = '#248aa2'
        rice_qty['fg'] = "white"
    else:
        rice_qty['state'] = "disabled"




def nine():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "9")
    else:
        result.insert("end", "9")

def eight():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "8")
    else:
        result.insert("end", "8")

def seven():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "7")
    else:
        result.insert("end", "7")

def six():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "6")
    else:
        result.insert("end", "6")

def five():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end", "5")
    else:
        result.insert("end", "5")

def four():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end", "4")
    else:
        result.insert("end","4")

def three():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","3")
    else:
        result.insert("end", "3")

def two():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","2")
    else:
        result.insert("end", "2")

def one():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end", "1")
    else:
        result.insert("end", "1")

def zero():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","0")
    else:
        result.insert("end", "0")

def plus():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end", "+")
    else:
        result.insert("end","+")

def minus():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0, "end")
        result.insert("end","-")
    else:
        result.insert("end","-")

def mul():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","*")
    else:
        result.insert("end","*")

def divide():
    if 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
        result.insert("end","/")
    else:
        result.insert("end","/")

def equal():
    if result.get() == "":
        result.insert("end", "error")
    elif result.get()[0] == "0" or result.get()[0] == "+" or result.get()[0] == "*" or result.get() [0] == "/":
        result.delete(0,"end")
        result.insert("end", "error")
    elif 'error' in result.get() or '=' in result.get():
        result.delete(0,"end")
    else:
        res = result.get()
        res = eval(res)
        result.insert("end"," = ")
        result.insert("end", res)

def clear():
    result.delete(0,"end")



def send():
    root = tk.Tk()
    root.geometry('300x400')
    root['bg'] = "white"

    frame4 = Frame(root, width=300, height=60, relief=RIDGE, borderwidth=5, bg='#248aa2',
                   highlightbackground="white", highlightcolor="white")
    frame4.place(x=0,y=0)

    l2 = Label(frame4, text="Send Bill", font=('roboto', 22, 'bold'), bg='#248aa2', fg="#ffffff")
    l2.place(x=85, y=1)

    frame5 = Frame(root, width=300, height=340, relief=RIDGE, borderwidth=5, bg='#248aa2', highlightbackground="white",
                   highlightcolor="white")
    frame5.place(x=0, y=55)

    innerframe5 = Frame(frame5, width=285, height=325, relief=RIDGE, borderwidth=3, bg='#248aa2', highlightbackground="white",
                        highlightcolor="white")
    innerframe5.place(x=0, y=0)

    l3 = LabelFrame(innerframe5, text="Send Bill Through SMS", width=270, height=310, borderwidth=3,
                    font=('verdana', 10, 'bold'), fg='#248aa2', relief=RIDGE)
    l3.place(x=2, y=2)

    l4 = Label(innerframe5, text="Phone Number", font=('verdana', 10, 'bold'))
    l4.place(x=40, y=40)

    number = Entry(innerframe5, width=30, borderwidth=2)
    number.place(x=40, y=70)

    l5 = Label(innerframe5, text="Bill Details", font=('verdana', 10, 'bold'))
    l5.place(x=40, y=100)

    b_detail = ScrolledText(innerframe5, width=23, height=7, relief = RIDGE, borderwidth = 3)
    b_detail.place(x=40, y=130)
    b_detail.insert(1.0, bill_details.get(1.0, 'end'))

    def send_bill():
        ph_number = number.get()
        messages = b_detail.get("1.0", "end-1c")

        if ph_number == "":
            messagebox.showerror("Error", 'Please fill the phone number')
        elif messages == "": messagebox.showerror("Error", 'Bill Details is empty')

        else:
            url = "https://www.fast2sms.com/dev/bulk"
            api = ""  # go to fast2sms.com signup to get the free api and put it into here in api variable
            querystring = {"authorization": api, "sender_id": "FSTSMS", "message": messages, "language":"english",
                           "route":"p", "numbers":ph_number}
            headers = {'cache-control': "no-cache"}
            requests.request("GET", url, headers=headers, params=querystring)
            messagebox.showinfo("Send SMS", 'Bill has been send to your successfully')


    send_msg = Button(innerframe5, text="Send Bill", relief=RAISED, borderwidth = 2, font = ('verdana', 8, 'bold'),
                      bg = '#248aa2', fg="white", padx=20, command= send_bill)
    send_msg.place(x=100, y=255)

    root.mainloop()

def exit():
    message = messagebox.askquestion('Notepad', "Do you want to exit the app")
    if message == "yes":
        root.destroy()
    else:
        "return"

def cleared_bill():
    lassi_qty.delete(0, 'end')
    lassi.deselect()
    lassi_qty['state'] = "disabled"
    coffee_qty.delete(0, 'end')
    coffee.deselect()
    coffee_qty['state'] = "disabled"
    tea_qty.delete(0, 'end')
    tea.deselect()
    tea_qty['state'] = "disabled"
    juice_qty.delete(0, 'end')
    juice.deselect()
    juice_qty['state'] = "disabled"
    shakes_qty.delete(0, 'end')
    shakes.deselect()
    shakes_qty['state'] = "disabled"
    milk_qty.delete(0, 'end')
    milk.deselect()
    milk_qty['state'] = "disabled"
    redbull_qty.delete(0, 'end')
    redbull.deselect()
    redbull_qty['state'] = "disabled"

    roti_qty.delete(0, 'end')
    roti.deselect()
    roti_qty['state'] = "disabled"
    makhni_qty.delete(0, 'end')
    makhni.deselect()
    makhni_qty['state'] = "disabled"
    paneer_qty.delete(0, 'end')
    paneer.deselect()
    paneer_qty['state'] = "disabled"
    paratha_qty.delete(0, 'end')
    paratha.deselect()
    paratha_qty['state'] = "disabled"
    mix_qty.delete(0, 'end')
    mix.deselect()
    mix_qty['state'] = "disabled"
    rice_qty.delete(0, 'end')
    rice.deselect()
    rice_qty['state'] = "disabled"

    drinks_cost.delete(0, 'end')
    food_cost.delete(0, 'end')
    service_charge_cost.delete(0, 'end')
    paid_tax_cost.delete(0, 'end')
    sub_total_cost.delete(0, 'end')
    total_cost_cost.delete(0, 'end')

    bill_details.delete(1.0, 'end')


root = tk.Tk()
root.geometry('650x400')
root.maxsize(650,390)
root.minsize(650,390)
root.title("Restaurant Management System")

frame = Frame (root, width=650,height=70, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame.place(x=0,y=0)

l1 = Label(frame, text="Restaurant Management System", font=('roboto', 30, 'bold'), bg='#248aa2',fg="#ffffff")
l1.place(x=10,y=4)

frame1= Frame(root, width=450, height=230, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame1.place(x=0,y=70)

innerframe1 = Frame(frame1, width=150, height=220, relief=RIDGE, borderwidth=3, bg='#248aa2', highlightbackground="white",
                    highlightcolor="white")
innerframe1.place(x=0,y=0)

drinks = LabelFrame(innerframe1, text="Drinks", width=135, height=205, borderwidth=3, font=('verdana', 10, 'bold'),
                    fg='#248aa2', relief=RIDGE, highlightbackground="white")
drinks.place(x=2,y=2)

lassi_var = IntVar()
lassi = Checkbutton (drinks, text="Lassi", variable=lassi_var, font=('verdana', 8, 'bold'), onvalue=1, offvalue=0,
                     command=lassi_chk)
lassi.place(x=2,y=2)
lassi_qty = Entry (drinks, width=7, borderwidth=4, relief=SUNKEN, state='disabled')
lassi_qty.place(x=74,y=2)
lassi_qty.insert(0,"0")

coffee_var = IntVar()
coffee = Checkbutton (drinks, text="Coffee", variable=coffee_var, font=('verdana', 8, 'bold'), onvalue=1, offvalue=0,
                    command=coffee_chk)
coffee.place(x=2,y=22)
coffee_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state="disabled")
coffee_qty.place(x=74,y=22)

tea_var = IntVar()
tea = Checkbutton(drinks, text="Tea", variable=tea_var, font=('verdana', 8, 'bold'), onvalue=1, offvalue=0,
                command=tea_chk)
tea.place(x=2,y=44)
tea_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state="disabled")
tea_qty.place(x=74,y=44)

juice_var = IntVar()
juice = Checkbutton (drinks, text="Juice", variable=juice_var, font=('verdana', 8, 'bold'), onvalue=1, offvalue=0,
                     command=juice_chk)
juice.place(x=2,y=66)
juice_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state="disabled")
juice_qty.place(x=74,y=66)

shakes_var = IntVar()
shakes = Checkbutton (drinks, text="Shakes", variable=shakes_var, font=('verdana', 8, 'bold'), onvalue=1, offvalue=0,
                      command=shakes_chk)
shakes.place(x=2,y=88)
shakes_qty = Entry (drinks, width=7, borderwidth=4, relief=SUNKEN, state="disabled")
shakes_qty.place(x=74,y=88)
milk_var = IntVar()
milk = Checkbutton (drinks, text="Milk", variable=milk_var, font=('verdana', 8, 'bold'), onvalue=1, offvalue=0,
                    command=milk_chk)
milk.place(x=2,y=110)
milk_qty = Entry (drinks, width=7, borderwidth=4, relief=SUNKEN, state="disabled")
milk_qty.place(x=74,y=110)

redbull_var = IntVar()
redbull = Checkbutton(drinks, text="Redbull", variable=redbull_var, font=('verdana', 8, 'bold'), onvalue=1, offvalue=0,
                      command=redbull_chk)
redbull.place(x=2,y=154)
redbull_qty = Entry(drinks, width=7, borderwidth=4, relief=SUNKEN, state="disabled")
redbull_qty.place(x=74,y=154)

innerframe2 = Frame(frame1, width=290,height=220, relief=RIDGE, borderwidth=3,bg='#248aa2', highlightbackground="white",
                    highlightcolor="white")
innerframe2.place(x=151,y=0)

foods = LabelFrame (innerframe2, text="Foods", width=275, height=205, borderwidth=3, font=('verdana', 10, 'bold'),
                    fg='#248aa2', relief=RIDGE, highlightbackground="white")
foods.place(x=2,y=2)


roti_var = IntVar()
roti = Checkbutton (foods, text="Roti", variable=roti_var, font=('verdana', 8, 'bold'), command=roti_chk)
roti.place(x=2,y=2)
roti_qty = Entry (foods, width=15, borderwidth=4, relief=SUNKEN, state="disabled")
roti_qty.place(x=140,y=2)

makhni_var = IntVar()
makhni = Checkbutton (foods, text="Dal Makhni", variable=makhni_var, font=('verdana', 8, 'bold'),
                          command=makhni_chk)
makhni.place(x=2,y=22)
makhni_qty = Entry (foods, width=15, borderwidth=4, relief=SUNKEN, state="disabled")
makhni_qty.place(x=140,y=22)

paneer_var = IntVar()
paneer = Checkbutton (foods, text="Mutter Paneer", variable=paneer_var, font=('verdana', 8, 'bold'),
                             command=paneer_chk)
paneer.place(x=2,y=44)
paneer_qty = Entry(foods, width=15, borderwidth=4, relief=SUNKEN, state="disabled")
paneer_qty.place(x=140,y=44)

paratha_var = IntVar()
paratha = Checkbutton (foods, text="Paratha", variable=paratha_var, font=('verdana', 8, 'bold'), command=paratha_chk)
paratha.place(x=2,y=66)
paratha_qty = Entry(foods, width=15, borderwidth=4, relief=SUNKEN, state="disabled")
paratha_qty.place(x=140,y=66)

mix_var = IntVar()
mix = Checkbutton (foods, text="Mix Veg", variable=mix_var, font=('verdana', 8, 'bold'), command=mix_chk)
mix.place(x=2,y=88)
mix_qty = Entry (foods, width=15, borderwidth=4, relief=SUNKEN, state="disabled")
mix_qty.place(x=140,y=88)

rice_var = IntVar()
rice = Checkbutton (foods, text="Rice", variable=rice_var, font=('verdana', 8, 'bold'), command=rice_chk)
rice.place(x=2,y=154)
rice_qty = Entry (foods, width=15, borderwidth=4, relief=SUNKEN, state="disabled")
rice_qty.place(x=140,y=154)

frame2= Frame(root, width=450, height=90, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame2.place(x=0,y=300)

innerframe3 = Frame(frame2, width=440, height=80, relief=RIDGE, borderwidth=3,bg='#248aa2', highlightbackground="white",
                    highlightcolor="white")
innerframe3.place(x=0,y=0)

cost_of_drinks = Label(innerframe3, text="Cost of Drinks", font=('verdana', 8, 'bold'))
cost_of_drinks.place(x=2,y=2)

drinks_cost =Entry (innerframe3, width=13, borderwidth=4, relief=SUNKEN)
drinks_cost.place(x=130,y=0)

cost_of_foods =Label(innerframe3, text="Cost of Foods", font=('verdana', 8, 'bold'))
cost_of_foods.place(x=2,y=24)

food_cost =Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
food_cost.place(x=130,y=22)

service_charge =Label (innerframe3, text="Service Charge", font=('verdana', 8, 'bold'))
service_charge.place(x=2,y=46)
service_charge_cost =Entry (innerframe3, width=13, borderwidth=4, relief=SUNKEN)
service_charge_cost.place(x=130,y=44)

paid_tax = Label (innerframe3, text="Paid Tax", font=('verdana', 8, 'bold'))
paid_tax.place(x=250,y=2)
paid_tax_cost = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
paid_tax_cost.place(x=330,y=0)

sub_total = Label (innerframe3, text="Sub Total", font=('verdana', 8, 'bold'))
sub_total.place(x=250,y=24)
sub_total_cost = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
sub_total_cost.place(x=330,y=22)

total_cost = Label (innerframe3, text="Total Cost", font=('verdana', 8, 'bold'))
total_cost.place(x=250,y=46)
total_cost_cost = Entry(innerframe3, width=13, borderwidth=4, relief=SUNKEN)
total_cost_cost.place(x=330,y=44)

frame3 = Frame(root, width=200, height=320, relief=RIDGE, borderwidth=5, bg='#248aa2')
frame3.place(x=450,y=70)

innerframe4 = Frame(frame3, width=190,height=310, relief=RIDGE, borderwidth=3,bg='#248aa2', highlightbackground="white",
                    highlightcolor="white", highlightthickness=1)
innerframe4.place(x=0,y=0)

result = Entry (innerframe4, width=28, relief=SUNKEN, borderwidth=3)
result.place(x=2,y=0)

nine = Button (innerframe4, text="9", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
               fg="white", command=nine)
nine.place(x=0,y=24)

eight = Button (innerframe4, text="8", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
                fg="white", command=eight)
eight.place(x=48,y=24)

seven = Button (innerframe4, text="7", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
                fg="white", command=seven)
seven.place(x=96,y=24)

plus = Button(innerframe4, text="+", padx=6, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='white',
              fg="black",command=plus)
plus.place(x=144,y=24)

six = Button(innerframe4, text="6", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
             fg="white", command=six)
six.place(x=0,y=50)

five = Button (innerframe4, text="5", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
               fg="white", command=five)
five.place(x=48,y=50)

four = Button (innerframe4, text="4", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
               fg="white", command=four)
four.place(x=96,y=50)

minus = Button (innerframe4, text="-", padx=8, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='white',
                fg="black", command=minus)
minus.place(x=144,y=50)

three = Button (innerframe4, text="3", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
                fg="white", command=three)
three.place(x=0, y=76)

two = Button(innerframe4, text="2", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
             fg="white", command=two)
two.place(x=48,y=76)

one = Button(innerframe4, text="1", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
             fg="white", command=one)
one.place(x=96, y=76)

multiply = Button (innerframe4, text="*", padx=7, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='white',
                   fg="black", command=mul)
multiply.place(x=144,y=76)

zero = Button(innerframe4, text="0", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
               fg="white",command=zero)
zero.place(x=0,y=102)

clear = Button(innerframe4, text="C", padx=15, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2',
                fg="white", command=clear)
clear.place(x=48,y=102)

equal = Button(innerframe4, text="=", padx=15, relief=RAISED, borderwidth=2,font=('verdana', 10, 'bold'), bg='#248aa2',
                fg="white", command=equal)
equal.place(x=96,y=102)

divide = Button(innerframe4, text="/", padx=7, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='white',
                fg="black",command=divide)
divide.place(x=144,y=102)

bill_details = ScrolledText(innerframe4, width=23,height=9, relief=SUNKEN, borderwidth=3, font=('courier',9,''))
bill_details.place(x=0,y=130)

total = Button(innerframe4, text="Total", relief=RAISED, borderwidth=2, font=('verdana', 8, 'bold'), bg='#248aa2',
               fg="white",command=total_bills)
total.place(x=0,y=275)

save = Button (innerframe4, text="Save", relief=RAISED, borderwidth=2, font=('verdana', 8, 'bold'), bg='#248aa2',
               fg="white", command=save)
save.place(x=43,y=275)

send = Button(innerframe4, text="Send", relief=RAISED, borderwidth=2, font=('verdana', 8, 'bold'), bg='#248aa2',
              fg="white", command=send)
send.place(x=82,y=275)

exit = Button (innerframe4, text="Exit", relief=RAISED, borderwidth=2, font=('verdana', 8, 'bold'), bg='#248aa2',
               fg="white", command=exit)
exit.place(x=124,y=275)

clr = Button(innerframe4, text="C", relief=RAISED, borderwidth=2, font=('verdana', 8, 'bold'), bg='#248aa2',
             fg="white", command=cleared_bill)
clr.place(x=160,y=275)

root.mainloop()