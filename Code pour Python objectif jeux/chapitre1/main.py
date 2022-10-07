from random import random, randint, choice, sample
#valeurs = list()
#for i in range(11):
# valeur = int(random() * 10 + 1)
    #valeur = randint(1, 10)
    #   valeurs.append(valeur)
#print(valeurs)

#d1 = list()

#for i in range(50):
#    d1.append(randint(1, 6) + randint(1, 6) + randint(1, 6))
#print(d1)
#d2 = list()
#for i in range(200):
#   d2.append(randint(1, 8) + randint(1, 8))
#print(d2)

#des_truque = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6 ,6, 6, 6, 6]
#for i in range(100):
    #print(choice(des_truque), end = '\t')

def choix(liste):
    n = randint(0, len(liste) -1)
    return liste[n]
liste = [n for n in range(10)]
print(choix(liste))
x = 12,3
print("{.1f}".format(x))

