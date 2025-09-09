import csv

class Etudiant:
    """
    Cette classe permet de créer un profil étudiant en entrant :
        son nom : str
        son année de naissance : int
        son gpa: float
        s'il connait le python: Booléen
    """
    def __init__(self,nom,annee_naissance,gpa,connais_python):
        self.nom=nom
        self.annee_naissance=annee_naissance
        self.gpa=gpa
        self.connais_python=connais_python

    #Getter/Setter pour chacun de nos attributs
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,val):
        if type(val) is not str:
            raise TypeError("Le nom doit être une chaine de caractère")
        self._nom=val

    @property
    def annee_naissance(self):
        return self._annee_naissance
    @annee_naissance.setter
    def annee_naissance(self, val):
        if type(val) is not int:
            raise TypeError("L'année de naissance doit ête un entier")
        self._annee_naissance=val

    @property
    def gpa(self):
        return self._gpa
    @gpa.setter
    def gpa(self,val):
        if type(val) is not float:
            raise TypeError("le gpa doit être un float")
        self._gpa=val

    @property
    def connais_python(self):
        return self._connais_python
    @connais_python.setter
    def connais_python(self,val):
        if type(val) is not bool:
            raise TypeError("La valeur de connais_python doit être un booléen")
        self._connais_python=val


    def to_dict(self):
        """
        Cette méthode permet de retourner un dictionnaire rassemblant tout les attributs
        """
        return {"Nom":self.nom , "GPA":self.gpa,"Annee_Naissance": self.annee_naissance ,"Connais_Python":self.connais_python}

    @classmethod
    def from_dict(cls,dict):
        """
        Méthode de classe permettant de créer un objet étudiant
        Le paramètre entré dict est un dictionnaire crée par la méthode to_dict
        La méthode retourne donc un objet étudiant avec les attributs du dictionnaire
        """
        return Etudiant(dict["Nom"],int(dict["Annee_Naissance"]),float(dict["GPA"]),bool(dict["Connais_Python"]))


class Groupe:
    def __init__(self,liste_etu):
        self.liste_etu=liste_etu

    @property
    def liste_etu(self):
        return self._liste_etu
    @liste_etu.setter
    def liste_etu(self,val):
        for i in val:
            if type(i) is not Etudiant:
                raise TypeError("Les éléments doivent être des objets etudiants")
        self._liste_etu=val

    def sauvegarder_csv(self,nomcsv):
        """
        La méthode permet de sauvegarder liste des étudiants et leur caractériqtiques dans un fichier csv à partir de la liste(Etudiant Object)
        Le paramètre nomcsv doit être le nom d'un fichier csv préalablement crée vide dans le même dossier
        La méthode permet donc d'écrire dans le fichier csv où chaque ligne correspond à un étudiant
        """
        csvfile=open(nomcsv,"w")
        writer = csv.DictWriter(csvfile, fieldnames=["Nom","Annee_Naissance","GPA","Connais_Python"],delimiter=";")
        writer.writeheader()
        for i in self.liste_etu:
            writer.writerow(i.to_dict())

    @classmethod
    def charger_csv(cls,nomcsv):
        """
        Méthode de classe permettant de créér un objet groupe avec une liste des étudians à partir d'un nom de fichiers csv
        Le paramètre nomcsv doit être le nom d'un fichier csv préalablement crée dans le même dossier
        La méthode retourne l'objet groupe souhaité en vérifiant à chaque fois les conditions sur les attributs
        """
        with open(nomcsv,newline='') as csvfile:
            reader = csv.DictReader(csvfile ,delimiter=";")
            liste_etu=[]
            for i in reader:
                if i is not {'Nom': '', 'Annee_Naissance': '', 'GPA': '', 'Connais_Python': ''}:
                    liste_etu.append(Etudiant.from_dict(i))
        return Groupe(liste_etu)


def main():
    E1=Etudiant("Bernard",2000,3.0,False)
    E2=Etudiant("Yves",2001,3.5,False)
    E3=Etudiant("Nicolas",2002,4.0,True)
    print(E1.to_dict())
        # Retourne un dictionnaire de l'étudiant 1 : {'Nom': 'Bernard', 'GPA': 3.0, 'Annee_Naissance': 2000, 'Connais_Python': False}
    liste_etu1=[E1,E2,E3]
    Groupe(liste_etu1).sauvegarder_csv("csv.csv")
        # On sauvegarde bien les données voulu dans une table csv
    print(Groupe.charger_csv('csv.csv').liste_etu[0].to_dict()["Nom"])
        # On vérifie ici si l'object crée convient à notre table csv : Bernard


"""
print(Groupe.charger_csv('csv.csv').liste_etu[0].to_dict()['Nom'])
"""

main()