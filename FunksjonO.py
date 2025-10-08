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


def importer_studieplan(Emnenavn, Semester, Studiepoeng):
    filnavn = "Studieplan_energi.txt"
    """
    Leser fag fra tekstfil og fyller listene Emnenavn, Semester og Studiepoeng.
    Format i filen skal være:
        Emnenavn : Semester : Studiepoeng
    hvor Semester er "Host" eller "Vaar"
    Linjer som starter med # eller som er tomme blir hoppet over.
    Returnerer de oppdaterte listene.
    """
    try:
        with open(filnavn, "r", encoding="utf-8") as f:
            linjer = f.readlines()
    except FileNotFoundError:
        print(f"Filen '{filnavn}' ble ikke funnet.")
        return Emnenavn, Semester, Studiepoeng

    antall = 0
    for i, linje in enumerate(linjer, start=1):
        linje = linje.strip()
        if not linje or linje.startswith("#") or ":" not in linje:
            continue

        # Split på ":"
        deler = linje.split(":")
        
        if len(deler) < 3:
            print(f"For få elementer i linje {i}: '{linje}'")
            continue

        navn = deler[0].strip()
        sem_str = deler[1].strip()
        sp_str = deler[2].strip()

        # Normaliser semester-navn (håndter store/små bokstaver)
        sem_str_lower = sem_str.lower()
        if sem_str_lower == "host":
            semester = "Host"
        elif sem_str_lower == "vaar":
            semester = "Vaar"
        else:
            print(f"Ukjent semester '{sem_str}' i linje {i}: '{linje}'")
            continue

        try:
            studiepoeng = float(sp_str.replace(",", "."))
        except ValueError:
            print(f"Feil i linje {i}: '{linje}' (studiepoeng ikke tall)")
            continue

        # Sjekk om emnet allerede finnes
        if navn in Emnenavn:
            print(f"Emnet '{navn}' finnes allerede og hoppes over")
            continue

        Emnenavn.append(navn)
        Semester.append(semester)
        Studiepoeng.append(studiepoeng)
        antall += 1

    print(f"\nImporterte {antall} fag fra '{filnavn}'.")
    return Emnenavn, Semester, Studiepoeng 
