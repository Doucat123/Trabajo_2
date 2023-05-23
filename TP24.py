#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima 
# de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad 
# de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

def posicion(pila):
    aux = pila()
    count = 0
    while (pila.size() > 0):
        dat = pila.pop()
        count +=1
        if dat.nombre == "Rocket Raccoon":
            print (count)
        if dat.nombre == "Groot":
            print (count)
        aux.append(dat)
    while (aux.size() > 0):
        dat = aux.pop()
        pila.append(dat)

def masde4(pila):
    aux = pila()
    while (pila.size() > 0):
        dat = pila.pop()
        if dat.numpelis > 5:
            print (dat.nombre)
            print (dat.nombre+ " participo en "+dat.numpelis+" peliculas")
        aux.append(dat)
    while (aux.size() > 0):
        dat = aux.pop()
        pila.append(dat)

def viudanegra(pila):
    aux = pila()
    while (pila.size() > 0):
        dat = pila.pop()
        if dat.nombre == "Black widow":
            print ("Black widow aparecio en este numero de peliculas="+dat.numpelis)
        aux.append(dat)
    while (aux.size() > 0):
        dat = aux.pop()
        pila.append(dat)

def pempieza(pila):
    aux = pila()
    while (pila.size() > 0):
        dat = pila.pop()
        if dat.nombre.startwhit("C") or dat.nombre.startwhit("D") or dat.nombre.startwhit("G"):
            print (dat)
        aux.append(dat)
    while (aux.size() > 0):
        dat = aux.pop()
        pila.append(dat)