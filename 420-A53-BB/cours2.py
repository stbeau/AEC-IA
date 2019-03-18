__author__ = '1995282'


def p1():
    bias = 3 # créer une nouvelle variabole locale
    return bias

def p2():
    global biais # pour pouvoir modifier une variable globale
    biais = 3
    return biais

def calcul_exponent(a,b):
    return a**b

def calcul_exponent(a=5,b=2.):
    '''
    Retourne la base à l>'exposant b --> a^b
    :param a: Base
    :param b: Exposant
    :return: Base**Exposant
    '''
    return a**b



if __name__ == '__main__':
    biais = 5
    p1()
    print("a):",biais)
    p2()
    print("b):",biais)
    print(calcul_exponent(12,2))
    print(calcul_exponent())


class Etudiant:
    pass
obj1 = Etudiant()

print(obj1)

class Etudiant:
    def __init__(self,nom,prenom,code,note_finale):
        self.nom = nom
        self.prenom = prenom
        self.code = code
        self.note_finale = note_finale

    def __str__(self):
        return "nom:{}, prenom:{}, code:{}, note_finale:{}".format(self.nom,self.prenom,self.code,self.note_finale)

    def venir_college(self):
        print("Etudiant vient au collège")
        self.note_finale+=5

    def ecouter(self):





obj1 = Etudiant("S","B","199",100)

print(obj1)




