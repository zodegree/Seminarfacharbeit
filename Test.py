def GL_ANZ():
    master = Tk()
    p = Canvas(master, width=400, height=400)
    p.grid(row=400, column=200)
    p.create_line(200, 0, 200, 400)
    p.create_line(0, 200, 400, 200)

    def bruch(s):
        try:
            t = ''
            m = ''
            trigger = ''
            for i in range(0, len(s), 1):
                hilf = s[i]
                if hilf == '/':
                    trigger = 'aktiv'
                elif trigger == 'aktiv':
                    m = m + hilf
                else:
                    t = t + hilf
            ausgabe = int(t) / int(m)
        except ValueError:
            ausgabe = float(s)
        return ausgabe

    print('y=cx^2+bx+a')
    c = bruch(input('c='))  # n
    b = bruch(input('b='))  # x
    a = bruch(input('a='))  # x^2

    if c == 0:  # linear
        d = abs(b)

        if d < 1 / 10000:
            print('Das ist zu niedrig')
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
            print('Das ist zu hoch')

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

        skalierung = input('Geben sie ein, ob die Skalierung automatisch(1) oder manuell(2) erfolgen soll: ')
        if skalierung != '1' and skalierung != '2':
            print('ENTWEDER 1 ODER 2 SCHREIBEN!!! SO SCHWER IST DAS NICHT!!!')
            pm = 0
            ln = 0
        elif skalierung == '1':
            e = abs(a)
            if e > 30 * d:
                print('a darf höchstens 30 mal so groß, wie b sein, um eine optimale Skallierung zu erreichen')
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
                print('a muss min. 1/10 von b betragen, um eine optimale Skallierung zu erreichen')

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
                    print('Kein x vorhanden')
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
            bx = int(input('Geben sie das maximale x im intervall an (positiv und ganzzahlig): '))
            by = int(input('Geben sie das maximale y im intervall an (positiv und ganzzahlig): '))
            for i in range(5, 20, 5):
                hilfx = (i / 5) * (bx / 4)
                hilfy = (i / 5) * (by / 4)
                p.create_text(200 + 10 * i, 215, text=round(abs(hilfx), 2))  # text(breite,höhe,text='text')  #rechts
                p.create_text(200 - 10 * i, 215, text=round(-abs(hilfx), 2))  # links
                p.create_text(180, 200 - 10 * i, text=round(abs(hilfy), 2))  # oben
                p.create_text(178, 200 + 10 * i, text=round(-abs(hilfy), 2))  # unten
            pm = (bx / by) * b
            ln = a / ((by / 4) / 50)

        if round(a + b) == a + b:
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

    else:
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
        skalierung = input('Geben sie ein, ob die Skalierung automatisch(1) oder manuell(2) erfolgen soll: ')
        if skalierung != '1' and skalierung != '2':
            print('ENTWEDER 1 ODER 2 SCHREIBEN!!! SO SCHWER IST DAS NICHT!!!')
            pm = 0
            ln = 0
        elif skalierung == '1':
            hil = 1
            if d >= 1000:
                print('Das ist zu hoch! Nicht optimale Skalierung möglich')
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
                print('Das ist zu niedrig! Keine optimale Skalierung möglich')
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
            bx = int(input('Geben sie das maximale x im intervall an (positiv und ganzzahlig): '))
            by = int(input('Geben sie das maximale y im intervall an (positiv und ganzzahlig): '))
            qx = bx / 4 / 5
            qy = by / 4 / 5
            mc = c / 10
            hil = bx / by
            if c == 1:
                hil = 2
            else:
                hil = hil
            for x in range(-200, 201, 1):
                # print(x*x,'x^2')
                e = ((50 / (bx / 4)) * (x - 1) + 200)
                f = 400 - (c * (50 / (by / 4)) * (x - 1) * (x - 1) + b * (50 / (by / 4)) * (x - 1) + 200) - a * (
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