__author__ = '1995282'



def saisir_infocorps():
    masse = float(input("Quelle est votre masse en kg ? : "))
    taille = float(input("Quelle est votre taille en m ? : "))
    return masse, taille

def calcul_imc(masse:float,taille:float):
    return masse/(taille**2)

def affiche_imc(imc):
    print("Votre indice de masse corporelle est {:.2f} kg/m^2".format(imc))

def obtenir_donnees_classification_imc():
    risque = ["Accru","Moindre","Accru","Élevé","Très élevé","Extrêmement élevé"]
    classification = ["Poids insuffisant","Poids normal","Excès de poids","Obésité, classe I","Obésité, classe II","Obésité, classe III"]
    imc_val = [18.5,25,30,35,40,float("inf")]
    return risque,classification,imc_val

def obtenir_class_number_imc(imc,imc_val):
    for imc_class_num in range(len(imc_val)):
        if imc < imc_val[imc_class_num]:
            break
    return imc_class_num

def affiche_classification_risque(imc_class_num,classification,risque):
    print("Classification : {}".format(classification[imc_class_num]))
    print("Risques : {}".format(risque[imc_class_num]))


if __name__ == '__main__':
    masse,taille = saisir_infocorps()
    imc = calcul_imc(masse,taille)
    risque,classification,imc_val = obtenir_donnees_classification_imc()
    imc_class_num = obtenir_class_number_imc(imc,imc_val)
    affiche_imc(imc)
    affiche_classification_risque(imc_class_num,classification,risque)








