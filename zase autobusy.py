#otvorenie suboru
subor = open("bus_vytazenost.txt","r")

#zadeklarovanie premennych
kapacita = subor.readline()
pocet_zastavok = 0
naplnenost = 0
naj = 0

#vytvorenie prazdnych zoznamov a slovnika
zastavky = []
presiahnute = []
vytazenost = {}

def zistenie(): #funkcia na zistenie pozadovanych info
    #zadeklarovanie globalnych premennych
    global pocet_zastavok, kapacita, naplnenost
    
    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        #rozdelenie riadku na hodnoty
        riadocek = riadok.split()

        #vypocet naplnenosti pre zastavku
        naplnenost = naplnenost + int(riadocek[0]) - int(riadocek[1])

        #podmienka na vlozenie do zoznamu a slovnika
        if len(riadocek) == 3:
            zastavky.append(riadocek[2])
            vytazenost[riadocek[2]] = naplnenost
        elif len(riadocek) == 4:
            zastavky.append(riadocek[2]+" "+riadocek[3])
            vytazenost[riadocek[2]+" "+riadocek[3]] = naplnenost

        #zmena premennej
        pocet_zastavok += 1

def porovnavanie(): #funkcia na porovnavanie zistenych info
    #zadeklarovanie globalnej premennej
    global naj
    
    for i in range(len(vytazenost)): #cyklus v hodnote velkosti slovnika
        #podmienka na zapisanie presiahnutej zastavky do slovnika
        if int(list(vytazenost.values())[i]) > 50:
            presiahnute.append(list(vytazenost.keys())[i])

        #podmienka na zistenie najvacsieho poctu cestujucich
        if int(list(vytazenost.values())[i]) > naj:
            naj = int(list(vytazenost.values())[i])

#zavolanie funkcii
zistenie()
porovnavanie()

#vypisanie pozadovanych hodnot   
print("Dokopy zastávok:",pocet_zastavok)
print("Všetky zastávky:",", ".join(zastavky))
print("Zastávky s presiahnutou kapacitou:",", ".join(presiahnute))
print("Naraz najviac ľudí:",naj)

#zatvorenie suboru
subor.close()
