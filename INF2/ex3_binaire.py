from pickle import load, dump


class Etudiant:
    """
    Cette classe permet de créer un profil étudiant en entrant :
        son nom : str
        son année de naissance : int
        son gpa: float
        s'il connait le python: Booléen
    """

    def __init__(self, nom, annee_naissance, gpa, connais_python):
        self.nom = nom
        self.annee_naissance = annee_naissance
        self.gpa = gpa
        self.connais_python = connais_python

    # Getter/Setter pour chacun de nos attributs
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, val):
        if type(val) is not str:
            raise TypeError("Le nom doit être une chaine de caractère")
        self._nom = val

    @property
    def annee_naissance(self):
        return self._annee_naissance

    @annee_naissance.setter
    def annee_naissance(self, val):
        if type(val) is not int:
            raise TypeError("L'année de naissance doit ête un entier")
        self._annee_naissance = val

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, val):
        if type(val) is not float:
            raise TypeError("le gpa doit être un float")
        self._gpa = val

    @property
    def connais_python(self):
        return self._connais_python

    @connais_python.setter
    def connais_python(self, val):
        if type(val) is not bool:
            raise TypeError("La valeur de connais_python doit être un booléen")
        self._connais_python = val

    def to_dict(self):
        """
        Cette méthode permet de retourner un dictionnaire rassemblant tout les attributs
        """
        return {"Nom": self.nom, "GPA": self.gpa, "Annee_Naissance": self.annee_naissance,
                "Connais_Python": self.connais_python}


def ecriture_binaire(texte, chemin):
    '''
    Cette fonction assure l'écriture d'un élément texte de n'importe quel type dans un fichier binaire
    '''
    with open(chemin, "wb") as f:
        dump(texte, f)


def lecture_binaire(chemin):
    '''
    Cette fonction permet la lecture et récupération du contenu d'un fichier binaire
    en une chaine de caractère qui est ensuite retournée
    '''
    with open("étudiantbinaire.pkl", "rb") as file:
        contenu = load(file)
    return contenu


def comparaison(l1, l2):
    '''
    Cette fonction permet de comparer le contenu entre 2 listes qu'elle prend en paramètre d'entrée,
    puis elle permet d'afficher un message suite à la comparaison (absence de return).
    '''
    # Affichage des étudiants présents dans la liste crée (sans passer par le fichier bianire)
    print("\nElements obtenus dans la liste créée à partir de la classe Etudiant :")
    for element in l1:
        print(element)

    # Affichage des étudiants provenant du contenu du fichier binaire et comparaison avec la liste d'origine
    print("\nElements obtenus dans la liste récupérée dans le fichier binaire :")
    for i in range(0, len(l2)):
        if l2[i] == l1[i]:
            print(l2[i], "-> identique à la liste d'origine")
        else:
            print(l2[i], "-> différent de la liste d'origine")


def main():
    # Implémentation de 3 étudiants utilisés comme exemple pour la suite de l'exercice
    E1 = Etudiant("DUPONT Jacques", 2002, 4.5, True)
    E2 = Etudiant("MONT David", 1998, 3.2, False)
    E3 = Etudiant("LENTIL Jeanne", 2001, 3.9, True)
    liste = [E1.to_dict(), E2.to_dict(), E3.to_dict()]

    ecriture_binaire(liste,
                     "étudiantbinaire.pkl")  # ecriture de la liste contenant les étudiants dans un fichier binaire
    liste_binaire = lecture_binaire("étudiantbinaire.pkl")  # lecture et récupération de la liste du fichier binaire

    comparaison(liste, liste_binaire)
    ''' Affichage obtenu :
    Elements obtenus dans la liste créée à partir de la classe Etudiant :
    {'Nom': 'DUPONT Jacques', 'GPA': 4.5, 'Annee_Naissance': 2002, 'Connais_Python': True}
    {'Nom': 'MONT David', 'GPA': 3.2, 'Annee_Naissance': 1998, 'Connais_Python': False}
    {'Nom': 'LENTIL Jeanne', 'GPA': 3.9, 'Annee_Naissance': 2001, 'Connais_Python': True}

    Elements obtenus dans la liste récupérée dans le fichier binaire :
    {'Nom': 'DUPONT Jacques', 'GPA': 4.5, 'Annee_Naissance': 2002, 'Connais_Python': True} -> identique à la liste d'origine
    {'Nom': 'MONT David', 'GPA': 3.2, 'Annee_Naissance': 1998, 'Connais_Python': False} -> identique à la liste d'origine
    {'Nom': 'LENTIL Jeanne', 'GPA': 3.9, 'Annee_Naissance': 2001, 'Connais_Python': True} -> identique à la liste d'origine
    '''

    # Réponse à la question 2
    print("\nQuestion : Quels avantages et désavantages voyez‑vous à l’utilisation du mode texte ou binaire ?")
    print(
        "Réponse : \n   L'avantage d'écrire au sein d'u fichier texte permet d'ouvrir ce fichier sans utiliser Python, "
        "\n et de le comprendre dans sa totalité. Toutefois, lors de l'écriture, les éléments à ajouter doivent être inscrits"
        "\n un à un et en format STR, ceci peut demander l'adaptation du programme pour l'écriture de liste, de dictionnaire..."
        "\n   Pour ce qui est de l'usage de fichiers binaires, l'avantage premier est de pouvoir y inscrire des listes, des "
        "\n dictionnaires... et cela directement sans avoir à les transformer en chaîne de caractère au préalable. Ceci permet "
        "\n donc de transférer des fichiers sans avoir à les modifier et ainsi de les récupérer très facilement. Cependant, "
        "\n l'utilisation de Python et/ou d'un programme de lecture du fichier binaire est donc obligatoire puisque le fichier "
        "\n PKL n'est donc pas lisible en lecture seul (à l'inverse du fichier texte).")


main()