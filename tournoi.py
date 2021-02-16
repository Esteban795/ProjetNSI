from player import Player
from match import Match,Round

class Tournoi:
    def __init__(self,nombre_joueurs:int,nom:str,lieu:str,date:str,nb_tours=4):
        self.nb_joueurs = nombre_joueurs
        self.liste_joueurs = []
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nb_tours = nb_tours
        self.liste_rounds = []
        self.liste_perdants = []
    
    def serialize(self):
        return self.__dict__

    def ajouter_joueurs(self):
        for _ in range(self.nb_joueurs):
            lastname = input("Nom de famille : ")
            firstname = input("Prénom : ")
            date = input("Date de naissance : ")
            gender = input("Sexe : ")
            ranking = int(input("Classement du joueur : "))
            print("\n")
            joueur = Player(lastname,firstname,date,gender,ranking)
            self.liste_joueurs.append(joueur)

    def afficher_joueurs(self):
        if len(self.liste_joueurs) == 0:
            return "Aucun joueur n'a encore été ajouté."
        else:
            for i in self.liste_joueurs:
                print('Nom : {0[nom_famille]} ; Prénom : {0[prenom]} ; Date de naissance : {0[date_naissance]} ; Sexe : {0[sexe]} ; Classement : {0[classement]}'.format(i.serialize()))

    def premier_tour(self):
        l = len(self.liste_joueurs)
        sorted_by_rank = sorted(self.liste_joueurs,key=lambda player: player.classement)
        mid = int(l//2)
        sup = sorted_by_rank[:mid]
        inf = sorted_by_rank[mid:]
        liste_matchs = []
        for i in range(mid):
            match = Match(sup[i],inf[i])
            match.resultat(int(input("Indiquez 1 si le joueur 1 a gagné le match, sinon 2. En cas d'égalité, 1/2 : ")))
            liste_matchs.append(match)
        tour = Round(liste_matchs)
        self.liste_rounds.append(tour)
        matchs_done = tour.afficher_liste_matchs()
        for i in matchs_done:
            joueur_perdant = "".join(["joueur",str(i.serialize()['perdant'])])
            self.liste_perdants.append(i.serialize()[joueur_perdant])
            self.liste_joueurs.remove(i.serialize()[joueur_perdant])
        self.afficher_joueurs()
        self.afficher_perdants()
    
    def afficher_perdants(self):
        if len(self.liste_perdants) == 0:
            return "Personne n'a encore perdu."
        else:
            for i in self.liste_perdants:
                print('Nom : {0[nom_famille]} ; Prénom : {0[prenom]} ; Date de naissance : {0[date_naissance]} ; Sexe : {0[sexe]} ; Classement : {0[classement]}'.format(i.serialize()))
