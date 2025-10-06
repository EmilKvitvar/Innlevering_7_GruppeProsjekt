import FunksjonerE as E
import FunksjonO as O

Emnekoder = []



while True:
      Valg = 0
      #MENY:
      E.meny()
      valg = E.check_int("Valg: ")
      
      if valg == None:
            break

      elif valg == 1: #Lag et nytt emne 
            resultat = E.Nytt_emne()  # Kaller funksjonen og lagrer resultatet
            
            if resultat == None:  # Brukeren avbrøt
                print("Avbrutt!")
            else:
                # "Henter" verdiene fra funksjonen
                emnenavn, semester, studiepoeng = resultat
                
                print(f"\nNytt emne opprettet:")
                print(f"Emnekode: {emnenavn}")
                print(f"Semester: {semester}")
                print(f"Studiepoeng: {studiepoeng}")
                
                # Legger emnet til i listen
                Emnekoder.append({"navn": emnenavn, "semester": semester, "studiepoeng": studiepoeng})
                
            input("Trykk enter for å fortsette...")
      
      elif valg == 2:
            #Legg til et emne i studeplanen
            continue

      elif valg == 3:
            #Skriv ut ei liste over alle registrerte emner
            continue



      else:
            print("\n Velg et av valgene ")
            input("Trykk enter")            