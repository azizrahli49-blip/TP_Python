from time import sleep
def cache(fonction):
    '''
    Fonction qui permet de créer un dictionnaire associant un paramètre à son résultat pour une fonction donnée,
    quand la fonction sera appelée pour ce paramètre, le cache pour donner directement le résultat sans avoir à réexécuter la fonction.
    entrée : paramètre
    sortie :  résultat de ce paramètre pour la fonction appelée
    '''
    dict={}
    def wrapper(parametre):
        if parametre in dict.keys():
            return dict[parametre]
        else:
            dict[parametre]=fonction(parametre)
            return dict[parametre]
    return wrapper

@cache
def somme_chiffre(nombre):
    '''
    Fonction utilisée pour tester le cache, elle fait la somme des chiffres composants un nombre.
    entrée : nombre --> entier
    sortie : somme des chiffres --> entier
    '''
    sleep(2)
    return sum(int(c) for c in str(nombre))

def main():
    '''
    Test de la fonction somme_chiffre pour plusieurs nombres :
        - si le nombre n'a pas encore été testé alors la fonction s'exécute (avec un temps de latence de 5 sec : sleep(5))
        - si le nombre a déjà été testé alors le résultat est directement récupéré dans le dictionnaire du cache
    '''
    print(somme_chiffre(123456789))
    print(somme_chiffre(55555))
    print(somme_chiffre(11111111))
    print(somme_chiffre(123456789))     # retour de la valeur beaucoup plus rapidement car il fait appel au cache

main()