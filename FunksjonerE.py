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

def Nytt_emne():
    while True:
        Nytt_emne_navn = check_var("Hva er Emnekoden? eks:DAT120: ")
        while True:
            xsemester = input("Hvilket semester? \n [1] Høst \n [2] Vår ").lower().strip()
            if xsemester == "høst" or xsemester == "host" or xsemester == "1":
                semester = "Høst"
                break
            elif xsemester == "vår" or xsemester == "vaar" or xsemester == "2":
                semester = "Vår "
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
             
    
        return Nytt_emne_navn, semester, studiepoeng
    



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