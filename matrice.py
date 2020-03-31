# -*- coding: utf-8 -*-
"""
    Projet Labyrinthe
    Projet Python 2020 - Licence Informatique UNC (S3 TREC7)

   Module matrice
   ~~~~~~~~~~~~~~~
   
   Ce module gère une matrice. 
"""

#-----------------------------------------
# contructeur et accesseurs
#-----------------------------------------

def Matrice(nbLignes,nbColonnes,valeurParDefaut=0):
    """
    crée une matrice de nbLignes lignes sur nbColonnes colonnes en mettant 
    valeurParDefaut dans chacune des cases
    paramètres: 
      nbLignes un entier strictement positif qui indique le nombre de lignes
      nbColonnes un entier strictement positif qui indique le nombre de colonnes
      valeurParDefaut la valeur par défaut
    résultat la matrice ayant les bonnes propriétés
    """
    M=[[valeurParDefaut for i in range(nbColonnes)] for j in range(nbLignes)]
    return M

def getNbLignes(matrice):
    """
    retourne le nombre de lignes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice)

def getNbColonnes(matrice):
    """
    retourne le nombre de colonnes de la matrice
    paramètre: matrice la matrice considérée
    """
    return len(matrice[0])

def getVal(matrice,ligne,colonne):
    """
    retourne la valeur qui se trouve en (ligne,colonne) dans la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
    """
    return matrice[ligne][colonne]

def setVal(matrice,ligne,colonne,valeur):
    """
    met la valeur dans la case se trouve en (ligne,colonne) de la matrice
    paramètres: matrice la matrice considérée
                ligne le numéro de la ligne (en commençant par 0)
                colonne le numéro de la colonne (en commençant par 0)
                valeur la valeur à stocker dans la matrice
    cette fonction ne retourne rien mais modifie la matrice
    """
    matrice[ligne][colonne]=valeur


#------------------------------------------        
# decalages
#------------------------------------------
def decalageLigneAGauche(matrice, numLig, nouvelleValeur=0):
    """
    permet de décaler une ligne vers la gauche en insérant une nouvelle
    valeur pour remplacer la premiere case à droite de cette ligne
    le fonction retourne la valeur qui a été éjectée
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat la valeur qui a été ejectée lors du décalage
    """
    valEjectée=0
    valEjectée=matrice[numLig-1][0]
    matrice[numLig-1].pop(0)
    matrice[numLig-1].append(nouvelleValeur)
    
    return valEjectée

def decalageLigneADroite(matrice, numLig, nouvelleValeur=0):
    """
    decale la ligne numLig d'une case vers la droite en insérant une nouvelle
    valeur pour remplacer la premiere case à gauche de cette ligne
    paramèteres: matrice la matrice considérée
                 numLig le numéro de la ligne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valEjectée=0
    valEjectée=matrice[numLig-1][-1]
    matrice[numLig-1].pop(-1)
    matrice[numLig-1].insert(0,nouvelleValeur)

    return valEjectée

def decalageColonneEnHaut(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le haut en insérant une nouvelle
    valeur pour remplacer la premiere case en bas de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valEjectée=0
    valEjectée=matrice[0][numCol-1]
    for i in range(len(matrice)-1):
      matrice[i][numCol-1]=matrice[i+1][numCol-1]
    
    matrice[-1].pop(numCol-1)
    matrice[-1].insert(numCol-1,nouvelleValeur)

    return valEjectée
    

def decalageColonneEnBas(matrice, numCol, nouvelleValeur=0):
    """
    decale la colonne numCol d'une case vers le bas en insérant une nouvelle
    valeur pour remplacer la premiere case en haut de cette ligne
    paramèteres: matrice la matrice considérée
                 numCol le numéro de la colonne à décaler
                 nouvelleValeur la valeur à placer
    résultat: la valeur de la case "ejectée" par le décalage
    """
    valEjectée=0
    valEjectée=matrice[-1][numCol-1]
    
    for i in reversed(range(len(matrice))):
      matrice[i][numCol-1]=matrice[i-1][numCol-1]
    
    matrice[0].pop(numCol-1)
    matrice[0].insert(numCol-1,nouvelleValeur)

    return valEjectée
if __name__=="__main__":

  m=Matrice(7,7,0)
  print(setVal(m,4,3,1))
  print(m)
  print(getNbLignes(m))
  print(getNbColonnes(m))
  print(getVal(m,1,3))
  print(setVal(m,1,3,5))
  print(setVal(m,2,4,11))
  print(m)
  print(decalageLigneAGauche(m,1,6))
  print(m)
  print(decalageLigneADroite(m,2,15))
  print(m)
  print(setVal(m,2,4,11))
  print(setVal(m,5,4,8))
  print(setVal(m,4,4,2))
  print(setVal(m,3,4,3))
  print(m)
  print(decalageColonneEnHaut(m,4,10))
  print(m)
  print(decalageColonneEnBas(m,4,14))
  print(m)
  print(decalageColonneEnHaut(m,4,9))
  print(m)
  print(decalageColonneEnHaut(m,3,2))
  print(m)
