from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import random
from datetime import *

root = Tk()
page_home = Frame(root)
root.geometry("800x400")
root.title("Railways")
l1 = Label(root, text="RAILWAY RESERVATION", bg="brown", fg="white", font=50).grid(row=0, column=1000)
# l1.grid(row=0,column=1000)
import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")

conn.execute('''CREATE TABLE RAILWAYS
         (ID INT PRIMARY KEY  NOT NULL,
         NAME  TEXT  NOT NULL,
         STARTING_LOCATION TEXT  NOT NULL,
         DESTINATION TEXT  NOT NULL,
         DEPARTURE_TIME NOT NULL );''')
print("Table created successfully")

conn.execute('''CREATE TABLE CLASS
            (ID TEXT NOT NULL,
            CLASS TEXT NOT NULL,
            FARE INT NOT NULL,
            SEATS_AVAILABLE INT);''')

conn.execute("INSERT INTO RAILWAYS (ID,NAME,STARTING_LOCATION,DESTINATION,DEPARTURE_TIME) \
      VALUES (2309, 'Avantika Express', 'Indore_Jn', 'Mumbai_Central', '9:00A.M' )")

conn.execute("INSERT INTO RAILWAYS (ID,NAME,STARTING_LOCATION,DESTINATION,DEPARTURE_TIME) \
      VALUES (3275, 'Brindavan Express', 'Bangalore', 'Chennai_Central', '10:00A.M' )")

conn.execute("INSERT INTO RAILWAYS (ID,NAME,STARTING_LOCATION,DESTINATION,DEPARTURE_TIME) \
      VALUES (4375, 'Deccan Express', 'Mumbai', 'Pune', '11:00A.M' )")

conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('2309','1A',23000,5 )")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('2309','2A',13000,4 )")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('2309','3A',13000,3 )")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('2309','SL',10000,2)")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('2309','2S',8000,5)")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('3275','1A',23000,5 )")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('3275','2A',13000,8 )")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('3275','3A',13000,9 )")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('3275','SL',10000,12 )")
conn.execute("INSERT INTO CLASS (ID,CLASS,FARE,SEATS_AVAILABLE) \
      VALUES ('3275','2S',8000,5 )")

'''
cursor = conn.execute("SELECT ID,NAME, STARTING_LOCATION,DESTINATION,DEPARTURE_TIME from RAILWAYS ")
for row in cursor:
   print("TRAIN NUMBER = ", row[0])
   print("NAME = ", row[1])
   print("STARTING LOCATION = ", row[2])
   print("DESTINATION = ", row[3])
   print("TIME OF DEPARTURE = ",row[4])

'''

conn.execute('''CREATE TABLE SEAT_INFO
            (ID TEXT NOT NULL,
            DATE TEXT NOT NULL,
            CLASS TEXT NOT NULL,
            SEATS INT NOT NULL,
            BOOKED_STATUS TEXT NOT NULL);''')

conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',1,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',2,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',3,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',4,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',5,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',6,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',7,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','1A',8,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2A',9,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2A',10,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2A',11,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2A',12,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2A',13,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2A',14,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2A',15,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','3A',16,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','3A',17,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','3A',18,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','3A',19,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2L',20,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2L',21,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2L',22,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2L',23,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2S',24,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2S',25,'YES' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2S',26,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2S',27,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2S',28,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2S',29,'NO' )")
conn.execute("INSERT INTO SEAT_INFO (ID,DATE,CLASS,SEATS,BOOKED_STATUS) \
      VALUES ('2309','2020-03-18','2S',30,'NO' )")

conn.execute('''CREATE TABLE PERSONAL_INFO
            (NAME TEXT PRIMARY KEY NOT NULL,
            PASSWORD TEXT NOT NULL,
            ADDRESS TEXT NOT NULL,
            NUMBER INT NOT NULL,
            EMAIL TEXT NOT NULL);''')

conn.execute("INSERT INTO PERSONAL_INFO (NAME,PASSWORD,ADDRESS,NUMBER,EMAIL) \
      VALUES ('SHRUTHI','SHRUPES','BANGALORE',7619568999,'saishruthi@gmail.com' )")
