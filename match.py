class Round:
    def __init__(self,liste_matchs): 
        self.liste_matchs = liste_matchs
    
    def afficher_liste_matchs(self):
        return self.liste_matchs


class Match:
    def __init__(self,joueur0,joueur1):
        self.joueur0 = joueur0
        self.joueur1 = joueur1
        self.perdant = -1
    def resultat(self,valeur):
        self.perdant = 1 if valeur == 1 else 0
    def serialize(self):
        return self.__dict__