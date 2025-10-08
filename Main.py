import FunksjonerE as E
import FunksjonO as O
import joakim2 as J

Emnenavn_liste = []
Semester_liste = []
Studiepoeng_liste = []
Studieplan = [[] for i in range (6)]




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


      elif valg == 3:
            J.print_liste_av_registrerte_emner(Emnenavn_liste, Semester_liste, Studiepoeng_liste)
      
      elif valg == 4:
            E.print_studieplan(Studieplan)

      elif valg == 5:
            studiepoeng_total = E.gyldig_studieplan(Emnenavn_liste, Semester_liste, Studiepoeng_liste, Studieplan)
            if studiepoeng_total == 180:
                  print("Studieplanen er 180 poeng og gyldig")
            else:
                  print(f"Studieplanen er ugyldig, du mangler {180-studiepoeng_total} poeng")
            input("Trykk enter...")

      elif valg == 7:
            Emnenavn_liste,Semester_liste,Studiepoeng_liste, = O.importer_studieplan(Emnenavn_liste, Semester_liste, Studiepoeng_liste)

      else:
            print("\n Velg et av valgene ")
            input("Trykk enter")            