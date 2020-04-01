# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module listeJoueurs
   ~~~~~~~~~~~~~~~~~~~
   
   Ce module gère la liste des joueurs. 
"""
import random
from joueur import *

def ListeJoueurs(nomsJoueurs):
    """
    créer une liste de joueurs dont les noms sont dans la liste de noms passés en paramètre
    Attention il s'agit d'une liste de joueurs qui gère la notion de joueur courant
    paramètre: nomsJoueurs une liste de chaines de caractères
    résultat: la liste des joueurs avec un joueur courant mis à 0
    """
    ListeJoueurCourant=0
    listeJoueur=[]
    for i in nomsJoueurs:
      listeJoueur.append(Joueur(i))
    return(listeJoueur, ListeJoueurCourant)
    
    
def ajouterJoueur(joueurs, joueur):
    """
    ajoute un nouveau joueur à la fin de la liste
    paramètres: joueurs un liste de joueurs
                joueur le joueur à ajouter
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    for i in joueur:
      joueurs[0].append(Joueur(i))

def initAleatoireJoueurCourant(joueurs):
    """
    tire au sort le joueur courant
    paramètre: joueurs un liste de joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    return random.choice(joueurs[0])
    
def distribuerTresors(joueurs,nbTresors=24, nbTresorMax=0):
    """
    distribue de manière aléatoire des trésors entre les joueurs.
    paramètres: joueurs la liste des joueurs
                nbTresors le nombre total de trésors à distribuer (on rappelle 
                        que les trésors sont des entiers de 1 à nbTresors)
                nbTresorsMax un entier fixant le nombre maximum de trésor 
                            qu'un joueur aura après la distribution
                            si ce paramètre vaut 0 on distribue le maximum
                            de trésor possible  
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    i=0
    j=0
    if nbTresorMax==0:
      nbTresorMax=24
    while i<nbTresorMax :
      if j==len(joueurs[0]):
        j=0
      x=random.randint(0,24)
      ajouterTresor(joueurs[0][j],x)
      i=i+1
      j=j+1
    return joueurs 

def changerJoueurCourant(joueurs):
    """
    passe au joueur suivant (change le joueur courant donc)
    paramètres: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    return joueurs[1]+1

def getNbJoueurs(joueurs):
   """
  retourne le nombre de joueurs participant à la partie
  paramètre: joueurs la liste des joueurs
  résultat: le nombre de joueurs de la partie
   """
   return len(joueurs[0])

def getJoueurCourant(joueurs):
    """
    retourne le joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le joueur courant
    """
    return joueurs[-1] 

def joueurCourantTrouveTresor(joueurs):
    """
    Met à jour le joueur courant lorsqu'il a trouvé un trésor
    c-à-d enlève le trésor de sa liste de trésors à trouver
    paramètre: joueurs la liste des joueurs
    cette fonction ne retourne rien mais modifie la liste des joueurs
    """
    x=joueurs[1]
    tresorTrouve(joueurs[0][x])
    return joueurs[0][x]

def nbTresorsRestantsJoueur(joueurs,numJoueur):
    """
    retourne le nombre de trésors restant pour le joueur dont le numéro 
    est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur
    résultat: le nombre de trésors que joueur numJoueur doit encore trouver
    """
    return getNbTresorsRestants(joueurs[0][numJoueur])

def numJoueurCourant(joueurs):
    """
    retourne le numéro du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le numéro du joueur courant
    """
    return getJoueurCourant(joueurs)
    
    

def nomJoueurCourant(joueurs):
    """
    retourne le nom du joueur courant
    paramètre: joueurs la liste des joueurs
    résultat: le nom du joueur courant
    """
    x=joueurs[1]
    return getNom(joueurs[x])
    

def nomJoueur(joueurs,numJoueur):
    """
    retourne le nom du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le nom du joueur numJoueur
    """
    return getNom(joueurs[0][numJoueur])

def prochainTresorJoueur(joueurs,numJoueur):
    """
    retourne le trésor courant du joueur dont le numero est donné en paramètre
    paramètres: joueurs la liste des joueurs
                numJoueur le numéro du joueur    
    résultat: le prochain trésor du joueur numJoueur (un entier)
    """
    return prochainTresor(joueurs[0][numJoueur])

def tresorCourant(joueurs):
    """
    retourne le trésor courant du joueur courant
    paramètre: joueurs la liste des joueurs 
    résultat: le prochain trésor du joueur courant (un entier)
    """ 
    return prochainTresor(joueurs[1])

def joueurCourantAFini(joueurs):
    """
    indique si le joueur courant a gagné
    paramètre: joueurs la liste des joueurs 
    résultat: un booleen indiquant si le joueur courant a fini
    """
    jcourant=joueurs[0][1]
    fini=False
    if (len(jcourant))==None:
      fini=True
    else:
      fini=False 
    return fini 


if __name__=="__main__":
    toto=ListeJoueurs(["titi","tete","marc","lisa"])
    print(toto)
    ajouterJoueur(toto, ['tim'])
    print(toto)
    print(initAleatoireJoueurCourant(toto))
    print(distribuerTresors(toto,nbTresors=24,nbTresorMax=10))
    print(toto)
    print(joueurCourantTrouveTresor(toto))
    print(joueurCourantTrouveTresor(toto))
    print(getNbJoueurs(toto))
    print(changerJoueurCourant(toto))
    print(getJoueurCourant(toto))
    print(nomJoueurCourant(toto))
    print(nbTresorsRestantsJoueur(toto,2))
    print(nomJoueur(toto,1))
    print(prochainTresorJoueur(toto,2))
    print(numJoueurCourant(toto))
    print(joueurCourantAFini(toto))