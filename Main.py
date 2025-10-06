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
            # Slik "fanger" du verdiene som returneres fra funksjonen:
            emnenavn, semester, studiepoeng = E.Nytt_emne()
            
            # Nå har du verdiene i separate variabler:
            print(f"Emnenavn: {emnenavn}")
            print(f"Semester: {semester}")
            print(f"Studiepoeng: {studiepoeng}")
            
            # Du kan også lagre i listen
            Emnekoder.append(emnenavn)
            
            input("Trykk enter...")
      
      elif valg == 2:
            #Legg til et emne i studeplanen
            continue

      elif valg == 3:
            #Skriv ut ei liste over alle registrerte emner
            continue



      else:
            print("\n Velg et av valgene ")
            input("Trykk enter")            