class Tournoi:
    def __init__(self,nb_players:int,name:str,location:str,date:str,number_of_rounds=4,players_list=[],list_of_rounds=[],players_who_lost=[],players_still_in_the_tournament=[]):
        self.nb_players = nb_players
        self.players_list = players_list
        self.name = name
        self.location = location
        self.date = date
        self.number_of_rounds = number_of_rounds
        self.list_of_rounds = list_of_rounds
        self.players_still_in_the_tournament = players_still_in_the_tournament
        self.players_who_lost = players_who_lost
    
    def serialize(self):
        return self.__dict__

    def ajouter_joueur(self,player):
        self.players_list.append(player)

    def premier_tour(self):
        l = len(self.players_list)
        sorted_by_rank = sorted(self.players_list,key=lambda player: player.classement)
        mid = int(l//2)
        sup = sorted_by_rank[:mid]
        inf = sorted_by_rank[mid:]
        liste_matchs = []
        for i in range(mid):
            match = Match(sup[i],inf[i])
            match.resultat(int(input("Indiquez 1 si le joueur 1 a gagné le match, sinon 2. En cas d'égalité, 1/2 : ")))
            liste_matchs.append(match)
        tour = Round(liste_matchs)
        self.list_of_rounds.append(tour)
        for i in liste_matchs:
            joueur_perdant = "".join(["joueur",str(i.serialize()['perdant'])])
            self.players_who_lost.append(i.serialize()[joueur_perdant])
            self.players_list.remove(i.serialize()[joueur_perdant])
        self.afficher_joueurs()
        self.afficher_perdants()
        self.number_of_rounds -= 1
    
    def reste_tournoi(self):
        while self.number_of_rounds > 0:
            liste_matchs = []
            for i in range(0,len(self.players_list) - 1,2):
                match = Match(self.players_list[i],self.players_list[i + 1])
                match.resultat(int(input("Indiquez 1 si le joueur 1 a gagné le match, sinon 2. En cas d'égalité, 1/2 : ")))
                liste_matchs.append(match)
            tour = Round(liste_matchs)
            self.list_of_rounds.append(tour)
            for i in liste_matchs:
                joueur_perdant = "".join(["joueur",str(i.serialize()['perdant'])])
                self.players_who_lost.append(i.serialize()[joueur_perdant])
                self.players_list.remove(i.serialize()[joueur_perdant])
            self.afficher_joueurs()
            self.afficher_perdants()
            self.number_of_rounds -= 1
            if len(self.players_list) == 1:
                self.fin_tournoi()
                break

    def fin_tournoi(self):
        print('{0[nom_famille]} {0[prenom]} est le grand vainqueur de notre tournoi !'.format(self.players_list[0].serialize()))
        