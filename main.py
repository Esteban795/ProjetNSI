from tournoi import Tournoi
from player import Player
from tinydb import TinyDB
from match import Match

db = TinyDB("db.json")

"""joueurs = int(input("Nombre de joueurs dans ce tournoi : "))
nom_tournoi = input("Nom du tournoi : ")
lieu_tournoi = input("Lieu du tournoi : ")
date_tournoi = input("Date du tournoi : ")
tours = int("".join([str(int(joueurs/2)) if joueurs%2 == 0 else str(int(joueurs/2) + 1)]))
tournoi = Tournoi(joueurs,nom_tournoi,lieu_tournoi,date_tournoi,tours)"""

tournoi = Tournoi(3,"Tournoi du Mans","Mans","11/08/2003",2)
print(tournoi.serialize())
tournoi.ajouter_joueurs()
tournoi.afficher_joueurs()
tournoi.premier_tour()