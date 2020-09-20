import random
from os import system


cijferNaarLetter = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J"}
LetterNaarCijfer = {"A":0,"a":0,"1":0,"B":1,"b":1,"2":1,"C":2,"c":2,"3":2,"D":3,"d":3,"4":3,"E":4,"e":4,"5":4,"F":5,"f":5,"6":5,"G":6,"g":6,"7":6,"H":7,"h":7,"8":7,"I":8,"i":8,"9":8,"J":9,"j":9,"10":9,}
speelveld = []
goodFlags = 0
for i in range(10):
  rij = []
  for l in range(10):
    rij.append("x")
  speelveld.append(rij)


def tweeDlijstVoledigIntsMaken(LIST):
  for i in range(0,len(LIST)):
    for k in range(0,len(LIST[i])):
      try:
        print("  " + LIST[i][k])
      except TypeError:
          LIST[i][k] = str(LIST[i][k])
  system("cls")
  return LIST




def creëerSpeelveld(speelveld):
  print("    ",end="")
  for i in range (10):
    print(" " + cijferNaarLetter[i] + "  ",end="")
  print("")
  i = 0
  for rij in speelveld:
    print("   ", end="")
    for l in range(41):
      print("-",end="")
    print("")
    print(i+1,end=" ")
    if i+1 < 10 :
        print(" ",end="")
    for kolom in rij:
      print("| ",end="")
      print(kolom,end=" ")
    print("|")
    i += 1
  print("   ",end="")
  for i in range(41):
    print("-",end="")
  print("")
  

def plaatsBommen():
  bommenVeld = []
  for i in range(10):
    rij = []
    for l in range(10):
      bomOfNiet = random.randint(0,6)
      if bomOfNiet == 1:
        rij.append(True)
      else:
        rij.append(False)
    bommenVeld.append(rij)
  return bommenVeld

def creëerBlauwdrukBommen(bommenVeld):
  blauwdruk = []
  bombs = 0
  for i in range(10):
    rij = []
    for l in range(10):
      rij.append(0)
    blauwdruk.append(rij)
  r = 0
  for rij in bommenVeld:
    k = 0
    for kolom in rij:
      if kolom == False:
        for nr in range(r-1,r+2):
          if nr in range(0,10):
            for nk in range(k-1,k+2):
              if nk in range(0,10):
                if bommenVeld[nr][nk]==True:
                  blauwdruk[r][k] +=1
      else:
        blauwdruk[r][k]="b"
        bombs += 1
      if blauwdruk[r][k] == 0:
        blauwdruk[r][k] = " "
      k +=1
    r += 1
  blauwdruk = tweeDlijstVoledigIntsMaken(blauwdruk)      
  return blauwdruk,bombs



def decodeInput():
  zet = input("geef een coördinnaat en de actie op in de vorm letter,cijfer,actie. Als actie kun je het vakje toen door <T> te typen, om een flag te plaatsen typ <F>        ")
  zet = zet.split(",")
  zet[0] = LetterNaarCijfer[zet[0]]
  zet[1] = LetterNaarCijfer[zet[1]]
  return zet


def speelZet(zet,speelveld,blauwdruk,bombs,goodFlags):   
  einde = False
  ToRevael = []
  newList =[]
  AlreadyChecked = []
  if zet[len(zet)-1] == "F" or zet[len(zet)-1] == "f":
    speelveld[zet[1]][zet[0]] = "F"
    if blauwdruk[zet[1]][zet[0]] == "b":
      goodFlags += 1
  elif zet[len(zet)-1] == "T" or zet[len(zet)-1] == "t":
    newList.append(zet[1])
    newList.append(zet[0])
    ToRevael.append(newList)
    while len(ToRevael) > 0 and einde == False:
      print(AlreadyChecked)
      coördinaat = ToRevael.pop(0)
      CoördinaatgetalA = coördinaat[0]
      CoördinaatgetalB = coördinaat[1]
      inhoud = blauwdruk[CoördinaatgetalA][CoördinaatgetalB]
      speelveld[CoördinaatgetalA][CoördinaatgetalB] = inhoud
      if inhoud == "b":
        print("je bent op een mijn gestapt")
        einde = True
      elif not coördinaat in AlreadyChecked and einde == False:
        AlreadyChecked.append(coördinaat)
        if inhoud == " " :
          for r in range(CoördinaatgetalA-1,CoördinaatgetalA+2):
            if r in range(0,10):
              for k in range(CoördinaatgetalB-1,CoördinaatgetalA+2):
                if k in range(0,10):
                  ToRevael.append([r,k])
  if goodFlags == bombs:
    print("Je hebt alle bommen gevonden, proficiat!")
    einde = True
  return speelveld,goodFlags,einde

      
stop = False



bommenVeld = plaatsBommen()
blauwdruk,bombs = creëerBlauwdrukBommen(bommenVeld)
while stop == False:
  creëerSpeelveld(speelveld)
  zet = decodeInput()
  system("cls")
  speelveld,goodFlags,einde = speelZet(zet,speelveld,blauwdruk,bombs,goodFlags)
  print(zet)
  if einde == True:
    stop = True
    creëerSpeelveld(speelveld)
input("done")