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


if __name__ == "__main__":
    lag_nytt_emne()
    print(emnekoder, semestre, studiepoeng)

