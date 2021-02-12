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
            print("\n")
            self.liste_joueurs.append(Player(lastname,firstname,date,s,ranking))

    def afficher_joueurs(self):
        if len(self.liste_joueurs) == 0:
            return
        else:
            for i in self.liste_joueurs:
                print('Nom : {0[nom_famille]} ; Prénom : {0[prenom]} ; Date de naissance : {0[date_naissance]} ; Sexe : {0[sexe]} ; Classement : {0[classement]}'.format(i.serialize()))

    def tour()

x = Tournoi(2,"Tournoi du Mans","Mans","13/09/2016",4)