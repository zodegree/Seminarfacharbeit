from sympy import *

def ü(n,w):                             # Berechnungs Funktion, welche Eingabe erhält und verarbeitet, sowie wieder zurückgibt
                                        # Aufspalten der Gleichung in ein Array,
                                        # danach Übergabe beider Teile in jeweilige Variablen
    n = n.split("=")
    gll = n[0]
    glr = n[1]
                                        # Terme werden mit der Funktion vereinf() in ein ,
                                        # für das Programm verständliches Array, umgewandelt
    gll1 = vereinf(gll)
    glr1 = vereinf(glr)
    if(gll1 == 0 or glr1 == 0):         # Wenn Gleichung nicht verarbeitet werden kann, so ist Rückgabewert ERROR
        return "ERROR"
                                        # Vereinfachen der Terme
    gll2 = add(gll1)
    glr2 = add(glr1)
    wo = umst(gll2, glr2, w)            # die Terme werden wieder zusammenbearbeitet, um sie umzustellen
                                        # Erneutes Vereinfachen der Terme
    gll3 = add(wo[0])
    glr3 = add(wo[1])
    return(out(gll3) + "=" + out(glr3)) # Rückgabe eines Strings, welcher für den User verständlich ist

def sy(n,w):                            # dies ist eine Vergleichsfunktion, welche das Paket sympy benutzt,
                                        # sowie die Korrektheit der Berechnung sichern soll

    n = n.split("=")                    # Aufspaltung der Gleichung in ein Array
                                        # Umwandeln der Terme von Strings in ein von sympy lesbares Format
    eq_1 = sympify(n[0])
    eq_2 = sympify(n[1])

    eq = Eq(eq_1,eq_2)                  # Aufstellen einer für sympy lesbaren Gleichung
    result = str(solveset(eq,w))        # Lösen der Gleichung mit solveset
    result = result[1:-1]               # Löschen der Geschweiften Klammern
    result = w+"="+result               # Ausgabeform bilden
    return result

def klm(x,m):                           # Auflösen von Klammern, welche einen Multiplikator m,
                                        # sowie eine Variable besitzt
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = vereinf(x)                      # Term mit der Funktion vereinf() in ein ,
                                        # für das Programm verständliches Array, umgewandelt
    if (x == 0):                        # Wenn Gleichung nicht verarbeitet werden kann, so ist Rückgabewert ERROR
        return "ERROR"
    for i in range (0, len(x), 1):
        try:
            if (x[i][1] in alphabet):
                x[i][2] *= m            # Faktor der Variable wird mit Multiplikator m multipliziert
        except TypeError:
            x[i][1] *= m                # Zahlen der Klammer werden mit dem Multiplikator m multipliziert
    x = add(x)                          # Term wird mit der add() Funktion vereinfacht
    x = out(x)                          # Term wird nun wieder zu String, damit Funktion vereinf()
                                        # Klammer verarbeiten kann
    if (x[0] != "-"):
        x = "+"+x
    return x

def kl(x):                              # Auflösen von Klammern
    x = vereinf(x)                      # Term mit der Funktion vereinf() in ein ,
                                        # für das Programm verständliches Array, umgewandelt
    if(x==0):                           # Wenn Gleichung nicht verarbeitet werden kann, so ist Rückgabewert ERROR
        return "ERROR"
    x = add(x)                          # Term wird mit der add() Funktion vereinfacht
    x = out(x)                          # Term wird nun wieder zu String, damit Funktion vereinf()
                                        # Klammer verarbeiten kann
    if (x[0] != "-"):
        x = "+"+x
    return x

