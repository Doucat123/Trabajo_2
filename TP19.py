#Dada una pila de películas de las que se conoce su título, estudio cinematográfico y año de estreno,
#desarrollar las funciones necesarias para resolver las siguientes actividades:

#a. mostrar los nombre películas estrenadas en el año 2014;
#b. indicar cuántas películas se estrenaron en el año 2018;
#c. mostrar las películas de Marvel Studios estrenadas en el año 2016.



def pelis_2014(pila):
    aux = pila()
    while (pila.size() > 0):
        dat = pila.pop()
        if dat.año == 2014:
            print (dat.peli.nombre)
        aux.append(dat)
    while (aux.size() > 0):
        dat = aux.pop()
        pila.append(dat)

def numero_2018(pila):
    aux = pila()
    count = 0
    while (pila.size() > 0):
        dat = pila.pop()
        if dat.año == 2018:
            count +=1
        aux.append(dat)
    while (aux.size() > 0):
        dat = aux.pop()
        pila.append(dat)
    print (count)

def numero_2018(pila):
    aux = pila()
    while (pila.size() > 0):
        dat = pila.pop()
        if dat.año == 2016 and dat.productora == "Marvel Studios":
            print (dat)
        aux.append(dat)
    while (aux.size() > 0):
        dat = aux.pop()
        pila.append(dat)
