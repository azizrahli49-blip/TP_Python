class PoupeeRusse():
    def __init__(self, nom, taille, est_ouverte = False, dans = "rien", contient = "vide"):
        '''
        Constructeur contenant l'ensemble des paramètres propres à chaque objet de la classe.
        Nous noterons que 3 variables sont définies par défaut : la poupée est fermée, elle est vide et elle ne se trouve pas dans une autre poupée.
        '''
        self.nom = nom
        self.taille = taille
        self.est_ouverte = est_ouverte
        self.dans = dans
        self.contient = contient

    @property
    def nom(self):
        return self._nom
    @property
    def taille(self):
        return self._taille
    @property
    def est_ouverte(self):
        return self._est_ouverte
    @property
    def dans(self):
        return self._dans
    @property
    def contient(self):
        return self._contient

    @nom.setter
    def nom(self, val):
        if type(val) is not str :
            raise TypeError("Le nom doit être une chaîne de caractère")
        self._nom = val
    @taille.setter
    def taille(self, val):
        if type(val) is not int :
            raise TypeError("La taille doit être un entier")
        elif val<0 :
            raise ValueError("La taille doit être positive")
        self._taille = val
    @est_ouverte.setter
    def est_ouverte(self, val):
        if type(val) is not bool :
            raise TypeError("La variable est_ouverte doit être un booléen")
        self._est_ouverte = val
    @dans.setter
    def dans(self, val):
        '''
        Nous noterons que cette variable prend comme valeur l'objet/la poupée contenant celle ci,
        elle prend donc l'ensemble de l'objet correspondant et pas uniquement son nom.
        Si la poupée n'est pas contenue par une autre, la variable prend la chaine de caractère "rien".
        '''
        if type(val) is not PoupeeRusse and val!="rien":
            raise TypeError("Cette poupée ne peut être contenue que dans une autre poupée")
        self._dans = val
    @contient.setter
    def contient(self, val):
        '''
        De la même manière que pour la variable self.dans, celle ci contient la poupée contenue,
        elle ne prend en compte que la poupée directe (non pas une chaine des poupées contenues jusqu'à la plus petite).
        Dans le cas où la poupée est vide, la variable prend la valeur "vide".
        exemple : p2=PoupeeRusse("p2", 2, contient=p1)
        résultat : Nom: p2 - Taille: 2 - Ouverte?: False - Dans: rien - Contient: p1
        '''
        if type(val) is not PoupeeRusse and val!="vide" :
            raise TypeError("Ce qui est contenu dans cette poupée doit aussi être une/des poupée(s)")
        self._contient=val

    def ouvrir(self):
        '''
        Cette fonction permet d'ouvrir la poupée si elle était fermée et si elle n'est pas dans une autre poupée.
        exemple : p1=PoupeeRusse("p1",1)
        résultat :Nom: p1 - Taille: 1 - Ouverte?: False - Dans: rien - Contient: vide
        utilisation de la fonction : p1.ouvrir()
        résultat : Nom: p1 - Taille: 1 - Ouverte?: True - Dans: rien - Contient: vide
        '''
        if self.est_ouverte==False and self.dans=="rien":
            self.est_ouverte=True
        else :
            print(f"La poupée {self.nom} ne peut pas être ouverte")

    def fermer(self):
        '''
        Cette fonction permet de fermer la poupée si elle était ouverte et si elle ne se trouve pas dans une autre poupée.
        utilisation de la fonction après celle précédente (pour ouvrir) : p1.fermer()
        résultat : Nom: p1 - Taille: 1 - Ouverte?: False - Dans: rien - Contient: vide
        '''
        if self.est_ouverte==True and self.dans=="rien":
            self.est_ouverte=False
        else :
            print(f"La poupée {self.nom} ne peut pas être fermée")

    def placer_dans(self, p):
        '''
        Cette fonction permet de mettre une première poupée dans une seconde. Les conditions sont :
            - la seconde doit être vide et pas dans une autre poupée
            - la première ne doit pas être dans une autre poupée également
            - la première doit être plus petite que la deuxième
            - la première doit être fermée et la deuxième ouverte
        exemple : p2.ouvrir() puis p1.placer_dans(p2)
        résultat pour la plus petite poupée : Nom: p1 - Taille: 1 - Ouverte?: False - Dans: p2 - Contient: vide
        résultat pour la plus grande poupée : Nom: p2 - Taille: 2 - Ouverte?: True - Dans: rien - Contient: p1
        '''
        if p.dans=="rien" and p.contient=="vide" :
            if self.dans=="rien" :
                if p.est_ouverte==True and self.est_ouverte==False :
                    if self.taille<p.taille:
                        self.dans=p
                        p.contient=self
                    else :
                        print(f"La poupée à mettre ({self.nom}) doit être plus petite que celle qui doit la contenir ({p.nom})")
                else :
                    print(f"La poupée la plus grande ({p.nom}) doit être ouverte et la plus petite ({self.nom}) fermée")
            else :
                print(f"La poupée que vous souhaitez placer ({self.nom}) ne doit pas être dans une autre poupée")
        else :
            print(f"La poupée que vous voulez remplir ({p.nom}) doit être vide et pas dans une autre poupée")

    def sortir_de(self):
        '''
        Cette fonction permet de sortir une poupée d'une autre, en vérifiant qu'elle s'y trouve bien et si la plus grande
        est ouverte.
        exemple : p1 est dans p2 on a alors l'instruction p1.sortir_de ()
        résultats avant : Nom :p1 - Taille : 1 - Ouverte? : False  - Dans : p2 - Contient : vide
                          Nom :p2 - Taille : 2 - Ouverte? : True  - Dans : rien - Contient : p1
        résultats après : Nom :p1 - Taille : 1 - Ouverte? : False  - Dans : rien - Contient : vide
                          Nom :p2 - Taille : 2 - Ouverte? : True  - Dans : rien - Contient : vide
        '''
        if self.dans=="rien" :
            print(f"La poupée {self.nom} n'est pas dans une autre poupée")
        elif (self.dans).est_ouverte==True :
            self.dans.contient="vide"
            self.dans="rien"
        else :
            print(f"La poupée {self.dans.nom}, contenant la poupée {self.nom} que vous ssouhaitez sortir, est fermée")

    def __str__(self):
        '''
        Cette fonction permet l'affichage des données de l'objet.
        Nous avons ajouter à cela un code permettant de faire la liste des poupées contenues par la poupée appelée.
        exemple : p1 est placée dans p2, qui est ensuite placée dans p3
        résultats : Nom :p1 - Taille : 1 - Ouverte? : False  - Dans : p2 - Contient : vide
                    Nom :p2 - Taille : 2 - Ouverte? : False  - Dans : p3 - Contient : p1
                    Nom :p3 - Taille : 3 - Ouverte? : True  - Dans : rien - Contient : p2 qui contient p1
        '''
        list=[]
        chaine=""
        contenues=self.contient
        while contenues!="vide":
            list.append(contenues)
            contenues = contenues.contient
        for i in range (0,len(list)) :
            chaine+=str(list[i].nom)+(" qui contient " if i!=len(list)-1 else " ")
        return (f"Nom :{self.nom} - Taille : {self.taille} - Ouverte? : {self.est_ouverte} "
                f" - Dans : {self.dans.nom if self.dans!="rien" else self.dans}"
                f" - Contient : {chaine if chaine!="" else self.contient}")

