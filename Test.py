import Semi
def GL_RES():
    n = ["2x-2=y","2.5x+5x-13-1=y"]
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
    print(n[0],"USE")
    n[0] = Semi.ü(n[0], varlist[0])
    return (n[0])
print(GL_RES())
