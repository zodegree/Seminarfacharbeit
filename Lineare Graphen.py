from tkinter import *






b=int(input('Wählen sie die Länge des Graphen in beide Richtungen(Möglichst eine gerade Zahl): '))   #Gesamtbreite des Fensters
h=b                                         #Gesamthöhe des Fensters
w=b//10                                        #Waagerecht
s=w                                         #Senkrecht

master=Tk()
f=Canvas(master, width=b, height=h)
f.grid(row=b,column=int(h/2))


f.create_line(w,b/2,h-w,b/2)                #x-Achse
f.create_line(h-w,b/2,h-w-20,b/2-5)         #Pfeile erstellen
f.create_line(h-w,b/2,h-w-20,b/2+5)         #
f.create_line(h/2,s,h/2,b-s)                #y-Achse
f.create_line(h/2,s,h/2-5,s+20)             #Pfeile erstellen
f.create_line(h/2,s,h/2+5,s+20)             #
#for i in range(s,b-s,10):                  #Achsenbeschriftung
#    f.create_line(h/2,i,h/2+5,i)
#    f.create_line(i,h/2,i,h/2+5)

master.mainloop()