__author__ = '1995282'

#f = open("data/heures.txt")

#print(f.read())

#print(f.readlines())

#f.close()


with open("data/heures.txt") as f2:
    #print(f2.readlines())
    listing = f2.readlines()
    for ligne in listing:
        #print(ligne)
        #code, nom, j1, j2, j3, j4 , j5 = ligne.split()
        mot = ligne.split()
        somme = sum(map(float,mot[2:-1]))
        moyenne = somme/len(mot[2:-1])
        print("{} Code {} a travaillé {:5.2f} heures avec une moyenne de {:.2f}/ jour".format(mot[1],mot[0],somme,moyenne))

