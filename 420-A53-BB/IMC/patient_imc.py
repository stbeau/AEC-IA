__author__ = '1995282'

class Patient:
    def __init__(self,nom,age,poids,taille):
        self.nom = nom
        self.age = age
        self.poids = poids
        self.taille = taille

    def __str__(self):
        print("Nom : {}, Age : {}, Poids : {}, Taille : {}".format(nom,age,poids,taille))

class imc(Patient):
    def __init__(self,nom,age,poids,taille):
        Patient.__init__(self,nom,age,poids,taille)
        self.initialiser_classification_imc()
        self.calculer_imc()
        self.calculer_numero_classe_imc()

    def initialiser_classification_imc(self):
        self.risque = ["Accru","Moindre","Accru","Élevé","Très élevé","Extrêmement élevé"]
        self.classification = ["Poids insuffisant","Poids normal","Excès de poids","Obésité, classe I","Obésité, classe II","Obésité, classe III"]
        self.imc_val = [18.5,25,30,35,40,float("inf")]

    def calculer_imc(self):
        self.imc = self.poids/(self.taille**2)

    def obtenir_imc(self):
        return self.imc

    def affiche_imc(self):
        self.calculer_imc()
        print("L'imc de {} est {:.2f} kg/m^2.".format(self.nom,self.obtenir_imc()))

    def calculer_numero_classe_imc(self):
        for position in range(len(self.imc_val)):
            if self.imc < self.imc_val[position]:
                break
        self.numero_classe_imc = position

    def obtenir_numero_classe_imc(self):
        return self.numero_classe_imc

    def determiner_classification_imc(self):
        self.initialiser_classification_imc()
        self.calculer_imc()
        self.calculer_numero_classe_imc()

    def afficher_classe_imc(self):
        self.determiner_classification_imc()
        print("Classification : {}".format(self.classification[self.obtenir_numero_classe_imc()]))
        print("Risques : {}".format(self.risque[self.obtenir_numero_classe_imc()]))



class Patient2:
    def __init__(self,nom,age,poids,taille):
        self.nom = nom
        self.age = age
        self.poids = poids
        self.taille = taille
        self.initialiser_classification_imc()

    def __str__(self):
        print("Nom : {}, Age : {}, Poids : {}, Taille : {}".format(nom,age,poids,taille))

    def initialiser_classification_imc(self):
        self.risque = ["Accru","Moindre","Accru","Élevé","Très élevé","Extrêmement élevé"]
        self.classification = ["Poids insuffisant","Poids normal","Excès de poids","Obésité, classe I","Obésité, classe II","Obésité, classe III"]
        self.imc_val = [18.5,25,30,35,40,float("inf")]

    def calculer_imc(self):
        self.imc = self.poids/(self.taille**2)

    def obtenir_imc(self):
        return self.imc

    def affiche_imc(self):
        self.calculer_imc()
        print("L'imc de {} est {:.2f} kg/m^2.".format(self.nom,self.obtenir_imc()))

    def calculer_numero_classe_imc(self):
        for position_imc_class in range(len(self.imc_val)):
            if self.imc < self.imc_val[position_imc_class]:
                break
        self.numero_classe_imc = position_imc_class

    def obtenir_numero_classe_imc(self):
        return self.numero_classe_imc

    def determiner_classification_imc(self):
        self.initialiser_classification_imc()
        self.calculer_imc()
        self.calculer_numero_classe_imc()

    def afficher_classe_imc(self):
        self.determiner_classification_imc()
        print("Classification : {}".format(self.classification[self.obtenir_numero_classe_imc()]))
        print("Risques : {}".format(self.risque[self.obtenir_numero_classe_imc()]))



def saisir_infocorps():
    masse = float(input("Quelle est votre masse en kg ? : "))
    taille = float(input("Quelle est votre taille en m ? : "))
    return masse, taille


if __name__ == '__main__':

    p = Patient("Steph",30,80,1.9)
    p.affiche_imc()
    p.afficher_classe_imc()
