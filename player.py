class Player:
    def __init__(self,nom_famille,prenom,date_naissance,sexe,classement:int,identifier:int):
        self.nom_famille = nom_famille
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.id = identifier

    def serialize(self):
        return self.__dict__

    def changer_classement(self,valeur:int):
        self.classement = valeur