import numpy as np
import numpy

width, height = input().split()
width, height = int(width), int(height)

field = np.zeros((height, width), int) # leeres array bestehend aus Nullen in der richtigen Größe
print(" ")  # deutlichere Trennung von Eingabe und Ausgabe

anzahl = int(input())
for i in range(0, anzahl):  # jeder Adler wird einzeln überprüft
    hawk = input().split()
    x = 0
    time = int(hawk[2]) # hawk[2] ungleich 0
# die Himmelsrichtungen werden einzeln angegeben, da sich das Gefüge von Fall zu Fall unterscheidet
    if hawk[3] == "N":
        for a in range(height): # die Felder werden der Reihe nach überprüft
            if field[height - int(hawk[1]) + x, int(hawk[0]) - 1] == 3: # wenn das Feld schon als unsicher erklärt wurde kann es nicht mehr umklassifiziert werden
                pass
            elif time > 30:
                field[height - int(hawk[1]) + x, int(hawk[0]) - 1] = 2  # Der Fall 2,sicher durch Zeit ist "besser" als Fall 4(da,4 mit unknown angegeben wird).Daher davor.
            elif height - int(hawk[1])+x >= 15:   # >= muss sein
                field[height - int(hawk[1]) + x, int(hawk[0]) - 1] = 4  #Feld sicher durch Rückweg
            else:
                field[height - int(hawk[1]) + x, int(hawk[0]) - 1] = 3 # unsicher
            time = time + 1
            x = x - 1  # nach oben


    if hawk[3] == "S":
        for a in range(height):
            if field[height - int(hawk[1])+x, int(hawk[0]) - 1] == 3:
                pass
            elif time > 30:  #<= nicht
                field[height - int(hawk[1]) + x, int(hawk[0]) - 1] = 2
            elif height-(height - int(hawk[1])+x) > 15:   # Klammer wichtig
                field[height - int(hawk[1]) + x, int(hawk[0]) - 1] = 4
            else:
                field[height - int(hawk[1]) + x, int(hawk[0]) - 1] = 3
            time = time + 1
            x = x + 1   #nach unten


    if hawk[3] == "O":
        for a in range(width):
            if field[height - int(hawk[1]), int(hawk[0]) - 1 + x] == 3: # x beim anderen Kor-teil als bei N/S
                pass
            elif time > 30:
                field[height - int(hawk[1]), int(hawk[0]) - 1 + x] = 2
            elif width - (int(hawk[0]) - 1 + x) > 15:  # Klammer wichtig
                field[height - int(hawk[1]), int(hawk[0]) - 1 + x] = 4
            else:
                field[height - int(hawk[1]), int(hawk[0]) - 1 + x] = 3
            time = time + 1
            x = x + 1   #nach rechts

    if hawk[3] == "W":
        for a in range(width):
            if field[height - int(hawk[1]), int(hawk[0]) - 1 + x] == 3:
                pass
            elif time > 30:
                field[height - int(hawk[1]), int(hawk[0]) - 1 + x] = 2
            elif int(hawk[0]) - 1 + x >= 15:  # >= no -width
                field[height - int(hawk[1]), int(hawk[0]) - 1 + x] = 4
            else:
                field[height - int(hawk[1]), int(hawk[0]) - 1 + x] = 3
            time = time + 1
            x = x - 1   #nach links

position = numpy.argwhere(field == 2).ravel()   #koordinaten der 2en als eindimensionales array
x=0
for i in range(len(position)//2):
    print(position[1+x]+1,height-position[0+x],1,30)    #Ausgabe normaler Koordinaten(nicht Numpy mit [0,0] in der linken oberen Ecke)
    x=x+2


position = numpy.argwhere(field == 4).ravel()
x=0
for i in range(len(position)//2):
    print(position[1+x]+1,height-position[0+x],"unknown")
    x=x+2
field = str(field)
print("0 steht für absolut sicher; 2 für sicher ; 3 für unsicher")
print(numpy.core.defchararray.replace(field,"4","2")) #Ausgabe des Feldes bei der die 4en durch 2er ersetzt werden

if time > 30:
    field[height - int(hawk[1]), int(hawk[0]) - 1 + x] = 2
    print(int(hawk[0]) + x, int(hawk[1]), 1, 30) #Angabe des sicheren Fel-des direkt nach „der Umbenennung“ von 0 zu 2
