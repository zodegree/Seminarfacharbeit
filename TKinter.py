from math import *
from sympy import *
from tkinter import *
import Semi
import random

#def GL_ADD(nframe):
#    Text(nframe, height=2, width=2)
#    T.grid(row=0, column=1)
#    T.insert(END, "=")
#    IN1 = Entry(nframe)
#    IN1.grid(row=0, column=0)
#    IN2 = Entry(nframe)
#    IN2.grid(row=0, column=2)
#    n1 = IN1.get()
#    n2 = IN2.get()
#    return(n1,n2)
def GL_ANZ():
    nframe = Tk()
    nframe.title("Gleichungen graphisch anzeigen")
    def Scal():
        c = IN1.get()
        b = IN2.get()
        a = IN3.get()
        def aut():
            skalierung = "1"
            #print("M",[a,b,c])
            nframe.destroy()
            bx = 0
            by = 0
            GL_ANZF(a,b,c,bx,by,skalierung)
        def man():
            for widget in nframe.winfo_children():
                widget.destroy()
            def butclick():
                bx = int(IN4.get())
                by = int(IN5.get())
                nframe.destroy()
                GL_ANZF(a,b,c,bx,by,skalierung)
            skalierung = "2"
            L1 = Label(nframe,text='Geben sie das maximale x im intervall an (positiv und ganzzahlig): ').grid(row=0,column=0)
            IN4 = Entry(nframe)
            IN4.grid(row=0,column=1)
            L2 = Label(nframe, text='Geben sie das maximale y im intervall an (positiv und ganzzahlig): ').grid(row=1,column=0)
            IN5 = Entry(nframe)
            IN5.grid(row=1,column=1)
            B = Button(nframe, text="Gleichung ausgeben",command=butclick).grid(row=2,columnspan=2)
        for widget in nframe.winfo_children():
            widget.destroy()
        L = Label(nframe,text="Wählen sie eine Art der Skalierung").pack(side="top")
        B = Button(nframe,text="automatisch",command=aut).pack(side="top")
        B1 = Button(nframe, text="manuell", command=man).pack(side="top")

        def GL_ANZF(a, b, c, bx, by, skalierung):
            master = Tk()
            master.title("Graphische Ausgabe")
            p = Canvas(master, width=400, height=400)
            p.grid(row=400, column=200)
            p.create_line(200, 0, 200, 400)  # erstellen der x- und y- Achse
            p.create_line(0, 200, 400, 200)

            def bruch(s):  # funktion um einen bruch zur floatzahl zu machen
                try:
                    t = ''
                    m = ''
                    trigger = ''
                    for i in range(0, len(s), 1):
                        hilf = s[i]
                        if hilf == '/':  # nach '/' suchen
                            trigger = 'aktiv'
                        elif trigger == 'aktiv':
                            m = m + hilf
                        else:
                            t = t + hilf
                    ausgabe = int(t) / int(m)  # den zähler durch den nenner teilen
                except ValueError:
                    ausgabe = float(s)  # wenn es kein Bruch ist, dann passiert nichts
                return ausgabe

            # print('y=cx^2+bx+a')
            # c = bruch(input('c='))  # n
            # b = bruch(input('b='))  # x
            # a = bruch(input('a='))  # x^2

            c = bruch(c)
            b = bruch(b)
            a = bruch(a)

            if c == 0:  # linear
                d = abs(b)

                if d < 1 / 10000:  # autoskalierung linear
                    master.destroy()
                    popup = Tk()
                    popup.title("WARNUNG")
                    L = Label(popup, text='b ist zu niedrig').pack(side="top")
                    B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
                    popup.mainloop()
                    # print('b ist zu niedrig')
                elif d >= 1 / 10000 and d <= 1 / 1000:
                    lx = 1 / 100
                    ly = d / (lx)
                elif d > 1 / 1000 and d < 1 / 100:
                    lx = 1 / 10
                    ly = d / (lx)
                elif d >= 1 / 100 and d < 33:
                    lx = 1
                    ly = d
                elif d >= 33 and d < 3333:
                    lx = 10
                    ly = d / (lx)
                elif d >= 3333 and d <= 33333:
                    lx = 100
                    ly = round(d / (lx))
                else:
                    master.destroy()
                    popup = Tk()
                    popup.title("WARNUNG")
                    L = Label(popup, text='b ist zu hoch').pack(side="top")
                    B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
                    popup.mainloop()
                    # print('Das ist zu hoch')

                # Beschriftung:
                for i in range(200, 410, 10):  # x-Achse(rechts)
                    p.create_line(i, 200, i, 205)
                for i in range(200, -20, -10):  # x-Achse(links)
                    p.create_line(i, 200, i, 205)
                for i in range(200, 410, 10):  # y-Achse(unten)
                    p.create_line(200, i, 195, i)
                for i in range(200, -20, -10):  # y-Achse(oben)
                    p.create_line(200, i, 195, i)
                # große Markierungen
                for i in range(200, 450, 50):
                    p.create_line(i, 200, i, 210)
                for i in range(200, -100, -50):
                    p.create_line(i, 200, i, 210)
                for i in range(200, 450, 50):
                    p.create_line(200, i, 190, i)
                for i in range(200, -100, -50):
                    p.create_line(200, i, 190, i)

                # skalierung = input('Geben sie ein, ob die Skalierung automatisch(1) oder manuell(2) erfolgen soll: ')
                if skalierung != '1' and skalierung != '2':
                    print('ENTWEDER 1 ODER 2 SCHREIBEN!!! SO SCHWER IST DAS NICHT!!!')
                    pm = 0
                    ln = 0
                elif skalierung == '1':
                    e = abs(a)
                    if e > 30 * d:  # autoskalierung des
                        master.destroy()
                        popup = Tk()
                        popup.title("WARNUNG")
                        L = Label(popup,
                                  text='a darf höchstens 30 mal so groß, wie b sein, um eine optimale Skallierung zu erreichen').pack(
                            side="top")
                        B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
                        popup.mainloop()
                        # print('a darf höchstens 30 mal so groß, wie b sein, um eine optimale Skallierung zu erreichen')
                    elif e == 0:
                        lx = lx
                        ly = ly
                        ln = 0
                    elif e == d:
                        lx = lx
                        ly = ly
                        if a >= 0:
                            ln = 50
                        else:
                            ln = -50
                    elif e > d and e <= 30 * d:
                        lx = lx / 10
                        ly = 10 * ly
                        if a >= 0:
                            ln = 50 // ((10 * d) / e)
                        else:
                            ln = -(50 // ((10 * d) / e))
                    elif e < d and e > d / 10:
                        lx = lx
                        ly = ly
                        if a >= 0:
                            ln = 50 // (d / e)
                        else:
                            ln = -(50 // (d / e))
                    else:
                        master.destroy()
                        popup = Tk()
                        popup.title("WARNUNG")
                        L = Label(popup,
                                  text='a muss min. 1/10 von b betragen, um eine optimale Skallierung zu erreichen').pack(
                            side="top")
                        B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
                        popup.mainloop()
                        # print('a muss min. 1/10 von b betragen, um eine optimale Skallierung zu erreichen')

                    for i in range(5, 20, 5):
                        try:
                            hilfx = (i / 5) / lx
                            if abs(hilfx) >= 1:
                                hilfx = int(hilfx)
                            else:
                                hilfx = round(hilfx, 2)
                            hilfy = (i / 5) * ly
                        except NameError:
                            hilfx = 0
                            hilfy = 0
                            # print('Kein x vorhanden')
                            master.destroy()
                            popup = Tk()
                            popup.title("WARNUNG")
                            L = Label(popup, text='Kein x vorhanden').pack(side="top")
                            B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
                            popup.mainloop()
                        # print(round(hilfe+0.01))
                        # hilfe=int(hilfe)
                        # print(hilfe)
                        p.create_text(200 + 10 * i, 215, text=abs(hilfx))  # text(breite,höhe,text='text')  #rechts
                        p.create_text(200 - 10 * i, 215, text=-abs(hilfx))  # links
                        p.create_text(180, 200 - 10 * i, text=round(abs(hilfy), 2))  # oben
                        p.create_text(178, 200 + 10 * i, text=round(-abs(hilfy), 2))  # unten
                        if b >= 0:
                            pm = 1
                        else:
                            pm = -1

                else:
                    # bx = int(input('Geben sie das maximale x im intervall an (positiv und ganzzahlig): '))
                    # by = int(input('Geben sie das maximale y im intervall an (positiv und ganzzahlig): '))
                    for i in range(5, 20, 5):
                        hilfx = (i / 5) * (bx / 4)
                        hilfy = (i / 5) * (by / 4)
                        p.create_text(200 + 10 * i, 215,
                                      text=round(abs(hilfx), 2))  # text(breite,höhe,text='text')  #rechts
                        p.create_text(200 - 10 * i, 215, text=round(-abs(hilfx), 2))  # links
                        p.create_text(180, 200 - 10 * i, text=round(abs(hilfy), 2))  # oben
                        p.create_text(178, 200 + 10 * i, text=round(-abs(hilfy), 2))  # unten
                    pm = (bx / by) * b
                    ln = a / ((by / 4) / 50)

                if round(a + b) == a + b:  # erstellung des graphen
                    for x in range(-2000, 2001, 1):
                        e = ((x - 1) + 200)
                        f = 400 - ((x - 1) * pm + 200) - ln
                        g = (x + 200)
                        h = 400 - (x * pm + 200) - ln
                        p.create_line(e, f, g, h, fill='red')

                elif round(a + b, 1) == a + b:
                    for x in range(-2000, 2001, 1):
                        e = (((x - 1) + 200))
                        f = (400 - ((x - 1) * pm + 200) - ln)
                        g = ((x + 200))
                        h = (400 - (x + 200) * pm - ln)
                        p.create_line(e, f, g, h, fill='yellow')
                else:
                    for x in range(-2000, 2001, 1):
                        e = round((((x - 1) + 200)), 2)
                        f = round((400 - ((x - 1) * pm + 200) - ln), 2)
                        g = round(((x + 200)), 2)
                        h = round((400 - (x * pm + 200) - ln), 2)
                        p.create_line(e, f, g, h, fill='blue')

            else:  # autoskalierung quadratisch
                mc = c / 10
                d = abs(c)
                e = abs(b)
                f = abs(a)
                # Beschriftung:
                for i in range(200, 410, 10):  # x-Achse(rechts)
                    p.create_line(i, 200, i, 205)
                for i in range(200, -20, -10):  # x-Achse(links)
                    p.create_line(i, 200, i, 205)
                for i in range(200, 410, 10):  # y-Achse(unten)
                    p.create_line(200, i, 195, i)
                for i in range(200, -20, -10):  # y-Achse(oben)
                    p.create_line(200, i, 195, i)
                # große Markierungen
                for i in range(200, 450, 50):
                    p.create_line(i, 200, i, 210)
                for i in range(200, -100, -50):
                    p.create_line(i, 200, i, 210)
                for i in range(200, 450, 50):
                    p.create_line(200, i, 190, i)
                for i in range(200, -100, -50):
                    p.create_line(200, i, 190, i)
                # skalierung = input('Geben sie ein, ob die Skalierung automatisch(1) oder manuell(2) erfolgen soll: ')
                if skalierung != '1' and skalierung != '2':
                    print('ENTWEDER 1 ODER 2 SCHREIBEN!!! SO SCHWER IST DAS NICHT!!!')
                    pm = 0
                    ln = 0
                elif skalierung == '1':
                    hil = 1
                    if d >= 1000:
                        # print('Das ist zu hoch! Nicht optimale Skalierung möglich')
                        master.destroy()
                        popup = Tk()
                        popup.title("WARNUNG")
                        L = Label(popup, text='Das ist zu hoch! Nicht optimale Skalierung möglich').pack(side="top")
                        B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
                        popup.mainloop()
                    elif d >= 100:
                        qx = 1 / 100
                        qy = 1 / 100
                        mc = mc / 100
                    elif d < 100 and d >= 10:
                        qx = 1 / 10
                        qy = 1 / 10
                        mc = mc / 10
                    elif d < 10 and d >= 1 / 10:
                        qx = 1
                        qy = 1
                        mc = mc
                    elif d < 1 / 10 and d >= 1 / 100:
                        qx = 10
                        qy = 10
                        mc = 10 * mc
                    elif d <= 1 / 1000:
                        # print('Das ist zu niedrig! Keine optimale Skalierung möglich')
                        master.destroy()
                        popup = Tk()
                        popup.title("WARNUNG")
                        L = Label(popup, text='Das ist zu niedrig! Keine optimale Skalierung möglich').pack(side="top")
                        B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
                        popup.mainloop()
                    else:
                        qx = 100
                        qy = 100
                        mc = 100 * mc
                    for x in range(-200, 201, 1):
                        # print(x*x,'x^2')
                        e = ((x - 1) + 200)
                        f = 400 - (mc * (x - 1) * (x - 1) + b * (x - 1) / qx + 200) - a * 10 / qx
                        g = (x + 200)
                        h = 400 - (mc * x * x + b * x / qx + 200) - a * 10 / qx
                        # print(e,f,g,h)
                        p.create_line(e, f, g, h, fill='red')

                else:
                    # bx = int(input('Geben sie das maximale x im intervall an (positiv und ganzzahlig): '))
                    # by = int(input('Geben sie das maximale y im intervall an (positiv und ganzzahlig): '))
                    qx = bx / 4 / 5
                    qy = by / 4 / 5
                    mc = c / 10
                    hil = bx / by
                    if c == 1:
                        hil = 2
                    else:
                        hil = hil
                    for x in range(-200, 201, 1):  # erstellung des graphen
                        # print(x*x,'x^2')
                        e = ((50 / (bx / 4)) * (x - 1) + 200)
                        f = 400 - (
                        c * (50 / (by / 4)) * (x - 1) * (x - 1) + b * (50 / (by / 4)) * (x - 1) + 200) - a * (
                            200 / by)
                        g = ((50 / (bx / 4)) * x + 200)
                        h = 400 - (c * (50 / (by / 4)) * x * x + b * (50 / (by / 4)) * x + 200) - a * (200 / by)
                        # print(e,f,g,h)
                        p.create_line(e, f, g, h, fill='red')

                for i in range(5, 20, 5):
                    p.create_text(200 + 10 * i, 215, text=i * qx)
                    p.create_text(200 - 10 * i, 215, text=-i * qx)
                    p.create_text(175, 200 - 10 * i, text=i * qy)
                    p.create_text(175, 200 + 10 * i, text=-i * qy)

            master.mainloop()
    HINT = Label(nframe, text="Bitte geben sie die Werte der folgenden Gleichung an!").grid(row=0,columnspan=2)
    L = Label(nframe,text="y=c*x^2+b*x+a").grid(row=1,columnspan=2)
    L2 = Label(nframe,text="c = ").grid(row=2,column=0)
    IN1 = Entry(nframe)
    IN1.grid(row=2,column=1)
    L3 = Label(nframe, text="b = ").grid(row=3, column=0)
    IN2 = Entry(nframe)
    IN2.grid(row=3, column=1)
    L4 = Label(nframe, text="a = ").grid(row=4, column=0)
    IN3 = Entry(nframe)
    IN3.grid(row=4, column=1)
    B = Button(nframe,text="Eingaben übernehmen", command=Scal).grid(row=5,columnspan=2)
    nframe.mainloop()

def Lernprogramm():
    nframe=Tk()
    nframe.title("Lernprogramm")
    def GL_VGL(iget):
        outpr = Semi.ü(out, "x")
        outpr = outpr.split("=")
        outpr = outpr[0] + "=" + str(round(float(outpr[1]), 2))
        if(iget == outpr):
            L = Label(nframe,text="Lösung ist Richtig!").pack(side="top")
        else:
            L = Label(nframe, text="Lösung oder Eingabeform ist Falsch! Das richtige Ergebnis lautet:"+outpr).pack(side="top")

    # Erstellung von zwei zufällig generierten Termen
    left_obj = []
    right_obj = []
    left_objanz = random.randrange(1,5,1)
    right_objanz = random.randrange(1,5,1)
    for i in range(0,left_objanz,1):
        obj = []
        if(random.random()>0.5):
            obj.append("+")
        else:
            obj.append("-")
        if(random.random()>0.7):
            obj.append(float(random.randrange(1,9990,1)/10))
        else:
            obj.append("x")
            obj.append(random.randrange(1,500,1)/10)
        left_obj.append(obj)
    for i in range(0,right_objanz,1):
        obj = []
        if(random.random()>0.5):
            obj.append("+")
        else:
            obj.append("-")
        if(random.random()>0.7):
            obj.append(float(random.randrange(1,9990,1)/10))
        else:
            obj.append("x")
            obj.append(random.randrange(1,500,1)/10)
        right_obj.append(obj)
    #print(left_obj,right_obj)
    out = Semi.out(left_obj)+"="+Semi.out(right_obj)
    if("x" not in out):
        out = out+"x"
    T = Label(nframe,width=70,text="Lösen sie folgende Gleichung. Beachten sie dabei die Form x=errechnete Zahl,\n zu nutzen, sowie die errechnete Zahl auf 2 Dezimalstellen \nnach dem Komma nach dem Bruch anzugeben.\n Bei Zahlen, welche auf ,00 enden würden bitte .0 angeben. \n Im allgemeinen ist das Komma durch einen Punkt zu ersetzen.")
    T.pack(side="top")
    L = Label(nframe,text=out).pack(side="top")
    IN = Entry(nframe)
    IN.pack(side="top")
    B = Button(nframe,text="Ergebnis prüfen",command=lambda: GL_VGL(IN.get())).pack(side="top")
    nframe.mainloop()

def GL_UMST():
    def GL_RS(popup,n,w):
        popup.destroy()

    def GL_PRINT(n,w):
        if (w not in n):
            popup = Tk()
            popup.title("WARNUNG")
            L = Label(popup, text=w+" ist nicht in der eingegebenen Gleichung vorhanden").pack(side="top")
            B = Button(popup, text='Ok', command=lambda: popup.destroy()).pack(side="top")
            popup.mainloop()
        elif (Semi.ü(n, w) == "ERROR"):
            print("ERROR")
            L = Label(nframe, text=Semi.sy(n,w),bg="white").grid(row=3,column=1,sticky=W+E)


        elif (Semi.ü(n, w) != Semi.sy(n, w)):
            L = Label(nframe, text=Semi.ü(n, w),bg="white").grid(row=3, column=1,sticky=W+E)
            popup = Tk()
            popup.title("WARNUNG")
            L1 = Label(popup, text="Beim Lösen der Gleichung ist möglicherweise Fehler aufgetreten.\nBitte vergleichen sie mit der angezeigten Lösung.")
            L1.pack(side="top")
            L2 = Label(popup, text=Semi.sy(n, w))
            L2.pack(side="top")
            B = Button(popup, text="Fenster schließen", command= lambda: GL_RS(popup,n,w))
            B.pack(side="top")
            popup.mainloop()
        else:
            L = Label(nframe, text=Semi.ü(n, w),bg="white").grid(row=3, column=1,sticky=W+E)

    nframe=Tk()
    nframe.title("Gleichung umstellen")
    HIN = Label(nframe, text="Beachten sie: 2x muss als 2*x eingegeben werden").grid(row=0)
    T = Label(nframe, text="Geben sie die zu lösende Gleichung ein:")
    T.grid(row=1,column=0)
    IN = Entry(nframe)
    IN.grid(row=1,column=1)
    T1 = Label(nframe,text="Geben sie die Variable ein, nach welcher umgestellt werden soll")
    T1.grid(row=2,column=0)
    IN2 = Entry(nframe)
    IN2.grid(row=2,column=1)
    B = Button(nframe, text="Gleichung lösen", command=lambda: GL_PRINT(IN.get(),IN2.get())).grid(row=3)
    nframe.mainloop()


def GL_SYS():
    #alphabet = "abcdefghijklmnopqrstuvwxyz"
    nframe = Tk()
    nframe.title("Gleichungssysteme berechnen")
    n = []

    #def GL_RES():
    #    varlist = ["x", "y"]
        # for i in n:
        #    for j in range(0,len(i),1):
        #        if(i[j] not in varlist and i[j] in alphabet):
        #            varlist.append(i[j])
    #    for i in range(0, 2, 1):
    #        var = varlist[i]
    #        GL = n[0]
    #        GL2 = n[1]
    #        print(varlist[i], varlist)
    #        if (var in GL):
    #            if (i == 0):
    #                UseGL = Semi.ü(GL, var)
    #                UseGL2 = Semi.ü(GL2, var)
    #            else:
    #                out = Semi.ü(UseGL[2:] + "=" + UseGL2[2:], var)
    #    while var in n[0]:
    #        delindex = n[0].index(var)
    #        n[0] = n[0][:delindex] + out[2:] + n[0][delindex + 1:]
    #    print(n[0], "USE")
    #    UseGL = Semi.ü(n[0], varlist[0])
    #    print(UseGL)
    #    L = Label(nframe, text="SP = ("+str(round(float(out[2:]),3))+"|"+str(round(float(UseGL[2:]),3))+")").pack(side="bottom")
    def GL_RES():
        res = solve(n)
        L = Label(nframe, text=res).pack(side="bottom")





    def GL_PRINT():
        eq = IN.get().split("=")
        eq_0 = sympify(eq[0])
        eq_1 = sympify(eq[1])
        n.append(Eq(eq_0,eq_1))
        L = Label(nframe, text=IN.get()).pack(side="top")
        if(len(n) >= 2):
            B = Button(nframe, text="Gleichungssystem berechnen", command=lambda: GL_RES()).pack(side="bottom")

    for widget in nframe.winfo_children():
        widget.destroy()
    HINT = Label(nframe, text="Bitte geben sie die Gleichungen,\nwelche zum Gleichungssytem gehören, an!").pack(
        side="top")
    HIN = Label(nframe, text="Beachten sie: 2x muss als 2*x eingegeben werden").pack(side="top")
    HIN2 = Label(nframe, text="Geben sie jeweils nur eine Gleichung mit einem Gleichungszeichen an").pack(side="top")
    IN = Entry(nframe)
    IN.pack(side="bottom")
    B = Button(nframe, text="Eingabe einlesen", command=lambda: GL_PRINT()).pack(side="bottom")
    nframe.mainloop()


mainframe = Tk() # create a Tk mainframe window
mainframe.title("Gleichungsprogramm")

w = 400 # Breite des Fensters
h = 325 # Höhe des Fensters

# erkennen der Bildschirmauflösung
ws = mainframe.winfo_screenwidth()
hs = mainframe.winfo_screenheight()

# Berechnen der x und y Koordinate für das Fenster
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# Position und Größe des Fenster
mainframe.geometry('%dx%d+%d+%d' % (w, h, x, y))

b1 = Button(mainframe, text="Gleichung umstellen", command=GL_UMST)
b1.place(relx=0.5, rely=0.35, anchor=CENTER)
b2 = Button(mainframe, text="Lernprogramm starten", command=Lernprogramm)
b2.place(relx=0.5, rely=0.45, anchor=CENTER)
b3 = Button(mainframe, text="Gleichungssystem berechnen", command=GL_SYS)
b3.place(relx=0.5, rely=0.55, anchor=CENTER)
b4 = Button(mainframe, text="Gleichungen graphisch anzeigen", command=GL_ANZ)
b4.place(relx=0.5, rely=0.65, anchor=CENTER)

mainframe.mainloop()
