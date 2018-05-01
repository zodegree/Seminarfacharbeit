alphabet = "abcdefghijklmnopqrstuvwxyz"
o=[["+","4*3"]]
for i in range(0, len(o), 1):

    n = str(o[i][1])
    if ("*" in n):
        n = n.split("*")
        while (len(n) != 1):
            #if(str(n[0]) in alphabet):
            #    n.append(n[0])
            #    n.remove(n[0])
            #elif(str(n[1]) in alphabet):
            #    o[i][1] = n[1]
            #    n.remove(n[1])
            #    o[i][2] = int(n[0])
            #    pass
            n[0] = float(n[0])*float(n[1])
            n.remove(n[1])
            o[i][1] = n[0]
print(o,"o")