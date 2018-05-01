from tkinter import *
import Semi

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

def GL_UMST():
    def GL_PRINT(n,w):

        L = Label(nframe, text=Semi.ü(n,w)).grid(row=2,column=1)

    nframe=Tk()
    T = Label(nframe, text="Geben sie die zu lösende Gleichung ein:")
    T.grid(row=0,column=0)
    IN = Entry(nframe)
    IN.grid(row=0,column=1)
    T1 = Label(nframe,text="Geben sie die Variable ein, nach welcher umgestellt werden soll")
    T1.grid(row=1,column=0)
    IN2 = Entry(nframe)
    IN2.grid(row=1,column=1)
    B = Button(nframe, text="Gleichung lösen", command=lambda: GL_PRINT(IN.get(),IN2.get())).grid(row=2)
    nframe.mainloop()


def GL_SYS():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    nframe = Tk()
    n = []

    def GL_RES():
        n = ["2x-2=y", "2.5x+5x-13-1=y"]
        varlist = ["x", "y"]
        # for i in n:
        #    for j in range(0,len(i),1):
        #        if(i[j] not in varlist and i[j] in alphabet):
        #            varlist.append(i[j])
        for i in range(0, 2, 1):
            var = varlist[i]
            GL = n[0]
            GL2 = n[1]
            print(varlist[i], varlist)
            if (var in GL):
                if (i == 0):
                    UseGL = Semi.ü(GL, var)
                    UseGL2 = Semi.ü(GL2, var)
                else:
                    out = Semi.ü(UseGL[2:] + "=" + UseGL2[2:], var)
        while var in n[0]:
            delindex = n[0].index(var)
            n[0] = n[0][:delindex] + out[2:] + n[0][delindex + 1:]
        print(n[0], "USE")
        n[0] = Semi.ü(n[0], varlist[0])
        L = Label(nframe, text="SP = ("+out[2:]+"|"+UseGL[2:]+")")






    def GL_PRINT():
        n.append(IN.get())
        L = Label(nframe, text=IN.get()).pack(side="top")
        if(len(n) >= 2):
            B = Button(nframe, text="Schnittpunkte berechnen", command=lambda: GL_RES()).pack(side="bottom")

    for widget in nframe.winfo_children():
        widget.destroy()
    IN = Entry(nframe)
    IN.pack(side="bottom")
    B = Button(nframe, text="Eingabe einlesen", command=lambda: GL_PRINT()).pack(side="bottom",fill=BOTH)
    nframe.mainloop()


mainframe = Tk() # create a Tk mainframe window
mainframe.title("GLX2000")

w = 400 # width for the Tk mainframe
h = 325 # height for the Tk mainframe

# get screen width and height
ws = mainframe.winfo_screenwidth() # width of the screen
hs = mainframe.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk mainframe window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
mainframe.geometry('%dx%d+%d+%d' % (w, h, x, y))

b1 = Button(mainframe, text="Gleichungen umstellen", command=GL_UMST)
b1.place(relx=0.5, rely=0.4, anchor=CENTER)
b2 = Button(mainframe, text="Lineare Gleichungen anzeigen", command=GL_UMST)
b2.place(relx=0.5, rely=0.5, anchor=CENTER)
b3 = Button(mainframe, text="Gleichungssysteme berechnen", command=GL_SYS)
b3.place(relx=0.5, rely=0.6, anchor=CENTER)

mainframe.mainloop() # starts the mainloop
