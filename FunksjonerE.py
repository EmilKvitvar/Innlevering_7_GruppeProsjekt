def check_float(variabel):
    while True:
        multiplikator = {"m": 1_000_000, "k": 1_000 } #prøver noe nytt 
        verdi = input(variabel).strip().lower().replace(",",".")
        if verdi.endswith("x"):
            return None
        try:
            if verdi[-1] in multiplikator:
                return float(verdi[:-1]) * multiplikator[verdi[-1]]
            else:
                return float(verdi)
        
        except ValueError:
            print("\nSkriv et gyldig tall")
        
def check_int(variabel):
    while True:
        multiplikator = {"m": 1_000_000, "k": 1_000 }
        verdi = input(variabel).lower().strip().replace(";",".")

        if verdi.endswith("x"):
            return None
        try:
            if verdi[-1] in multiplikator:
                return int(verdi[:-1]) * multiplikator[verdi[-1]]
            
            else:
                return int(verdi)
        except ValueError:
            print("\nSkriv et gyldig tall")

def check_var(variabel):
    while True:
        verdi = input(variabel).lower().strip().replace("å","aa").replace("ø","o").replace("æ","ae")

        if verdi.endswith("x"):
            return None
        else:
            return verdi

def Nytt_emne(Gammelt_emne):
    while True:
        Nytt_emne_navn = check_var("Hva er Emnekoden? eks:DAT120: ").upper()
        
        if Nytt_emne_navn in Gammelt_emne:
            print(f"{Nytt_emne_navn} er allerede lagt til, vil du \n[1] Beholde og legge til et nytt emne \
                  \n[2] Fjerne faget fra minnet?")
            gammel_valg = check_int("")
            if gammel_valg == 1:
                continue  # Start på nytt med nytt emnenavn
            elif gammel_valg == 2:
                # Returner emnet som skal fjernes
                return Nytt_emne_navn, None, None, 1
            else:
                continue


        while True:
            xsemester = input("Hvilket semester? \n [1] Høst \n [2] Vår \n ").lower().strip()
            if xsemester == "høst" or xsemester == "host" or xsemester == "1":
                semester = "Host"
                break
            elif xsemester == "vår" or xsemester == "vaar" or xsemester == "2":
                semester = "Vaar "
                break
            else:
                "Skriv høst eller vår!"
                print("Trykk enter")

        while True:
            studiepoeng = check_float("Hvor mange studiepoeng gir emnet? ")
            if studiepoeng < 0:
                print("Det kan ikke være mindre enn 0")
            elif studiepoeng > 30:
                print("Det kan ikke være over 30")
            else:
                break 
        print(f"Emnenavnet er {Nytt_emne_navn}")
        print(f"Faget er på {semester.lower()}en")
        print(f"Du får {studiepoeng} studiepoeng")
        while True:
            x = check_var("Ser dette riktig ut? [1/ja] eller [2/nei]: ")
            if x == "ja" or x == "1":
                ferdig = 1
                break
            elif x == "nei" or x == "2":
                ferdig = 0
                break
            else:
                print("Skriv 'ja' eller '1' for ja, 'nei' eller '2' for nei")
                continue
        if ferdig == 1:
            Fjerne = 0
            break
        else:
            continue
    
    return Nytt_emne_navn, semester, studiepoeng, Fjerne

def sjekk_studiepoeng_i_semester(semester_nr, Emnenavn, Studiepoeng, Studieplan):
    total = 0
    for emne_i_semester in Studieplan[semester_nr]:
        if emne_i_semester in Emnenavn:
            indeks = Emnenavn.index(emne_i_semester)
            total += Studiepoeng[indeks]
    return total

def finn_emne_i_studieplan(emne_navn, Studieplan):
    for semester_nr in range(len(Studieplan)):
        if emne_navn in Studieplan[semester_nr]:
            return semester_nr
    return None

