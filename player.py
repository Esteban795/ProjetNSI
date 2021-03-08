class Player:
    def __init__(self,nom_famille,prenom,date_naissance,sexe,classement:int,identifier:int):
        self.lastname = nom_famille
        self.firstname = prenom
        self.date = date_naissance
        self.sexe = sexe
        self.rank = classement
        self.id = identifier

    def serialize(self):
        return self.__dict__

    def changer_classement(self,valeur:int):
        self.rank = valeur