# Variabler og lister
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

def legg_til_emne_i_studieplan(liste_semester, liste_emnekode, liste_studiepoeng):
    print()
    print(liste_semester, liste_emnekode, liste_studiepoeng)

    # Spør hvilket emne som skal legges inn i hvilket semester.
    emne_index = int(input("Velg emnet etter hvilket nummer det er i lista (Bruk tall): ")) - 1
    print(f"Du valgte: {liste_emnekode[emne_index]}")
    semester_studieplan = int(input("Hvilket semester ønsker du å legge emne til i? Velg 1-6: "))
    print(f"Du valgte semester {semester_studieplan}")

    # Sjekk gyldighet i semester
    if semester_studieplan < 0 or semester_studieplan >= 6:
        print("Ugyldig semester")
        return

    # Sjekk om emnet er i studieplanen
    for s in studieplan:
        if liste_emnekode[emne_index] in s:
            print(f"{liste_emnekode[emne_index]} er allerede i studieplanenen, den ble ikke lagt til.")
            return
    
    # Sjekk om emnet passer med  semesterets type
    semestertype = "Høst" if semester_studieplan in (1, 3, 5) else "Vår"
    if liste_semester[emne_index] != semestertype:
        print(f"Emnet kan ikke legges til i {semestertype}-semesteret.")
        return

    # Sjekk om det er over 30 studiepoeng
    total_studiepoeng_i_semester = sum(liste_studiepoeng[liste_emnekode.index(emnekode)] for emnekode in studieplan[semester_studieplan - 1])
    if total_studiepoeng_i_semester + liste_studiepoeng[emne_index] > 30:
        print("Emnet ble ikke lagt til studieplanen fordi studieplanen overskrider 30 studiepoeng med emnet du ville legge til.")
        return
    
    studieplan[semester_studieplan - 1].append(liste_emnekode[emne_index])
    print(f"{liste_emnekode[emne_index]} ble lagt til i studieplanen")

def print_liste_av_registrerte_emner(liste_emnekode, liste_semester, liste_studiepoeng):
    print("De registrerte emnene er: ")
    nummer = 0
    for i, j, k in zip(liste_emnekode, liste_studiepoeng, liste_semester):
        nummer +=1
        print(f"{nummer}  {i}     {j}     {k}")
    input("Trykk enter")

def lagre_emner_til_fil(liste_emnekode, liste_studiepoeng, liste_semester, filnavn="emner.txt"):
    with open(filnavn, "w", encoding="utf-8") as fil:
        fil.write("Emnekode\tStudiepoeng\tSemester\n")
        for kode, poeng, sem in zip(liste_emnekode, liste_studiepoeng, liste_semester):
            fil.write(f"{kode}\t{poeng}\t{sem}\n")
    print(f"Emner lagret til {filnavn}")

def lagre_studieplan_til_fil(studieplan, filnavn="studieplan.txt"):
    with open(filnavn, "w", encoding="utf-8") as fil:
        for i, semester in enumerate(studieplan, start=1):
            fil.write(f"Semester {i}:\n")
            for emnekode in semester:
                fil.write(f"  - {emnekode}\n")
            fil.write("\n")
    print(f"Studieplan lagret til {filnavn}")

if __name__ == "__main__":
    while True:
        legg_til_emne_i_studieplan(liste_semester, liste_emnekode,liste_studiepoeng)
        print(studieplan)
        
if __name__ == "__main__":
    print_liste_av_registrerte_emner(liste_emnekode)


    