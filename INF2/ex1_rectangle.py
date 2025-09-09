class Rectangle():
    def __init__(self, longueur, largeur):
        '''
        Ce constrcteur permet d'initialiser tous les paramètres de la classe, nous noterons que les conditions propres à chacun
        des paramètres sont présents ici ainsi que dans les getter et les setter (nous ne pouvon spas utiliser les property donc
        nous sommes obliger de répéter les instructions pour qu'elles soient prises en compte dès l'initialisation d'un objet.
        '''
        if type(longueur) is not float:
            raise TypeError("La longueur doit être un float")
        elif longueur < 0:
            raise ValueError("La longueur doit être positive")
        self.longueur = longueur
        if type(largeur) is not float:
            raise TypeError("La largeur doit être un float")
        elif largeur < 0:
            raise ValueError("La largeur doit être positive")
        self.largeur = largeur

    def get_longueur(self):
        return self.longueur
    def set_longueur(self, val):
        if type(val) is not float :
            raise TypeError("La longueur doit être un float")
        elif val<0:
            raise ValueError("La longueur doit être positive")
        self.longueur=val

    def get_largeur(self):
        return self.largeur
    def set_largeur(self, val):
        if type(val) is not float:
            raise TypeError("La largeur doit être un float")
        elif val < 0:
            raise ValueError("La largeur doit être positive")
        self.largeur = val

    def perimetre(self):
        '''
        Cette méthode permet de retourner le périmètre pour un objet Rectangle donné.
        exemple 1 : Longueur : 10.0 - Largeur : 12.2 - Perimetre : 44.4
        exemple 2 : Longueur : 5.3 - Largeur : 5.3 - Perimetre : 21.2
        '''
        return (self.largeur*2)+(self.longueur*2)

    def aire(self):
        '''
        Cette méthode permet de retourne l'aire pour un objet Rectangle demandé.
        exemple 1 : Longueur : 10.0 - Largeur : 12.2 - Aire : 122.0
        exemple 2 : Longueur : 5.3 - Largeur : 5.3 - Aire : 28.09
        '''
        return self.longueur*self.largeur

    def est_carre(self):
        '''
        Cette méthode retourne True lorsque que l'objet Rectangle est carré (longueur=largeur), sinon False par défaut.
        exemple 1 : Longueur : 10.0 - Largeur : 12.2 - Ce n'est pas un carré --> a retourné False
        exemple 2 : Longueur : 5.3 - Largeur : 5.3 - C'est un carré --> a retourné True
        '''
        if self.largeur==self.longueur:
            return True

    def le_plus_grand(self, other):
        '''
        Cette méthode permet de comparer l'aire de deux objets et d'envoyer un message indiquant le plus grand.
        exemple 1 : print(r1.le_plus_grand(r2))
        résultat 1 : le plus grand est le premier/celui de gauche
        exemple 2 : print(Rectangle.le_plus_grand(r3,r2))
        résultat 2 : le plus grand est le second/celui de droite
        '''
        if (type(other) is not Rectangle) or (type(self) is not Rectangle) :
            raise TypeError("Un de ces éléments n'est pas un rectangle")
        if self.aire()>other.aire():
            return f"le plus grand est le premier/celui de gauche"
        else:
            return f"le plus grand est le second/celui de droite"

    def afficher(self):
        print(f"Longueur : {self.longueur} - Largeur : {self.largeur} - Perimetre : {self.perimetre()} - Aire : {self.aire()} - {"C'est un carré" if self.est_carre() else "Ce n'est pas un carré"}")

def main():
    r1=Rectangle(10.0,12.2)
    r2=Rectangle(5.3,5.3)
    r3=Rectangle(2.9,5.0)
    r4=0
    r1.afficher()                           # Longueur : 10.0 - Largeur : 12.2 - Perimetre : 44.4 - Aire : 122.0 - Ce n'est pas un carré
    r2.afficher()                           # Longueur : 5.3 - Largeur : 5.3 - Perimetre : 21.2 - Aire : 28.09 - C'est un carré
    print(r1.le_plus_grand(r2))             # le plus grand est le premier/celui de gauche
    print(Rectangle.le_plus_grand(r3,r2))   # le plus grand est le second/celui de droite
    print(r1.le_plus_grand(r4))             # TypeError: Un de ces éléments n'est pas un rectangle


main()


