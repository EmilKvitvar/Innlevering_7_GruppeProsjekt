def meny():
    print("lag et nytt emne")
    print("legg til et emne i studieplanen")
    print("skriv ut et liste over alle registrerte emner")
    print("skriv ut studieplanen med hvilke emner som er i hvert semester")
    print("sjekk om studieplanen er gyldig eller ikke")
    print("lagre emnene og studieplanen til fil")
    print("les inn emnene og studieplan til fil")
    print("avslutt")


emnekoder         = []    #fag
semestre          = []    # oddetall(høst) og partall(vår)
studiepoeng_liste = []    # heltall

def lag_nytt_emne():
    kode = input( "skriv emnekode her:")
    semester = input("skriv semester, (høst/ vår):")
    studiepoeng = int(input("skriv inn antall studeipoeng:"))

    emnekoder.append(kode)
    semestre.append(semester)
    studiepoeng_liste.append(studiepoeng)

    print (f"emnet{kode}, ({semester},{studiepoeng} stp) er lagt til")


def importer_studieplan(filnavn, Emnenavn, Semester, Studiepoeng):
    filnavn = "Studieplan_energi.txt"
    """
    Leser fag fra tekstfil og fyller listene Emnenavn, Semester og Studiepoeng.
    Format i filen skal være:
        Emnenavn;Semester;Studiepoeng
    eller
        Emnenavn,Semester,Studiepoeng
    Linjer som starter med # eller som er tomme blir hoppet over.
    Returnerer antall fag som ble importert.
    """
    try:
        with open(filnavn, "r", encoding="utf-8") as f:
            linjer = f.readlines()
    except FileNotFoundError:
        print(f"Filen '{filnavn}' ble ikke funnet.")
        return 0

    antall = 0
    for i, linje in enumerate(linjer, start=1):
        linje = linje.strip()
        if not linje or linje.startswith("#"):
            continue

        # Finn separator
        if ";" in linje:
            deler = linje.split(";")
        elif "," in linje:
            deler = linje.split(",")
        else:
            print(f"Ugyldig format i linje {i}: '{linje}' (mangler ; eller ,)")
            continue

        if len(deler) < 3:
            print(f"For få elementer i linje {i}: '{linje}'")
            continue

        navn = deler[0].strip()
        sem_str = deler[1].strip()
        sp_str = deler[2].strip()

        try:
            semester = int(sem_str)
            studiepoeng = float(sp_str.replace(",", "."))
        except ValueError:
            print(f"Feil i linje {i}: '{linje}' (semester/studiepoeng ikke tall)")
            continue

        Emnenavn.append(navn)
        Semester.append(semester)
        Studiepoeng.append(studiepoeng)
        antall += 1

    print(f"\nImporterte {antall} fag fra '{filnavn}'.")
    return navn, semester, studiepoeng 
