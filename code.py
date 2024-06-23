# Import necessary libraries
import sqlite3
import tkinter
from tkinter import *
import time
import random
from tkinter import messagebox
from PIL import Image,ImageTk
import os

# Function for the second window
#------------------------------------ ADMIN CODE -----------------------------------
def second_window():
    first.destroy()
    from PIL import Image, ImageTk

    # Define the HomeWindow function
    def HomeWindow():
        second.destroy()

        # Create the main window
        root = Tk()
        root.geometry("1500x740+0+0")
        root.title("Restaurant Billing System")

        # Load a background image
        load = Image.open("C:/Users/Lenovo/PycharmProjects/Restaurant_billing/food.jpeg")
        background_image = ImageTk.PhotoImage(load)
        background_label = Label(root, image=background_image)
        background_label.place(x=0, y=0, relheight=1, relwidth=1)

        # Create a database for orders bills
        table = sqlite3.connect("bills.db")
        table.execute('''CREATE TABLE IF NOT EXISTS BILLS
        (ORDER_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FRIES_MEAL TEXT,LUNCH_MEAL TEXT,BURGER_MEAL TEXT,PIZZA_MEAL TEXT,CHEESE_BURGER TEXT,DRINKS TEXT,MEAL_1 TEXT,MEAL_2 TEXT,COST TEXT,SERVICE_CHARGE TEXT,TAX TEXT,SUBTOTAL TEXT,TOTAL TEXT);''')
        table.commit()

        table1 = sqlite3.connect("orderschef.db")
        table1.execute('''CREATE TABLE IF NOT EXISTS ORDERSCHEF
        (ORDER_NUMBER INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,FRIES_MEAL TEXT,LUNCH_MEAL TEXT,BURGER_MEAL TEXT,PIZZA_MEAL TEXT,CHEESE_BURGER TEXT,DRINKS TEXT,MEAL_1 TEXT,MEAL_2 TEXT,COST TEXT,SERVICE_CHARGE TEXT,TAX TEXT,SUBTOTAL TEXT,TOTAL TEXT);''')
        table1.commit()

        # Define the price list GUI function
        def price():
            # Create a new window for price list
            master = Tk()
            master.geometry("550x650")
            master.title("Price List")
            # ... (code for displaying price list)
            f1 = Frame(master)
            f1.pack(side=TOP)
            x = Label(f1, text="PRICE LIST\n", font=("comic sans ms", "15", "underline", "bold"), fg="steel blue")
            x.pack()

            f2 = Frame(master)
            f2.pack(side=LEFT)
            a1 = Label(f2, text="ITEMS\n", font=("comic sans ms", "10", "underline"), fg="steel blue")
            a1.pack()
            a = Label(f2,
                      text="FRIES MEAL\n\nLUNCH MEAL\n\nBURGER MEAL\n\nPIZZA MEAL\n\nCHESSE BURGER\n\nDRINKS\n\nMEAL 1-\nFRIES MEAL+BURGER MEAL+DRINKS\n\nMEAL 2-\nPIZZA MEAL+CHESSE BURGER+DRINKS",
                      font=("comic sans ms", "15"), fg="steel blue")
            a.pack()

            f3 = Frame(master)
            f3.pack(side=RIGHT)
            b1 = Label(f3, text="PRICE\n", font=("comic sans ms", "10", "underline"), fg="steel blue")
            b1.pack()
            b = Label(f3, text="Rs 50\n\nRs 150\n\nRs 50\n\nRs 200\n\nRs 70\n\nRs 30\n\n\nRs 200\n\n\nRs 250",
                      font=("comic sans ms", "15"), fg="steel blue")
            b.pack()

            master.mainloop()

        # -------------------------------------------------------------------------------
        # Create variables for input fields
        name=StringVar()
        phoneno=StringVar()
        gmail=StringVar()
        ran = StringVar()
        fries = StringVar()
        lunch = StringVar()
        burger = StringVar()
        pizza = StringVar()
        cheese_burger = StringVar()
        drinks = StringVar()
        meal_1 = StringVar()
        meal_2 = StringVar()
        cost = StringVar()
        service = StringVar()
        tax = StringVar()
        sub_total = StringVar()
        final = StringVar()

        global order

        # use of class for calculations
        class Calculate:
            def price(self, e2, e3, e4, e5, e6, e7, m1, m2):
                # ... (code for price calculations)
                try:
                    global a, b, c, d, e, f, g, h
                    a = int(e2.get())
                    b = int(e3.get())
                    c = int(e4.get())
                    d = int(e5.get())
                    e = int(e6.get())
                    f = int(e7.get())
                    g = int(m1.get())
                    h = int(m2.get())
                    global costoffries, costoflunch, costofburger, costofpizza, costofchesseburger, costofdrinks, costofmeal1, costofmeal2, costofmeal, Service, PaidTax, OverAllCost
                    costoffries = a * 50
                    costoflunch = b * 150
                    costofburger = c * 50
                    costofpizza = d * 200
                    costofchesseburger = e * 70
                    costofdrinks = f * 30
                    costofmeal1 = g * 200
                    costofmeal2 = h * 250
                    costofmeal = ('%.2f' % (
                                costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2))
                    charge = ((
                                          costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2) / 99)
                    pay = ((
                                       costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2) * 0.05)
                    subtotal = (
                                costoffries + costoflunch + costofburger + costofpizza + costofchesseburger + costofdrinks + costofmeal1 + costofmeal2)
                    Service = ('%.2f' % charge)
                    OverAllCost = (charge + pay + subtotal)
                    PaidTax = ('%.2f' % pay)
                    cost.set(costofmeal)
                    service.set(Service)
                    tax.set(PaidTax)
                    sub_total.set(costofmeal)
                    final.set(OverAllCost)

                    table.execute(
                        "INSERT INTO BILLS(FRIES_MEAL,LUNCH_MEAL,BURGER_MEAL,PIZZA_MEAL,CHEESE_BURGER,DRINKS,MEAL_1,MEAL_2,COST,SERVICE_CHARGE,TAX,SUBTOTAL,TOTAL)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (str(costoffries), str(costoflunch), str(costofburger), str(costofpizza),
                         str(costofchesseburger),
                         str(costofdrinks), str(costofmeal1), str(costofmeal2), str(costofmeal), str(Service),
                         str(PaidTax),
                         str(costofmeal), str(OverAllCost),))
                    table.commit()
                    table1.execute(
                        "INSERT INTO ORDERSCHEF(FRIES_MEAL,LUNCH_MEAL,BURGER_MEAL,PIZZA_MEAL,CHEESE_BURGER,DRINKS,MEAL_1,MEAL_2,COST,SERVICE_CHARGE,TAX,SUBTOTAL,TOTAL)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (str(a), str(b), str(c), str(d),
                         str(e),
                         str(f), str(g), str(h), str(costofmeal), str(Service),
                         str(PaidTax),
                         str(costofmeal), str(OverAllCost),))
                    table1.commit()
                    messagebox.showinfo("Success", "Bill Successfully Saved..")
                    '''
                    print(table.execute("select * from bills"))
                    items=[]
                    for row in table.execute("SELECT * FROM BILLS ORDER BY ORDER_NUMBER DESC LIMIT 1"):
                        for i in len(row):
                            print(row[i])
                            if row[i]!=0:
                                items.append(i)

                        p=row
                       # print(p)
                       '''
                except:
                    messagebox.showwarning("WARNING", "Invalid Input")

            # generating bill

            def bill(self):
                # ... (code for generating the bill)
                localtime = time.strftime('%d-%m-%y   %H:%M:%S')
                file = open("bills.txt", "w")
                file.write(localtime + "\n\n")
                file.write("THE ANUBHAV SPICE RESTAURANT\n\n")
                file.write("Address:"
                           "123 Main Street,\n"
                           "Ambala Cantt,\n"
                           "Ambala, Haryana, India\n")
                file.write("Phone: +91 123-456-7890\n\n")
                file.write("-----------------------------------------------------------\n\n")
                file.write("order number : " + str(order) + "\n\n\n")
                file.write("ITEM                    QUANTITY                AMOUNT                        TOTAL\n")
                if (costoffries != 0):
                    file.write("Fries                   " + str(
                        a) + "                         Rs 50" + "                       Rs " + str(costoffries) + "\n")
                if (costoflunch != 0):
                    file.write("Lunch                   " + str(
                        b) + "                         Rs 150" + "                      Rs " + str(costoflunch) + "\n")
                if (costofburger != 0):
                    file.write("Burger                  " + str(
                        c) + "                         Rs 50" + "                       Rs " + str(costofburger) + "\n")
                if (costofpizza != 0):
                    file.write("Pizza                   " + str(
                        d) + "                         Rs 200" + "                       Rs " + str(costofpizza) + "\n")
                if (costofchesseburger != 0):
                    file.write("Cheese burger           " + str(
                        e) + "                         Rs 70" + "                       Rs " + str(
                        costofchesseburger) + "\n")
                if (costofdrinks != 0):
                    file.write("Drinks                  " + str(
                        f) + "                         Rs 30" + "                       Rs " + str(costofdrinks) + "\n")
                if (costofmeal1 != 0):
                    file.write("Meal1                   " + str(
                        g) + "                         Rs 200" + "                       Rs " + str(costofmeal1) + "\n")
                if (costofmeal2 != 0):
                    file.write("Meal2                   " + str(
                        h) + "                         Rs 250" + "                       Rs " + str(costofmeal2) + "\n")

                file.write("\n")
                file.write("Cost of Meal : Rs " + str(costofmeal) + "\nService : Rs " + str(Service) + "\nTax : Rs " + str(
                    PaidTax) + "\nTotal : Rs " + str(OverAllCost))
                file.write("\n\n")
                file.write("-----------------------------------------------------------\n")
                file.write("                      Thanks To Visit")



        # Define the amount function
        def amount():
            if e21.get() == "" or e22.get() == "" or e23.get() == "" or not e21.get().isalpha() or len(e22.get()) != 10 or e23.get() == "@gmail.com":
                messagebox.showwarning("WARNING", "FILL DETAILS CAREFULLY")
            else:
                print(e21.get())
                print(e22.get())
                print(e23.get())
                c = Calculate()
                c.price(e2, e3, e4, e5, e6, e7, m1, m2)



        # Define the call_bill function
        def call_bill():
            c = Calculate()
            c.bill()
            os.startfile("bills.txt")

        # ------------------------------------------------------------------------

        # order NUMBER
        # x=random.randint(1,500)
        # order=str(x)
        global order
        order = 1
        ran.set(order)
        # ----------------------------------------------------------------

        # giving default values to different variables
        fries.set(0)
        lunch.set(0)
        burger.set(0)
        pizza.set(0)
        cheese_burger.set(0)
        drinks.set(0)
        meal_1.set(0)
        meal_2.set(0)

        # ----------------------------------------------------------------

        # function to reset all values
        def reset():
            global order
            name.set("")
            phoneno.set("")
            gmail.set("@gmail.com")
            order = order + 1
            ran.set(order)
            fries.set(0)
            lunch.set(0)
            burger.set(0)
            pizza.set(0)
            cheese_burger.set(0)
            drinks.set(0)
            meal_1.set(0)
            meal_2.set(0)
            cost.set(0)
            service.set(0)
            tax.set(0)
            final.set(0)

        def time_display():
            localtime = time.strftime('%d-%m-%y   %H:%M:%S')
            time1.configure(text=localtime)
            frame1.after(200, time_display)

        # ------------------------------------------------------------------------


        # main window GUI representation
        frame1 = Frame(root)
        frame1.pack(side=TOP)

        x = Label(frame1, text="RESTAURANT BILLING SYSTEM", font=("comic sans ms", '30', "bold", "underline"),
                  fg="steel blue", bd=10, anchor=W)
        x.grid(row=0, column=0)

        localtime = time.strftime('%d-%m-%y   %H:%M:%S')
        time1 = Label(frame1, text=localtime, font=("comic sans ms", "20", "bold", "italic"), fg="steel blue", anchor=W)
        time1.grid(row=1, column=0)
        time_display()
        # -----------------------------------------

        frame2 = Frame(root)
        frame2.pack(side=LEFT)

        lbl1 = Label(frame2, text="Order No.", font=("comic sans ms", "15"), fg="steel blue")
        lbl1.grid(row=0)
        e1 = Entry(frame2, textvariable=ran, font=("comic sans ms", "15"), fg="steel blue",state='disabled')
        e1.grid(row=0, column=1)
        #-------------------
        lbl21 = Label(frame2, text="Name", font=("comic sans ms", "15"), fg="steel blue")
        lbl21.grid(row=1)
        e21 = Entry(frame2, textvariable=name, font=("comic sans ms", "15"), fg="steel blue")
        e21.grid(row=1, column=1)


        lbl22 = Label(frame2, text="Phone Number", font=("comic sans ms", "15"), fg="steel blue")
        lbl22.grid(row=2)
        e22 = Entry(frame2, textvariable=phoneno, font=("comic sans ms", "15"), fg="steel blue")
        e22.grid(row=2, column=1)


        lbl23 = Label(frame2, text="Email", font=("comic sans ms", "15"), fg="steel blue")
        lbl23.grid(row=3)
        e23 = Entry(frame2, textvariable=gmail, font=("comic sans ms", "15"), fg="steel blue")
        e23.grid(row=3, column=1)
        #-------------------------------
        lbl2 = Label(frame2, text="Fries Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl2.grid(row=4)
        e2 = Entry(frame2, textvariable=fries, font=("comic sans ms", "15"), fg="steel blue")
        e2.grid(row=4, column=1)

        lbl3 = Label(frame2, text="Lunch Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl3.grid(row=5)
        e3 = Entry(frame2, textvariable=lunch, font=("comic sans ms", "15"), fg="steel blue")
        e3.grid(row=5, column=1)

        lbl4 = Label(frame2, text="Burger Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl4.grid(row=6)
        e4 = Entry(frame2, textvariable=burger, font=("comic sans ms", "15"), fg="steel blue")
        e4.grid(row=6, column=1)

        lbl5 = Label(frame2, text="Pizza Meal", font=("comic sans ms", "15"), fg="steel blue")
        lbl5.grid(row=7)
        e5 = Entry(frame2, textvariable=pizza, font=("comic sans ms", "15"), fg="steel blue")
        e5.grid(row=7, column=1)

        lbl6 = Label(frame2, text="Cheese Burger", font=("comic sans ms", "15"), fg="steel blue")
        lbl6.grid(row=8)
        e6 = Entry(frame2, textvariable=cheese_burger, font=("comic sans ms", "15"), fg="steel blue")
        e6.grid(row=8, column=1)


        # ------------------------------------

        frame3 = Frame(root)
        frame3.pack(side=RIGHT)

        meal1 = Label(frame3, text="Meal 1", font=("comic sans ms", "15"), fg="steel blue")
        meal1.grid(row=0)
        m1 = Entry(frame3, textvariable=meal_1, font=("comic sans ms", "15"), fg="steel blue")
        m1.grid(row=0, column=1)

        meal2 = Label(frame3, text="Meal 2", font=("comic sans ms", "15"), fg="steel blue")
        meal2.grid(row=1)
        m2 = Entry(frame3, textvariable=meal_2, font=("comic sans ms", "15"), fg="steel blue")
        m2.grid(row=1, column=1)

        lbl7 = Label(frame3, text="Drinks", font=("comic sans ms", "15"), fg="steel blue")
        lbl7.grid(row=2)
        e7 = Entry(frame3, textvariable=drinks, font=("comic sans ms", "15"), fg="steel blue")
        e7.grid(row=2, column=1)

        lbl8 = Label(frame3, text="Cost", font=("comic sans ms", "15"), fg="steel blue")
        lbl8.grid(row=3)
        e8 = Entry(frame3, textvariable=cost, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e8.grid(row=3, column=1)

        lbl9 = Label(frame3, text="Service Charge", font=("comic sans ms", "15"), fg="steel blue")
        lbl9.grid(row=4)
        e9 = Entry(frame3, textvariable=service, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e9.grid(row=4, column=1)

        lbl10 = Label(frame3, text="Tax", font=("comic sans ms", "15"), fg="steel blue")
        lbl10.grid(row=5)
        e10 = Entry(frame3, textvariable=tax, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e10.grid(row=5, column=1)

        lbl11 = Label(frame3, text="Subtotal", font=("comic sans ms", "15"), fg="steel blue")
        lbl11.grid(row=6)
        e11 = Entry(frame3, textvariable=cost, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e11.grid(row=6, column=1)

        lbl12 = Label(frame3, text="Total", font=("comic sans ms", "15"), fg="steel blue")
        lbl12.grid(row=7)
        e12 = Entry(frame3, textvariable=final, font=("comic sans ms", "15"), fg="steel blue", state='disabled')
        e12.grid(row=7, column=1)

        # ------------------------------------------------------------------

        # buttons and their working
        frame4 = Frame(root)
        frame4.pack(side=BOTTOM)
        price = Button(frame4, text="price \n list", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                       command=price)
        price.grid(row=0, column=0, padx=7, pady=7)
        total = Button(frame4, text="total \n amount", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                       command=amount)
        total.grid(row=0, column=5, padx=7, pady=7)
        reset = Button(frame4, text="reset", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                       command=reset)
        reset.grid(row=0, column=10, padx=7, pady=7)
        exit = Button(frame4, text="exit", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                      command=quit)
        exit.grid(row=0, column=15, padx=7, pady=7)
        bill = Button(frame4, text="generate \n bill", height=2, width=7, font=("comic sans ms", "11"), fg="steel blue",
                      command=call_bill)
        bill.grid(row=0, column=20, padx=7, pady=7)

        # --------------------------------------------------------

        # end of mainloop
        root.mainloop()

    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `member` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                HomeWindow()
                USERNAME.set("")
                PASSWORD.set("")
                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()

    second = Tk()
    second.title(" Login ")
    second.geometry("{0}x{1}+0+0".format(second.winfo_screenwidth(),second.winfo_screenheight()))
    load2 = Image.open("C:/Users/Lenovo/PycharmProjects/Restaurant_billing/adminlogin.jpg")
    background_image2 = ImageTk.PhotoImage(load2)
    background_label2 = Label(second, image=background_image2)
    background_label2.place(x=0, y=0, relheight=1, relwidth=1)

    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # ==============================FRAMES=========================================
    # Top = Frame(root)
    # Top.pack(side=TOP, fill=X,pady=50)
    # Top.place(relx=0.4,rely=0.2)
    Form = Frame(second, height=500, width=500, bg='white',borderwidth=2,relief='solid')
    # Form.pack(side=TOP, pady=100)
    # Form.pack(side=TOP,padx=40,pady=40)
    Form.place(relx=0.33, rely=0.2)
    # ==============================LABELS=========================================
    lbl_title = Label(Form, text="Enter \n Username  and  Password  \n to  Login ", font=('Lucida Handwriting', 15), bg='white',fg='LightSkyBlue3')
    lbl_title.grid(row=0, pady=30, columnspan=2)
    empty = Label(Form, text="", bg='white')
    empty.grid(row=1)

    lbl_username = Label(Form, text="Username:", font=('Lucida Handwriting', 12), bd=15, bg='white')
    lbl_username.grid(row=2, sticky='w', padx=20)
    lbl_password = Label(Form, text="Password:", font=('Lucida Handwriting', 12), bd=15, bg='white')
    lbl_password.grid(row=4, sticky='w', padx=20)
    lbl_text = Label(Form, bg='white')
    lbl_text.grid(row=6, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=('Lucida Handwriting',10), width=30,bg="gray99")
    username.grid(row=3, column=0, pady=5)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=('Lucida Handwriting',10), width=30,bg='gray99')
    password.grid(row=5, column=0, pady=5)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Log In", font=('Lucida Handwriting',15), width=30, command=Login,bg='LightSkyBlue3')
    btn_login.grid(pady=15, padx=30, row=8, columnspan=2, sticky='w')
    btn_login.bind('<Return>', Login)

    # ==============================NEW USER - SIGN UP=================================
    btn_signup = Button(Form, text="Cancel", font=('Lucida Handwriting',15), width=30, command=exit,bg='LightSkyBlue3')
    btn_signup.grid(pady=15, padx=30, row=9, columnspan=2, sticky='w')

    #Database for Login Username and password
    def Database():
        global conn, cursor
        conn = sqlite3.connect("admin.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `member` WHERE `username` = 'admin' AND `password` = 'admin123' and username='anubhav' and password='anubhav123'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `member` (username, password) VALUES('admin', 'admin123')")
            cursor.execute("INSERT INTO `member` (username, password) VALUES('anubhav', 'anubhav123')")
            conn.commit()
    second.mainloop()

#------------------------------------ CHEF CODE -----------------------------------
def secondchef_window():

    first.destroy()
    from PIL import Image, ImageTk
    def HomeChefWindow():
        secondchef.destroy()
        conn = sqlite3.connect('orderschef.db')
        cursor = conn.cursor()

        third = Tk()
        third.title(" SignUp ")
        third.geometry("{0}x{1}+0+0".format(third.winfo_screenwidth(), third.winfo_screenheight()))
        load2 = Image.open("C:/Users/Lenovo/PycharmProjects/Restaurant_billing/chef.jpg")
        background_image2 = ImageTk.PhotoImage(load2)
        background_label2 = Label(third, image=background_image2)
        background_label2.place(x=0, y=0, relheight=1, relwidth=1)

        # ==============================FRAMES=========================================

        Form = Frame(third, height=200, width=1000, bg='white', borderwidth=2, relief='solid')
        Form.place(relx=0.1, rely=0.20)

        cursor.execute(
            "SELECT ORDER_NUMBER FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        orderno = (cursor.fetchall())

        lbl_p = Label(Form, text=orderno, font=('Lucida Handwriting', 30), bd=15, bg='Red')
        lbl_p.grid(column=0, row=1, rowspan=2, sticky='w', padx=25, pady=30)
        #
        Form1 = Frame(third, height=200, width=1000, bg='white', borderwidth=2, relief='solid')
        Form1.place(relx=0.1, rely=0.5)
        #
        cursor.execute(
            "WITH CTE AS(SELECT ORDER_NUMBER,rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT ORDER_NUMBER FROM CTE WHERE number = 2;")
        orderno2 = (cursor.fetchall())

        lbl_p = Label(Form1, text=orderno2, font=('Lucida Handwriting', 30), bd=15, bg='Red')
        lbl_p.grid(column=0, row=1, rowspan=2, sticky='w', padx=25, pady=30)

        def delmin():
            conn = sqlite3.connect("orderschef.db")
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
            conn.commit()

        # ==============================BUTTON WIDGETS=================================
        btn_ready = Button(Form, text="READY", font=('Lucida Handwriting', 15), width=7, height=5, bg='LightGreen',
                           command=delmin)
        btn_ready.grid(pady=25, padx=30, column=10, row=1, sticky='w', rowspan=2)

        btn_ready = Button(Form1, text="READY", font=('Lucida Handwriting', 15), width=7, height=5, bg='LightGreen')
        btn_ready.grid(pady=25, padx=30, column=10, columnspan=2, rowspan=2, row=1, sticky='w')

        # ---------------------------------------------------------------------------------------

        # Create and display labels for each text value in different columns
        lbl1 = Label(Form, text="FRIES MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl1.grid(column=1, row=1, sticky='w', padx=5, pady=10)
        cursor.execute(
            "SELECT FRIES_MEAL FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        fries = (cursor.fetchall())
        lbl_fr = Label(Form, text=fries, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=1, row=2, sticky='w', padx=5, pady=10)

        lbl2 = Label(Form, text="LUNCH MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl2.grid(column=2, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "SELECT LUNCH_MEAL FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        lunch = (cursor.fetchall())
        lbl_fr = Label(Form, text=lunch, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=2, row=2, sticky='w', padx=5, pady=10)

        lbl3 = Label(Form, text="BURGER MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl3.grid(column=3, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "SELECT BURGER_MEAL FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        burger = (cursor.fetchall())
        lbl_fr = Label(Form, text=burger, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=3, row=2, sticky='w', padx=5, pady=10)

        lbl4 = Label(Form, text="PIZZA MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl4.grid(column=4, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "SELECT PIZZA_MEAL FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        pizza = (cursor.fetchall())
        lbl_fr = Label(Form, text=pizza, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=4, row=2, sticky='w', padx=5, pady=10)

        lbl5 = Label(Form, text="CHEESE BURGER", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl5.grid(column=5, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "SELECT CHEESE_BURGER FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        cheeseburger = (cursor.fetchall())
        lbl_fr = Label(Form, text=cheeseburger, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=5, row=2, sticky='w', padx=5, pady=10)

        lbl6 = Label(Form, text="DRINKS", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl6.grid(column=6, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "SELECT DRINKS FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        drinks = (cursor.fetchall())
        lbl_fr = Label(Form, text=drinks, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=6, row=2, sticky='w', padx=5, pady=10)

        lbl7 = Label(Form, text="MEAL_1", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl7.grid(column=7, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "SELECT MEAL_1  FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        meal1 = (cursor.fetchall())
        lbl_fr = Label(Form, text=meal1, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=7, row=2, sticky='w', padx=5, pady=10)

        lbl8 = Label(Form, text="MEAL_2", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl8.grid(column=8, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "SELECT MEAL_2 FROM ORDERSCHEF WHERE ORDER_NUMBER IN(SELECT MIN(ORDER_NUMBER) FROM ORDERSCHEF);")
        meal2 = (cursor.fetchall())
        lbl_fr = Label(Form, text=meal2, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=8, row=2, sticky='w', padx=5, pady=10)

        # Create and display labels for each text value in different columns
        lbl9 = Label(Form1, text="FRIES MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl9.grid(column=1, row=1, sticky='w', padx=5, pady=10)
        cursor.execute(
            "WITH CTE AS(SELECT FRIES_MEAL, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT FRIES_MEAL FROM CTE WHERE number = 2;")
        fries = (cursor.fetchall())
        lbl_fr9 = Label(Form1, text=fries, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr9.grid(column=1, row=2, sticky='w', padx=5, pady=10)

        lbl10 = Label(Form1, text="LUNCH MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl10.grid(column=2, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "WITH CTE AS(SELECT LUNCH_MEAL, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT LUNCH_MEAL FROM CTE WHERE number = 2;")
        lunch = (cursor.fetchall())
        lbl_fr10 = Label(Form1, text=lunch, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr10.grid(column=2, row=2, sticky='w', padx=5, pady=10)

        lbl11 = Label(Form1, text="BURGER MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl11.grid(column=3, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "WITH CTE AS(SELECT BURGER_MEAL, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT BURGER_MEAL FROM CTE WHERE number = 2;")
        burger = (cursor.fetchall())
        lbl_fr11 = Label(Form1, text=burger, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr11.grid(column=3, row=2, sticky='w', padx=5, pady=10)

        lbl12 = Label(Form1, text="PIZZA MEAL", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl12.grid(column=4, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "WITH CTE AS(SELECT PIZZA_MEAL, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT PIZZA_MEAL FROM CTE WHERE number = 2;")
        pizza = (cursor.fetchall())
        lbl_fr12 = Label(Form1, text=pizza, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr12.grid(column=4, row=2, sticky='w', padx=5, pady=10)

        lbl13 = Label(Form1, text="CHEESE BURGER", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl13.grid(column=5, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "WITH CTE AS(SELECT CHEESE_BURGER, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT CHEESE_BURGER FROM CTE WHERE number = 2;")
        cheeseburger = (cursor.fetchall())
        lbl_fr13 = Label(Form1, text=cheeseburger, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr13.grid(column=5, row=2, sticky='w', padx=5, pady=10)

        lbl14 = Label(Form1, text="DRINKS", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl14.grid(column=6, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "WITH CTE AS(SELECT DRINKS, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT DRINKS FROM CTE WHERE number = 2;")
        drinks = (cursor.fetchall())
        lbl_fr = Label(Form1, text=drinks, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=6, row=2, sticky='w', padx=5, pady=10)

        lbl15 = Label(Form1, text="MEAL_1", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl15.grid(column=7, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "WITH CTE AS(SELECT MEAL_1, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT MEAL_1 FROM CTE WHERE number = 2;")
        meal1 = (cursor.fetchall())
        lbl_fr = Label(Form1, text=meal1, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=7, row=2, sticky='w', padx=5, pady=10)

        lbl16 = Label(Form1, text="MEAL_2", font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl16.grid(column=8, row=1, sticky='w', padx=5, pady=5)
        cursor.execute(
            "WITH CTE AS(SELECT MEAL_2, rank() OVER(ORDER BY ORDER_NUMBER) AS number FROM ORDERSCHEF ) SELECT MEAL_2 FROM CTE WHERE number = 2;")
        meal2 = (cursor.fetchall())
        lbl_fr = Label(Form1, text=meal2, font=('Lucida Handwriting', 10), bd=15, bg='White', anchor='center')
        lbl_fr.grid(column=8, row=2, sticky='w', padx=5, pady=10)

        third.mainloop()
    def Login(event=None):
        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_text.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM `SDATA` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                HomeChefWindow()
                USERNAME.set("")
                PASSWORD.set("")
                lbl_text.config(text="")
            else:
                lbl_text.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
        cursor.close()
        conn.close()
    def third_window():
        secondchef.destroy()
        def Signup(event=None):
            if (
                    NAME.get() == "" or
                    CONTACT_NO.get() == "" or
                    EMAIL.get() == "" or
                    USERNAME.get() == "" or
                    PASSWORD.get() == "" or
                    CONFIRM_PASSWORD.get() == ""
            ):
                lbl_text.config(text="Please complete all required fields!", fg="red")
            elif PASSWORD.get() != CONFIRM_PASSWORD.get():
                lbl_text.config(text="Password does not match the confirmed password!", fg="red")
            else:
                # All fields are filled and passwords match
                # You should insert the user data into the database here
                # Assuming you have a database connection `conn` and cursor `cursor`
                conn = sqlite3.connect("Signupdata.db")
                cursor = conn.cursor()
                cursor.execute('''CREATE TABLE IF NOT EXISTS SDATA
                            (Name TEXT NOT NULL, Contactno TEXT NOT NULL, Email TEXT NOT NULL,Username TEXT PRIMARY KEY ,Password TEXT NOT NULL,Confirmpassword TEXT NOT NULL);''')
                cursor.execute("INSERT INTO SDATA "
                               "(Name, Contactno, Email, Username, Password, Confirmpassword)"
                               "VALUES (?, ?, ?, ?, ?, ?)",
                               (
                                   NAME.get(),
                                   CONTACT_NO.get(),
                                   EMAIL.get(),
                                   USERNAME.get(),
                                   PASSWORD.get(),
                                   CONFIRM_PASSWORD.get()
                               )
                               )
                cursor.close()
                conn.commit()  # Commit the changes to the database
                conn.close()  # Close the database connection
                lbl_text.config(text="Signup successful!", fg="green")

        third = Tk()
        third.title(" SignUp ")
        third.geometry("{0}x{1}+0+0".format(third.winfo_screenwidth(), third.winfo_screenheight()))
        load3 = Image.open("C:/Users/Lenovo/PycharmProjects/Restaurant_billing/login.jpg")
        background_image3 = ImageTk.PhotoImage(load3)
        background_label3 = Label(third, image=background_image3)
        background_label3.place(x=0, y=0, relheight=1, relwidth=1)

        # ==============================VARIABLES======================================
        USERNAME = StringVar()
        PASSWORD = StringVar()
        CONFIRM_PASSWORD = StringVar()
        NAME = StringVar()
        CONTACT_NO = StringVar()
        EMAIL = StringVar()

        # ==============================FRAMES=========================================
        # Top = Frame(root)
        # Top.pack(side=TOP, fill=X,pady=50)
        # Top.place(relx=0.4,rely=0.2)
        Form = Frame(third, height=500, width=500, bg='white', borderwidth=2, relief='solid')
        # Form.pack(side=TOP, pady=100)
        # Form.pack(side=TOP,padx=40,pady=40)
        Form.place(relx=0.33, rely=0.05)
        # ==============================LABELS=========================================
        lbl_title = Label(Form, text="Signup Page", font=('Lucida Handwriting', 15),
                          bg='white', fg='LightSkyBlue3')
        lbl_title.grid(row=0, pady=15, columnspan=2)

        lbl_name = Label(Form, text="Name:", font=('Lucida Handwriting', 12), bd=15, bg='white')
        lbl_name.grid(row=1, sticky='w', padx=20)

        lbl_contactno = Label(Form, text="Contact:", font=('Lucida Handwriting', 12), bd=15, bg='white')
        lbl_contactno.grid(row=3, sticky='w', padx=20)

        lbl_email = Label(Form, text="Email:", font=('Lucida Handwriting', 12), bd=15, bg='white')
        lbl_email.grid(row=5, sticky='w', padx=20)

        lbl_username1 = Label(Form, text="Username:", font=('Lucida Handwriting', 12), bd=15, bg='white')
        lbl_username1.grid(row=7, sticky='w', padx=20)

        lbl_password1 = Label(Form, text="Password:", font=('Lucida Handwriting', 12), bd=15, bg='white')
        lbl_password1.grid(row=9, sticky='w', padx=20)

        lbl_confirmpassword = Label(Form, text="Confirm Password:", font=('Lucida Handwriting', 12), bd=15, bg='white')
        lbl_confirmpassword.grid(row=11, sticky='w', padx=20)

        lbl_text = Label(Form, bg='white')
        lbl_text.grid(row=13, columnspan=2)
        # ==============================ENTRY WIDGETS==================================

        name = Entry(Form, textvariable=NAME, font=('Lucida Handwriting', 10), width=30, bg='gray99')
        name.grid(row=2, column=0, pady=5,padx=65)

        contactno = Entry(Form, textvariable=CONTACT_NO, font=('Lucida Handwriting', 10), width=30, bg='gray99')
        contactno.grid(row=4, column=0, pady=5)

        email = Entry(Form, textvariable=EMAIL, font=('Lucida Handwriting', 10), width=30, bg='gray99')
        email.grid(row=6, column=0, pady=5)

        username = Entry(Form, textvariable=USERNAME, font=('Lucida Handwriting', 10), width=30, bg="gray99")
        username.grid(row=8, column=0, pady=5)

        password = Entry(Form, textvariable=PASSWORD, show="*", font=('Lucida Handwriting', 10), width=30, bg='gray99')
        password.grid(row=10, column=0, pady=5)

        confirmpassword = Entry(Form, textvariable=CONFIRM_PASSWORD, show="*", font=('Lucida Handwriting', 10),
                                width=30,
                                bg='gray99')
        confirmpassword.grid(row=12, column=0, pady=5)

        # ==============================BUTTON WIDGETS=================================
        btn_signup = Button(Form, text="Sign Up", font=('Lucida Handwriting', 15), width=30, command=Signup,
                            bg='LightSkyBlue3')
        btn_signup.grid(pady=5, padx=30, row=14, columnspan=2, sticky='w')
        btn_signup.bind('<Return>', Signup)


        btn_login1 = Button(Form, text="Back to Login", font=('Lucida Handwriting', 15), width=30, command=third.destroy,
                            bg='LightSkyBlue3')
        btn_login1.grid(pady=15, padx=30, row=15, columnspan=2, sticky='w')


        third.mainloop()

    secondchef = Tk()
    secondchef.title(" Login ")
    secondchef.geometry("{0}x{1}+0+0".format(secondchef.winfo_screenwidth(), secondchef.winfo_screenheight()))
    load2 = Image.open("C:/Users/Lenovo/PycharmProjects/Restaurant_billing/cheflogin.jpg")
    background_image2 = ImageTk.PhotoImage(load2)
    background_label2 = Label(secondchef, image=background_image2)
    background_label2.place(x=0, y=0, relheight=1, relwidth=1)

    # ==============================VARIABLES======================================
    USERNAME = StringVar()
    PASSWORD = StringVar()

    # ==============================FRAMES=========================================
    # Top = Frame(root)
    # Top.pack(side=TOP, fill=X,pady=50)
    # Top.place(relx=0.4,rely=0.2)
    Form = Frame(secondchef, height=500, width=500, bg='white', borderwidth=2, relief='solid')
    # Form.pack(side=TOP, pady=100)
    # Form.pack(side=TOP,padx=40,pady=40)
    Form.place(relx=0.33, rely=0.2)
    # ==============================LABELS=========================================
    lbl_title = Label(Form, text="Enter \n Username  and  Password  \n to  Login ", font=('Lucida Handwriting', 15),
                      bg='white', fg='LightSkyBlue3')
    lbl_title.grid(row=0, pady=30, columnspan=2)
    empty = Label(Form, text="", bg='white')
    empty.grid(row=1)

    lbl_username = Label(Form, text="Username:", font=('Lucida Handwriting', 12), bd=15, bg='white')
    lbl_username.grid(row=2, sticky='w', padx=20)
    lbl_password = Label(Form, text="Password:", font=('Lucida Handwriting', 12), bd=15, bg='white')
    lbl_password.grid(row=4, sticky='w', padx=20)
    lbl_text = Label(Form, bg='white')
    lbl_text.grid(row=6, columnspan=2)

    # ==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=('Lucida Handwriting', 10), width=30, bg="gray99")
    username.grid(row=3, column=0, pady=5)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=('Lucida Handwriting', 10), width=30, bg='gray99')
    password.grid(row=5, column=0, pady=5)

    # ==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Log In", font=('Lucida Handwriting', 15), width=30, bg='LightSkyBlue3',command=Login)
    btn_login.grid(pady=15, padx=30, row=8, columnspan=2, sticky='w')
    btn_login.bind('<Return>', Login)

    # ==============================NEW USER - SIGN UP=================================
    btn_signup = Button(Form, text="Sign Up (New User)", font=('Lucida Handwriting', 15), width=30, bg='LightSkyBlue3',command=third_window)
    btn_signup.grid(pady=15, padx=30, row=9, columnspan=2, sticky='w')

    def Database():
        global conn, cursor
        conn = sqlite3.connect("signupdata.db")
        cursor = conn.cursor()

    secondchef.mainloop()


# Create the main application window
first=Tk()
first.geometry("{0}x{1}+0+0".format(first.winfo_screenwidth(), first.winfo_screenheight()))
load4=Image.open("C:/Users/Lenovo/PycharmProjects/Restaurant_billing/fd1.jpg")
background_image4=ImageTk.PhotoImage(load4)
background_label4=Label(first, image=background_image4)
background_label4.place(x=0,y=0,relheight=1,relwidth=1)
background_label4.config(bg="white")

welcome=Label(first,text="        Welcome to The Anubhav Spices Restaurant ",font=("comic sans ms",'30',"bold"),fg="orange",bd=10,anchor=W,bg="white")
welcome.grid(row=5,column=10)

adminlogin=Button(first,text="ADMIN LOGIN",bg="white",font=("comic sans ms",'20',"bold"),fg="orange",command=second_window)
adminlogin.place(relx=0.2, rely=0.4, anchor=NE)
adminlogin.config(cursor="heart")

cheflogin=Button(first,text="CHEF LOGIN",bg="white",font=("comic sans ms",'20',"bold"),fg="orange",command=secondchef_window)
cheflogin.place(relx=0.4, rely=0.4, anchor=NE)
cheflogin.config(cursor="heart")

cancel=Button(first,text="CANCEL",bg="white",font=("comic sans ms",'20',"bold"),fg="orange",command=exit)
cancel.place(relx=0.55, rely=0.4, anchor=NE)
cancel.config(cursor="heart")

first.mainloop()
