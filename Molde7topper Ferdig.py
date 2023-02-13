# listene mine og en variabel
storliste = []
finliste = []
loop = 1


# klasser og startid for menn og kvinner

def klasserogstartm(k, t):
    for o in range(10, 81, 5):
        o1 = int((o - 5) / 5)
        todesimaler = t + 0.02 * (o1 - 1)
        print(k + str(o1) + " " + str("%.2f" % todesimaler))


# meny
def meny():
    print()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print()
    print("Hei, velkommen til Molde7Topper")
    print()
    print("Hva vil du gjøre?")
    print("1. påmelding")
    print("2. Se hvem som er påmeldt")
    print("3. Starttidspunkt")
    print("4. avslutt")


# starter en while løkke
while True:
    # variabler
    outatime = 1
    startid = 0.0
    n1 = 0
    # henter menyen
    meny()
    # inputen lar brukeren velge hva han vil gjøre
    x = input()
    # Hvis brukeren valgte valg 1.
    if x == "1":
        # starter en while løkke
        while outatime == 1:
            # lar brukeren skrive inn navne sitt
            nvn = str(input("skriv inn hele navnet ditt? "))
            # spør om brukeren er med i en klubb
            kl = input("Er du medlem i en klubb? tast 1 for ja og tast 2 for nei ")
            # hvis brukeren er med i en klubb så spør koden hvilken klubb han er med i
            if kl == "1":
                kl = str(input("Hvilken klubb er du med i? "))
            # hvis brukeren ikke er med i en klubb skriver koden ingen klubb for å beholde posisjonen på dataen.
            elif kl == "2":
                kl = "ingen klubb"
            # feil melding
            else:
                print("ugyldig input")
                continue
            # prøv spør brukeren når han er født
            try:
                alder = int(input("Når er du født? "))
            # hvis det ikke går skriv en feilmelding
            except ValueError:
                print("ugyldig input")
                continue
            # spør hvilket kjønn brukeren er
            print("hvilket kjønn er du?")
            print("Tast 1 for mann")
            print("Tast 2 for kvinne")
            # lar brukeren velge kjønn
            kj = (input())
            # hvis kjønn er mann blir variabelen "M" og blir lagret lengere nede i koden
            if kj == "1":
                kj = "M"
            # hvis kjønn er kvinne blir variabelen "M" og blir lagret lengere nede i koden
            elif kj == "2":
                kj = "K"
            # feilmelding
            else:
                print("ugyldig input")
                continue
            # spør hvilken distanse brukeren vil delta i
            print("Hvilken distanse vil du delta i? ")
            print("Tast 1 for ultra (40km)")
            print("Tast 2 for vanlig (19km)")
            # lar brukeren velge distanse
            d = int(input())
            # hvis distanse er ultra blir variabelen "ultra" og blir lagret lengere nede i koden
            if d == 1:
                d = "ultra"
            # hvis distanse er vanlig blir variabelen "vanlig" og blir lagret lengere nede i koden
            elif d == 2:
                d = "vanlig"
            # feilmeldig
            else:
                print("ugyldig input")
                continue

            # spør hvilket år deltakeren skal løpe
            aar = int(input("Hvilket år skal du delta i? "))
            # matte for å finne ut hvor gammel brukeren er når han skal løpe
            alder = aar - alder
            # for løkke for å lage klasser fra 10-80 og hopper med 5. f.eks 10-15, 15-20, osv.
            for n in range(10, 81, 5):
                # hvis "for løkka" er mindre en alder og "for løkka" + 5.
                # finner n1 ut hvilken klasse du kommer i f.eks m1, m2, k1, k2, osv.
                # disse klassene blir bestemt sånn at, fra alderen 10-15, blir klasse "M/K" 1 osv.
                if n <= alder < n + 5:
                    n1 = int((n - 5) / 5)
                    # Hvis kjønnet er man blir
                    # startiden til klassen din regnut ut fra kl 10.00 og framover med 2 min interval.
                    if kj == "M":
                        startid = 10.00 + 0.02 * (n1 - 1)
                        # Hvis kjønnet ikke er man blir
                        # startiden til klassen din regnet ut ut fra kl 9.00 og framover med 2 min interval.
                    else:
                        startid = 9.00 + 0.02 * (n1 - 1)
            # lager klasen din
            klasse = kj + str(n1)
            # printer en melding som sier at påmeldingen er vellyket og printer navn, klasse og startid.
            print("påmelding vellyket")
            print(nvn, klasse, startid)
            # legger all informasjon inn i en liste
            finliste = [nvn, alder, kl, d, klasse, startid, aar]
            # lagrer lista i en større liste
            storliste.append(finliste)
            # lager en knapp som lar deg gå tilbake
            otat = int(input("tast 1 for å gå tilbake"))
            # den gjør det med å ødellege loopen som vi lagde i starten av if setningen.
            if otat == 1:
                outatime = 0
            break

    # Hvis brukeren valgte valg 1.
    elif x == "2":
        # starter en loop
        while outatime == 1:
            # printer en meny
            print("1. se alle")
            print("2. se alle fra en klasse")
            print("3. se alle fra en klubb")
            # inputen gjør at brukeren kan velge fra menyen
            pr = int(input())

            # Hvis brukeren valgte valg 1.
            if pr == 1:
                # lager en for løkke sånn at all informasjonen kommer nedover og ikke bortover
                for l in storliste:
                    print(l)
                    # lager en knapp som lar deg gå tilbake
                    otat = int(input("tast 1 for å gå tilbake"))
                    # den gjør det med å ødellege loopen som vi lagde i starten av if setningen.
                    if otat == 1:
                        outatime = 0

            # Hvis brukeren valgte valg 2.
            elif pr == 2:
                # spør hvilken klasse du vil se medlemer fra
                print("Hvilken klasse vil du se medlemer fra")
                # inputen gjør at brukeren kan skrive inn en klasse han vil se medlemmer fra
                sokord = input()
                # for løkka gjør at vi kan søke i den store lista med alle deltakerene.
                for l in storliste:
                    # søker etter samme ord i posisjon 4 i listan
                    if l[4] == sokord:
                        # skriver ut alle med samme søke ord i posisjon 4
                        print(l)
                # lager en knapp som lar deg gå tilbake
                otat = int(input("tast 1 for å gå tilbake"))
                # den gjør det med å ødellege loopen som vi lagde i starten av if setningen.
                if otat == 1:
                    outatime = 0

            # Hvis brukeren valgte valg 3.
            elif pr == 3:
                print("Hvilken klubb vil du se medlemer fra")
                # inputen gjør at brukeren kan skrive inn en klubb han vil se medlemmer fra
                sokord = input()
                # for løkka gjør at vi kan søke i den store lista med alle deltakerene.
                for l in storliste:
                    # søker etter samme ord i posisjon 2 i listan
                    if l[2] == sokord:
                        # skriver ut alle med samme søke ord i posisjon 2
                        print(l)
                # lager en knapp som lar deg gå tilbake
                otat = int(input("tast 1 for å gå tilbake"))
                # den gjør det med å ødellege loopen som vi lagde i starten av if setningen.
                if otat == 1:
                    outatime = 0

    # Hvis brukeren valgte valg 3.
    elif x == "3":
        # starter en løkke
        while outatime == 1:
            # lar deg velge mellom menn sin startid og kvinner sin startid
            print("Tast 1 for mann")
            print("Tast 2 for kvinne")
            kj2 = int(input())
            # hvis brukeren valgte mann printer startidene til mennene
            if kj2 == 1:
                klasserogstartm("M", 10.00)
            # hvis brukeren valgte mann printer startidene til kvinnene
            elif kj2 == 2:
                klasserogstartm("K", 09.00)
            # feilmeldig
            else:
                print("ugyldig input")
                continue

            print()
            # lager en knapp som lar deg gå tilbake
            otat = int(input("tast 1 for å gå tilbake"))
            # den gjør det med å ødellege loopen som vi lagde i starten av if setningen.
            if otat == 1:
                outatime = 0

    # hvis brukeren valgte valg 4.
    elif x == "4":
        # slutter programmet
        exit()

    # feilmeldig
    else:
        print("ugyldig input")
        continue
