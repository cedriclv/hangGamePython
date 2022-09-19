from tkinter import *
from random import *

#Selection mot à tirer
listWords = ["fleur", "voiture", "maison", "garage", "parking"]
nbAlea = randrange(0, len(listWords))
motChoisi = listWords[nbAlea]
motChoisi = motChoisi.upper()


nbFautes = 0
lettresTrouvees = []
motChoisiCache = motChoisi
winnerStatus = False


def testVictoire():
    global winnerStatus
    compteurLettreOk = 0
    for le in motChoisi:
        statutLettreTrouvé = False
        #		while statutLettreTrouvé == False:
        for l in lettresTrouvees:
            if l == le:
                statutLettreTrouvé = True
        if statutLettreTrouvé == True:
            compteurLettreOk = compteurLettreOk + 1
    if compteurLettreOk == len(motChoisi):
        winnerStatus = True


def winLoseMsg(winSt, nbF):
    if winSt == True:
        canvasDessin.create_text(100,
                                 250,
                                 text="YOU WIN",
                                 font='Helvetica 80 bold',
                                 anchor="sw",
                                 fill="green",
                                 angle=15)
    if winSt == False and nbF >= 11:
        canvasDessin.create_text(100,
                                 150,
                                 text="YOU LOSE",
                                 font='Helvetica 80 bold',
                                 anchor="sw",
                                 fill="red",
                                 angle=-15)


def testEtDessin(motATester, lettreATester):
    testLettre(motATester, lettreATester)
    dessinPendu(nbFautes)
    ecritureMot()
    testVictoire()
    winLoseMsg(winnerStatus, nbFautes)


def testLettre(motATester, lettreATester):
    global nbFautes
    i = 0
    mauvaisChoix = True
    while i < len(motATester):
        if motATester[i] == lettreATester:
            lettresTrouvees.append(lettreATester)
            mauvaisChoix = False
        i = i + 1
    if mauvaisChoix == True:
        nbFautes = nbFautes + 1
    print("nb de fautes :", nbFautes)


#Afficher chaque lettre du mot
#determiner le nb de lettre, ensuite faire un boucle pour mettre x fois "_"
def ecritureMot():
    x, y = 100, 80
    i = 0
    while i < len(motChoisi):
        lettreAEcrire = "_"
        for l in lettresTrouvees:
            if (l == motChoisi[i]):
                lettreAEcrire = l
        canvasMot.create_text(x,
                              y,
                              text=lettreAEcrire,
                              font='Helvetica 40 bold',
                              anchor="sw")
        x = x + 40
        i = i + 1


#Fonctions creation touche clavier
def creationTouche(nomTouche, x1, y1):
    boutonTempo = Button(canvasClavier,
                         text=nomTouche,
                         command=lambda: testEtDessin(motChoisi, nomTouche))
    boutonTempo.place(x=x1, y=y1, height=30, width=30)


#Fonctions affichage clavier
def tracerLigneClavier(lettresClavierRang1, xDebut, yDebut):
    i = 0
    while i < len(lettresClavierRang1):
        creationTouche(lettresClavierRang1[i], xDebut, yDebut)
        xDebut = xDebut + 60
        i = i + 1


#Creer Fenetre

maFenetre = Tk()

#Creer 2 panelWindow

panelHaut = PanedWindow(maFenetre,
                        orient=HORIZONTAL,
                        width=800,
                        height=400,
                        bg="blue")
panelHaut.pack()
panelBas = PanedWindow(maFenetre,
                       orient=HORIZONTAL,
                       width=800,
                       height=100,
                       bg="black")
panelBas.pack()

#Creer Canvas
canvasDessin = Canvas(panelHaut, width=770, height=300, bg="lightblue")
canvasDessin.pack()
canvasMot = Canvas(panelHaut, width=780, height=80, bg="purple")
canvasMot.pack()
canvasClavier = Canvas(panelBas, width=780, height=150, bg="green")
canvasClavier.pack()

XDebDess, yDebDess = 300, 250


#Afficher Dessin
def dessinPendu(nbF):
    canvasDessin.delete("all")
    if nbF >= 1:
        x0, y0, x1, y1 = XDebDess, yDebDess, XDebDess + 200, yDebDess + 0
        canvasDessin.create_line(x0, y0, x1, y1, fill="green")
    if nbF >= 2:
        x0, y0, x1, y1 = (x0 + x1) / 2, y0, (x0 + x1) / 2, y0 - 200
        canvasDessin.create_line(x0, y0, x1, y1, fill="blue")
    if nbF >= 3:
        x0, y0, x1, y1 = x0, y1, x1 + 100, y1
        canvasDessin.create_line(x0, y0, x1, y1, fill="purple")
    if nbF >= 4:
        x0, y0, x1, y1 = x1, y1, x1, y1 + 50
        canvasDessin.create_line(x0, y0, x1, y1, fill="orange")
    if nbF >= 5:
        x0, y0, x1, y1 = x1 - 20, y1, x1 + 20, y1 + 2 * 20
        canvasDessin.create_oval(x0, y0, x1, y1, fill="blue")
    if nbF >= 6:
        x0, y0, x1, y1 = x1 - 20, y1, x1 - 20, y1 + 40
        canvasDessin.create_line(x0, y0, x1, y1, fill="yellow")
    if nbF >= 7:
        x0, y0, x1, y1 = x0, y0, x1 + 30, y0 + 30
        canvasDessin.create_line(x0, y0, x1, y1, fill="green")
    if nbF >= 8:
        x0, y0, x1, y1 = x0, y0, x1 - 30 * 2, y1
        canvasDessin.create_line(x0, y0, x1, y1, fill="purple")
    if nbF >= 9:
        x0, y0, x1, y1 = x0, y0 + 40, x0 + 35, y0 + 40 + 35
        canvasDessin.create_line(x0, y0, x1, y1, fill="black")
    if nbF >= 10:
        x0, y0, x1, y1 = x0, y0, x1 - 2 * 35, y1
        canvasDessin.create_line(x0, y0, x1, y1, fill="orange")


#    canvasDessin.create_text(50,
#                             200,
#                             text=("Essais", "Restants", 11 - nbF),
#                             font='Helvetica 25 bold',
#                             anchor="sw")

dessinPendu(nbFautes)

#Afficher chaque lettre du mot
#determiner le nb de lettre, ensuite faire un boucle pour mettre x fois "_"

ecritureMot()
#Afficher Clavier

x, y = 100, 10

lettresClavierRang1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
lettresClavierRang2 = ["J", "K", "L", "M", "N", "O", "P", "Q", "R"]
lettresClavierRang3 = ["S", "T", "U", "V", "W", "X", "Y", "Z"]

tracerLigneClavier(lettresClavierRang1, x, y)
y = y + 50
tracerLigneClavier(lettresClavierRang2, x, y)
x = x + 60
y = y + 50
tracerLigneClavier(lettresClavierRang3, x, y)

maFenetre.mainloop()
