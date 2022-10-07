class Voiture:
    totalVoitures = 0

    def __init__(self, fabricant, modele, annee, couleur, nbportes, nbplaces):
        self.fabricant = fabricant
        self.modele = modele
        self.annee = annee
        self.couleur = couleur
        self.nbPortes = nbportes
        self.nbPlaces = nbplaces
        Voiture.totalVoitures = Voiture.totalVoitures + 1

    @staticmethod
    def getTotalVoitures():
        return Voiture.totalVoitures
class SUV(Voiture):
    totalSUV = 0
    def __init__(self, fabricant, modele, annee, couleur, nbportes, nbplaces):
        Voiture.__init__(self, fabricant, modele, annee, couleur, nbportes, nbplaces)
        SUV.totalSUV = SUV.totalSUV + 1
    @staticmethod
    def getTotalSUV():
        return SUV.totalSUV
    def tirerRoulotte(self):
        print("Je peux tirer une roulotte")
class Decapotable(Voiture):
    totalDecapotables = 0
    def __init__(self, fabricant, modele, annee, couleur, nbportes, nbplaces):
        Voiture.__init__(self, fabricant, modele, annee, couleur, nbportes, nbplaces)
        Decapotable.totalDecapotables = Decapotable.totalDecapotables + 1
    @staticmethod
    def getTotalDecapotables():
        return Decapotable.totalDecapotables
    def retracterToit(self):
        print("Je possède un toit que je peux retracter")


uneDecapotable = Decapotable("BMW", "Série 4", 2012, "Bleu", 2, 4)
uneDecapotable.retracterToit()
uneDecapotable = Decapotable("Audi", "A3", 2019, "Rouge", 2, 4)
uneDecapotable.retracterToit()
uneDecapotable = Decapotable("Mazda", "MX-5", 2020, "blanche", 2, 2)
uneDecapotable.retracterToit()
unSUV = SUV("Toyota", "C-HR", 2019, "Gris", 4, 5)
unSUV.tirerRoulotte()
unSUV = SUV("Kia", "Niro", 2019, "Bleu", 4, 5)
print("Total de voiture créées : ", Voiture.getTotalVoitures())
print("Total de décapotables créées : ", Decapotable.getTotalDecapotables())
print("Total de SUV créés : ", SUV.getTotalSUV())
