import time
from sympy import *
def ü(n,w):
    n = n.split("=")
    gll = n[0]
    glr = n[1]
    gll1 = vereinf(gll)
    glr1 = vereinf(glr)
    gll2 = add(gll1)
    glr2 = add(glr1)
    wo = umst(gll2, glr2, w)
    gll3 = add(wo[0])
    glr3 = add(wo[1])
    print(out(gll3) + "=" + out(glr3))
    return(out(gll3) + "=" + out(glr3))

def sy(n,w):
    n = n.split("=")
    eq_1 = sympify(n[0])
    eq_2 = sympify(n[1])
    eq = Eq(eq_1,eq_2)
    result = str(solveset(eq,w))
    result = result[1:-1]
    result = w+"="+result
    print(result)
    return result

def klm(x,m):
    # Ablauf der Vereinfachung
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = vereinf(x)
    for i in range (0, len(x), 1):
        try:
            if (x[i][1] in alphabet):
                x[i][2] *= m
        except TypeError:
            x[i][1] *= m
    x = add(x)
    x = out(x)
    if (x[0] != "-"):
        x = "+"+x
    return x

def kl(x):
    # Ablauf der Vereinfachung
    x = vereinf(x)
    x = add(x)
    x = out(x)
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
        if (x[i] == "("):
            nc = i-1
            if(x[i-1]=="*"):
                while nc != -1:
                    nc -= 1
                    if(x[nc] in operations and nc != 0):
                        mlt = float(x[nc-1:i-1])
                        break
                    elif(x[nc] in operations and nc == 0):
                        mlt = float(x[:i - 1])
                        break
            a = i
        if (x[i] == ")" and a != 0):
            if(mlt != "M" and nc == 0):
                x = klm(x[a + 1:i],mlt) + x[i + 1:]
                mlt = "M"
            elif(mlt != "M"):
                x = x[:nc]+klm(x[a + 1:i], mlt) + x[i + 1:]
                mlt = "M"
            else:
                x = x[:a]+kl(x[a+1:i])+x[i+1:]
        elif (x[i] == ")"):
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
    while i < n:
        if (x[i] == "/"):
            k = i + 1
            while k < len(x):
                if (x[k] in operations):
                    break
                k += 1
            u = 1 / float(x[i + 1:k])
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
    # alle Subtrahenten aus der Summanden-Liste suchen, trennen und alles gesplitet in eine neue Liste speichern
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
    # alle Elemente der Liste in floats umwandeln, alle anderen prüfen, ob es Variablen sind
    for i in range(0, len(gl), 1):
        try:
            gl[i][1] = float(gl[i][1])
        except ValueError:
            t = str(gl[i][1]) # string mit Variable
            q = 0
            k = 0
            if("*" in t):
                while k < len(t):
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
                    k += 1
                if(q == 0):
                    q = mult([[0, t]])
                    gl[i][1]=q[0][1]
            else:
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
    for i in range(0, len(o), 1):
        search_list.append(o[i][1])
        if ("." in str(o[i][1])):
            ind = str(o[i][1]).index(".")
            fn = len(str(o[i][1])[ind+1:])
            if (fn > f):
                f = fn
    for i in range(0, len(o), 1):
        if (f != 0 and str(o[i][1]) not in alphabet):
            o[i][1] *= (10**f)
    for r in range (0, len(search_list), 1):
        addvalue = 0
        try:
            if(search_list[r] in alphabet and search_list[r] not in twiceattemp):
                twiceattemp.append(search_list[r])
                for n in range(0, len(search_list), 1):
                    if(search_list[r] == search_list[n]):
                        addvalue += o[n][2]
                o[r][2] = addvalue
                li.append(o[r])
        except TypeError:
            pass


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
            k /= (10**f)
        s = ["+",k]
        li.append(s)
    else:
        s = ["+",k]
        li.append(s)
    return li

def out(o):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    a = ""
    for i in range(0, len(o), 1):
        if (str(o[i][1]) in alphabet and o[i][2] != 1):
            a = a + str(o[i][0]) + str(o[i][2]) + str(o[i][1])
        elif(str(o[i][1]) in alphabet and o[i][2] == -1):
            a = a + str(o[i][0]) + "-" + str(o[i][1])
        else:
            cpy = str(o[i][1])
            if(cpy[-2:]==".0"):
                cpy = cpy[:-2]
            a = a + str(o[i][0]) + cpy
        if(i==0 and a[0]=="+"):
            a = a[1:]
    while "--" in a:
        ix = a.index("--")
        a = a[:ix] + "+" + a[ix+2:]
    while "+-" in a:
        ix = a.index("+-")
        a = a[:ix] + "-" + a[ix+2:]
    while "+0.0" in a:
        ix = a.index("+0.0")
        a = a[:ix] + a[ix + 4:]
    return a

def mult(o):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(o), 1):

        n = str(o[i][1])
        if ("*" in n):
            n = n.split("*")
            while (len(n) != 1):
                if(str(n[0]) in alphabet):
                    n.append(n[0])
                    n.remove(n[0])
                elif(str(n[1]) in alphabet):
                    o[i][1] = n[1]
                    n.remove(n[1])
                    o[i][2] = int(n[0])
                    pass
                n[0] = float(n[0])*float(n[1])
                n.remove(n[1])
                o[i][1] = n[0]
    return o

def umst(a,b,w):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c = []
    for i in range (0, len(a), 1):
        c.append(a[i][1])
    d = []
    for i in range (0, len(b), 1):
        d.append(b[i][1])
    f = []
    try:
        e = c.index(w)
        c = []
        c.append(a[e])
        f = []
        for i in range(0, len(a), 1):
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
    except ValueError:
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
    c = add(c)
    if(c[0][0] == "-"):
        m = c[0][2]*-1
    else:
        m = c[0][2]
    for i in range (0, len(f), 1):
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

ü("x+5=10","x")
#sy("x+5=10","x")
