from player import Player
from random import *

class Tournoi:
    def __init__(self,nombre_joueurs,nom,lieu,date:str,nb_tours=4):
        self.nb_joueurs = nombre_joueurs
        self.liste_joueurs = []
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nb_tours = nb_tours

    def serialize(self):
        return self.__dict__

    def ajouter_joueurs(self):
        for i in range(self.nb_joueurs):
            lastname = input("Nom de famille : ")
            firstname = input("Prénom : ")
            date = input("Date de naissance : ")
            s = input("Sexe : ")
            ranking = int(input("Classement du joueur : "))
            joueur = Player(lastname,firstname,date,s,ranking)
            self.liste_joueurs.append(joueur.serialize())

    def afficher_joueurs(self):
        if len(self.liste_joueurs) == 0:
            return
        else:
            for i in self.liste_joueurs:
                print('Nom : {0[nom_famille]} ; Prénom : {0[prenom]} ; Date de naissance : {0[date_naissance]} ; Sexe : {0[sexe]} ; Classement : {0[classement]}'.format(i))

    def premier_tour(self):
        l = len(self.liste_joueurs)
        sorted_by_rank = sorted(self.liste_joueurs,key=lambda player: player['classement'])
        mid = int(l//2)
        if l%2 == 0:
            sup = sorted_by_rank[:mid]
            inf = sorted_by_rank[mid:]
        else:
            sup = sorted_by_rank[:mid + 1]
            inf = sorted_by_rank[mid + 1:]
        print(sup,inf)