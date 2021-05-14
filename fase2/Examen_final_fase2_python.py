import psycopg2
import sys
import os
from tkinter import *
import tkinter.messagebox

conn = psycopg2.connect(
    host="localhost",
    database="pytest",
    user="proyectos",
    password="proyectos123"
)
cur=conn.cursor()

window = Tk()

window.title("Bienvenido al programa de la aerolinea")

window.geometry('450x400')


co = 0
be = 0
pe = 0
sub = 0
su=IntVar()
tot = 0
t = IntVar()
sel = IntVar()
cc=IntVar()
cb=IntVar()
cp=IntVar()
des = 0
d=IntVar()
comst = BooleanVar()
bebst = BooleanVar()
pelst = BooleanVar()
comv = comst.get()
bebv = bebst.get()
pelv = pelst.get()
vcc = cc.get()
vcb = cb.get()
vcp = cp.get()
s1 = sel.get()

def reporte():
    cur.execute("SELECT * FROM Aerolinea ;")
    db = cur.fetchall()
    lista = Listbox(window, width=20, heigh=15)
    lista.grid(row=8, columnspan=4, sticky=W+E)
    for x in db:
        lista.insert(END, x)
    conn.commit
 
 
def limpia():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def calc():
    s1 = sel.get()
    comv = comst.get()
    bebv = bebst.get()
    pelv = pelst.get()
    vcc = cc.get()
    vcb = cb.get()
    vcp = cp.get()

    try:
        if s1 == 1:
            co = 50
            be = 35
            pe = 70
        elif s1 ==2:
            co = 40
            be = 25
            pe = 55
        elif s1 ==3:
            co = 25
            be = 25
            pe = 25
        totserv = int(comv)*vcc + int(bebv)*vcb + int(pelv)*vcp
        if totserv >= 10:
            de=("10%")
            des=10
        if totserv < 10 and s1 == 1 and comv == True and bebv == True and pelv ==True:
            de=("5%")
            des=5
        if s1 != 1 and totserv < 10:
            de=("0%")
            des=0
        d.set(de)
        sub = int(comv)*vcc*co+int(bebv)*vcb*be+int(pelv)*vcp*pe
        tot = sub - (sub*des/100)
        su.set(sub)
        t.set(tot)
        cur.execute("insert into Aerolinea (subtotal, descuento, total) values (%s,%s,%s);", (sub,de,tot))
        conn.commit()
    except:
        limpia()

c11 = Label (window, text="Tipo de servicio")
c11.grid (column=2,row =0)
c12 = Label (window, text="Comida")
c12.grid (column=2,row =1)
c13 = Label (window, text="Bebida")
c13.grid (column=2,row =2)
c14 = Label (window, text="Película")
c14.grid (column=2,row =3)
c21 = Label (window, text="1ra Clase")
c21.grid (column=3,row =0)
c22 = Label (window, text="50")
c22.grid (column=3,row =1)
c23 = Label (window, text="35")
c23.grid (column=3,row =2)
c24 = Label (window, text="70")
c24.grid (column=3,row =3)
c31 = Label (window, text="2da Clase")
c31.grid (column=4,row =0)
c32 = Label (window, text="40")
c32.grid (column=4,row =1)
c33 = Label (window, text="25")
c33.grid (column=4,row =2)
c34 = Label (window, text="55")
c34.grid (column=4,row =3)
c41 = Label (window, text="3ra Clase")
c41.grid (column=5,row =0)
c42 = Label (window, text="25")
c42.grid (column=5,row =1)
c43 = Label (window, text="10")
c43.grid (column=5,row =2)
c44 = Label (window, text="25")
c44.grid (column=5,row =3)

Li = Button(window, text="Limpiar", command=limpia)
Li.grid(column=1, row=0)

Ca = Button(window, text="Calcular", command=calc)
Ca.grid(column=1, row=1)

Re = Button(window, text="Reporte", command=reporte)
Re.grid(column=1, row=2)

Sa = Button(window, text="Salir", command=window.destroy)
Sa.grid(column=1, row=3)

pri = Radiobutton (window,  text='Primera Clase', value =1, variable=sel)
pri.grid(column=1, row=4)

sec = Radiobutton (window,  text='Segunda Clase', value =2, variable=sel)
sec.grid(column=1, row=5)

ter = Radiobutton (window,  text='Tercera Clase', value =3, variable=sel)
ter.grid(column=1, row=6)

com = Checkbutton(window, text='Comida', var=comst)
com.grid(column=2, row=4)
beb = Checkbutton(window, text='Bebida', var=bebst)
beb.grid(column=2, row=5)
pel = Checkbutton(window, text='Película', var=pelst)
pel.grid(column=2, row=6)

s1 = Spinbox(window, from_=0, to=100, width=5, state="readonly", textvariable=cc)
s1.grid(column=3, row=4)
s2 = Spinbox(window, from_=0, to=100, width=5, state="readonly", textvariable=cb)
s2.grid(column=3, row=5)
s3 = Spinbox(window, from_=0, to=100, width=5, state="readonly", textvariable=cp)
s3.grid(column=3, row=6)

subtotal  = Label (window, text="Subtotal")
subtotal.grid(column=4, row=5)
serv = Label(window, textvariable=su, relief=RAISED )
serv.grid(column=4, row=6)

descuento = Label(window, text="Descuento")
descuento.grid(column=5, row=5)
desc = Label(window, textvariable=d, relief=RAISED )
desc.grid(column=5, row=6)

total = Label(window, text="Total")
total.grid(column=6, row=5)
tota = Label(window, textvariable=t, relief=RAISED )
tota.grid(column=6, row=6)

window.mainloop()

