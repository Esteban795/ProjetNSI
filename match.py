class Round:
    def __init__(self,liste_matchs): 
        self.liste_matchs = liste_matchs

    def afficher_liste_matchs(self):
        return self.liste_matchs

class Match:
    def __init__(self,joueur1,joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.gagnant = -1
    def resultat(self,valeur):
        self.gagnant = valeur
    def serialize(self):
        return self.__dict__