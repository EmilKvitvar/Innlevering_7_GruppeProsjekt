import FunksjonerE as E
import FunksjonO as O

Emnenavn_liste = []
Semester_liste = []
Studiepoeng_liste = []
Studieplan = [[] for i in range (6)]

#Fag for å teste:



while True:
      Valg = 0
      #MENY:
      E.meny()
      valg = E.check_int("Valg: ")
      
      if valg == None:
            break

      elif valg == 1: #Lag et nytt emne 
            emnenavn, semester, studiepoeng, Fjerne = E.Nytt_emne(Emnenavn_liste)

            if Fjerne == 1:
                  
                  if emnenavn in Emnenavn_liste:
                        indeks = Emnenavn_liste.index(emnenavn)
                        
                        fjernet_emne = Emnenavn_liste.pop(indeks)
                        fjernet_semester = Semester_liste.pop(indeks)
                        fjernet_studiepoeng = Studiepoeng_liste.pop(indeks)
                        
                        print(f"Fjernet: {fjernet_emne} - {fjernet_semester} - {fjernet_studiepoeng} studiepoeng")
                  else:
                        print(f"Feil: {emnenavn} finnes ikke i listen!")
            else:
                  Emnenavn_liste.append(emnenavn)
                  Semester_liste.append(semester)
                  Studiepoeng_liste.append(studiepoeng)
                  print(f"La til: {emnenavn} - {semester} - {studiepoeng} studiepoeng")
                  
            input("Trykk enter...")
      
      elif valg == 2:
            E.legg_til_emne_i_studieplanen(Emnenavn_liste, Semester_liste,Studiepoeng_liste, Studieplan)
            continue

      elif valg == 3:
            #Skriv ut ei liste over alle registrerte emner
            continue



      else:
            print("\n Velg et av valgene ")
            input("Trykk enter")            