def main():
    p1=PoupeeRusse("p1",1)
    p2=PoupeeRusse("p2", 2)
    p3=PoupeeRusse("p3",3)
    print(p1, "\n", p2, "\n", p3)
    '''
    Nom :p1 - Taille : 1 - Ouverte? : False  - Dans : rien - Contient : vide 
    Nom :p2 - Taille : 2 - Ouverte? : False  - Dans : rien - Contient : vide 
    Nom :p3 - Taille : 3 - Ouverte? : False  - Dans : rien - Contient : vide
    '''
    p2.ouvrir()
    p1.placer_dans(p2)
    p2.fermer()
    p3.ouvrir()
    p2.placer_dans(p3)
    print(p1, "\n", p2, "\n", p3)
    '''
    Nom :p1 - Taille : 1 - Ouverte? : False  - Dans : p2 - Contient : vide 
    Nom :p2 - Taille : 2 - Ouverte? : False  - Dans : p3 - Contient : p1  
    Nom :p3 - Taille : 3 - Ouverte? : True  - Dans : rien - Contient : p2 qui contient p1 
    '''
    p2.sortir_de()
    p1.sortir_de() # message d'erreur : p1 ne peut pas être sortie car p2 est fermée
    p2.ouvrir()
    p1.sortir_de() # p1 est sortie
    print(p1, "\n", p2, "\n", p3)
    '''
    Nom :p1 - Taille : 1 - Ouverte? : False  - Dans : rien - Contient : vide
    Nom :p2 - Taille : 2 - Ouverte? : True  - Dans : rien - Contient : vide
    Nom :p3 - Taille : 3 - Ouverte? : True  - Dans : rien - Contient : vide
    '''
    p3.fermer()
    p3.placer_dans(p2) # message d'erreur : p3 est plus grande que p2
    p3.ouvrir()
    p1.placer_dans(p3)
    p2.placer_dans(p3) # message d'erreur p3 contient déjà une poupée
    print(p1, "\n", p2, "\n", p3)
    '''
    Nom :p1 - Taille : 1 - Ouverte? : False  - Dans : p3 - Contient : vide
    Nom :p2 - Taille : 2 - Ouverte? : True  - Dans : rien - Contient : vide 
    Nom :p3 - Taille : 3 - Ouverte? : True  - Dans : rien - Contient : p1 
    '''


main()

