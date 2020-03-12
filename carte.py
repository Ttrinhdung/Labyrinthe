# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random
#Trinh dung


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
    """
    permet de créer une carte:
    paramètres:
    nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
    tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
    pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
    """
    d=dict()
    d["nord"]=nord
    d["est"]=est
    d["sud"]=sud
    d["ouest"]=ouest
    d["tresor"]=tresor
    d["pions"]=pions

    return d

def estValide(c):
    """
    retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
    paramètre: c une carte
    """
    cptmur=0
    if c["nord"]==True:
      cptmur+=1
    if c["est"]==True:
      cptmur+=1
    if c["sud"]==True:
      cptmur+=1
    if c["ouest"]==True:
      cptmur+=1

    if cptmur<=2:
      return True
    else: 
      return False  

def murNord(c):
    """
    retourne un booléen indiquant si la carte possède un mur au nord
    paramètre: c une carte
    """
    return c["nord"]


def murSud(c):
    """
    retourne un booléen indiquant si la carte possède un mur au sud
    paramètre: c une carte
    """
    return c["sud"]


def murEst(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'est
    paramètre: c une carte
    """
    return c["est"]

def murOuest(c):
    """
    retourne un booléen indiquant si la carte possède un mur à l'ouest
    paramètre: c une carte
    """
    return c["ouest"]


def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    return c["pions"]

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c["pions"]=listePions


def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    return len(c["pions"])

def possedePion(c,pion):
    """
    retourne un booléen indiquant si la carte possède le pion passé en paramètre
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    """
    if pion in c["pions"]:
      return True
    else:
      return False



def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    return c["tresor"]

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    a=0
    a=c["tresor"]
    c["tresor"]=0
    return a

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    a=0
    a=c["tresor"]
    c["tresor"]=tresor
    return a

def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    for i in range(len(c["pions"])):
      if c["pions"][i-1]==pion:
        del c["pions"][i-1]

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    if pion not in c["pions"]:
      c["pions"].append(pion)

def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    N=c["nord"]
    E=c["est"]
    S=c["sud"]
    O=c["ouest"]

    c["nord"]=O
    c["est"]=N
    c["sud"]=E
    c["ouest"]=S

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    N=c["nord"]
    E=c["est"]
    S=c["sud"]
    O=c["ouest"]

    c["nord"]=E
    c["est"]=S
    c["sud"]=O
    c["ouest"]=N
    
def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    from random import randrange
    nombreAleatoire = randrange(1,10)
    print(nombreAleatoire)

    for i in range(nombreAleatoire):
      tournerHoraire(c) 

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    code=0
    if c["nord"]==True:
      code+=1
    if c["est"]==True:
      code+=2
    if c["sud"]==True:
      code+=4
    if c["ouest"]==True:
      code+=8
    return code

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
    bin(code)
    return code
def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    
    listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']
    return listeCartes[coderMurs(c)]

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1["nord"]==False and carte2["sud"]==False:
      return True
    else:
      return False
    pass

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1["sud"]==False and carte2["nord"]==False:
      return True
    else:
      return False

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    if carte1["ouest"]==False and carte2["est"]==False:
      return True
    else:
      return False

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    if carte1["est"]==False and carte2["ouest"]==False:
      return True
    else:
      return False

if __name__=="__main__":

  c=Carte(True,False,False,True,4,[1,2,4])
  c2=Carte(True,True,False,False,3,[])
  print(c)
  print(estValide(c))
  print(murNord(c))
  print(murEst(c))
  print(murSud(c))
  print(murOuest(c))
  print(getListePions(c))
  print(setListePions(c,[2,3]))
  print(c["pions"])
  print(c)
  print(getNbPions(c))
  print(possedePion(c,3))
  print(getTresor(c))
  print(prendreTresor(c))
  print(c["tresor"])
  print(mettreTresor(c,2))
  print(c["tresor"])
  print(c)
  print(prendrePion(c,2))
  print(c)
  tournerHoraire(c)
  print(c)
  tournerAntiHoraire(c)
  print(c)
  print(poserPion(c,2))
  print(c)
  print(poserPion(c,1))
  print(c)
  print(prendrePion(c,1))
  print(passageNord(c,c2))
  print(passageSud(c,c2))
  print(passageOuest(c,c2))
  print(passageEst(c,c2))
  print(decoderMurs(c,6))
  print(coderMurs(c))
  print(c)
  print(toChar(c))

  print(decoderMurs(c,4))