conn.execute("INSERT INTO PERSONAL_INFO (NAME,PASSWORD,ADDRESS,NUMBER,EMAIL) \
      VALUES ('SAHANA','SAHANAPES','BANGALORE',7676283621,'sahanam308@gmail.com' )")
conn.execute("INSERT INTO PERSONAL_INFO (NAME,PASSWORD,ADDRESS,NUMBER,EMAIL) \
      VALUES ('ROSHNI','ROSHNIPES','BANGALORE',8904146651,'roshnishivu50@gmail.com' )")

conn.execute('''CREATE TABLE BOOKING_INFO
            (NAME TEXT  NOT NULL,
            PNR TEXT PRIMARY KEY NOT NULL,
            TRAIN_NO INT NOT NULL,
            DATE TEXT NOT NULL,
            CLASS TEXT NOT NULL,
            SEAT INT NOT NULL,
            AMOUNT INT NOT NULL,
            STATUS TEXT NOT NULL);''')

conn.execute("INSERT INTO BOOKING_INFO (NAME,PNR,TRAIN_NO,DATE,CLASS,SEAT,AMOUNT,STATUS) \
      VALUES ('SHRUTHI','123',2309,'2021-03-18','1A',2,46000,'BOOKED' )")
conn.execute("INSERT INTO BOOKING_INFO (NAME,PNR,TRAIN_NO,DATE,CLASS,SEAT,AMOUNT,STATUS) \
      VALUES ('SAHANA','146',2309,'2021-03-19','2A',1,13000,'BOOKED' )")
conn.execute("INSERT INTO BOOKING_INFO (NAME,PNR,TRAIN_NO,DATE,CLASS,SEAT,AMOUNT,STATUS) \
      VALUES ('ROSHNI','203',2309,'2021-03-19','1A',2,46000,'CANCELLED' )")
conn.execute("INSERT INTO BOOKING_INFO (NAME,PNR,TRAIN_NO,DATE,CLASS,SEAT,AMOUNT,STATUS) \
      VALUES ('SUPRAJA','243',2309,'2021-03-19','SL',2,20000,'BOOKED' )")

conn.commit()


def raise_frame(frame):
    frame.tkraise()


f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
f4 = Frame(root)
f5 = Frame(root)
f6 = Frame(root)
f7 = Frame(root)
f8 = Frame(root)
f9 = Frame(root)
f10 = Frame(root)
f11 = Frame(root)
f12 = Frame(root)
f13 = Frame(root)
f14 = Frame(root)

for frame in (f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14):
    frame.grid(row=1000, column=1000, sticky="news")

b1 = Button(f1, text="CHECK TRAIN DETAILS", font=14, command=lambda: raise_frame(f2))
b1.grid(row=2, column=5, padx=10, pady=10)

sql_select_query1 = """select STARTING_LOCATION from RAILWAYS"""
cursor1 = conn.cursor()
cursor1.execute(sql_select_query1)
records1 = cursor1.fetchall()
start = StringVar()
l1 = Label(f2, text="From city", font=14).grid(row=20, column=10)
c1 = ttk.Combobox(f2, value=records1, textvariable=start).grid(row=20, column=20)

sql_select_query2 = """select DESTINATION from RAILWAYS"""
cursor2 = conn.cursor()
cursor2.execute(sql_select_query2)
records2 = cursor2.fetchall()
dest = StringVar()
l2 = Label(f2, text="Destination", font=14).grid(row=40, column=10)
c2 = ttk.Combobox(f2, value=records2, textvariable=dest).grid(row=40, column=20)

class1 = StringVar()
l3 = Label(f2, text="Class", font=14).grid(row=60, column=10)
c3 = ttk.Combobox(f2, value=["1A", "2A", "3A", "SL", "2S"], textvariable=class1).grid(row=60, column=20)

date1 = StringVar()
l4 = Label(f2, text="Date of travel", font=14).grid(row=80, column=10)
s4 = Spinbox(f2, value=("2020-03-18", "2020-03-19"), textvariable=date1).grid(row=80, column=20)

b2 = Button(f2, text="<<Prev", command=lambda: raise_frame(f1))
b2.grid(row=10, column=0)


