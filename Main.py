import FunksjonerE as E
import FunksjonO as O

Emnenavn = []
Semester= []
Studiepoeng = []


while True:
      Valg = 0
      #MENY:
      E.meny()
      valg = E.check_int("Valg: ")
      
      if valg == None:
            break

      elif valg == 1: #Lag et nytt emne 
            emnenavn, semester, studiepoeng = E.Nytt_emne()
            
            Emnenavn.append(emnenavn)
            Semester.append(semester)
            Studiepoeng.append(studiepoeng)
            
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