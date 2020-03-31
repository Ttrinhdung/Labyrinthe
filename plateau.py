# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module plateau
   ~~~~~~~~~~~~~~
   
   Ce module gère le plateau de jeu. 
"""

from matrice import *
from carte import *
from random import *

def Plateau(nbJoueurs, nbTresors):
    """
    créer un nouveau plateau contenant nbJoueurs et nbTrésors
    paramètres: nbJoueurs le nombre de joueurs (un nombre entre 1 et 4)
                nbTresors le nombre de trésor à placer (un nombre entre 1 et 49)
    resultat: un couple contenant
              - une matrice de taille 7x7 représentant un plateau de labyrinthe où les cartes
                ont été placée de manière aléatoire
              - la carte amovible qui n'a pas été placée sur le plateau
    """

    p=dict()
    p["nbJoueurs"]=nbJoueurs
    p["nbTresors"]=nbTresors
    listeCartesAmovibles=creerCartesAmovibles(12,nbTresors)
    p["plateau"]=nouveauPlateau=Matrice(7,7,0)
    setVal(nouveauPlateau,0,0,Carte(True,False,False,True,0))
    setVal(nouveauPlateau,0,2,Carte(True,False,False,False,1))
    setVal(nouveauPlateau,0,4,Carte(True,False,False,False,2))
    setVal(nouveauPlateau,0,6,Carte(True,False,False,False,0,[1,2,3,4]))
    setVal(nouveauPlateau,2,0,Carte(False,False,False,True,3))
    setVal(nouveauPlateau,2,2,Carte(False,False,False,True,4))
    setVal(nouveauPlateau,2,4,Carte(True,False,False,False,5))
    setVal(nouveauPlateau,2,6,Carte(False,True,False,False,6))
    setVal(nouveauPlateau,4,0,Carte(False,False,False,True,7))
    setVal(nouveauPlateau,4,2,Carte(False,False,True,False,8))
    setVal(nouveauPlateau,4,4,Carte(False,True,False,False,9))
    setVal(nouveauPlateau,4,6,Carte(False,True,False,False,10))
    setVal(nouveauPlateau,6,0,Carte(False,False,True,True,0))
    setVal(nouveauPlateau,6,2,Carte(False,False,True,False,11))
    setVal(nouveauPlateau,6,4,Carte(False,False,True,False,12))
    setVal(nouveauPlateau,6,6,Carte(False,True,True,False,0))
    
    cpt=0
    for i in range(7):
      for j in range(7):
        if nouveauPlateau[i][j]==0:
          nouveauPlateau[i][j]=listeCartesAmovibles[cpt]
          cpt+=1
    
    p["carteAmovible"]=listeCartesAmovibles[-1]

    return p

def creerCartesAmovibles(tresorDebut,nbTresors):
    """
    fonction utilitaire qui permet de créer les cartes amovibles du jeu en y positionnant
    aléatoirement nbTresor trésors
    la fonction retourne la liste, mélangée aléatoirement, des cartes ainsi créées
    paramètres: tresorDebut: le numéro du premier trésor à créer
                nbTresors: le nombre total de trésor à créer
    résultat: la liste mélangée aléatoirement des cartes amovibles créees
    """
    listeCartesAmovibles=[]
    jonction=[1,2,4,8]
    angle=[3,6,9,12]
    toutDroit=[10,5]
    i=0
    while i<6:
      i+=1
      code=choice(jonction)
      c=Carte(True,False,True,False)
      decoderMurs(c,code)
      listeCartesAmovibles.append(c)
    j=0
    while j<16:
      j+=1
      code=choice(angle)
      c=Carte(True,False,True,False)
      decoderMurs(c,code)
      listeCartesAmovibles.append(c)
    k=0
    while k<12:
      k+=1
      code=choice(toutDroit)
      c=Carte(True,False,True,False)
      decoderMurs(c,code)
      listeCartesAmovibles.append(c)
    for i in range(nbTresors-tresorDebut+1):
      mettreTresor(listeCartesAmovibles[i],i+tresorDebut)
    shuffle(listeCartesAmovibles)
    return listeCartesAmovibles



def prendreTresorPlateau(plateau,lig,col,numTresor):
    """
    prend le tresor numTresor qui se trouve sur la carte en lin,col du plateau
    retourne True si l'opération s'est bien passée (le trésor était vraiment sur
    la carte
    paramètres: plateau: le plateau considéré
                lig: la ligne où se trouve la carte
                col: la colonne où se trouve la carte
                numTresor: le numéro du trésor à prendre sur la carte
    resultat: un booléen indiquant si le trésor était bien sur la carte considérée
    """
    c=getVal(p["plateau"],lig,col)
    if numTresor==prendreTresor(c):
      return True
    else:
      return False

def getCoordonneesTresor(plateau,numTresor):
    """
    retourne les coordonnées sous la forme (lig,col) du trésor passé en paramètre
    paramètres: plateau: le plateau considéré
                numTresor: le numéro du trésor à trouver
    resultat: un couple d'entier donnant les coordonnées du trésor ou None si
              le trésor n'est pas sur le plateau
    """
    for i in range(7):
      for j in range(7):
        if getTresor(p["plateau"][i][j])==numTresor:
          return (i,j)


def getCoordonneesJoueur(plateau,numJoueur):
    """
    retourne les coordonnées sous la forme (lig,col) du joueur passé en paramètre
    paramètres: plateau: le plateau considéré
                numJoueur: le numéro du joueur à trouver
    resultat: un couple d'entier donnant les coordonnées du joueur ou None si
              le joueur n'est pas sur le plateau
    """
    for i in range(7):
      for j in range(7):
        if numJoueur in getListePions(p["plateau"][i][j]):
          return (i,j)

def prendrePionPlateau(plateau,lin,col,numJoueur):
    """
    prend le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    prendrePion(p["plateau"][lin][col],numJoueur)

def poserPionPlateau(plateau,lin,col,numJoueur):
    """
    met le pion du joueur sur la carte qui se trouve en (lig,col) du plateau
    paramètres: plateau:le plateau considéré
                lin: numéro de la ligne où se trouve le pion
                col: numéro de la colonne où se trouve le pion
                numJoueur: le numéro du joueur qui correspond au pion
    Cette fonction ne retourne rien mais elle modifie le plateau
    """
    c=getVal(p["plateau"],lin,col)
    poserPion(c,numJoueur)
    
    


def accessible(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du labyrinthe
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: un boolean indiquant s'il existe un chemin entre la case de départ
              et la case d'arrivée
    """
    pass

def accessibleDist(plateau,ligD,colD,ligA,colA):
    """
    indique si il y a un chemin entre la case ligD,colD et la case ligA,colA du plateau
    mais la valeur de retour est None s'il n'y a pas de chemin, 
    sinon c'est un chemin possible entre ces deux cases sous la forme d'une liste
    de coordonées (couple de (lig,col))
    paramètres: plateau: le plateau considéré
                ligD: la ligne de la case de départ
                colD: la colonne de la case de départ
                ligA: la ligne de la case d'arrivée
                colA: la colonne de la case d'arrivée
    résultat: une liste de coordonées indiquant un chemin possible entre la case
              de départ et la case d'arrivée
    """
    pass
if __name__=="__main__":
  p=Plateau(2,34)
  print(p)
  print(prendreTresorPlateau(p,1,2,1))
  print(getCoordonneesTresor(p,30))
  print(p["plateau"])
  print(getCoordonneesJoueur(p,2))
  print(prendrePionPlateau(p,0,6,3))
  print(p["plateau"])
  print(getCoordonneesJoueur(p,2))
  print(poserPionPlateau(p,6,6,3))
  print(p["plateau"])