def train_details():
    origin = start.get()
    destination = dest.get()
    class2 = class1.get()
    global id, train_name, starting, ending, time1, class3, fare, seats, date2
    date2 = date1.get()
    print(date2)
    sql_select_query3 = """select * from RAILWAYS  where STARTING_LOCATION = ? AND DESTINATION = ?"""
    cursor3 = conn.cursor()
    cursor3.execute(sql_select_query3, (origin, destination))
    for row in cursor3:
        print("TRAIN NUMBER = ", row[0])
        id = str(row[0])
        train_name = str(row[1])
        starting = str(row[2])
        ending = str(row[3])
        time1 = str(row[4])
    print("TRAIN NUMBER = ", id)
    num = str(id)
    sql_select_query4 = """select * from CLASS where ID = ? AND CLASS = ?"""
    cursor4 = conn.cursor()
    cursor4.execute(sql_select_query4, (num, class2))
    for row in cursor4:
        print("CLASS : ", row[1])
        class3 = str(row[1])
        print("FARE: ", row[2])
        fare = str(row[2])
        seats = str(row[3])
    raise_frame(f3)
    T = Text(f3, height=15, width=52)
    s_id = "ID: " + id + "\n" + "TRAIN NAME: " + train_name + "\n" + "STARING LOCATION: " + starting + "\n" + "DESTINATION: " + ending + "\n" + "TIME OF DEPARTURE: " + time1 + "\n" + "CLASS: " + class3 + "\n" + "FARE: " + fare + "\n" + "SEATS AVAILABLE: " + seats
    T.insert(END, s_id)
    T.grid(row=10, column=10)


b3 = Button(f2, text="SUBMIT", command=train_details, font=4)
b3.grid(row=90, column=90)

b31 = Button(f3, text="BOOK THE TICKET", command=lambda: raise_frame(f4), font=4)
b31.grid(row=80, column=90)

b4 = Button(f4, text="<<Prev", command=lambda: raise_frame(f3))
b4.grid(row=20, column=0)

b5 = Button(f1, text="CHECK BOOKING STATUS", font=14, command=lambda: raise_frame(f13))
b5.grid(row=4, column=5, padx=10, pady=10)

name_var2 = StringVar()
passw_var2 = StringVar()
lb1 = Label(f13, text="Username", font=14)
lb1.grid(row=40, column=10)
name_entry1 = Entry(f13, textvariable=name_var2)
name_entry1.grid(row=40, column=20)

lb2 = Label(f13, text="Password", font=14)
lb2.grid(row=60, column=10)
pass_entry1 = Entry(f13, textvariable=passw_var2, show="*")
pass_entry1.grid(row=60, column=20)


def status():
    global pnr2
    name1 = name_var2.get()
    sql_select_query6 = """select * from BOOKING_INFO  where NAME = ?"""
    cursor6 = conn.cursor()
    cursor6.execute(sql_select_query6, (name1,))
    global name2, train_no1, date2, class4, seat1, amount1, status1
    for row in cursor6:
        # NAME,PNR,TRAIN_NO,DATE,CLASS,SEAT,AMOUNT,STATUS
        name2 = str(row[0])
        pnr2 = str(row[1])
        train_no1 = str(row[2])
        date2 = str(row[3])
        class4 = str(row[4])
        seat1 = str(row[5])
        amount1 = str(row[6])
        status1 = str(row[7])
    raise_frame(f14)
    if (status1 == "BOOKED"):
        lab3 = Label(f14, text="BOOKED", font=14).grid(row=40, column=10)
        sql_select_query7 = """select * from RAILWAYS  where ID = ?"""
        cursor7 = conn.cursor()
        cursor7.execute(sql_select_query7, (train_no1,))
        global train_name1, starting1, ending1, time2
        for row in cursor7:
            train_name1 = str(row[1])
            starting1 = str(row[2])
            ending1 = str(row[3])
            time2 = str(row[4])
        T = Text(f14, height=15, width=52)
        s_id = "NAME: " + name2 + "\n" + "PNR:  " + pnr2 + "\n" + "TRAIN ID: " + train_no1 + "\n" + "TRAIN NAME: " + train_name1 + "\n" + "STARING LOCATION: " + starting1 + "\n" + "DESTINATION: " + ending1 + "\n" + "TIME OF DEPARTURE: " + time2 + "\n" + "CLASS: " + class4 + "\n" + "FARE: " + amount1 + "\n" + "SEATS: " + seat1
        T.insert(END, s_id)
        T.grid(row=10, column=10)
    else:
        lab3 = Label(f14, text="CANCELLED", font=14).grid(row=40, column=10)
    pb2 = Button(f14, text="<<prev", command=lambda: raise_frame(f1)).grid(row=0, column=0)


