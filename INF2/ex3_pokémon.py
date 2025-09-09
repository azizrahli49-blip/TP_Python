from random import randint

class Pokemon:
    def __init__(self,nom,pv,atk):
        self.nom=nom
        self.pv=pv
        self.atk=atk

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,val):
        if type(val) is not str:
            raise TypeError("Le nom doit être une chaîne de caractères")
        self._nom=val
    @property
    def pv(self):
        return self._pv
    @pv.setter
    def pv(self, val):
        if type(val) is not int:
            raise TypeError("Le nombre de points de vie doit être un entier")
        if val < 0:
            raise ValueError("Le nombre de points de vie doit être positif ou nul")
        self._pv = val
    @property
    def atk(self):
        return self._atk
    @atk.setter
    def atk(self, val):
        if type(val) is not int:
            raise TypeError("Les points de dégâts doivent être  représenté par un entier")
        if val < 0:
            raise ValueError("Les points de dégâts doivent être  représenté par un entier positif ou nul")
        self._atk = val

    def est_KO(self):
        '''
        Cette méthode retourne si la pokémon est KO ou non en fonction de ses points de vie.
        exemple : print(Bou.est_KO) avant son attaque avec Gou puis après (Goupix gagne)
        résultat : False --> True
        '''
        return True if self.pv==0 else False

    def attaquer(self,autre):
        '''
        Cette méthode permet de calculer le nombre de points de vie du Pokémon attaqué en fonction des points de
        dégâts du Pokémon qui attaque ainsi que que selon leur espèce. En effet, on notera que l'appel de la méthode
        'calc_multiplicateur' permet de récupérer un facteur d'attaque selon les pokémons en question, elle se
        retrouve dans chacune des classes filles.
        Cette méthode ne retourne donc aucune valeur mais permet de modifier celles des variables.
        '''
        aleatoire = round(randint(0,self.atk) * self.calc_multiplicateur(autre))
        if autre.pv-aleatoire >0:
            autre.pv-= aleatoire
        else:
            autre.pv=0

    def combattre(self,autre):
        '''
        Cette méthode simule le combat entre deux pokémons. Elle compte le nombre de round avant que l'un des deux pokémon
        soit KO, pour cela elle appelle les méthodes 'est_KO' et 'attaquer'. Elle retour à la fin du combat le gagnant
        du duel et le nombre de round total.
        exemple 1 : print(Gou.combattre((Bul)))
        résultat 1 : Goupix a gagné en 17 round
        exemple 2 : print(Psy.combattre(Bou))
        résultat 2 : Boustiflor a gagné en 5 round
        '''
        round=0
        while not (self.est_KO() or autre.est_KO()):
            round+=1
            self.attaquer(autre)
            if not autre.est_KO():
                autre.attaquer(self)
        return f"{autre.nom if self.est_KO() else self.nom} a gagné en {round} round"

    def __str__(self):
        return f"NOM: {self.nom} - PV : {self.pv} - ATK : {self.atk}"


class PokemonFeu(Pokemon):
    def __init__(self,nom,pv,atk):
        Pokemon.__init__(self,nom,pv,atk)

    def calc_multiplicateur(self, autre):
        '''
        Cette méthode, que l'on retrouve dans les 4 classes filles, perrmet de calculer le facteur multipliant le dégât des
        attaques des pokémons en fonction de l'adversaire qu'il rencontre.
        exemple 1 : print(Pik.calc_multiplicateur(Psy)) --> retourne 1 car Pikatchu est un pokémon normal
        exemple 2 : print(Sal.calc_multiplicateur(Bul)) --> retourne 2 car Salamèche est un pokémon feu et Bulbizard et un pokémon plante.
        '''
        if type(autre) is PokemonPlante:
            return 2
        if type(autre) is (PokemonFeu or PokemonEau):
            return 0.5
        return 1


class PokemonPlante(Pokemon):
    def __init__(self,nom,pv,atk):
        Pokemon.__init__(self,nom,pv,atk)

    def calc_multiplicateur(self, autre):
        if type(autre) is PokemonEau:
            return 2
        if type(autre) is (PokemonFeu or PokemonPlante):
            return 0.5
        return 1


class PokemonEau(Pokemon):
    def __init__(self,nom,pv,atk):
        Pokemon.__init__(self,nom,pv,atk)

    def calc_multiplicateur(self, autre):
        if type(autre) is PokemonFeu:
            return 2
        if type(autre) is (PokemonEau or PokemonPlante):
            return 0.5
        return 1

class PokemonNormal(Pokemon):
    def __init__(self,nom,pv,atk):
        Pokemon.__init__(self,nom,pv,atk)

    def calc_multiplicateur(self, autre):
        return 1


def main():
    Pik=PokemonNormal("Pikachu",100,10)
    Bul=PokemonPlante('Bulbizard',100,1)
    Sal=PokemonFeu("Salamèche",75,10)
    Car=PokemonEau("Carapuce", 80,5)
    Gou=PokemonFeu("Goupix", 110, 6)
    Psy=PokemonEau("Psykokwak", 65, 12)
    Bou=PokemonPlante("Boustiflor", 108, 9)
    print(Pik)
    print(Bul)
    print(Sal)
    print(Car)
    '''
    NOM: Pikachu - PV : 100 - ATK : 10
    NOM: Bulbuzard - PV : 100 - ATK : 1
    NOM: Salamèche - PV : 75 - ATK : 10
    NOM: Carapuce - PV : 80 - ATK : 5
    '''
    # print(Bul.est_KO()) --> False
    print(Gou.combattre((Bul)))
    # print(Bul.est_KO()) --> True
    print(Sal.combattre(Car))
    print(Psy.combattre(Bou))
    print(Bou.combattre(Pik))
    '''
    Goupix a gagné en 17 round
    Carapuce a gagné en 18 round
    Boustiflor a gagné en 6 round
    Pikachu a gagné en 16 round
    '''
    # print(Pik.calc_multiplicateur(Psy)) --> 1
    # print(Sal.calc_multiplicateur(Bul)) --> 2


main()