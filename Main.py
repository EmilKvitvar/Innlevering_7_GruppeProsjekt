# ===================================================================
# STUDIEPLANLEGGER - GRUPPEPROSJEKT DAT120
# ===================================================================
# Et program som hjelper studenter med å lage og administrere studieplan
# Funksjoner:
# - Legge til/fjerne emner med validering
# - Organisere emner i 6 semestre (3 år)
# - Validere at studieplanen er på 180 studiepoeng totalt
# - Lagre og laste studieplan fra fil
# - Kontrollere at emner er i riktige semestre (Høst/Vår)
# ===================================================================

# Importerer egne moduler med ulike funksjoner
import FunksjonerE as E    # Emil sine funksjoner - validering og emnehåndtering
import FunksjonO as O      # Ole sine funksjoner - meny og filhåndtering  
import joakim2 as J        # Joakim sine funksjoner - utskrift og lagring

# Globale lister for å lagre emnedata
Emnenavn_liste = []        # Liste over alle emnekoder (f.eks. "DAT120")
Semester_liste = []        # Liste over hvilke semestre emnene tilhører ("Høst"/"Vår")
Studiepoeng_liste = []     # Liste over studiepoeng for hvert emne
Studieplan = [[] for i in range (6)]  # 2D-liste: 6 semestre med tomme lister


# HOVEDLØKKE - Programmet kjører til bruker avslutter
while True:
      Valg = 0
      # Viser hovedmenyen til brukeren
      O.meny()
      valg = E.check_int("Valg: ")  # Validert input fra bruker
      
      if valg == None:
            break

      # VALG 1: Lag et nytt emne eller fjern eksisterende emne
      elif valg == 1: 
            emnenavn, semester, studiepoeng, Fjerne = E.Nytt_emne(Emnenavn_liste)

            # Hvis bruker valgte å fjerne et emne
            if Fjerne == 1:
                  
                  if emnenavn in Emnenavn_liste:
                        # Finn indeksen til emnet som skal fjernes
                        indeks = Emnenavn_liste.index(emnenavn)
                        
                        # Fjern emnet fra alle tre lister samtidig
                        fjernet_emne = Emnenavn_liste.pop(indeks)
                        fjernet_semester = Semester_liste.pop(indeks)
                        fjernet_studiepoeng = Studiepoeng_liste.pop(indeks)
                        
                        print(f"Fjernet: {fjernet_emne} - {fjernet_semester} - {fjernet_studiepoeng} studiepoeng")
                  else:
                        print(f"Feil: {emnenavn} finnes ikke i listen!")
            
            # Hvis bruker valgte å legge til nytt emne
            else:
                  # Legg til emnet i alle tre lister
                  Emnenavn_liste.append(emnenavn)
                  Semester_liste.append(semester)
                  Studiepoeng_liste.append(studiepoeng)
                  print(f"La til: {emnenavn} - {semester} - {studiepoeng} studiepoeng")
                  
            input("Trykk enter...")  # Pause før vi går tilbake til menyen
      
      # VALG 2: Legg til emne i studieplanen (fordel emner på semestre)
      elif valg == 2:
            E.legg_til_emne_i_studieplanen(Emnenavn_liste, Semester_liste,Studiepoeng_liste, Studieplan)

      # VALG 3: Vis alle registrerte emner i en oversiktlig liste
      elif valg == 3:
            J.print_liste_av_registrerte_emner(Emnenavn_liste, Semester_liste, Studiepoeng_liste)
      
      # VALG 4: Vis studieplanen semester for semester
      elif valg == 4:
            E.print_studieplan(Studieplan)

      # VALG 5: Valider om studieplanen er gyldig (180 studiepoeng)
      elif valg == 5:
            studiepoeng_total = E.gyldig_studieplan(Emnenavn_liste, Semester_liste, Studiepoeng_liste, Studieplan)
            if studiepoeng_total == 180:
                  print("Studieplanen er 180 poeng og gyldig")
            else:
                  print(f"Studieplanen er ugyldig, du mangler {180-studiepoeng_total} poeng")
            input("Trykk enter...")

      # VALG 6: Lagre data til filer (emner eller studieplan)
      elif valg == 6:
            skrive_til_fil_input = E.check_int("Trykk 1 for å skrive emner til fil eller trykk 2 for å skrive studieplan til fil.")
            if skrive_til_fil_input == 1:
                  # Lagrer alle emner med deres info til tekstfil
                  J.lagre_emner_til_fil(Emnenavn_liste, Studiepoeng_liste, Semester_liste, filnavn="emner.txt")
                  print("Emnene ble lagret til fil")
                  input("Trykk enter")

            elif skrive_til_fil_input == 2:
                  # Lagrer den organiserte studieplanen til tekstfil
                  J.lagre_studieplan_til_fil(Studieplan, filnavn="studieplan.txt")
                  print("Studieplanen ble lagret til fil.")
                  input("Trykk enter")

      # VALG 7: Les inn ferdig studieplan fra fil
      elif valg == 7:
            Emnenavn_liste,Semester_liste,Studiepoeng_liste, = O.importer_studieplan(Emnenavn_liste, Semester_liste, Studiepoeng_liste)

      # Ugyldig valg - vis feilmelding
      else:
            print("\n Velg et av valgene ")
            input("Trykk enter")            