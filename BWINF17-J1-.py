deko = int(input())  # Sektion Eingabe
anzahl = int(input())
buecher = []  # Erstellen einer leeren Liste
for i in range(0, anzahl):  # input in Liste einordnen
    buecher.append(int(input()))  # im Beispiel erwähnte Typ-Änderung des inputs
buecher.sort()  # elemente der liste der Größe nach sortieren


# Sektion Programm
a = int(buecher[0])  #das erste(also kleinste) Element der Liste ist die erste Vergleichszahl (a genannt)
for i in buecher:  # alle Elemente der Liste werden überprüft

    if i == "X":  # überspringen der Platzhalter
        continue

    if buecher[buecher.index(i) - 1] == "X":  # die Zahl nach dem Platzhalter ist die neue Vergleichszahl
        a = i
        continue

    if int(a) + 30 < int(i):  # Ist die zu überprüfende Zahl weiter als 30mm von der Vergleichszahl entfert?
        buecher.insert(buecher.index(i), "X")  # Ja,-->einsetzen des Platzhalters
    # falls keine Bedinung erfüllt wird, wird das nächste Element der Liste überprüft

# Sektion Ausgabe
if buecher.count("X") > deko:  # Ausgabe: zu wenig deko
    print("Die Aufstellung ist nicht möglich: Deko benötigt:", buecher.count("X"), "; Deko vorhanden:", deko)
    print("Aufstellung mit ", buecher.count("X"), "Dekorationen:", buecher)
elif buecher.count("X") < deko:  # "Sonderfall": zu viel deko
    print("Aufstellung möglich, allerdings werden", deko - buecher.count("X"), "Dekorationen nicht benötigt")
    print("Aufstellung:", buecher)
elif buecher.count("X") == deko:  # Ausgabe: Aufstellung möglich
    print("Es ist möglich!")
    print("Aufstellung:", buecher)

