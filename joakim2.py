if __name__ == "__main__":
    liste_semester = []
    liste_semester.append("Høst")     
    liste_semester.append("Høst")     
    liste_semester.append("Høst")     
    liste_semester.append("Høst")    
    liste_semester.append("Vår")  

    liste_emnekode = []
    liste_emnekode.append("ELE100")   
    liste_emnekode.append("DAT120")   
    liste_emnekode.append("MAT100")   
    liste_emnekode.append("FYS103")   
    liste_emnekode.append("KJE100")  

    liste_studiepoeng = []
    liste_studiepoeng.append(10)      
    liste_studiepoeng.append(10)     
    liste_studiepoeng.append(5)       
    liste_studiepoeng.append(10)      
    liste_studiepoeng.append(10)      

    studieplan = [[] for i in range(6)]

# ========== STUDIEPLANLEGGING ==========
def legg_til_emne_i_studieplan(liste_semester, liste_emnekode, liste_studiepoeng):
    """
    # Lar bruker velge et emne og plassere det i et bestemt semester
    # Validerer at semestertype stemmer (Høst/Vår) og at emnet ikke allerede finnes
    """
    print()
    print(liste_semester, liste_emnekode, liste_studiepoeng)  # Viser tilgjengelige emner

    # Be bruker velge emne fra listen
    emne_index = int(input("Velg emnet etter hvilket nummer det er i lista (Bruk tall): ")) - 1
    print(f"Du valgte: {liste_emnekode[emne_index]}")
    
    # Be bruker velge hvilket semester (1-6)
    semester_studieplan = int(input("Hvilket semester ønsker du å legge emne til i? Velg 1-6: "))
    print(f"Du valgte semester {semester_studieplan}")

    # Validering: Sjekk at semester er gyldig (1-6)
    if semester_studieplan < 0 or semester_studieplan >= 6:
        print("Ugyldig semester")
        return

    # Sjekk om emnet allerede er plassert i studieplanen
    for s in studieplan:
        if liste_emnekode[emne_index] in s:
            print(f"{liste_emnekode[emne_index]} er allerede i studieplanenen, den ble ikke lagt til.")
            return
    
    # Validering: Sjekk at emnet passer med semesterets type
    # Oddetall semester (1,3,5) = Høst, Partall semester (2,4,6) = Vår
    semestertype = "Høst" if semester_studieplan in (1, 3, 5) else "Vår"
    if liste_semester[emne_index] != semestertype:
        print(f"Emnet kan ikke legges til i {semestertype}-semesteret.")
        return

    # Validering: Sjekk at semesteret ikke får over 30 studiepoeng
    # Beregner nåværende studiepoeng i det valgte semesteret
    total_studiepoeng_i_semester = sum(liste_studiepoeng[liste_emnekode.index(emnekode)] for emnekode in studieplan[semester_studieplan - 1])
    if total_studiepoeng_i_semester + liste_studiepoeng[emne_index] > 30:
        print("Emnet ble ikke lagt til studieplanen fordi studieplanen overskrider 30 studiepoeng med emnet du ville legge til.")
        return
    
    # Alt OK - legg til emnet i det valgte semesteret
    studieplan[semester_studieplan - 1].append(liste_emnekode[emne_index])
    print(f"{liste_emnekode[emne_index]} ble lagt til i studieplanen")

# ========== UTSKRIFT OG VISNING ==========
def print_liste_av_registrerte_emner(liste_emnekode, liste_semester, liste_studiepoeng):
    # Viser alle registrerte emner i en oversiktlig tabell
    # Nummererer emnene for lett referanse
    
    print("De registrerte emnene er: ")
    nummer = 0
    for i, j, k in zip(liste_emnekode, liste_studiepoeng, liste_semester):
        nummer +=1
        print(f"{nummer}  {i}     {j}     {k}")  # Nummer, emnekode, studiepoeng, semester
    input("Trykk enter")

# ========== FILLAGRING ==========
def lagre_emner_til_fil(liste_emnekode, liste_studiepoeng, liste_semester, filnavn="emner.txt"):
    # Lagrer alle emner til en tekstfil i tabellformat
    # Bruker tab-separerte verdier for lesbarhet
    
    with open(filnavn, "w", encoding="utf-8") as fil:
        fil.write("Emnekode\tStudiepoeng\tSemester\n")  # Overskrifter
        for kode, poeng, sem in zip(liste_emnekode, liste_studiepoeng, liste_semester):
            fil.write(f"{kode}\t{poeng}\t{sem}\n")  # Data rad for rad
    print(f"Emner lagret til {filnavn}")

def lagre_studieplan_til_fil(studieplan, filnavn="studieplan.txt"):
    # Lagrer den organiserte studieplanen til fil
    # Viser hvilke emner som er i hvert semester
    
    with open(filnavn, "w", encoding="utf-8") as fil:
        for i, semester in enumerate(studieplan, start=1):
            fil.write(f"Semester {i}:\n")
            for emnekode in semester:
                fil.write(f"  - {emnekode}\n")  # Innrykk for å vise hierarki
            fil.write("\n")
    print(f"Studieplan lagret til {filnavn}")

if __name__ == "__main__":
    while True:
        legg_til_emne_i_studieplan(liste_semester, liste_emnekode,liste_studiepoeng)
        print(studieplan)
        
if __name__ == "__main__":
    print_liste_av_registrerte_emner(liste_emnekode)


    