def vereinf(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-*/"
    gl = []
    mlt = "M"
    i = 0
    n = len(x)
                                        # Klammern werden von innen nach außen aufgelöst und einzeln vereinfacht
    while i < n:
        if (x[i] == "("):               # Herausfinden eines Faktors, wenn er vor der Klammer steht
            nc = i-1
            if(x[i-1]=="*"):
                while nc != -1:
                    nc -= 1
                    if(x[nc] in operations and nc != 0):
                        mlt = float(x[nc-1:i-1])
                        break
                    elif(nc == 0):
                        mlt = float(x[:i - 1])
                        break
            a = i
        if (x[i] == ")" and a != 0):    # Übergeben der Klammern in die jeweiligen Funktionen,
                                        # sowie erstellen neuer Terme ohne Klammern
            nc = i+1
            if (x[i + 1] == "*"):       # Herausfinden eines Faktors, wenn er hinter der Klammer steht
                while nc != len(x):
                    nc += 1
                    if (x[nc] in operations):
                        mlt = float(x[i + 1:nc + 1])
                        break
                    elif (nc == len(x)):
                        mlt = float(x[i+2:])
                        break
            if(mlt != "M" and nc == 0):
                x = klm(x[a + 1:i],mlt) + x[i + 1:]
                mlt = "M"
            elif(mlt != "M"):
                x = x[:nc]+klm(x[a + 1:i], mlt) + x[i + 1:]
                mlt = "M"
            else:
                x = x[:a]+kl(x[a+1:i])+x[i+1:]
        elif (x[i] == ")"):             # Übergeben der Klammern in die jeweiligen Funktionen, wenn eine Klammer,
                                        # am Anfang des Termes steht, sowie erstellen neuer Terme ohne Klammern
            nc = i + 1
            if (x[i + 1] == "*"):
                while nc < len(x):
                    nc += 1
                    if (x[nc] in operations):
                        mlt = float(x[i+2:nc])
                        break
                    elif (nc == len(x)-1):
                        mlt = float(x[i + 2:])
                        break
            if (mlt != "M" and nc == 0):
                x = klm(x[a + 1:i], mlt) + x[nc+1:]

                mlt = "M"
            elif (mlt != "M"):
                x = klm(x[a + 1:i], mlt) + x[nc+1:]
                mlt = "M"
            else:
                x = kl(x[a + 1:i]) + x[i + 1:]
        i += 1
        n = len(x)
#    while "--" in x:
#        ix = x.index("--")
#        x = x[:ix] + "+" + x[ix+2:]
#    while "+-" in x:
#        ix = x.index("+-")
#        x = x[:ix] + "-" + x[ix+2:]
    while "-+" in x:
        ix = x.index("-+")
        x = x[:ix] + "-" + x[ix+2:]
                                        # Division wird in Multiplikation umgewandelt
    i = 0
    while i < n:
        if (x[i] == "/"):
            k = i + 1
            while k < len(x):
                if (x[k] in operations):
                    break
                k += 1
            try:
                u = 1 / float(x[i + 1:k])
            except IndexError:
                return 0

            x = x[:i] + "*" + str(u) + x[k:]
            i = 0
        i += 1
        n = len(x)
    x = x.split("+")
                                        # alle Summanden mit Parametern in eine Liste speichern
    for i in range(0, len(x), 1):
        z1 = []
        z1.append("+")
        z1.append(x[i])
        gl.append(z1)
                                        # alle Subtrahenten aus der Summanden-Liste suchen,
                                        # trennen und alles gesplitet in eine neue Liste speichern
    for i in range(0, len(gl), 1):
        k = gl[i]
        k=k[1]
        if ("-" in k):
            k = k.split("-")
            gl[i][1] = k[0]
            for l in range(1, len(k), 1):
                z1 = []
                z1.append("-")
                z1.append(k[l])
                gl.append(z1)
                                        # alle Elemente der Liste in floats umwandeln,
                                        # alle anderen prüfen, ob es Variablen/Multiplikation sind
    for i in range(0, len(gl), 1):
        try:
            gl[i][1] = float(gl[i][1])
        except ValueError:              # Strings mit Multiplikation, sowie mit Variablen werden bearbeitet
            t = str(gl[i][1])
            q = 0
            k = 0
            if("*" in t):
                while k < len(t):
                                        # Multiplikation mit einer Variable wird herausgesucht und bearbeitet
                    if (t[k] in alphabet):
                        try:
                            if(t[k+1] in operations):
                                t = t[k+2:] + "*" + t[:k+1]
                                k = len(t)-1
                        except IndexError:
                            pass
                        try:
                            gl[i][1] = t[k:]
                            q = mult([[0,t[:k]]])
                            gl[i].append(q[0][1])

                        except IndexError:
                            gl[i][1] = t[k:]
                            q = mult([[0, t[:k]+"1"]])
                            gl[i].append(q[0][1])

                        except TypeError:
                            return 0

                    k += 1
                if(q == 0):             # einfache Multiplikation von Zahlen wird bearbeitet
                    q = mult([[0, t]])
                    if (q==0):
                        return 0
                    gl[i][1]=q[0][1]
            else:                       # Variablen der Form ax/ohne Faktor werden in ein Array umgewandelt
                for k in range(0, len(t), 1):
                    if(t[k] in alphabet and k!=0):
                        gl[i].append(float(t[:k]))
                        gl[i][1]=t[k:]
                        pass
                    elif(t[k] in alphabet):
                        gl[i].append(int(1))
    for i in range(0, len(gl), 1):
        try:
            if("" in gl[i]):
                gl.remove(gl[i])
        except IndexError:
            pass
    return gl

def add(o):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    k = 0
    li = []
    search_list = []
    twiceattemp = []
    f = 0
    for i in range(0, len(o), 1):       # Anzahl der Nachkommastellen, der Zahl mit den meisten Zahlen wird gesucht
        search_list.append(o[i][1])     # search_list ist die Suchliste für Variablen
        if ("." in str(o[i][1])):
            ind = str(o[i][1]).index(".")
            fn = len(str(o[i][1])[ind+1:])
            if (fn > f):
                f = fn
    for i in range(0, len(o), 1):       # Zahlen werden so multipliziert, dass keine Zahl eine Nachkommastelle hat
        if (f != 0 and str(o[i][1]) not in alphabet):
            o[i][1] *= (10**f)
                                        # Addieren der einzelnen Variabeln
    for r in range (0, len(search_list), 1):
        addvalue = 0
        try:
            if(search_list[r] in alphabet and search_list[r] not in twiceattemp):
                twiceattemp.append(search_list[r])
                for n in range(0, len(search_list), 1):
                    if(search_list[r] == search_list[n] and o[n][0]=="+"):
                        addvalue += o[n][2]
                    elif(search_list[r] == search_list[n] and o[n][0]=="-"):
                        addvalue -= o[n][2]
                o[r][2] = addvalue
                o[r][0] = "+"
                li.append(o[r])
        except TypeError:
            pass

                                        # Zahlen werden aufaddiert
    for i in range(0, len(o), 1):
        try:
            if("+" == o[i][0]):
                k += float(o[i][1])
            elif("-" == o[i][0]):
                k -= float(o[i][1])
        except ValueError:
            pass
    if (k != 0):
        if (f != 0):
            k /= (10**f)                # Gesamtwert wird wieder zu einer Kommazahl, falls nötig
        s = ["+",k]
        li.append(s)
    else:
        s = ["+",k]
        li.append(s)
    return li

def out(o):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    a = ""
    for i in range(0, len(o), 1):       # Objekte des Arrays werden wieder zurück in einen String geschrieben
        if (str(o[i][1]) in alphabet and o[i][2] != 1):
            cpy = str(o[i][2])
            if (cpy[-2:] == ".0"):      # Unnötige ,0 Endungen werden nicht in den String geschrieben
                cpy = cpy[:-2]
            a = a + str(o[i][0]) + cpy + str(o[i][1])
        elif(str(o[i][1]) in alphabet and o[i][2] == -1):
            a = a + str(o[i][0]) + "-" + str(o[i][1])
        else:
            cpy = str(o[i][1])
            if(cpy[-2:]==".0"):         # Unnötige ,0 Endungen werden nicht in den String geschrieben
                cpy = cpy[:-2]
            a = a + str(o[i][0]) + cpy
        if(i==0 and a[0]=="+"):         # ein Plus am Anfang eines Termes wird aus dem String gelöscht
            a = a[1:]
                                        # unnötige Doppelungen von Operationen werden vereinfacht
    while "--" in a:
        ix = a.index("--")
        a = a[:ix] + "+" + a[ix+2:]
    while "+-" in a:
        ix = a.index("+-")
        a = a[:ix] + "-" + a[ix+2:]
    while "+0" in a:
        ix = a.index("+0")
        a = a[:ix] + a[ix + 4:]
    return a

def mult(o):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    try:
        for i in range(0, len(o), 1):

            n = str(o[i][1])
            if ("*" in n):
                n = n.split("*")
                while (len(n) != 1):
                                        # Variablen werden aus dem zu bearbeitenden Array herausgetrennt
                    if(str(n[0]) in alphabet):
                        n.append(n[0])
                        n.remove(n[0])
                    elif(str(n[1]) in alphabet):
                        o[i][1] = n[1]
                        n.remove(n[1])
                        o[i][2] = float(n[0])
                        pass
                                        # Faktoren werden multipliziert
                    n[0] = float(n[0])*float(n[1])
                    n.remove(n[1])
                    o[i][1] = n[0]
    except TypeError:
        o=0
    except ValueError:
        o=0
    return o

def umst(a,b,w):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c = []
                                        # Speichern von jeder Variable/Zahl ohne Faktoren
                                        # und oder Vorzeichen in eine Liste
    for i in range (0, len(a), 1):
        c.append(a[i][1])
    d = []
    for i in range (0, len(b), 1):
        d.append(b[i][1])
    f = []                              # Endspeicher
    try:
        e = c.index(w)
        c = []
        c.append(a[e])
        f = []
        for i in range(0, len(a), 1):
                                        # Isolieren der gesuchten Variable
            if(a[i][0] == "+" and i != e):
                a[i][0] = "-"
                f.append(a[i])
            elif(a[i][0] == "-" and i != e):
                a[i][0] = "+"
                f.append(a[i])
        for i in range(0, len(b), 1):
            if(b[i][1] == w):
                cs = b[i]
                cs[2] = cs[2]*-1
                c.append(cs)
            else:
                f.append(b[i])
    except ValueError:                  # Gleiche Methode, nur dass die Variable auf der "falschen" Seite steht
        zw = a
        a = b
        b = zw
        zw = c
        c = d
        d = zw
        e = c.index(w)
        c = []
        c.append(a[e])
        f = []
        for i in range(0, len(a), 1):
            if (a[i][0] == "+" and i != e):
                a[i][0] = "-"
                f.append(a[i])
            elif (a[i][0] == "-" and i != e):
                a[i][0] = "+"
                f.append(a[i])
        for i in range(0, len(b), 1):
            if (b[i] == w):
                pass
            f.append(b[i])
    c = add(c)                          # c wird nun nochmal vereinfacht
    if(c[0][0] == "-"):
        m = c[0][2]*-1
    else:
        m = c[0][2]
    for i in range (0, len(f), 1):      # der Faktor der gesuchten Variablen wird nun bei beiden Termen dividiert
        try:
            if(f[i][1] in alphabet):
                f[i][2] = f[i][2]/m
        except:
            f[i][1] = f[i][1]/m
    c[0][2] = 1
    return (c, f)


#n = str(input("Formel eingeben"))
#w = str(input("nach welcher Variable soll umgestellt werden: "))
#n = n.split("=")
#gll = n[0]
#glr = n[1]
#glr1 = vereinf(glr)
#gll1 = vereinf(gll)
#glr11 = mult(glr1)
#gll11 = mult(gll1)
#glr2 = add(glr11)
#gll2 = add(gll11)
#print(gll2,glr2)
#wo = umst(gll2,glr2,w)
#gll3 = add(wo[0])
#glr3 = add(wo[1])
#print(out(gll3)+"="+out(glr3))
#print(ü("x*5=y","x"))
#print(sy("(4-x)*7+y=x","x")
#print(10/3)