b102 = Button(f13, text="SUBMIT", command=status, font=4)
b102.grid(row=90, column=90)


def cancel():
    raise_frame(f12)

    sql_select_query4 = """select * from BOOKING_INFO where NAME = ?"""
    cursor4 = conn.cursor()
    cursor4.execute(sql_select_query4, (name1,))
    global no_of_seats1
    for row in cursor4:
        no_of_seats1 = row[5]
    today = date.today()
    days1 = timedelta(1)
    days2 = timedelta(2)
    new_date1 = today + days1
    new_date2 = today + days2
    date_time_obj = datetime.strptime(date2, '%Y-%m-%d').date()
    if (new_date1 == date_time_obj):
        lab1 = Label(f12, text="50% of the amount paid shall be refunded:", font=14).grid(row=40, column=10)
        refund = (50.0 / 100) * int(amount1)
        lab11 = Label(f12, text=refund, font=14).grid(row=50, column=10)
        print(refund)
    elif (new_date2 == date_time_obj):
        lab2 = Label(f12, text="70% of the amount paid shall be refunded:", font=14).grid(row=40, column=10)
        refund = (70.0 / 100) * int(amount1)
        lab21 = Label(f12, text=refund, font=14).grid(row=50, column=10)
        print(refund)
    else:
        lab3 = Label(f12, text="Your total amount will be refunded:", font=14).grid(row=40, column=10)
        refund = int(amount1)
        lab31 = Label(f12, text=refund, font=14).grid(row=50, column=10)
        print(refund)

    def callback():
        if mb.askyesno('Verify', 'Are you sure you want to cancel??'):
            mb.showinfo("Cancel", "Ticket has been cancelled successfully")
            exit()
        else:
            mb.showinfo('No', 'Good Choice..Happy journey')

    b = Button(f12, text='Verify', command=callback, font=4).grid()


pb3 = Button(f12, text="<<prev", command=lambda: raise_frame(f1)).grid(row=0, column=0)


def login():
    global name1, password1, address1, number1, email1
    name1 = name_var1.get()
    password1 = passw_var1.get()

    print("The name is : " + name1)
    print("The password is : " + password1)

    name_var1.set("")
    passw_var1.set("")
    sql_select_query3 = """select * from PERSONAL_INFO  where NAME = ? AND PASSWORD = ?"""
    cursor3 = conn.cursor()
    cursor3.execute(sql_select_query3, (name1, password1))
    for row in cursor3:
        name1 = row[0]
        address1 = str(row[2])
        number1 = str(row[3])
        email1 = str(row[4])
    raise_frame(f10)
    global pnr1
    pnr1 = StringVar()
    l12 = Label(f10, text="PNR", font=14)
    l12.grid(row=40, column=10)
    pnr_entry = Entry(f10, textvariable=pnr1)
    pnr_entry.grid(row=40, column=20)
    b103 = Button(f10, text="SUBMIT", command=confirmation, font=4)
    b103.grid(row=90, column=9)


