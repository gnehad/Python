from random import randint

inf = 1
sup = 30
maxTentatives = 5
nombreSecret = randint(inf, sup)
print(f"J'ai choisi un nombre entre {int} et {sup}")
print(f"À vous de le deviner en {maxTentatives} tentatives au maximum")
trouve = False
n  = -1
nbEssais = 0
while(n != nombreSecret and nbEssais <= maxTentatives):
    nbEssais += 1
    print("Essai numéro ", nbEssais)
    n = int(input("Votre proposition : "))
    if(nombreSecret == n):
        print(f"Bravo! Vous avez trouvé {nombreSecret} en {nbEssais} tentatives")
    elif(n < nombreSecret):
        print("Trop petit")
    else:
        print("Trop grand")
if(n != nombreSecret):
    print(f"Vous avez échoué!!! Le nombre à deviner était {nombreSecret}")



