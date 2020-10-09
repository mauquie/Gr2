import random
import pokerlib

class Joueur:
  """Classe qui permet d'instancier les joueurs, avec les attributs  nom, main (ses cartes), tapis (ses jetons); ainsi que les combinaisons"""

  def __init__(self,nom="Ez",tapis=1000):
    self.nom=nom #Nom du joueur
    self.main = [] #Cartes du joueur
    self.tapis = tapis #Jetons de chaque joueur = attribut
    self.combinaison = None #Si le joueur possède une combinaison

  def evaluer(self):#prendre la meileure combinaison
    if combinaison1 > combinaison2: 
      print('main1 est plus forte que main2') 
    elif combinaison1 == combinaison2 : 
      print('main1 et main2 ont la même valeur') 
    else: 
      print('main2 est plus forte que main1')

    
  def nouvelle_donne(self):#modifier l'attribut main
    self.main.clear()

  def recevoir_cartes(self, zeubi):#Ajoutez des cartes à main
    self.main.append(zeubi)

  def __repr__(self): #Affiche le nom
    return f"{self.nom}"

class Carte:

  def __init__(self, couleur, rang): #Initialise les éléments de couleur et rang
    self.couleur = couleur
    self.rang = rang

  def __repr__(self): #retourne le jeu de cartes sous la forme "rang de couleur" 
    return f"{self.rang} de {self.couleur}"
    
class Partie:
  """Instancie la liste des joueurs, def jouer qui permet d'ajouter des joueurs"""
  joueurs = []

  def __init__(self):
    pass

  def jouer(self, nom='antoine'): #Ajoute des joueurs à la liste
    joueur = Joueur(nom) 
    Partie.joueurs.append(joueur)   

class Coup:
  """Paramètre de la partie, avec le croupier, et pour déterminer un gagnant"""

  def __init__(self,Croupier,joueur):
    self.croupier=Croupier
    self.gagnant=joueur
    self.joueur=[]

  def abattre(self):#compare les mains des joueurs et détermine le joueur gagnant 
    pass
    

class Croupier:
  """Permet d'attribuer tous les rôles du Croupier, c'est-à-dire les fonctions rassembler, couper, mélanger, distribuer, avec le paquet de cartes complet au début de la partie, avec la liste des cartes justement"""

  def __init__(self):
    self.paquet=[]
    self.couleur = ["P","C","K","T"]
    self.rang = ["2","3","4","5","6","7","8","9","X","Q","D","R","A"]

  def rassembler(self):
    """Rassembler un paquet de 52 cartes avec 2 for dans les deux listes couleur et rang"""
    for i in range(len(self.couleur)):
      for j in range(len(self.rang)):
        carte=Carte(self.couleur[i], self.rang[j])
        self.paquet.append(carte)

  def melanger(self):
    random.shuffle(self.paquet)

  def couper(self):
    paquet_coupe=0
    random.randint(1,paquet_coupe)
    for i in range(1,paquet_coupe):
      paquet_coupe.append(self.paquet[i])
      
  def distribuer(self):
    for i in range(len(self.joueurs)):
      for j in range (5):
        Partie.joueurs[i].recevoir_cartes(self.paquet[0])
        self.paquet.pop(0)

  def nouvelle_donne(self):
    self.rassembler
    self.melanger()
    self.couper

"""
couleur = ["P","C","K","T"]
rang = ["2","3","4","5","6","7","8","9","X","Q","D","R","A"]

for i in range(couleur):
  for j in range(rang):
    "C"+str(t)=carte(i,j)
joueur1 = joueur('Emie')
joueur1.main = [C1,C2,C3,C4,C5] """


p=Partie()
p.jouer("YOANN")

cr=Croupier()
cr.nouvelle_donne()
cr.distribuer()

c=Coup()
c.__init__()

j=joueur()
j.recevoir_cartes()
j.evauler()



main1 = [Carte(), Carte(), Carte(), Carte(), Carte()] 
main2 = [Carte(), Carte(), Carte(), Carte(), Carte()] 
combinaison1 = pokerlib.Combinaison(main1) 
combinaison2 = pokerlib.Combinaison(main2) 
print(combinaison1.name(), combinaison2.name())