def confirmation():
    global pnr2
    pnr2 = pnr1.get()
    pnr1.set("")
    sql_select_query5 = """select * from BOOKING_INFO  where NAME = ? AND PNR = ?"""
    cursor5 = conn.cursor()
    cursor5.execute(sql_select_query5, (name1, pnr2))
    global name2, train_no1, date2, class4, seat1, amount1
    for row in cursor5:
        # NAME,PNR,TRAIN_NO,DATE,CLASS,SEAT,AMOUNT,STATUS
        name2 = str(row[0])
        train_no1 = str(row[2])
        date2 = str(row[3])
        class4 = str(row[4])
        seat1 = str(row[5])
        amount1 = str(row[6])
    sql_select_query3 = """select * from RAILWAYS  where ID = ?"""
    cursor3 = conn.cursor()
    cursor3.execute(sql_select_query3, (train_no1,))
    global train_name1, starting1, ending1, time2
    for row in cursor3:
        train_name1 = str(row[1])
        starting1 = str(row[2])
        ending1 = str(row[3])
        time2 = str(row[4])
    raise_frame(f11)
    T = Text(f11, height=15, width=52)
    s_id = "NAME: " + name2 + "\n" + "PNR:  " + pnr2 + "\n" + "TRAIN ID: " + train_no1 + "\n" + "TRAIN NAME: " + train_name1 + "\n" + "STARING LOCATION: " + starting1 + "\n" + "DESTINATION: " + ending1 + "\n" + "TIME OF DEPARTURE: " + time2 + "\n" + "CLASS: " + class4 + "\n" + "FARE: " + amount1 + "\n" + "SEATS NUMBER: " + seat1
    T.insert(END, s_id)
    T.grid(row=10, column=10)
    bt12 = Button(f11, text="CONFIRM", command=cancel)
    bt12.grid(row=4, column=5, padx=10, pady=10)


name_var1 = StringVar()
passw_var1 = StringVar()

bt1 = Button(f1, text="CANCEL THE TICKET", font=14, command=lambda: raise_frame(f9))
bt1.grid(row=6, column=5, padx=10, pady=10)

l11 = Label(f9, text="Username", font=14)
l11.grid(row=40, column=10)
name_entry1 = Entry(f9, textvariable=name_var1)
name_entry1.grid(row=40, column=20)

l21 = Label(f9, text="Password", font=14)
l21.grid(row=60, column=10)
pass_entry1 = Entry(f9, textvariable=passw_var1, show="*")
pass_entry1.grid(row=60, column=20)

b102 = Button(f9, text="SUBMIT", command=login, font=4)
b102.grid(row=90, column=90)

name_var = StringVar()
passw_var = StringVar()


def submit():
    global name, password, address, number, email
    name = name_var.get()
    password = passw_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    passw_var.set("")
    sql_select_query3 = """select * from PERSONAL_INFO  where NAME = ? AND PASSWORD = ?"""
    cursor3 = conn.cursor()
    cursor3.execute(sql_select_query3, (name, password))
    result1 = cursor3.fetchone()
    if result1:
        raise_frame(f6)
        for row in cursor3:
            name = row[0]
            password = str(row[1])
            address = str(row[2])
            number = str(row[3])
            email = str(row[4])

    else:
        mb.showinfo("ERROR", "Wrong username or password!")

    l9 = Label(f6, text="No.of seats\n you wish to book", fg="red", font=10)
    l9.grid(row=60, column=1)
    global seats1
    seats1 = StringVar()
    c9 = Spinbox(f6, value=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), textvariable=seats1, font=10)
    c9.grid(row=60, column=80)
    b62 = Button(f6, text="PROCEED & PAY", command=payment, font=8)
    b62.grid(row=300, column=50)


def payment():
    global amount, no_of_seats
    no_of_seats = seats1.get()
    raise_frame(f7)
    T1 = Text(f7, height=5, width=20)
    amount = int(fare) * int(no_of_seats)
    text_fare = "Net Amount: " + str(amount)
    T1.insert(END, text_fare)
    T1.grid(row=10, column=10)
    b9 = Button(f7, text="<<Prev", command=lambda: raise_frame(f6))
    b9.grid(row=0, column=0)
    b10 = Button(f7, text="SUBMIT", command=message, font=4)
    b10.grid(row=90, column=90)


