class Player:
    def __init__(self,nom_famille,prenom,date_naissance,sexe,classement:int):
        self.nom_famille = nom_famille
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement

    def serialize(self):
        return self.__dict__
