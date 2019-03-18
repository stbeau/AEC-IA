__author__ = '1995282'


class Compte:
    def __init__(self, titulaire, montant, code):
        self._titulaire = titulaire
        self.__montant = montant
        self.code = code

    def __str__(self):
        return self.code

    def __del__(self):
        print("Le compte de code {} est effacé".format(self.code))

    def setTitulaire(self,titulaire):
        self._titulaire = titulaire

    def setMontant(self,montant):
        self.__montant = montant

    def obtenirTitulaire(self):
        return self._titulaire

    def obtenirMontant(self):
        return self.__montant

    def retirerArgent(self,montant):
        self.__montant -= montant

    def depotArgent(self,montant):
        self.__montant += montant



def main():
    obj1 = Compte(titulaire="FlouFlou",code="ABC123",montant=5000)
    obj2 = Compte(titulaire="FlouClair",code="AXY123",montant=4000)
    obj3 = Compte(titulaire="AnnieClairClair",code="118987",montant=77)

    obj2.depotArgent(1000)
    obj2.retirerArgent(50)

    print(obj2.obtenirMontant())


if __name__ == '__main__':
    main()