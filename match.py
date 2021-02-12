class Round:
    def __init(self,liste_matchs): 
        self.liste_matchs = liste_matchs

    def afficher_matchs(self):
        for i in self.liste_matchs:
            print(i)
class Match:
    def __init__(self,joueur1,joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.gagnant = 0
    
    def resultat(self,valeur):
        self.gagnant = valeur
    
    def serialize(self):
        return self.__dict__
    