def message():
    raise_frame(f8)
    mb.showinfo("Booking Confirmed", "Confirmation")
    l1 = Label(f8, text="TICKET", font=14).grid(row=40, column=10)
    global pnr
    pnr = random.randint(100, 999)

    def pnr_check(pnr):
        cursor3 = conn.cursor()
        cursor3.execute("""SELECT PNR FROM BOOKING_INFO WHERE PNR = ?""", (str(pnr),))
        result = cursor3.fetchone()
        return result

    result = pnr_check(pnr)
    if result:
        pnr = random.randint(100, 99)
        pnr_check(pnr)
    else:
        l1 = Label(f8, text="TICKET", font=14).grid(row=40, column=10)
        Booking_details = "PNR: " + str(pnr) + "\n" + "TRAIN ID: " + str(
            id) + "\n" + "TRAIN NAME: " + train_name + "\n" + "STARTING LOCATION: " + starting + "\n" + "DESTINATION: " + ending + "\n" + "TIME OF DEPARTURE: " + str(
            time1) + "\n" + "DATE: " + date2 + "\n" + "CLASS: " + class3 + "\n" + "FARE: " + fare + "\n" + "NAME: " + name + "\n"  # +  "NUMBER: " + number + "\n" + "EMAIL: " + email
        T2 = Text(f8, height=50, width=50)
        T2.insert(END, Booking_details)
        T2.grid(row=25, column=60)


username_var = StringVar()
password_var = StringVar()
address_var = StringVar()
phno_var = StringVar()
email_var = StringVar()


def save():
    username = username_var.get()
    pass1 = password_var.get()
    addr = address_var.get()
    phone = phno_var.get()
    mail = email_var.get()

    conn.execute("INSERT OR IGNORE INTO PERSONAL_INFO (NAME,PASSWORD,ADDRESS,NUMBER,EMAIL)\
            VALUES(?,?,?,?,?)",
                 [username, pass1, addr, phone, mail])

    if username == "" or pass1 == "" or addr == "" or phone == "" or mail == "":
        mb.showinfo("ERROR", "Enter all the fields!!")

    else:
        raise_frame(f4)


l1 = Label(f4, text="Username", font=14).grid(row=40, column=10)
name_entry = Entry(f4, textvariable=name_var).grid(row=40, column=20)

l2 = Label(f4, text="Password", font=14).grid(row=60, column=10)
pass_entry = Entry(f4, textvariable=passw_var, show="*").grid(row=60, column=20)

b6 = Button(f4, text="SUBMIT", command=submit, font=4)
b6.grid(row=90, column=90)

b7 = Button(f5, text="<<Prev", command=lambda: raise_frame(f4))
b7.grid(row=20, column=0)

b8 = Button(f4, text="REGISTER", font=4, command=lambda: raise_frame(f5))
b8.grid(row=90, column=120)

b1 = Button(f5, text="<<Prev", command=lambda: raise_frame(f4))
b1.grid(row=20, column=0)

l3 = Label(f5, text="Username", fg="purple", font=10).grid(row=60, column=10)
e3 = Entry(f5, textvariable=username_var).grid(row=60, column=20)

l4 = Label(f5, text="Password", fg="purple", font=10).grid(row=60, column=60)
e4 = Entry(f5, textvariable=password_var).grid(row=60, column=100)

l5 = Label(f5, text="Age", fg="purple", font=10).grid(row=100, column=10)
e5 = Entry(f5).grid(row=100, column=20)

l6 = Label(f5, text="Phone number", fg="purple", font=10).grid(row=100, column=60)
e6 = Entry(f5, textvariable=phno_var).grid(row=100, column=100)

l7 = Label(f5, text="Email", fg="purple", font=10).grid(row=140, column=10)
e7 = Entry(f5, textvariable=email_var).grid(row=140, column=20)

l8 = Label(f5, text="Address", fg="purple", font=10).grid(row=140, column=60)
e8 = Entry(f5, textvariable=address_var).grid(row=140, column=100)

r = IntVar()
r1 = Radiobutton(f5, text="Male", variable=r, value="Male", font=14).grid(row=160, column=20)
r2 = Radiobutton(f5, text="Female", variable=r, value="Female", font=14).grid(row=160, column=40)

mylabel = Label(f5, text="Gender", fg="purple", font=14).grid(row=160, column=10)

b61 = Button(f5, text="SAVE & SUBMIT", font=8, command=save)
b61.grid(row=300, column=50)

l9 = Label(f6, text="No.of seats\n you wish to book", fg="red", font=10).grid(row=60, column=1)
c9 = Spinbox(f6, value=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"), font=10).grid(row=60, column=80)

b62 = Button(f6, text="PROCEED & PAY", font=8)
b62.grid(row=300, column=50)

raise_frame(f1)
root.mainloop()
conn.close()
