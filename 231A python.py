k = input()
ceros = 0
unos = 0
resultado = 0
general = []
if k.isnumeric() == True:
    for i in range(int(k)):
        p = input()
        for i in p:
            general.append(i)
        for i in general:
            if i == ' ':
                general.remove(i)
            else:
                pass
        for i in general:
            if int(i) == 1:
                unos += 1
            elif int(i) == 0:
                ceros += 1
        if unos > ceros:
            resultado += 1
            ceros = 0
            unos = 0
            general = []
        else:
            ceros = 0
            unos = 0
            general = []
print(resultado)