def legg_til_emne_i_studieplanen(Emnenavn, Semester, Studiepoeng, Studieplan):
    if len(Emnenavn) == 0:
        print("Ingen emner registrert ennå!")
        input("Trykk enter")
        return
    
    
    for i in range(len(Emnenavn)):
        print(f"\n--- Emne {i+1} av {len(Emnenavn)} ---")
        print(f"Emne: {Emnenavn[i]}")
        print(f"Type: {Semester[i]} fag")
        print(f"Studiepoeng: {Studiepoeng[i]}")
        
        
        semester_i_plan = finn_emne_i_studieplan(Emnenavn[i], Studieplan)
        
        if semester_i_plan is not None:
            print(f"Dette emnet er allerede i semester {semester_i_plan + 1}")
            
            while True:
                print("[1] Beholde der det er (gå til neste emne)")
                print("[2] Flytte til annet semester") 
                print("[3] Fjerne fra studieplanen")
                
                valg = check_int("Hva vil du gjøre? ")
                
                if valg == 1:
                    print("Beholder emnet der det er")
                    break 
                elif valg == 2:
                    Studieplan[semester_i_plan].remove(Emnenavn[i])
                    print(f"Flytter {Emnenavn[i]} fra semester {semester_i_plan + 1}")
                    break 
                elif valg == 3:
                    Studieplan[semester_i_plan].remove(Emnenavn[i])
                    print(f"Fjernet {Emnenavn[i]} fra semester {semester_i_plan + 1}")
                    break 
                else:
                    print("Ugyldig valg! Prøv igjen.")
                
            
            
            if valg == 1 or valg == 3:
                continue
        
        
        print(f"\nHvor vil du plassere {Emnenavn[i]}?")
        
        
        if Semester[i] == "Host":
            mulige_semestre = [1, 3, 5]  
            print("Høstemne kan legges i semester [1], [3] eller [5]")
        else: 
            mulige_semestre = [2, 4, 6]   
            print("Våremne kan legges i semester [2], [4] eller [6]")
        
        print("[0] Ikke legg til / Hopp over")
        
        while True:
            semester_valg = check_int("Hvilket semester? ")
            
            if semester_valg == 0:
                print("Hopper over dette emnet")
                break
            elif semester_valg in mulige_semestre:
                semester_indeks = semester_valg - 1 
                
                
                nåværende_studiepoeng = sjekk_studiepoeng_i_semester(semester_indeks, Emnenavn, Studiepoeng, Studieplan)
                ny_total = nåværende_studiepoeng + Studiepoeng[i]
                
                print(f"Semester {semester_valg} har nå {nåværende_studiepoeng} studiepoeng")
                print(f"Å legge til {Emnenavn[i]} ({Studiepoeng[i]} studiepoeng) = {ny_total} totalt")
                
                if ny_total > 30:
                    print(f"FEIL: Dette vil gi {ny_total} studiepoeng, som er over 30!")
                    print("Du må velge et annet semester eller hoppe over dette emnet.")
                    print("Prøv igjen.")
                    # Ingen break - går tilbake til semester-valg
                else:
                    # Legg til emnet bare hvis det er 30 eller mindre
                    Studieplan[semester_indeks].append(Emnenavn[i])
                    print(f"La til {Emnenavn[i]} i semester {semester_valg}!")
                    break 
                break
            else:
                print(f"Ugyldig semester! Velg fra {mulige_semestre} eller [0] for å hoppe over.")
                
    
    print("\nFerdig med å gå gjennom emnene!")

def print_studieplan(studieplan_liste):
    for i in range(len(studieplan_liste)):
        print(f"I semester {i + 1} har du fagene:")
        if len(studieplan_liste[i]) == 0:
            print("  Ingen fag")
        else:
            for emne in studieplan_liste[i]:
                print(f"  {emne}")
        input("Trykk enter")

def gyldig_studieplan(Emnenavn, Semester, Studiepoeng, Studieplan):
    total = 0
    for semester_nr in range(len(Studieplan)):
        for emne_i_semester in Studieplan[semester_nr]:
            if emne_i_semester in Emnenavn:
                indeks = Emnenavn.index(emne_i_semester)
                total += Studiepoeng[indeks]
    return total



def meny():
    print(f"-----------Meny-----------\
            \n1. Lag et nytt emne\
            \n2. Legg til et emne i studieplanen\
            \n3. Skriv ut ei liste over alle registrerte emner\
            \n4. Skriv ut studieplanen med hvilke emner som er i hver semester\
            \n5. Sjekk om studieplanen er gyldig eller ikke\
            \n6. Lagre emnene og studieplanen til fil\
            \n7. Les inn emnene og studeplanen fra fil\
            \nX. Avslutt")

if __name__ == "__Main__":
    Nytt_emne()